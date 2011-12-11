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
    -o, --ostatus 	This is the Operational Status you are matching against.. Up or Down
    -a, --astatus	This is the Administrative Status you are matching against
    -s, --speed		This is the speed of the interface you want to match against.. 1gbps or 10gbps or 100mbs or 10mbs
    -n, --pname		This is where you can pass the Interface/Port name..  GigabitEthernet10/23 
    
    example below...
    python check_int_speed.py --device zenoss --community "public" --astatus "Up" --ostatus "Up"
    lo is Administratively  Up and Operationally Up and running at 10mbs
    eth0 is Administratively  Up and Operationally Up and running at 1gbps

    python check_int_speed.py --device switch --community "public" --astatus "Down" --ostatus "Down" --pname "GigabitEthernet10/23"
    GigabitEthernet10/23 is Administratively Down and Operationally Down and running at 1gbps

    python check_int_speed.py --device zenoss --community "public" --astatus "Up" --ostatus "Up" --speed "1gbps"
    eth0 is Administratively  Up and Operationally Up and running at 1gbps

    python check_int_speed.py --device switch --community "public" --astatus "Up" --ostatus "Up" --speed "1gbps"
    GigabitEthernet1/31 is Administratively  Up and Operationally Up and running at 1gbps
    GigabitEthernet1/37 is Administratively  Up and Operationally Up and running at 1gbps
    GigabitEthernet1/34 is Administratively  Up and Operationally Up and running at 1gbps

    python check_int_speed.py --device switch --community "public" --astatus "Down" --ostatus "Down"
    GigabitEthernet2/36 is Administratively  Down and Operationally Down and running at 1gbps
    Vlan1 is Administratively  Down and Operationally Down and running at 1gbps
    GigabitEthernet2/30 is Administratively  Down and Operationally Down and running at 1gbps
    GigabitEthernet10/20 is Administratively  Down and Operationally Down and running at 1gbps
    GigabitEthernet10/21 is Administratively  Down and Operationally Down and running at 1gbps

    """
    sys.exit(0)

def main():
    if ( community and device ):
        errorIndication, errorStatus, errorIndex, \
	    PortName = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', community), \
	    cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,2,2,1,2))
        errorIndication, errorStatus, errorIndex, PortAdminStatus = \
	    cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData\
	    ('test-agent', community),cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,2,2,1,7))
        errorIndication, errorStatus, errorIndex, PortOperStatus = \
	    cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData\
	    ('test-agent', community),cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,2,2,1,8))
        errorIndication, errorStatus, errorIndex, PortSpeed = \
	    cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData\
	    ('test-agent', community),cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,2,2,1,5))
    else:
        usage()

    portinfo = {}
    portspeed = {
            10000000000 : "10gbps",
            4294967295  : "10gbps",
	        1000000000  : "1gbps",
	        100000000   : "100mbs",
	        10000000    : "10mbs",
	        0           : "0mbs"
	        }

    portstatus = {
                 1 : "Up",
                 2 : "Down"
	         }


    for index in xrange(len(PortName)):
        pname = PortName[index][0][1]
        padminstatus = PortAdminStatus[index][0][1]
        poperstatus = PortOperStatus[index][0][1]
        pspeed = PortSpeed[index][0][1]
        portinfo[pname] =  [ [ portstatus[padminstatus], padminstatus ], [ portstatus[poperstatus], poperstatus ], [ portspeed[pspeed], pspeed ] ] 
    printPorts(portinfo)

def printPorts(portinfo):
    count = 0
    if pname:
        if portinfo.has_key(pname):
            if portinfo[pname][0][1] == 1 or portinfo[pname][1][1] == 1:
                stat = 0
                print "OK %s is Administratively %s and Operationally %s and running at %s| admin=%s oper=%s speed=%s" \
                    % (pname, portinfo[pname][0][0], portinfo[pname][1][0], portinfo[pname][2][0], portinfo[pname][0][1], \
                    portinfo[pname][1][1], portinfo[pname][2][1])
            elif portinfo[pname][0][1] == 2 or portinfo[pname][1][1] == 2:
                stat = 2
                print "CRITICAL %s is Administratively %s and Operationally %s and running at %s| admin=%s oper=%s speed=%s" \
                    % (pname, portinfo[pname][0][0], portinfo[pname][1][0], portinfo[pname][2][0], portinfo[pname][0][1],
                    portinfo[pname][1][1], portinfo[pname][2][1])
            sys.exit(stat)
        else:
            print "Interface %s does not exist" % (pname)
            sys.exit(2)
    status= ''
    STAT = 0
    for key, value in portinfo.items():
        #if value[0][0] == astatus and value[1][0] == ostatus and value[2][0] == speed:
        count += 1
        if value[0][1] == 1 or value[1][1] == 1:
            status += "OK %s is Administratively %s and Operationally %s and running at %s| admin=%s oper=%s speed=%s\n" \
                % (key, value[0][0], value[1][0], value[2][0], value[0][1],
                value[1][1], value[2][1])
        else:
            STAT = 1
            status += "CRITICAL %s is Administratively %s and Operationally %s and running at %s| admin=%s oper=%s speed=%s\n" \
                % (key, value[0][0], value[1][0], value[2][0], value[0][1],
                value[1][1], value[2][1])
    if count == 0:        
       print "There aren't any interfaces that are %s and running at %s" % (astatus, speed)
    else:
       print status
       sys.exit(STAT)

try:
     opts, args = getopt.getopt(sys.argv[1:], "c:d:p:i:s:a:o:n:h:",
     [ 'community=', 'device=', 'port=', 'pname=', 'intname=', 'astatus=', 'ostatus=', "speed=", 'help' ]
     )

except getopt.error:
     usage()
help = community = device = port = pname = intname = astatus = ostatus = speed = None

for opt, val in opts:
    if opt in ('-c', '--community'):
        community = val
    if opt in ('-d', '--device'):
        device = val
    if opt in ('-p', '--port'):
        port = val
    if opt in ('-n', '--pname'):
        pname = val
    if opt in ('-i', '--intname'):
        intname = val
    if opt in ('-o', '--ostatus'):
        ostatus = val
    if opt in ('-a', '--astatus'):
        astatus = val
    if opt in ('-s', '--speed'):
        speed = val
    if opt in ('-h', '--help'):
        help = usage()



if __name__ == '__main__':
    main()
