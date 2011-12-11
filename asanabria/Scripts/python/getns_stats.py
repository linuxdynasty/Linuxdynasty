#!/usr/bin/env python

import sys
import string

from optparse import OptionParser

from suds.client import Client
from suds.xsd.doctor import Import
from suds.xsd.doctor import ImportDoctor

__author__ = "Allen Sanabria"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"


def main():
    if options.hostname and options.username and options.password:
        url = "http://"+options.hostname+"/api/NSStat.wsdl"
        imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
        imp.filter.add("urn:NSConfig")  
        d = ImportDoctor(imp)
        client = Client(url, doctor=d, location="http://"+options.hostname+"/soap/", timeout=50000)
        loggedin = client.service.login(username=options.username, password=options.password)
        if loggedin.rc != 0:
            sys.exit(1)
        if options.list:
            vserver_list = getlistNames(client, options.list)
            for line in vserver_list:
                print line
        elif options.type:
            finalstats = printFinalStats(client)
            print finalstats
            sys.exit(exitval["OK"])
        client.service.logout()
    else:
        print "Please provide the Netscaler IPAddress and username/password\n pass the --help for more options"
        sys.exit(1)


def printFinalStats(client):
    stats_list = [] 
    stats = None
    if options.type == "service":
        stats = getSVCstats(client, options.name)
    elif options.type == "lbvserver":
        stats = getLBVstats(client, options.name)
    elif options.type == "tcp":
        stats = getTCPstats(client)
    elif options.type == "http":
        stats = getHTTPstats(client)
    for key, val in stats.items():
        stats_list.append(key+"="+str(val)+" ")
    finalstats = ""
    for line in stats_list:
        finalstats = finalstats + line
    return "OK|"+finalstats.rstrip(" ")

def getlistNames(client, get_options="lbvserver"):
    """return a list of names for either ( servicegroup, service, or lbvserver )"""
    lblist1 = None
    lblist2 = []
    if get_options == "lbvserver":
        lblist1 = client.service.statlbvserver()
        if lblist1.rc != 0:
            print "CRITICAL", lblist1.message
            sys.exit(exitval["CRITICAL"])
    elif get_options == "service":
        lblist1 = client.service.statservice()
        if lblist1.rc != 0:
            print "CRITICAL", lblist1.message
            sys.exit(exitval["CRITICAL"])
    else:
        print "Please pass either lbserver or service"
        sys.exit(exitval["CRITICAL"])

    if lblist1.rc == 0:
        for line in lblist1.List:  
            try:
                lblist2.append(line['name'])
            except AttributeError:
                lblist2.append(line['servicegroupname'])
                
    return lblist2


def getSVCstats(client, services):
    """return a list of Services and the servers attached to each Service
       and it associated information ( servername, port, svrstate, ipaddress of server )"""
    svcstats = {}
    slist = client.service.statservice(services)
    if slist.rc == 0:
        slist = slist.List[0]
        svcstats = {"totalrequests" : slist['totalrequests'], "requestsrate" : slist["requestsrate"],\
                   "totalresponses" : slist['totalresponses'], "responsesrate" : slist["responsesrate"], \
                   "totalrequestbytes" : slist['totalrequestbytes'], "requestbytesrate" : slist['requestbytesrate'], \
                   "totalresponsebytes" : slist["totalresponsebytes"], "responsebytesrate" : slist["responsebytesrate"], \
                   "curclntconnections" : slist["curclntconnections"], "surgecount" : slist["surgecount"], \
                   "cursrvrconnections" : slist["cursrvrconnections"], "svrestablishedconn" : slist["svrestablishedconn"], \
                   "throughput" : slist["throughput"], "throughputrate" : slist["throughputrate"], \
                   "activetransactions" : slist["activetransactions"]
                   } 
    else:
        print "CRITICAL", slist.message, " by the name of %s" % (services)
        sys.exit(exitval["CRITICAL"])
    return svcstats


def getLBVstats(client, vserver):
    """return a list of Services and the servers attached to each Service
       and it associated information ( servername, port, svrstate, ipaddress of server )"""
    lbvstats = {}
    vlist = client.service.statlbvserver(vserver)
    if vlist.rc == 0:
        vlist = vlist.List[0]
        lbvstats = {"tothits" : vlist['tothits'], "hitsrate" : vlist["hitsrate"],\
                   "totalrequests" : vlist['totalrequests'], "requestsrate" : vlist["requestsrate"], \
                   "totalresponses" : vlist['totalresponses'], "responsesrate" : vlist['responsesrate'], \
                   "totalrequestbytes" : vlist["totalrequestbytes"], "requestbytesrate" : vlist["requestbytesrate"], \
                   "totalresponsebytes" : vlist["totalresponsebytes"], "responsebytesrate" : vlist["responsebytesrate"], \
                   "totalpktsrecvd" : vlist["totalpktsrecvd"], "pktsrecvdrate" : vlist["pktsrecvdrate"], \
                   "totalpktssent" : vlist["totalpktssent"], "pktssentrate" : vlist["pktssentrate"], \
                   "curclntconnections" : vlist["curclntconnections"], "establishedconn" : vlist["establishedconn"], \
                   "cursrvrconnections" : vlist["cursrvrconnections"]
                   } 
    else:
        print "CRITICAL", vlist.message, " by the name of %s" % (vserver)
        sys.exit(exitval["CRITICAL"])
    return lbvstats

def getTCPstats(client):
    """return a list of Services and the servers attached to each Service
       and it associated information ( servername, port, svrstate, ipaddress of server )"""
    tcpstats = {}
    tcp_list = client.service.statprotocoltcp()
    if tcp_list.rc == 0:
        tcp_list = tcp_list.List[0]
        tcpstats = {"tcpcurclientconnestablished" : tcp_list['tcpcurclientconnestablished'], \
                   "tcpcurserverconnestablished" : tcp_list['tcpcurserverconnestablished'], "tcpcurclientconn" : tcp_list["tcpcurclientconn"], \
                   "tcpcurclientconnopening" : tcp_list['tcpcurclientconnopening'], "tcpcurclientconnclosing" : tcp_list['tcpcurclientconnclosing'], \
                   "tcpclientconnopenedrate" : tcp_list['tcpclientconnopenedrate'],
                   "tcpcurserverconn" : tcp_list["tcpcurserverconn"], "tcpcurserverconnopening" : tcp_list["tcpcurserverconnopening"], \
                   "tcpcurserverconnclosing" : tcp_list["tcpcurserverconnclosing"], "tcpserverconnopenedrate" : tcp_list["tcpserverconnopenedrate"], \
                   "tcpactiveserverconn" : tcp_list["tcpactiveserverconn"], "tcptotrxpkts" : tcp_list["tcptotrxpkts"], \
                   "tcprxpktsrate" : tcp_list["tcprxpktsrate"], "tcptotrxbytes" : tcp_list["tcptotrxbytes"], \
                   "tcprxbytesrate" : tcp_list["tcprxbytesrate"], "tcptottxpkts" : tcp_list["tcptottxpkts"], \
                   "tcptxpktsrate" : tcp_list["tcptxpktsrate"], "tcptottxbytes" : tcp_list["tcptottxbytes"], \
                   "tcptxbytesrate" : tcp_list["tcptxbytesrate"]
                   } 
    else:
        print "CRITICAL", tcp_list.message
        sys.exit(exitval["CRITICAL"])
    return tcpstats

def getHTTPstats(client):
    """return a list of Services and the servers attached to each Service
       and it associated information ( servername, port, svrstate, ipaddress of server )"""
    httpstats = {}
    http_list = client.service.statprotocolhttp()
    if http_list.rc == 0:
        http_list = http_list.List[0]
        httpstats = {"httptotrequests" : http_list['httptotrequests'], \
                   "httprequestsrate" : http_list['httprequestsrate'], "httptotresponses" : http_list["httptotresponses"], \
                   "httpresponsesrate" : http_list['httpresponsesrate'], "httptotrxrequestbytes" : http_list['httptotrxrequestbytes'], \
                   "httprxrequestbytesrate" : http_list['httprxrequestbytesrate'], "httprxrequestbytesrate" : http_list["httprxrequestbytesrate"], \
                   "httptotrxresponsebytes" : http_list["httptotrxresponsebytes"], "httprxresponsebytesrate" : http_list["httprxresponsebytesrate"], \
                   "httptotgets" : http_list["httptotgets"], "httpgetsrate" : http_list["httpgetsrate"], \
                   "httptotposts" : http_list["httptotposts"], "httppostsrate" : http_list["httppostsrate"], \
                   "httptotothers" : http_list["httptotothers"], "httpothersrate" : http_list["httpothersrate"], \
                   "httperrserverbusy" : http_list["httperrserverbusy"], "httperrserverbusyrate" : http_list["httperrserverbusyrate"], \
                   "httptottxresponsebytes" : http_list["httptottxresponsebytes"], "httptxresponsebytesrate" : http_list["httptxresponsebytesrate"]
                   } 
    else:
        print "CRITICAL", http_list.message
        sys.exit(exitval["CRITICAL"])
    return httpstats


usage = "usage: %prog [options] arg --username=username --password=password --netscaler=netscalerip"
parser = OptionParser(usage)
parser.add_option("-i", "--hostname", dest="hostname", help="Here you will put the netscaler IPAddress or the \
                 netscaler hostname")
parser.add_option("-u", "--username", dest="username", help="Your username")
parser.add_option("-p", "--password", dest="password",  help="Your password")
parser.add_option("-l", "--list", dest="list",
                    help="List all the names of the Virtual Servers and Services. \
Example --list=lbvserver, --list=service")
parser.add_option("-n", "--name", dest="name", help="Virtual Server that you want to grab statistics for.")
parser.add_option("-t", "--type", dest="type", help="Here you either pass service, lbvserver, tcp or http.\
                   example... --name=foobar --type=lbvserver  or --type=tcp or --type=http or --name=foobar --type=service")
(options, args) = parser.parse_args()

exitval = {
          "OK"       : 0,
          "WARNING"  : 1,
          "CRITICAL" : 2,
          "UNKNOWN"  : 3
          }

if __name__ == '__main__':
    main()
