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
"""This is a complete rewrite of the get_port.py script 04/12/09
This script now accurately reports all MAC Addresses on the Port that you specified
   *Also better error checking added
   *Cleaner Code
   *Reusable Functions
This scipt is intended for Administrator/Engineers who need to find the port on a switch 
that they are plugged into using either the MAC Address or the IP Address.
So far this has been tested on Cisco Switches, though I assume it will work on other ones as well"""

import sys 
import re
import string
import getopt

try:
    from pysnmp.entity.rfc3413.oneliner import cmdgen
except Exception, e:
    print "You need to download pysnmp and pyasn1", e
    sys.exit(1)


def walk( device, commVlan, oid  ):
    """This function will return the table of OID's that I am walking"""
    errorIndication, errorStatus, errorIndex, \
        generic = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', commVlan), \
        cmdgen.UdpTransportTarget((device, 161)), oid)
    return generic


def get( device, commVlan, oid, rval, indexOid="None" ):
    """This is essentially my geeric snmpget, but with options. Since if I am doing an
       snmpget, I will usually either pass a index ID or a list of ID's, This function makes
       my life easier, by not creating multiple getCmd's"""
    communities = [ commVlan, "4u5itu", "public" ]
    if not isinstance(rval, int):
        rval = 0
    oidN = list(oid)
    if isinstance(indexOid, int):
        oidN.append(indexOid)
	oidN = tuple(oidN)
    elif type(indexOid) == list:
        for i in indexOid:
            oidN.append(i)
        oidN = tuple(oidN)
    else:
        oidN = tuple(oidN)
    for comm in communities:
        errorIndication, errorStatus, errorIndex, \
            generic = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', comm), \
            cmdgen.UdpTransportTarget((device, 161)), oidN)
        if errorIndication:
            continue
	else:
            break
    if errorIndication:
        return errorIndication
    if rval == 0:
        return generic
    elif rval == 1:
        return generic[0][0]
    elif rval == 2:
        return generic[0][1]

def findIpByMac( commVlan, oid, nmac  ):
    """This Function will only return the IP Address of the MAC you are searching for if
       the IP Address is in the ARP table.  """
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

def findMacByIp( q, nip, IPAddr ):
    """This Function will return the MAC Address if the IPAddress was in the ARP table
       if not it will return None"""
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

def convertOctect(mack):
    """This Function will convert the OctectString into HEX"""
    mmap = map(hex, map(ord, mack[0][1])) 
    cmac = ""
    for i in range(len(mmap)):
        mmap[i] = re.sub("0x", "", mmap[i])
	mmap[i] = mmap[i].zfill(2)
    cmac = re.sub("\'|\,|\[|\]", "", str(mmap) )
    return cmac

if __name__ == '__main__':
    main()
