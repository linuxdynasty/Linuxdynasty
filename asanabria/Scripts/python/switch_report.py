#!/usr/bin/env python
#Copyright (C) 2009  Allen Sanabria
#This program is free software; you can redistribute it and/or modify it under 
#the terms of the GNU General Public License as published by the Free Software Foundation;
#either version 2 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#See the GNU General Public License for more details. You should have received a copy of i
#the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#This is the 1st revision of this script... 04/07/09
#Now at the 4th revision 1.4 04/09/09
#This scipt is intended for Administrator/Engineers who need to find the port on a switch 
#that they are plugged into using either the MAC Address or the IP Address.
#So far this has been tested on Cisco Switches, though I assume it will work on other ones as well

import sys 
import re
import string
import getopt

try:
    from pysnmp.entity.rfc3413.oneliner import cmdgen
except Exception, e:
    print "You need to download pysnmp and pyasn1", e
    sys.exit(1)

def usage():
    print """
    -d, --device	This is the device you want to scan
    -c, --community	This is the SNMP community string to use
     example below...
     python switch_report.py -d 192.168.101.1 -c public
     GigabitEthernet1/40,00 1b 90 99 3a 81,vlan1,
     GigabitEthernet10/15,00 23 5e ef 31 82,vlan1,GIG Laser office


    """
    sys.exit(0)


def main():
   if device and community:
       report()
   else:
       usage()

def walk( commVlan, oid  ):
    errorIndication, errorStatus, errorIndex, \
        generic = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', commVlan), \
        cmdgen.UdpTransportTarget((device, 161)), oid)
    return generic


def get( commVlan, oid, indexOid="None" ):
    oidN = list(oid)
    if isinstance(indexOid, int):
        oidN.append(indexOid)
	oidN = tuple(oidN)
    elif type(indexOid) == list:
        for i in indexOid:
            oidN.append(i)
        oidN = tuple(oidN)
    errorIndication, errorStatus, errorIndex, \
        generic = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', commVlan), \
        cmdgen.UdpTransportTarget((device, 161)), oidN)
    return generic

def findIpByMac( commVlan, oid, nmac  ):
    """This Function will return the IP Address that is attached to the mac """
    errorIndication, errorStatus, errorIndex, \
        PhysAddr = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', commVlan), \
        cmdgen.UdpTransportTarget((device, 161)), (oid))
    for mack in PhysAddr:
        cmac = convertOctect(mack)
        if re.search(nmac, cmac, re.IGNORECASE):
	    ipAddr = re.sub("\'|\(|\)|,", "", str(mack[0][0][-4:])).replace(" ", ".")
	    break
	else:
	    ipAddr = "The IP Address for this MAC is not in the ARP Table"
    return( ipAddr )

def findMacByIp( nip, IPAddr ):
    """This Function will return the MAC Address and its table"""
    count = 0
    nmac = ""
    for ipAddress in IPAddr:
	ipmap = re.sub("\'|\[|\]|\(|\)", "", re.sub(",\s", ".", str(ipAddress[0][0][-4:])))
	if ( re.search(nip, ipmap) ):
	    count += 1
	    nmac = convertOctect(ipAddress)
	    break
    if count == 1:
        return( nmac )
    else:
        nmac = None
	return( nmac )

def report():
   commTable = walk( community, oTable['entLogicalCommunity'] ) 
   conn_output = open("connnected_ports_on_"+device+".csv", "a")
   for comm in commTable:
     vlan = re.search( "\@(\d+)", str(comm[0][1]) ).group(1)
     bridgeTable = walk( comm[0][1], oTable['dot1dBasePort'] )
     if ( len(bridgeTable) == 0 ):
         continue
     for bindex in bridgeTable:
       ifI = get( comm[0][1], oTable['dot1dBasePortIfIndex'], indexOid = int(bindex[0][1]) )
       ifIndex = int(ifI[0][1])
       port = get( comm[0][1], oTable['ifDescr'], indexOid = ifIndex )
       port = port[0][1]
       decMacTable = walk( comm[0][1], oTable['dot1dTpFdbPort'] )
       decMac = ""
       if ( len(decMacTable) > 0 ):
         for dm in decMacTable:
	     if dm[0][1] == bindex[0][1]:
		 if ( len(dm[0][0]) > 0 ):
	             decMac = list(dm[0][0][-6:])
		     if ( len(decMac) == 0 ):
		         continue
	             else:
	                 mac = get( comm[0][1], oTable['dot1dTpFdbAddress'], indexOid = decMac )
			 mac = convertOctect(mac)
			 if ( len(mac) > 1 ):
			   alias = get( comm[0][1], oTable['ifAlias'], indexOid = ifIndex )
			   output = "%s,%s,vlan%s,%s\n" % ( port,mac,vlan,alias[0][1] )
			   print output
		           conn_output.write(output)
		           conn_output.flush()
		 else:
		     continue
         else:
	   continue
    
def convertOctect(mack):
    """This Function will convert the OctectString into HEX"""
    mmap = map(hex, map(ord, mack[0][1])) 
    cmac = ""
    for i in range(len(mmap)):
        mmap[i] = re.sub("0x", "", mmap[i])
	mmap[i] = mmap[i].zfill(2)
    cmac = re.sub("\'|\,|\[|\]", "", str(mmap) )
    return cmac

try:
     opts, args = getopt.getopt(sys.argv[1:], "c:d:i:m:n:h:",
     [ 'community=', 'device=', "mac=", 'ip=', 'pname=' 'help' ]
     )

except getopt.error:
     usage()
help = community = device = mac = ip = pname = None

oTable = { "entLogicalCommunity" : (1,3,6,1,2,1,47,1,2,1,1,4),
           "dot1dBasePort" : (1,3,6,1,2,1,17,1,4,1,1),
	   "dot1dTpFdbPort" : (1,3,6,1,2,1,17,4,3,1,2),
           "dot1dBasePortIfIndex" : (1,3,6,1,2,1,17,1,4,1,2),
	   "dot1dTpFdbAddress" :  (1,3,6,1,2,1,17,4,3,1,1),
	   "ifDescr" : (1,3,6,1,2,1,2,2,1,2),
	   "ifName" : (1,3,6,1,2,1,31,1,1,1,1),
	   "ifAlias" : (1,3,6,1,2,1,31,1,1,1,18),
	   "atPhysAddress" : (1,3,6,1,2,1,3,1,1,2)
	 }


for opt, val in opts:
    if opt in ('-c', '--community'):
        community = val
    if opt in ('-d', '--device'):
        device = val
    if opt in ('-m', '--mac'):
        mac = val
    if opt in ('-i', '--ip'):
        ip = val
    if opt in ('-n', '--pname'):
        pname = val
    if opt in ('-h', '--help'):
        help = usage()



if __name__ == '__main__':
    main()
