#!/usr/bin env python

import sys
import string

from optparse import OptionParser

from suds.client import Client
from suds.xsd.doctor import *

__author__ = "Allen Sanabria"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"


def main():
    if options.netscaler and options.username and options.password:
        url = "http://"+options.netscaler+"/api/NSConfig.wsdl"
        imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
        imp.filter.add("urn:NSConfig")  
        d = ImportDoctor(imp)
        client = Client(url, doctor=d, location="http://"+options.netscaler+"/soap/", timeout=50000)
        loggedin = client.service.login(username=options.username, password=options.password)
        if loggedin.rc != 0: sys.exit(1)
        if options.list:
            vserver_list = getlistNames(client, options.list)
            for line in vserver_list:
                print line
        elif options.server:
            printLBvservStatus(client, options.server)

        elif options.sgroup:
            if options.sgroup != "all":
                printSGlist(client, options.sgroup)
            elif options.sgroup == "all":
                sgroup_list = getlistNames(client, "servicegroup")
                printSGlist(client, sgroup_list)

        elif options.service:
            if options.service != "all":
                printSVClist(client, options.service)
            elif options.service == "all":
                services_list = getlistNames(client, "service")
                printSVClist(client, services_list)

        client.service.logout()
    else:
        print "Please provide the Netscaler IPAddress and username/password\n pass the --help for more options"
        sys.exit(1)


def printLBvservStatus(client, server=None):
    def printAll(vserver, lbvserver):
        sgroup_list = None
        service_list = None
        if lbvserver.rc == 0:
            try:
                sgroup_list = lbvserver.List[0]['servicegroupname']
            except AttributeError:
                pass

            try:
                service_list = lbvserver.List[0]['servicename']
            except AttributeError:
                pass

            if sgroup_list and service_list:
                printLBVserver(vserver, lbvserver.List)
                printSGlist(client, sgroup_list)
                printSVClist(client, service_list)
                return()
            elif service_list:
                printLBVserver(vserver, lbvserver.List)
                printSVClist(client, service_list)
                return()
            elif sgroup_list:
                printLBVserver(vserver, lbvserver.List)
                printSGlist(client, sgroup_list)
                return()
            else:
                print "No Services or ServiceGroups exist on this LBVserver %s" % ( vserver )
                return()
                #sys.exit(1)
        else:
            print lbvserver.message
            sys.exit(1)

    if server != "all":
        lbvserver = client.service.getlbvserver(server)
        if lbvserver.rc == 0:
            printAll(server, lbvserver)
            print "-" * 150
    elif server == "all":
        lbserver_list = getlistNames(client)
        for lbserver in lbserver_list:
            lbvserver = client.service.getlbvserver(lbserver)
            printAll(lbserver, lbvserver)
            print "-" * 150


def printLBVserver(vserver, lbvserver):
    print "\n", pFormat("Virtual Server", 40), pFormat("State", 10), pFormat("IPAddress", 20), pFormat("Port", 10), pFormat("Protocol", 10)
    print pFormat(lbvserver[0]['name'], 40), pFormat(lbvserver[0]['effectivestate'], 10), pFormat(lbvserver[0]['ipaddress2'], 20), \
                 pFormat(str(lbvserver[0]['port']), 10), pFormat(lbvserver[0]['servicetype'], 10)


def printSGlist(client, sgroup_list):
    sginfo = getSGinfo(client, sgroup_list)
    print pFormat("\nServiceGroup Name", 40), pFormat("SG State", 20), pFormat("Server Name", 30), pFormat("Status", 20),\
                 pFormat("IPAddress", 20), pFormat("Port", 10), pFormat("Protocol", 10)
    for key in sginfo.keys():
        print pFormat(sginfo[key]['group'], 40), pFormat(sginfo[key]['state'], 20), pFormat(sginfo[key]['servername'], 30),\
                     pFormat(sginfo[key]['status'], 20), pFormat(sginfo[key]['ipaddress'], 20), pFormat(str(sginfo[key]['port']), 10),\
                     pFormat(sginfo[key]['servicetype'], 10)


def printSVClist(client, service_list):
    svcinfo = getSVinfo(client, service_list)
    print pFormat("\nService Name", 40), pFormat("Server Name", 30), pFormat("Status", 20), pFormat("IPAddress", 20),\
                 pFormat("Port", 10), pFormat("Protocol", 10)
    for key in svcinfo.keys():
        print pFormat(svcinfo[key]['service'], 40), pFormat(svcinfo[key]['servername'], 30), pFormat(svcinfo[key]['status'], 20), \
                     pFormat(svcinfo[key]['ipaddress'], 20), pFormat(str(svcinfo[key]['port']), 10), pFormat(svcinfo[key]['servicetype'], 10)


def getlistNames(client, get_options="lbvserver"):
    """return a list of names for either ( servicegroup, service, or lbvserver )"""
    lblist1 = None
    lblist2 = []
    if get_options == "lbvserver":
        lblist1 = client.service.getlbvserver()
    elif get_options == "service":
        lblist1 = client.service.getservice()
    elif get_options == "servicegroup":
        lblist1 = client.service.getservicegroup()
    else:
        print "Please pass either lbserver, service, or servicegroup"
        sys.exit(1)

    if lblist1.rc == 0:
        for line in lblist1.List:  
            try:
                lblist2.append(line['name'])
            except AttributeError:
                lblist2.append(line['servicegroupname'])
                
    return lblist2


def getSGinfo(client, sgroup):
    """return a list of ServiceGroups and the servers attached to each ServiceGroup
       and it associated information ( servername, port, svcstate, ipaddress of server )"""
    sginfo = {}
    if type(sgroup) == str:
        sgroup = sgroup.split(",")
    for group in sgroup:
        glist = client.service.getservicegroup(group)
        if glist.rc == 0:
            glist = glist.List
            for i in range(len(glist[0]['servername'])):
                sginfo[glist[0]['servername'][i]] = {"group" : group, "servername" : glist[0]['servername'][i], "port" : glist[0]['port'][i], \
                 "status" : glist[0]['svcstate'][i], "ipaddress" : glist[0]['ipaddress'][i], "state" : glist[0]['state'],\
                 "servicetype" : glist[0]["servicetype"]} 
        else:
            print glist.message, " by the name of %s" % (group)
            sys.exit(1)
    return sginfo
    

def getSVinfo(client, services):
    """return a list of Services and the servers attached to each Service
       and it associated information ( servername, port, svrstate, ipaddress of server )"""
    svinfo = {}
    if type(services) == str:
        services = services.split(",")
    for service in services:
        slist = client.service.getservice(service)
        if slist.rc == 0:
            slist = slist.List
            svinfo[slist[0]['servername']] = {"service" : service, "servername" : slist[0]['servername'], "port" : slist[0]['port'] \
            , "status" : slist[0]['svrstate'], "ipaddress" : slist[0]['ipaddress'], "servicetype" : slist[0]["servicetype"]} 
        else:
            print slist.message, " by the name of %s" % (service)
            sys.exit(1)
    return svinfo


def pFormat(variable, width):
    """Pretty Printing in a column format"""
    varOut = variable + ' '  * ( width - len(variable) )
    return varOut


usage = "usage: %prog [options] arg --username=username --password=password --netscaler=netscalerip"
parser = OptionParser(usage)
parser.add_option("-n", "--netscaler", dest="netscaler", help="Here you will put the netscaler IPAddress or the \
                 netscaler hostname")
parser.add_option("-u", "--username", dest="username", help="Your username")
parser.add_option("-p", "--password", dest="password",  help="Your password")
parser.add_option("-l", "--list", dest="list",
                    help="List all the names of the Virtual Servers, Services, ServiceGroups. \
Example --list=lbvserver, --list=service, --list=servicegroup")
parser.add_option("-s", "--vserver", dest="server", help="Virtual Server that you want to query. You can choose\
                 a Virtual Server or you can pass all, so you get all the Virtual Servers and its associated \
                 ServiceGroups or Services. Example.... --vserver=\"foobar_test\" or --vserver=\"all\"")
parser.add_option("-g", "--sgroup", dest="sgroup", help="ServiceGroup that you want the info from")
parser.add_option("-c", "--service", dest="service", help="Service that you want the info from")
(options, args) = parser.parse_args()

if __name__ == '__main__':
    main()
