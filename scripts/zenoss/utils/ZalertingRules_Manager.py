#!/usr/bin/env python
""" 
    The goal of ZalertingRulerManager.py is to
    gives you the ability to look into you Alerting Rules
    and Schedules.
    This Script will allow you to do the following..
      * List All Alerting Rules and Schedules for all
        your users and groups
      * search for Alerting Rules by username or groupname
      * search Alerting Rules by Query
    More to come......
"""

import os
import sys
import re

from optparse import OptionParser
from time import ctime

#libs
import Globals
import Acquisition

from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from transaction import commit

__author__ = "Allen Sanabria"
__copyright__ = "Copyright 2010, LinuxDynasty"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"


def printAlertingRules(dmd, object, type):
    print "#"*80
    print "Alerting Rules for %s" % (object)
    if type == "users":
        obj = dmd.ZenUsers.getUserSettings(object)
    if type == "groups":
        obj = dmd.ZenUsers.getGroupSettings(object)
    rules = obj.getActionRules()
    if len(rules) >0:
        rules_dict = getAlertingRules(rules)
        for rule in rules:
            print " ","*"*60
            print "  Alerting Rule: \t%s" % (rule.id)
            print "  SQL Query: \t%s\n" % (rules_dict[rule.id]['query'])
            if len(rules_dict[rule.id]['schedule']) > 0:
                rules_dict = getWindows(rule, rules_dict)
                for window in rules_dict[rule.id]['schedule']:
                    print "  Windows for Alerting Rule %s" % (rule.id)
                    print "   Window:     \t%s" % (window['window'])
                    print "   Start time: \t%s" % \
                          (window['start'])
                    print "   Duration:   \t%s" % \
                          (window['duration'])
                    print " ","*"*60
                    print "\n"
    else:
        print "0 Alerting Rules for %s\n" % (obj.id)

#def printOnlyRulesWithSchedules(dmd, object):
def findQuery(dmd):
    query_dict = []
    rules_dict = {}
    user_list = dmd.ZenUsers.getAllUserSettingsNames()
    group_list = dmd.ZenUsers.getAllGroupSettingsNames()
    olist = []
    for g in group_list:
        olist.append(g)
    for u in user_list:
        olist.append(u)
    for object in olist:
        obj = dmd.ZenUsers.getGroupSettings(object)
        rules = obj.getActionRules()
        if len(rules) >0:
            rules_dict = getAlertingRules(rules)
            for rule in rules:
                if re.search(options.search, rules_dict[rule.id]['query']):
                    rules_dict[rule.id]['owner'] = object
                    if len(rules_dict[rule.id]['schedule']) > 0:
                        rules_dict = getWindows(rule, rules_dict)
                        query_dict.append(rules_dict[rule.id])
                    else:
                        query_dict.append(rules_dict[rule.id])
    return(query_dict)


def getAlertingRules(rules):
    rule_dict = {}
    for rule in rules:
        name = rule.id
        rule_dict[rule.id] = name = {"query" : rule.where}
        rule_dict[rule.id]['rule'] = rule.id
        schedule = rule.windows()
        rule_dict[rule.id]["schedule"] = schedule
    return(rule_dict)

def getWindows(rule, rule_dict):
    if len(rule_dict[rule.id]['schedule']) >0:
        i = 0
        for window in rule_dict[rule.id]['schedule']:
            name = window.id
            start = ctime(window.start)
            duration = "days %d hours %d minutes %d" %\
                       (window.duration//(24*60), window.duration//60%24,\
                       window.duration%60)
            rule_dict[rule.id]['schedule'][i] = name \
                     = {'window' : window.id, 'start' : start, 'duration' : duration}
            i+=1
    return(rule_dict)

def findUserOrGroup(dmd):
    olist = None
    name = None
    type = None
    if options.type == 'users':
        olist = dmd.ZenUsers.getAllUserSettingsNames()
        type = "users"
    elif options.type == 'groups':
        olist = dmd.ZenUsers.getAllGroupSettingsNames()
        type = "groups"
    for obj in olist:
        if re.search(obj, options.search):
            if options.type == 'users':
                name = dmd.ZenUsers.getUserSettings(obj)
            elif options.type == 'groups':
                name = dmd.ZenUsers.getGroupSettings(obj)
    return(name, type)

if __name__ == '__main__':
    usage = 'python %prog -l "all"\n\
             python %prog --search="/App/Log" --type="query"\n\
             python %prog --search="asanabria --type="users"\n\
             python %prog --search="Pager" --type="groups"'
    parser = OptionParser(usage)
    parser.add_option("-s", "--search", dest="search", 
                     help="regular expression of what you are searching for")
    parser.add_option("-t", "--type", dest="type", 
                     help="query|rule|users|groups\n \
                          Example.. --type=users, or --type=query")
    parser.add_option("-V", "--verbose", action="store_true", dest="verbose", 
                     default=False, help="Print output")
    parser.add_option("-l", "--list", dest="list", 
                     help='List either the users, groups, or all\n \
                          Example.. --list="all", or --list="users" or\n \
                          --list="groups"')
    (options, args) = parser.parse_args()

    
    dmd = ZenScriptBase(connect=True,noopts=True).dmd

    if options.list:
        if options.list == 'all' or options.list == 'users':
            object_list = dmd.ZenUsers.getAllUserSettingsNames()
            print "All users in Zenoss"
            for object in object_list:
                printAlertingRules(dmd, object, "users")

        if options.list == 'all' or options.list == 'groups':
            object_list = dmd.ZenUsers.getAllGroupSettingsNames()
            print "\nAll groups in Zenoss"
            for object in object_list:
                printAlertingRules(dmd, object, "groups")

    elif options.search:
        if options.type == 'users' or options.type == 'groups':
            object, type = findUserOrGroup(dmd)
            rules = object.getActionRules()
            printAlertingRules(dmd, object.id, type)
        
        elif options.type == 'query':
            query_dict = findQuery(dmd)
            if len(query_dict) >0:
                for line in query_dict:
                    print "#"*80
                    print "Owner = %s" % (line['owner'])
                    print "  Alerting Rule %s" % (line['rule'])
                    print "    Matching Query = %s" % (line['query'])
                    if len(line['schedule']) > 0:
                        for window in line['schedule']:
                            print "   Window:     \t%s" % (window['window'])
                            print "   Start time: \t%s" % \
                                  (window['start'])
                            print "   Duration:   \t%s" % \
                                  (window['duration'])
                            print " ","*"*60
                            print "\n"
                    print "\n"
        else:
            print "Pass --help for help"
            sys.exit(1)

    else:
        print "Pass the --help for more options"
        sys.exit(1)


