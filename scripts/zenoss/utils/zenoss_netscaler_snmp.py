#!/bin/env python
######################################################################
#Created by Allen Sanabria aka LinuxDynasty
#This script will sync the Netscaler Virtual Servers and Virtual Hosts
#To Zenoss. I made the Virtual Servers to be Systems in Zenoss
#Virtual Servers are == Systems in Zenoss
#Virtual Hosts are == Devices that are under the specified System.
#Example bpwww-cluster on the Netscaler
#under the Systems tab in Zenoss /bpwww-cluster is created
#The devices that are in that cluster will be placed under that system
#Started Nov 28
#Completed, Dec 1st
######################################################################

import sys, os, re, getopt, string
from xmlrpclib import Fault
from xmlrpclib import ServerProxy
from urllib import urlopen
from pysnmp.entity.rfc3413.oneliner import cmdgen


script = os.path.basename(sys.argv[0])
user = "zenoss"
passwd = 'zenoss'
util = '@zenoss'
base = "http://%s:%s%s:8080" % (user,passwd,util)
searchDevUrl = base+'/zport/dmd/Devices/searchDevices?queryString='
groupsUrl = base+'/zport/dmd/Groups/getOrganizerNames'
snmpurl = "/getSnmpOidTargets"

#####SNMP CONFIG#############
errorIndication, errorStatus, errorIndex, vServerOID = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', 'cci-ro'), cmdgen.UdpTransportTarget(('10.50.0.1', 161)), (1,3,6,1,4,1,5951,4,1,3,1,1,1) )
errorIndication, errorStatus, errorIndex, vClientOID = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', 'cci-ro'), cmdgen.UdpTransportTarget(('10.50.0.1', 161)), (1,3,6,1,4,1,5951,4,1,3,2,1,8) )
client = '2,1,8'
server = '1,1,1'
###############################

def main(args):
  for opt, val in opts:
    if opt in ('-h', '--help'):
      usage(0)
      break
    else:
      snmp_vsrv_parse(vServerOID)

def snmp_vsrv_parse(VserverOid):
  counter = 0
  for vsrv in VserverOid:
    vservOid = vsrv[0][0].prettyPrint()
    vservClient = vsrv[0][1].prettyPrint()
    p = re.compile("'")
    vserverCL = p.sub("", vservClient)
    xserv = re.sub('4.1.3.1.1.1', '4.1.3.2.1.8', vservOid)
    yserv = xserv.split('.')
    zserv = [int(x) for x in yserv]
    vserv = tuple(zserv)
    errorIndication, errorStatus, errorIndex, vHost = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', 'cci-ro'), cmdgen.UdpTransportTarget(('10.50.0.1', 161)), vserv )
    NULL = ([])
    if vHost != NULL:
      snmp_client_parse(vserverCL, vHost)

def snmp_client_parse(vserver, vclients):
   clientoid = vclients[0][0][0]
   clientname = vclients[0][0][1]
   for client in vclients:
     host = str(client[0][1])
     httpsearch = re.search("cc[0-9]{1,3}\-[0-9]{1,3}\-http", host)
     c9 = re.search("^c9", vserver)
     hostwww = re.sub("\-http", "", host)
     if httpsearch and c9 is None:
       editDevice(vserver, hostwww)

def editDevice(cluster, host):

  Zenoss = {'deviceName': '', 'devicePath': '', 'tag': '', 'serialNumber': '', 'zSnmpCommunity': 'cci-ro',
            'zSnmpPort': '161', 'zSnmpVer': 'v2c', 'rackSlot': '0', 'productionState': '1000', 'comments': '',
            'hwManufacturer': '', 'hwProductName': '', 'osManufacturer': '', 'osProductName': '',
            'locationPath': '', 'groupPaths': '', 'systemPaths': '', 'statusMonitors': '',
            'performanceMonitor': '', 'discoverProto': 'snmp', 'priority': '3'}

  Zenoss['deviceName'] = host
  Zenoss['systemPaths'] = cluster
  url = http(Zenoss['deviceName'])
  valid = re.search("http", url)
  if valid:
    snmp_out = http(url+snmpurl)
    Zenoss['zSnmpCommunity'] = snmp_out[0]
    Zenoss['zSnmpVer'] = snmp_out[1]
    sys_match = re.search("\w+", "cluster")
    if sys_match:
      Zenoss['systemPaths'] = "/%s" % (cluster)
   # groups_return = http(groupsUrl)
   # Zenoss['groupPaths'] = group_final(groups_return, Zenoss['systemPaths'])
    serv = ServerProxy (url,allow_none=1)
    serv.manage_editDevice(Zenoss['tag'], Zenoss['serialNumber'],
		  Zenoss['zSnmpCommunity'], Zenoss['zSnmpPort'], Zenoss['zSnmpVer'], Zenoss['rackSlot'],
		  Zenoss['productionState'], Zenoss['comments'], Zenoss['hwManufacturer'], Zenoss['hwProductName'],
		  Zenoss['osManufacturer'], Zenoss['osProductName'], Zenoss['locationPath'] , Zenoss['groupPaths'],
		  Zenoss['systemPaths'])
    if verbose:
      print "%s\n%s\n%s\n%s\n%s\n%s\n" % (url,Zenoss['zSnmpCommunity'],Zenoss['zSnmpVer'],Zenoss['comments'], Zenoss['systemPaths'],Zenoss['groupPaths'])

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
    snmp_ver = 'v2c'
    community = 'cci-ro'
    snmp_filter = re.sub("\[|\]|\'|\,|\(|\)", "", snmp_output)
    snmp_split = string.split(snmp_filter)
    snmp_final = [ community, snmp_ver ]
    #snmp_final = [ snmp_split[4], snmp_ver ]
    return snmp_final
  else:
    device_url = urlopen(searchDevUrl+url).geturl()
    match_url = re.search("query", device_url)
    if match_url:
      return "none"
    else:
      return device_url

#def group_final(groups, group_path):
#  y = 0
#  for b in  groups:
#    groups_match = re.search(group_path, groups[y])
#    if groups_match:
#      return groups[y]
#    y = y +1

def usage(code=0):
    print '''\nUsage: %s [-s|--switch]' % script
    -h, --help         This help message
    -v, --verbose      Added verbosity
    '''

try:
  opts, args = getopt.getopt(sys.argv[1:], ":hv",
  [ 'help', 'verbose' ]
  )
except getopt.error:
  usage(0)

help = verbose = None
for opt, val in opts:
  if opt in ('-v', '--verbose'):
    verbose = True

if __name__ == "__main__":
   main(sys.argv[1:])
