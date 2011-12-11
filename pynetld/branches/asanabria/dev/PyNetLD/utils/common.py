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

import os
import sys 
import re
import string
import getopt
from time import ctime
from socket import gethostbyaddr


try:
    from pysnmp.entity.rfc3413.oneliner import cmdgen
except Exception, e:
    print "You need to download pysnmp and pyasn1", e
    sys.exit(1)


    def verify_mac( nmac ):
        """Verifies the MAC Addresses that was inputed by the user
           And returns the newly converted nmac and the Valid code"""
        valid = ""
        if re.search("([0-9a-fA-F]{2}\:){5}[0-9a-fA-F]{2}", mac):
            nmac = re.sub("\:", " ", mac)
            valid = 1
        elif re.search("([0-9a-fA-F]{2}\-){5}[0-9a-fA-F]{2}", mac):
            nmac = re.sub("\-", " ", mac)
            valid = 1
        elif re.search("([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}", mac):
            nmac = re.sub("\s{2}", " ", re.sub("^\s|\s$", "", re.sub("\'|\,|\[|\]", "", str(re.split("([0-9a-fA-F]{2})", re.sub("\.", "", mac) ) ) ) ) )
            valid = 1
        elif re.search("([0-9a-fA-F]{2}\s){5}[0-9a-fA-F]{2}", mac):
            valid = 1
            pass
        else:
            valid = 0
        if verbose: print ctime(), " Finished Checking for mac" 
        return( nmac, valid )


    def walk( dswitch, commVlan, oid  ):
        """This function will return the table of OID's that I am walking"""
        #if verbose: print dswitch, commVlan, oid
        errorIndication, errorStatus, errorIndex, \
            generic = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', commVlan), \
            cmdgen.UdpTransportTarget((dswitch, 161)), oid)
        if errorIndication:
            return errorIndication
        return generic


    def get( device, commVlan, oid, rval, indexOid="None" ):
        """This is essentially my generic snmpget, but with options. Since if I am doing an
           snmpget, I will usually either pass a index ID or a list of ID's, This function makes
           my life easier, by not creating multiple getCmd's"""

        #if verbose: print ctime(), " In snmpget function " 
        if not isinstance(rval, int):
            rval = 0
        oidN = list(oid)
        if isinstance(indexOid, int):
            oidN.append(indexOid)
        elif type(indexOid) == list:
            oidN = oidN + map(int, indexOid)
        oidN = tuple(oidN)
        #if verbose: print oidN
        errorIndication, errorStatus, errorIndex, \
            generic = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', commVlan), \
            cmdgen.UdpTransportTarget((device, 161)), oidN)
        #if verbose: print ctime(), " Out of snmpget function " 
        if errorIndication:
            return (errorIndication, generic )
        if rval == 0:
            return (errorIndication, generic )
        elif rval == 1:
            return (errorIndication, generic[0][0] )
        elif rval == 2:
            return (errorIndication, str(generic[0][1]) )



    def hex2dec(mack):
        return int(mack, 16)

    def dec2hex(mack):
        return re.sub( "^0x", "", hex(mack) )


    def convertOctectMac(self, mack):
        """This Function will convert the OctectString into a Valid MAC Address"""
        mmap = map(hex, map(ord, mack) )
        cmac = mmap
        for i in xrange(len(mmap)):
            mmap[i] = re.sub("0x", "", mmap[i])
            mmap[i] = mmap[i].zfill(2)
        cmac = re.sub("\'|\,|\[|\]", "", str(mmap) )
        return cmac

    def convertOctectIp(self, hexip):
        """This Function will convert the OctectString into a valid Ip Address"""
        ip = map(hex, map(ord, hexip) )
        ip = map(hex2dec, ip)
        ip = re.sub("\,", ".",re.sub("\'|\[|\]|\s","", str(ip)))
        return ip

    def convertDecMac(self, mack):
        """This Function will convert the Decimal into HEX"""
        mmap = map(hex, mack) 
        cmac = mmap
        for i in xrange(len(mmap)):
            mmap[i] = re.sub("0x", "", mmap[i])
            mmap[i] = mmap[i].zfill(2)
        cmac = re.sub("\'|\,|\[|\]", "", str(mmap) )
        return cmac


