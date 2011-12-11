#!/bin/env python
##############################################################
#Created by Allen Sanabria aka LinuxDynasty aka PrNino69
#This is my attempt to essentially translate my perl zenoss
#syncing script to python, wish me LUCK...
#Started July 19
#Almost done July 20th
#Finally completed, July 24th
##############################################################

import sys
import os
import MySQLdb
import getopt
import re
import string
from xmlrpclib import Fault
from xmlrpclib import ServerProxy
from urllib import urlopen


script = os.path.basename(sys.argv[0])
mydb =  "test"
user = "test"
passwd = 'test'
util = '@test'
base = "http://%s:%s%s:8080" % (user,passwd,util)
searchDevUrl = base+'/zport/dmd/Devices/searchDevices?query='
groupsUrl = base+'/zport/dmd/Groups/getOrganizerNames'
snmpurl = "/getSnmpOidTargets"

def main(args):
  if lan:      
   output = mysql_con(val)
   editDevice(output)


def mysql_con(lan):
  Con = MySQLdb.connect(host=mydb, port=3306,
    user="readonly", passwd="", db="idb")
  Cursor = Con.cursor(  )
  sql = "select host,rack,switch,hardware,console,power,buildprof,conftag,project from servers a, projects b where (a.sn= b.sn and a.lan like '%"+lan+"%' AND b.project != 'webhost') order by host"
  Cursor.execute(sql)
  Results = Cursor.fetchall(  )
  Con.close(  )
  return Results

def editDevice(info):

  Zenoss = {'deviceName': '', 'devicePath': '', 'tag': '', 'serialNumber': '', 'zSnmpCommunity': 'monitor', 
            'zSnmpPort': '161', 'zSnmpVer': 'v1', 'rackSlot': '0', 'productionState': '1000', 'comments': '',
            'hwManufacturer': '', 'hwProductName': '', 'osManufacturer': '', 'osProductName': '',
            'locationPath': '', 'groupPaths': '', 'systemPaths': '', 'statusMonitors': '',
            'performanceMonitor': '', 'discoverProto': 'snmp', 'priority': '3'}

  x = 0
  for a in  info:
    Zenoss['deviceName'] = info[x][0]
    url = http(Zenoss['deviceName'])
    valid = re.search("http", url)
    if valid:
      snmp_out = http(url+snmpurl)
      Zenoss['zSnmpCommunity'] = snmp_out[0]
      Zenoss['zSnmpVer'] = snmp_out[1]
      Zenoss['comments'] = "Switch %s\n Hardware %s\n Console %s\n Power %s\n Build Profile %s" % (info[x][2],info[x][3],info[x][4],info[x][5],info[x][6])
      sys_match = re.search("\w+", "info[x][8]")
      if sys_match:
        Zenoss['systemPaths'] = "/%s" % (info[x][8])
      groups_return = http(groupsUrl)
      Zenoss['groupPaths'] = group_final(groups_return, Zenoss['systemPaths'])
      serv = ServerProxy (url,allow_none=1)
      serv.manage_editDevice(Zenoss['tag'], Zenoss['serialNumber'],
		  Zenoss['zSnmpCommunity'], Zenoss['zSnmpPort'], Zenoss['zSnmpVer'], Zenoss['rackSlot'],
		  Zenoss['productionState'], Zenoss['comments'], Zenoss['hwManufacturer'], Zenoss['hwProductName'],
		  Zenoss['osManufacturer'], Zenoss['osProductName'], Zenoss['locationPath'] , Zenoss['groupPaths'], Zenoss['systemPaths'])
      if verbose:
        print "%s\n%s\n%s\n%s\n%s\n%s\n" % (url,Zenoss['zSnmpCommunity'],Zenoss['zSnmpVer'],Zenoss['comments'], Zenoss['systemPaths'],Zenoss['groupPaths'])
    x = x +1

def http(url):
  group_match= re.search("getOrganizerNames", url)
  snmp_match= re.search("getSnmpOidTargets", url)
  if group_match:
    match = urlopen(groupsUrl).read()
    group_sub = re.sub("\'|\s+|\[|\]", "",match)
    group_list = group_sub.split(",")
    return group_list
  elif snmp_match:
    snmp_output = urlopen(url).read()
    snmp_ver = re.search("v1|v2c|v3", snmp_output)
    snmp_filter = re.sub("\[|\]|\'|\,|\(|\)", "", snmp_output)
    snmp_split = string.split(snmp_filter)
    snmp_final = [ snmp_split[4], snmp_ver.group() ]
    return snmp_final
  else:
    device_url = urlopen(searchDevUrl+url).geturl()
    match_url = re.search("query", device_url)
    if match_url:
      return "none"
    else:
      return device_url

def group_final(groups, group_path):
  y = 0
  for b in  groups:
    groups_match = re.search(group_path, groups[y])
    if groups_match:
      return groups[y]
    y = y +1

def usage(code=0):
    print '\nUsage: %s [-s|--switch]' % script
    print '''
    -l, --lan          bc,tm,fl...etc The lan it is on
    -h, --help         This help message 
    -v, --verbose      Added verbosity    
    '''

try:
  opts, args = getopt.getopt(sys.argv[1:], "l:hv",
  [ 'lan=', 'help', 'verbose' ]
  )
except getopt.error:
  usage(0)

help = lan = verbose = None
for opt, val in opts:
  if opt in ('-h', '--help'):
    usage(0)
  if opt in ('-v', '--verbose'):
    verbose = True
  if opt in ('-l', '--lan'):
    lan = val


if __name__ == "__main__":
   main(sys.argv[1:])
