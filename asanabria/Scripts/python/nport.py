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

def usage():
    print """
    -d, --device	This is the device you want to scan
    -c, --community	This is the SNMP community string to use
    -m, --mac 		This is the MAC Address you are using to search foir what port your device is plugged into
    -i, --ip		This is the IP Address you are using to find the MAC Address of the device and The port in the switched it is plugged into
    -n, --pname		This is the Port Name you are searching For
    example below..
    python port_report.py -d 192.168.101.1 -c public -i "192.168.101.201"
    This IPAddress is not in the ARP table

    python port_report.py -d 192.168.101.1 -c public -i "192.168.101.209"
    MAC  = 00 14 38 7f 6e 38
    Port = GigabitEthernet1/17
    Vlan = 175
    IPAddr = 192.168.101.209

    python port_report.py -d 192.168.101.1 -c public -m "00 14 38 4f 5e 39"
    MAC  = 00 14 38 4f 5e 39
    Port = GigabitEthernet1/17
    Vlan = 175
    IPAddr = 192.168.101.201

    python port_report.py -d 192.168.101.1 -c public -n "1/40"
    Port 1/40 has the below MAC Addresses associated with it
    MAC  = 00 1b 95 97 3c 81
    Port = GigabitEthernet1/40
    Vlan = 1
    IPAddr = The IP Address for this MAC is not in the ARP Table

    MAC  = 00 15 fa b4 10 06
    Port = GigabitEthernet1/40
    Vlan = 174
    IPAddr = The IP Address for this MAC is not in the ARP Table

    Total MAC Addresses associated with this interface 2

    python port_report.py -d 192.168.101.1 -c public -n "1/2"
    Port 1/2 has the below MAC Addresses associated with it
    MAC  = 08 00 0f 20 b3 aa
    Port = GigabitEthernet1/2
    Vlan = 176
    IPAddr = 192.168.101.104

    MAC  = 08 00 0f 21 d3 78
    Port = GigabitEthernet1/2
    Vlan = 173
    IPAddr = 192.168.101.105

    MAC  = 08 00 0f 20 b3 aa
    Port = GigabitEthernet1/2
    Vlan = 175
    IPAddr = 192.168.101.115
    
    """
    sys.exit(0)


def main():
    if ( community and device and ( mac or ip or pname ) ):
        commTable = walk( device, community, oTable["entLogicalCommunity"] ) 
	indexOid = ""
	rval = ""
	ifIndex = ""
	nip = ""
	nmac = ""
	ipAddr = ""
        if mac or ip:
	    if mac:
	        nmac = mac
		if re.search("([0-9a-fA-F]{2}\:){5}[0-9a-fA-F]{2}", mac):
		    nmac = re.sub("\:", " ", mac)
		elif re.search("([0-9a-fA-F]{2}\-){5}[0-9a-fA-F]{2}", mac):
		    nmac = re.sub("\-", " ", mac)
		elif re.search("([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}", mac):
		    nmac = re.sub("\s{2}", " ", re.sub("^\s|\s$", "", re.sub("\'|\,|\[|\]", "", str(re.split("([0-9a-fA-F]{2})", re.sub("\.", "", mac) ) ) ) ) )
		elif re.search("([0-9a-fA-F]{2}\s){5}[0-9a-fA-F]{2}", mac):
		    pass
		else:
		    print "you mac %s is in the wrong format" % (mac)
	            sys.exit(1)

	    if ip:
	        nip = ip
	        physTable = walk( device, community, oTable["atPhysAddress"] )
	        nmac = findMacByIp( device, nip, physTable )
	        if nmac == None:
	            print "This IPAddress is not in the ARP table"
		    sys.exit(1)
	    count = 0
            for comm in commTable:
                vlan = re.search( "\@(\d+)", str(comm[0][1]) ).group(1)
                macVlanTable = walk( device, comm[0][1], oTable["dot1dTpFdbAddress"] )
		if ( len(macVlanTable) > 0 ):
	            for macVlan in macVlanTable:
	                dM = list(macVlan[0][0][-6:])
                        if re.search(nmac, convertOctect(macVlan)):
			    count += 1
			    rval = 2
		            bIndex = int(get( device, comm[0][1], oTable["dot1dTpFdbPort"], rval, indexOid = dM ))
		            ifIndex = int(get( device, comm[0][1], oTable["dot1dBasePortIfIndex"], rval, indexOid = bIndex ))
		            ifDescr = str(get( device, comm[0][1], oTable["ifDescr"], rval, indexOid = ifIndex ))
		            ifSpeed = portspeed[get( device, comm[0][1], oTable["ifSpeed"], rval, indexOid = ifIndex )]
		            ifDuplex = duplex[get( device, comm[0][1], oTable["dot3StatsDuplexStatus"], rval, indexOid = ifIndex )]
                            if ip:
			        ipAddr = nip
			    else:
			        ipAddr = findIpByMac( comm[0][1], oTable["atPhysAddress"], nmac )
			    if re.search("(\d{1,3}\.){3}\d{1,3}", ipAddr ):
			        sysName = get( ipAddr, community, oTable["sysName"], rval )
			        sysDescr = get( ipAddr, community, oTable["sysDescr"], rval )
				print "SwitchPort = %s\nSwitchPortSpeed = %s\nSwitchPortDuplex = %s\nSwitchVlan = %s" % ( ifDescr, ifSpeed, ifDuplex, vlan )
			        print "HostName = %s\nHostDescr = %s\nHostMAC  = %s\nHostIP = %s\n" % ( sysName, sysDescr, nmac, ipAddr )
			    else:
			        print "MAC  = %s\nPort = %s\nSpeed = %s\nDuplex = %s\nVlan = %s\nIPAddr = %s\n" % ( nmac, ifDescr, ifSpeed, ifDuplex, vlan, ipAddr )
			    break
	        else:
		    continue
	        if count >= 1:
	            break
	        else:
                    continue
	    if count == 0:
	        print "This MAC %s Address is not part of any Vlan" % ( nmac )
		sys.exit(1)
	         
	if pname:
	    count = 0
	    mcount = 0
	    ifNameTable = walk( device, community, oTable["ifName"] )
	    pnamem = "\b\w+"+pname+"\b|\b"+pname+"\b"
	    pnamew = "\b\w+"+pname+"\b"
	    for iface in ifNameTable:
	        if ( re.search("[A-Z]+"+pname+"|"+pname, str(iface[0][1])) ):
		    count +=1
		    ifIndex = int(iface[0][0][-1])
		    break
	    if count == 0:
		print "Port passed does not match a given port name on the ifName snmp table"
		sys.exit(1)
            print "Port %s has the below MAC Addresses associated with it" % ( pname )
	    for comm in commTable:
                vlan = re.search( "\@(\d+)", str(comm[0][1]) ).group(1)
                vIfIndexTable = walk( device, comm[0][1], oTable["dot1dBasePortIfIndex"] )
		if ( len(vIfIndexTable) > 0 ):
	            for v in vIfIndexTable:
		        if ( ifIndex == int(v[0][1]) ):
		            bIndex = int(v[0][0][-1])
			    dM = walk( device, comm[0][1], oTable["dot1dTpFdbPort"] )
			    for d in dM:
			        if ( bIndex == int(d[0][1]) ):
				    mcount += 1
				    rval = 0
		                    nmac =  convertOctect( get( device, comm[0][1], oTable["dot1dTpFdbAddress"], rval, indexOid = list(d[0][0][-6:]) ) )
				    rval = 2
		                    ifDescr = get( device, comm[0][1], oTable["ifDescr"], rval, indexOid = ifIndex )
				    ipAddr = findIpByMac( comm[0][1], oTable["atPhysAddress"], nmac )
		                    ifSpeed = portspeed[get( device, comm[0][1], oTable["ifSpeed"], rval, indexOid = ifIndex )]
		                    ifDuplex = duplex[get( device, comm[0][1], oTable["dot3StatsDuplexStatus"], rval, indexOid = ifIndex )]
			            if re.search("(\d{1,3}\.){3}\d{1,3}", ipAddr ):
			                sysName = get( ipAddr, community, oTable["sysName"], rval )
			                sysDescr = get( ipAddr, community, oTable["sysDescr"], rval )
				        print "SwitchPort = %s\nSwitchPortSpeed = %s\nSwitchPortDuplex = %s\nSwitchVlan = %s" % ( ifDescr, ifSpeed, ifDuplex, vlan )
			                print "HostName = %s\nHostDescr = %s\nHostMAC  = %s\nHostIP = %s\n" % ( sysName, sysDescr, nmac, ipAddr )
			            else:
			                print "MAC  = %s\nPort = %s\nSpeed = %s\nDuplex = %s\nVlan = %s\nIPAddr = %s\n" % ( nmac, ifDescr, ifSpeed, ifDuplex, vlan, ipAddr )
	        else:
		   continue
            print "Total MAC Addresses associated with this interface %d" % ( mcount )
    else:
        usage()

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
	   "ifSpeed" : (1,3,6,1,2,1,2,2,1,5),
	   "ifAlias" : (1,3,6,1,2,1,31,1,1,1,18),
	   "sysName" : (1,3,6,1,2,1,1,5,0),
	   "sysDescr" : (1,3,6,1,2,1,1,1,0),
	   "dot3StatsDuplexStatus" : (1,3,6,1,2,1,10,7,2,1,19),
	   "atPhysAddress" : (1,3,6,1,2,1,3,1,1,2)
	 }

portspeed = { 
             10000000000 : "10gbps",
             4294967295  : "10gbps",
	     1000000000  : "1gbps",
	     100000000   : "100mbs",
	     10000000    : "10mbs",
	     0           : "0mbs"
	    }   

duplex = {
          1 : "unknown",
          2 : "halfDuplex",
	  3 : "fullDuplex"
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
