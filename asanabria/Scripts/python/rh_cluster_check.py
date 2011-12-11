#!/usr/bin/python
#Created by Allen Sanabria aka LinuxDynasty
#Copyright (C) 2009  Allen Sanabria

#This is my attempt to create a NAGIOS compatible check for RedHat Clustering
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
            sys.exit()
        
    except Exception, e:
        print e
        sys.exit()
    
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


    nodes = re.sub(" ", "", str(clustHash["rhcClusterNodesNames"]))
    nodes = nodes.split(",")
    availNodes = re.sub(" ", "", str(clustHash["rhcClusterAvailNodesNames"]))
    availNodes = availNodes.split(",")
    services = re.sub(" ", "", str(clustHash["rhcClusterServicesNames"]))
    services = services.split(",")
    if ( type == "cluster" ):
        status, cluster_info = CheckCluster({
                  "rhcClusterName" : clustHash["rhcClusterName"],
                  "rhcClusterQuorate" : clustHash["rhcClusterQuorate"],
                  "rhcClusterStatusCode" : clustHash["rhcClusterStatusCode"],
                  "totalnodes" : clustHash["rhcClusterNodesNum"],
                  "totalvotes" : clustHash["rhcClusterVotes"],
                  "votesquorate" : clustHash["rhcClusterVotesNeededForQuorum"]
                  })
        print "%s, %s is %s and %s" % ( status, cluster_info[0], cluster_info[1], cluster_info[2] )
        sys.exit(exitval[status])
    
    elif ( type == "node" ):
        if Exists(node_name, nodes):
            status, node_info = CheckNode({
                "name" : node_name,
                "status" : clustHash["rhcNodeStatusCode." + node_name][node_name]
                })
            print "%s, %s is %s" % ( status, node_info[0], node_info[1] )
            sys.exit(exitval[status])
        else:
            print "CRITICAL, %s does not exist on the cluster %s" % ( node_name, clustHash["rhcClusterName"] )
            sys.exit(exitval["CRITICAL"])

    elif ( type == "service" ):
        if Exists(service_name, services):
            status, service_info = CheckService({
                "name" : service_name,
                "status" : clustHash["rhcServiceStatusCode." + service_name][service_name],
                "node" : clustHash["rhcServiceRunningOnNode." + service_name][service_name]
                })

            if status == "OK":
                print "%s, %s is %s on %s" % ( status, service_info[0], service_info[1], service_info[2] )
            else:
                print "%s, %s is %s" % ( status, service_info[0], service_info[1] )
            sys.exit(exitval[status])
        else:
            print "CRITICAL, %s does not exist on the cluster %s" % ( service_name, clustHash["rhcClusterName"] )
            sys.exit(exitval["CRITICAL"])

def Exists(object, object_list):
    count = 0
    for line in object_list:
        if line == object:
            count +=1
    if count == 1:
        return True
    else:
        return False

def CheckCluster(cluster):
    output = (str(cluster["rhcClusterName"]), rhcClusterQuorate[cluster["rhcClusterQuorate"]], rhcClusterStatusCode[cluster["rhcClusterStatusCode"]])
    if ( cluster["rhcClusterQuorate"] == 1 and cluster["rhcClusterStatusCode"] == 1 ):
        return ("OK", output )
    elif ( cluster["rhcClusterQuorate"] == 1 and re.search("2|4|8", str(cluster["rhcClusterStatusCode"]) ) ):
        return  ("WARNING", output )
    elif ( cluster["rhcClusterQuorate"] == 0 and re.search("16|32", str(cluster["rhcClusterStatusCode"]) ) ):
        return ("CRITICAL", output )

def CheckNode(host):
    output = (str(host["name"]), rhcNodeStatusCode[int(host["status"])])
    status = int(host["status"])
    if ( status == 0 ):
        return ("OK", output )
    elif ( status == 1 ):
        return  ("WARNING", output )
    elif ( status == 2 ):
        return ("CRITICAL", output )

def CheckService(service):
    output = (str(service["name"]), rhcServiceStatusCode[int(service["status"])], str(service["node"]))
    status = int(service["status"])
    if ( status == 0 ):
        return ("OK", output )
    elif ( status == 1 or status == 2 ):
        return ("CRITICAL", output )


def Dec2Char(identifier):
    identity = map(chr, identifier)
    identity = re.sub("\[|\'|\,|\]|\s", '', str(identity))
    return( identity )

def usage():
    print """
    -d, --device     This is the device you want to scan
    -c, --community  This is the SNMP community string to use
    -n, --node       This is node name
    -s, --service    This is service name
    -t, --type       This is type of check ( cluster, service, node )
    examples below..
    
      python rh_cluster_check.py -d gfs1 -c public -t node -n gfs3
      OK, gfs3 is Participating in cluster
    
      python rh_cluster_check.py -d gfs1 -c public -t service -s CIM
      OK, CIM is running on gfs1.newschool.edu

      python rh_cluster_check.py -d gfs2 -c public -t cluster
      WARNING, MyCluster is Quorate and Some services not running
    """
    sys.exit(1)

exitval = {
            "OK" : 0,
            "WARNING" : 1,
            "CRITICAL" : 2,
            "UNKNOWN" : 3
           }

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
     opts, args = getopt.getopt(sys.argv[1:], "c:d:p:t:n:s:h:",
     [ 'community=', 'device=', 'port=', 'node_name=', 'service_name=', 'help', 'type' ]
     )   

except getopt.error:
     usage()
help = community = device = type = None
port = 161

for opt, val in opts:
    if opt in ('-c', '--community'):
        community = val 
    if opt in ('-d', '--device'):
        device = val 
    if opt in ('-t', '--type'):
        type = val 
    if opt in ('-n', '--node_name'):
        node_name = val 
    if opt in ('-s', '--service_name'):
        service_name = val 
    if opt in ('-p', '--port'):
        port = val 
    if opt in ('-h', '--help'):
        help = usage()

if __name__ == '__main__' and community and device and type or \
                community and device and type and node_name or \
                community and device and type and service_name:
    if re.search("cluster|node|service", type):        
        main()
    else:
        usage()
else:
    usage()
