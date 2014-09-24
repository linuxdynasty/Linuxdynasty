#!/usr/bin/env python
#Copyright (C) 2009  Allen Sanabria
#this is the equivalent of sho cdp nei on a cisco switch, but this is using snmp
#This program is free software; you can redistribute it and/or modify it under 
#the terms of the GNU General Public License as published by the Free Software Foundation;
#either version 2 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#See the GNU General Public License for more details. You should have received a copy of i
#the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""Revision 1.2 9/13/2009
   Catch all CDP connected switches, even if there is more then 1 switch seen
   through 1 port.
"""
"""Revision 1.1 9/11/2009
   Added --type option ( --type=detail )
"""
"""Revision 1.0 9/10/2009
   this is the equivalent of sho cdp nei on a cisco switch, but this is using snmp
"""
import os
import sys
import re
import string
import getopt


try:
    from pysnmp.entity.rfc3413.oneliner import cmdgen
except Exception, e:
    print "You need to download pysnmp and pyasn1", e
    sys.exit(1)

def main():
    cdp_table = {}
    ifTable = {}
    ifIndexTable =  walk( device, community, oTable["ifName"])
    address = walk( device, community, cdpTable["cdpCacheAddress"])
    deviceversion = walk( device, community, cdpTable["cdpCacheVersion"])
    deviceid = walk( device, community, cdpTable["cdpCacheDeviceId"])
    deviceport = walk( device, community, cdpTable["cdpCacheDevicePort"])
    deviceplatform = walk( device, community, cdpTable["cdpCachePlatform"])
    devicecapabilities = walk( device, community, cdpTable["cdpCacheCapabilities"])
    devicevtpmgmtdomain = walk( device, community, cdpTable["cdpCacheVTPMgmtDomain"])
    devicevlan = walk( device, community, cdpTable["cdpCacheNativeVLAN"])
    deviceduplex = walk( device, community, cdpTable["cdpCacheDuplex"])
    count =0
    for ifIndex in ifIndexTable[1]:
        ifTable[str(ifIndex[0][0][-1])] = str(ifIndex[0][1])
    for host in address[1]:
        cdp_table[str(host[0][0][-2:])] = {}
        cdp_table[str(host[0][0][-2:])]["ipaddr"] = convertOctectIp(str(host[0][1]))
    for host in deviceid[1]:
        cdp_table[str(host[0][0][-2:])]["name"] = str(host[0][1])
    for host in deviceport[1]:
        cdp_table[str(host[0][0][-2:])]["rport"] = str(host[0][1])
        cdp_table[str(host[0][0][-2:])]["lport"] = ifTable[str(host[0][0][-2])]
    for host in deviceplatform[1]:
        cdp_table[str(host[0][0][-2:])]["platform"] = str(host[0][1])
    for host in deviceversion[1]:
        cdp_table[str(host[0][0][-2:])]["version"] = str(host[0][1])
    for host in devicecapabilities[1]:
        cdp_table[str(host[0][0][-2:])]["capabilities"] = cdpCapabiltiyTable[hex(ord(host[0][1][-1]))]
    for host in devicevtpmgmtdomain[1]:
        cdp_table[str(host[0][0][-2:])]["domain"] = str(host[0][1])
    for host in devicevlan[1]:
        cdp_table[str(host[0][0][-2:])]["vlan"] = str(host[0][1])
    for host in deviceduplex[1]:
        cdp_table[str(host[0][0][-2:])]["duplex"] = duplex[int(host[0][1])]
    if type == "detail":
        sho_cdp_neighbor_detail(cdp_table)
    elif type == "normal":
        sho_cdp_neighbor(cdp_table)
def sho_cdp_neighbor_detail(cdp_table):
    for key in cdp_table:
        print "-"*30
        print PrintFormat("Device ID: " + cdp_table[key]["name"], 5)
        print "Entry address(es): "
        print " IP address: ", cdp_table[key]["ipaddr"]
        print PrintFormat("Platform: " + cdp_table[key]["platform"] + ",", 10), PrintFormat(" Capabilities: "+ cdp_table[key]["capabilities"], 5)
        print PrintFormat("Interface: " + cdp_table[key]["lport"] + ",", 10), PrintFormat("Port ID (outgoing port): " + cdp_table[key]["rport"],5)
        print "\n"
        print "Version :"
        print cdp_table[key]["version"]
        print "\n"
        try:
            print PrintFormat("VTP Management Domain: " + cdp_table[key]["domain"], 5)
        except Exception, e:
            pass
        print PrintFormat("Duplex: " + cdp_table[key]["duplex"], 5)
        print "Management address(es):"
        print " IP address: ", cdp_table[key]["ipaddr"]
        print "\n"
        print "-"*30
        print "\n"

def sho_cdp_neighbor(cdp_table):
    columnA = 40
    columnB = 20
    columnC = 20
    columnD = 30
    print "Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge"
    print "                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone"
    print PrintFormat("Device ID", columnA), PrintFormat("Local Interface", columnB), PrintFormat("Capability", columnC), \
          PrintFormat("Platform", columnD), PrintFormat("Remote Interface", columnC)
    for key in cdp_table:
        print PrintFormat(cdp_table[key]["name"], columnA), PrintFormat(cdp_table[key]["lport"], \
              columnB), PrintFormat(cdp_table[key]["capabilities"], columnC), PrintFormat(cdp_table[key]["platform"], columnD), \
              PrintFormat(cdp_table[key]["rport"], columnC)

def hex2dec(mack):
    return int(mack, 16) 

def dec2hex(mack):
    return re.sub( "^0x", "", hex(mack) )

def convertOctectIp(hexip):
    """This Function will convert the OctectString into HEX"""
    ip = map(hex, map(ord, hexip) )
    ip = map(hex2dec, ip) 
    ip = re.sub("\,", ".",re.sub("\'|\[|\]|\s","", str(ip)))
    return ip

def PrintFormat(variable, width):
    varOut = variable + ' '  * ( width - len(variable) )
    return varOut


def walk( dswitch, commVlan, oid  ):  
    """This function will return the table of OID's that I am walking"""
    if verbose: print dswitch, commVlan, oid 
    errorIndication, errorStatus, errorIndex, \
    generic = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', commVlan), \
    cmdgen.UdpTransportTarget((dswitch, 161)), oid)
    return ( (errorIndication, generic) )


def get( device, commVlan, oid, rval, indexOid="None" ):
    """This is essentially my generic snmpget, but with options. Since if I am doing an
    snmpget, I will usually either pass a index ID or a list of ID's, This function makes
    my life easier, by not creating multiple getCmd's"""

    if verbose: print ctime(), " In snmpget function " 
    if not isinstance(rval, int):
        rval = 0 
        oidN = list(oid)
    if isinstance(indexOid, int):
        oidN.append(indexOid)
    elif type(indexOid) == list:
        oidN = oidN + map(int, indexOid)
        oidN = tuple(oidN)
    if verbose: print oidN
    errorIndication, errorStatus, errorIndex, \
        generic = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', commVlan), \
        cmdgen.UdpTransportTarget((device, 161)), oidN)
    if verbose: print ctime(), " Out of snmpget function " 
    if errorIndication:
        return (errorIndication, generic )
    if rval == 0:
        return (errorIndication, generic )
    elif rval == 1:
        return (errorIndication, generic[0][0] )
    elif rval == 2:
        return (errorIndication, str(generic[0][1]) )

def usage():
    print """
    '-d, --device=switch'             This is the device you are connecting to.
    '-t, --type=normal|detail'        The default type is normal ( show cdp neighbor ), 
                                      The option is detail ( show cdp neighbor detail )
    '-c, --community=public'          This is the SNMP community string you are using to connect to the device.
    '-h, --help'                      Call this help menu.
    '-v', --verbose'
    """
    sys.exit(1)

cdpTable = { 
            "cdpCacheAddress"            : (1,3,6,1,4,1,9,9,23,1,2,1,1,4),
            "cdpCacheVersion"            : (1,3,6,1,4,1,9,9,23,1,2,1,1,5),
            "cdpCacheDeviceId"           : (1,3,6,1,4,1,9,9,23,1,2,1,1,6),
            "cdpCacheDevicePort"         : (1,3,6,1,4,1,9,9,23,1,2,1,1,7),
            "cdpCachePlatform"           : (1,3,6,1,4,1,9,9,23,1,2,1,1,8),
            "cdpCacheCapabilities"       : (1,3,6,1,4,1,9,9,23,1,2,1,1,9),
            "cdpCacheVTPMgmtDomain"      : (1,3,6,1,4,1,9,9,23,1,2,1,1,10),
            "cdpCacheNativeVLAN"         : (1,3,6,1,4,1,9,9,23,1,2,1,1,11),
            "cdpCacheDuplex"             : (1,3,6,1,4,1,9,9,23,1,2,1,1,12),
            "cdpGlobalMessageInterval"   : (1,3,6,1,4,1,9,9,23,1,3,1,0),
            "cdpGlobalHoldTime"          : (1,3,6,1,4,1,9,9,23,1,3,1,1),
            "cdpGlobalDeviceId"          : (1,3,6,1,4,1,9,9,23,1,3,1,2)
           }  

cdpCapabiltiyTable = {
                     "0x1" : "R",
                     "0x2" : "T",
                     "0x4" : "B",
                     "0x8" : "S",
                     "0x9"  : "R S",
                     "0x10" : "H",
                     "0x11" : "R H",
                     "0x12" : "T H",
                     "0x13" : "R T H",
                     "0x14" : "B H",
                     "0x15" : "R B H",
                     "0x16" : "T B H",
                     "0x18" : "S H",
                     "0x20" : "I",
                     "0x21" : "R I",
                     "0x22" : "T I",
                     "0x23" : "T R I",
                     "0x24" : "B I",
                     "0x25" : "R B I",
                     "0x28" : "S I",
                     "0x29" : "R S I",
                     "0x30" : "H I",
                     "0x31" : "R H I",
                     "0x32" : "T H I",
                     "0x33" : "R T H I",
                     "0x34" : "B H I",
                     "0x40" : "r"
                     }

oTable = {
         "ifName" : (1,3,6,1,2,1,31,1,1,1,1)
         }

duplex = { 
          1 : "unknown",
          2 : "halfDuplex",
          3 : "fullDuplex",
          '': "NotSet"
         }  
try:
    opts, args = getopt.getopt(sys.argv[1:], "c:d:t:hv",
          [ 'community=', 'device=', 'type=', 'help', 'verbose' ]
          )   
except getopt.error:
    usage()

help = community = device = verbose = None
type = "normal"

for opt, val in opts:
    if opt in ('-c', '--community'):
        community = val 
    if opt in ('-d', '--device'):
        device = val 
    if opt in ('-t', '--type'):
        type = val 
    if opt in ('-h', '--help'):
        help = usage()
    if opt in ('-v', '--verbose'):
        verbose = True

                                                                                                                       

if __name__ == '__main__' and device and community:
    main()
else:
    usage()
