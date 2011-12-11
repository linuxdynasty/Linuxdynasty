#!/usr/bin/env python
#Created by Allen Sanabria aka LinuxDynasty
#Copyright (C) 2009  Allen Sanabria

#This is my attempt to create the clustat command, using SNMP.
#I wanted a way to be able to get the clustat/cman_tool status outout
#with out having to logging into a node in the cluster.
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import sys 
import re
import string
import getopt
from time import ctime

try:
    from pysnmp.entity.rfc3413.oneliner import cmdgen
except Exception, e:
    print "You need to download pysnmp and pyasn1", e
    sys.exit(1)

def main():
    try:
        errorIndication, errorStatus, errorIndex, \
            ClustInfo = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', community), \
            cmdgen.UdpTransportTarget((device, port)), (1,3,6,1,4,1,2312,8))
        if errorIndication:
            print errorIndication
            sys.exit(1)
        
    except Exception, e:
        print e
        sys.exit(1)
    
    clustHash = {}
    for entry in ClustInfo:
        try:
            if clusterTable[tuple(entry[0][0])]:
                clustHash[clusterTable[tuple(entry[0][0][:11])]] = entry[0][1]
        except:
            if clusterTable[tuple(entry[0][0][:12])]:
                clustHash[clusterTable[tuple(entry[0][0][:12])]+"."+Dec2Char(tuple(entry[0][0][13:]))] \
                = {Dec2Char(tuple(entry[0][0][13:])) : str(entry[0][1])}
            pass


    cluster = {}
    column_a = 63
    column_b = 48
    column_c = 24
    nodes = re.sub(" ", "", str(clustHash["rhcClusterNodesNames"]))
    nodes = nodes.split(",")
    availNodes = re.sub(" ", "", str(clustHash["rhcClusterAvailNodesNames"]))
    availNodes = availNodes.split(",")
    services = re.sub(" ", "", str(clustHash["rhcClusterServicesNames"]))
    services = services.split(",")
    cluster = {
              "rhcClusterName" : clustHash["rhcClusterName"],
              "rhcClusterQuorate" : rhcClusterQuorate[clustHash["rhcClusterQuorate"]],
              "rhcClusterStatusCode" : rhcClusterStatusCode[clustHash["rhcClusterStatusCode"]],
              "totalnodes" : clustHash["rhcClusterNodesNum"],
              "totalvotes" : clustHash["rhcClusterVotes"],
              "votesquorate" : clustHash["rhcClusterVotesNeededForQuorum"]
              }
    for node in nodes:
        cluster[node] = {
                        "name" : node,
                        "status" : rhcNodeStatusCode[int(re.sub("\[|\]|\'","",str(clustHash["rhcNodeStatusCode." + node].values())))]
                        }
    if ( int(clustHash["rhcClusterServicesNum"]) >= 1 ):
        for service in services:
            cluster[service] = {
                           "name" : service,
                           "status" : rhcServiceStatusCode[int(re.sub("\[|\]|\'","",\
                           str(clustHash["rhcServiceStatusCode." + service].values())))],
                           "node" : clustHash["rhcServiceRunningOnNode." + service][service],
                           "mode" : clustHash["rhcServiceStartMode." + service][service]
                           }                

    print "Cluster Status for " + cluster["rhcClusterName"] + " @ " + ctime()
    print "Member Status: " + cluster["rhcClusterQuorate"]
    print "Total Nodes: ", cluster["totalnodes"]
    print "Total Votes: ", cluster["totalvotes"]
    print "Votes Needed For Quorum: ", cluster["votesquorate"]
    print "\n Member Name\t\t\t\t\t\t\tStatus"
    print " ------ ----\t\t\t\t\t\t\t------"
    for node in nodes:
        print " %s%s" % ( PrintFormat(cluster[node]["name"], column_a), cluster[node]["status"] )
    if ( int(clustHash["rhcClusterServicesNum"]) >= 1 ):
        print "\n Service Name\t\t\t\t\t\t\tOwner\t\t\t\t\t\tState\t\t\tStart Up Mode"
        print " ------- ----\t\t\t\t\t\t\t-----\t\t\t\t\t\t-----\t\t\t-------------" 
        for service in services:
             print " %s%s%s%s" % ( PrintFormat(cluster[service]["name"], column_a), \
                  PrintFormat(cluster[service]["node"], column_b), PrintFormat(cluster[service]["status"], column_c), \
                  cluster[service]["mode"] )
        sys.exit(0)

def PrintFormat(variable, width):
    varOut = variable + ' '  * ( width - len(variable) )
    return varOut

def Dec2Char(identifier):
    identity = map(chr, identifier)
    identity = re.sub("\[|\'|\,|\]|\s", '', str(identity))
    return( identity )

def usage():
    print """
    -d, --device    This is the device you want to scan
    -c, --community This is the SNMP community string to use
    """
    sys.exit(1)


rhcClusterStatusCode = {
                       1 : "All services and nodes functional",
                       2 : "Some services failed",
                       4 : "Some services not running",
                       8 : "Some nodes unavailable",
                       16 : "Not quorate",
                       32 : "Cluster stopped"
                       }

rhcClusterQuorate = {
                    0 : "Quorum Dissolved",
                    1 : "Quorate"
                    }

rhcNodeStatusCode = {
                    0 : "Participating in cluster",
                    1 : "Running, but not participating in cluster",
                    2 : "Not running"
                    }

rhcServiceStatusCode = {
                       0 : "running",
                       1 : "stopped",
                       2 : "failed"
                       }
clusterTable = {
               (1,3,6,1,4,1,2312,8,1,1,0): "rhcMIBVersion", 
               (1,3,6,1,4,1,2312,8,2,1,0): "rhcClusterName", 
               (1,3,6,1,4,1,2312,8,2,2,0) : "rhcClusterStatusCode",
               (1,3,6,1,4,1,2312,8,2,3,0) : "rhcClusterStatusDesc",
               (1,3,6,1,4,1,2312,8,2,4,0) : "rhcClusterVotesNeededForQuorum",
               (1,3,6,1,4,1,2312,8,2,5,0) : "rhcClusterVotes",
               (1,3,6,1,4,1,2312,8,2,6,0) : "rhcClusterQuorate",
               (1,3,6,1,4,1,2312,8,2,7,0) : "rhcClusterNodesNum",
               (1,3,6,1,4,1,2312,8,2,8,0) : "rhcClusterNodesNames",
               (1,3,6,1,4,1,2312,8,2,9,0) : "rhcClusterAvailNodesNum",
               (1,3,6,1,4,1,2312,8,2,10,0) : "rhcClusterAvailNodesNames",
               (1,3,6,1,4,1,2312,8,2,11,0) : "rhcClusterUnavailNodesNum",
               (1,3,6,1,4,1,2312,8,2,12,0) : "rhcClusterUnavailNodesNames",
               (1,3,6,1,4,1,2312,8,2,13,0) : "rhcClusterServicesNum",
               (1,3,6,1,4,1,2312,8,2,14,0) : "rhcClusterServicesNames",
               (1,3,6,1,4,1,2312,8,2,15,0) : "rhcClusterRunningServicesNum",
               (1,3,6,1,4,1,2312,8,2,16,0) : "rhcClusterRunningServicesNames",
               (1,3,6,1,4,1,2312,8,2,17,0) : "rhcClusterStoppedServicesNum",
               (1,3,6,1,4,1,2312,8,2,18,0) : "rhcClusterStoppedServicesNames",
               (1,3,6,1,4,1,2312,8,2,19,0) : "rhcClusterFailedServicesNum",
               (1,3,6,1,4,1,2312,8,2,20,0) : "rhcClusterFailedServicesNames",
               (1,3,6,1,4,1,2312,8,3,1,1,1) : "rhcNodeName",
               (1,3,6,1,4,1,2312,8,3,1,1,2) : "rhcNodeStatusCode",
               (1,3,6,1,4,1,2312,8,3,1,1,3) : "rhcNodeStatusDesc",
               (1,3,6,1,4,1,2312,8,3,1,1,4) : "rhcNodeRunningServicesNum",
               (1,3,6,1,4,1,2312,8,3,1,1,5) : "rhcNodeRunningServicesNames",
               (1,3,6,1,4,1,2312,8,3,2,1,1) : "rhcServiceName",
               (1,3,6,1,4,1,2312,8,3,2,1,2) : "rhcServiceStatusCode",
               (1,3,6,1,4,1,2312,8,3,2,1,3) : "rhcServiceStatusDesc",
               (1,3,6,1,4,1,2312,8,3,2,1,4) : "rhcServiceStartMode",
               (1,3,6,1,4,1,2312,8,3,2,1,5) : "rhcServiceRunningOnNode",
               }


try:
     opts, args = getopt.getopt(sys.argv[1:], "c:d:p:h:",
     [ 'community=', 'device=', 'port=', 'help' ]
     )   

except getopt.error:
     usage()
help = community = device = None
port = 161

for opt, val in opts:
    if opt in ('-c', '--community'):
        community = val 
    if opt in ('-d', '--device'):
        device = val 
    if opt in ('-p', '--port'):
        port = val 
    if opt in ('-h', '--help'):
        help = usage()

if __name__ == '__main__' and community and device:
    main()
else:
    usage()
