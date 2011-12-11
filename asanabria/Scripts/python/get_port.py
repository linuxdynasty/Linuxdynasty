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
    -m, --mac 		This is the MAC Address you are using to search foir what port your device is plugged into
    -i, --ip		This is the IP Address you are using to find the MAC Address of the device and The port in the switched it is plugged into
    -n, --pname		This is the Port Name you are searching For
    
    example below...
    python get_port.py -d "switch" -c "community" -m "mac address"

    MAC Address = 00 14 28 1f 2d 38
    IP Address = 192.168.101.100
    PortDescr = Vlan175
    Port = GigabitEthernet1/17

    python get_port.py -d "switch" -c "community" -i "ip address"

    MAC Address = 00 14 28 1f 2d 38
    IP Address = 192.168.101.100
    PortDescr = Vlan175
    Port = GigabitEthernet1/17

    python get_port.py -d "switch" -c "community" -n "2/16"

    Port 2/16
    MAC Address = 00 50 56 ab 67 b4
    IP Address = 192.168.101.101
    PortDescr = GigabitEthernet2/16


    """
    sys.exit(0)

def main():
    if ( community and device and ( mac or ip or pname ) ):
	nmac = ""
	mtabel = ""
        count = 0
	if ( pname ):
	   count += 1
	   indexPort, indexDescr = findIndex( pname )
	   vlanComm, vlanIndex = findCommunity( indexPort )
	   decNmac = findDecMacReverse( vlanComm, vlanIndex )
	   nmac = findMacReverse( vlanComm, decNmac )
	   ipAddr = findIpByMac( nmac )
           print "\nPort %s\n  MAC Address = %s\n  IP Address = %s\n  PortDescr = %s\n" % ( pname, nmac, ipAddr, indexDescr )
	if ( mac or ip ):
	    if mac:
                nmac = mac
                if re.search("([0-9a-fA-F]{2}\:){5}[0-9a-fA-F]{2}", mac):
                    nmac = re.sub("\:", " ", mac)
                elif re.search("([0-9a-fA-F]{2}\s){5}[0-9a-fA-F]{2}", mac):
                    pass
                else:
                    print "you mac %s is in the wrong format" % (mac)
	            sys.exit(1)
                errorIndication, errorStatus, errorIndex, \
	            PhysAddr = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', community), \
	            cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,3,1,1,2))
	    elif ip:
	        nip = ip
                errorIndication, errorStatus, errorIndex, \
	            IPAddr = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', community), \
	            cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,4,22,1,3))
	        PhysAddr, nmac = findMacByIp( nip, IPAddr )

            if len(PhysAddr) >= 1:
	        if len(PhysAddr) == 1:
	            mack = PhysAddr
	            count += 1
		    cmac = convertOctect(PhysAddr)
	        elif len(PhysAddr) > 1:
                    for mack in PhysAddr:
                        cmac = convertOctect(mack)
                        if re.search(nmac, cmac, re.IGNORECASE):
                            count += 1
			    break
	        ipAddr = findIpByMac( nmac )
                vlanID, pdescr = tbltranslate( nmac, mack )
                #vlanID, ipAddr, pdescr = tbltranslate( nmac, mack )
	        decVlanMac, listDecVlanMac = findVlanMac(vlanID, nmac)
	        portName = findPort(vlanID, decVlanMac, listDecVlanMac, nmac )
                print "\nMAC Address = %s\nIP Address = %s\nPortDescr = %s\nPort = %s\n" % (nmac, ipAddr, pdescr, portName )
	        sys.exit(0)

        if count < 1:
            print "MAC Address %s is not on this switch" % (mac)
            sys.exit(1)
    else:
        usage()

def findIpByMac( nmac ):
    """This Function will return the IP Address that is attached to the mac """
    errorIndication, errorStatus, errorIndex, \
        PhysAddr = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', community), \
        cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,3,1,1,2))
    if len(PhysAddr) >= 1:
	if len(PhysAddr) == 1:
	    mack = PhysAddr
	    count += 1
	    cmac = convertOctect(PhysAddr)
	    ipAddr = re.sub("\'|\(|\)|,", "", str(mack[0][0][-4:])).replace(" ", ".")
	elif len(PhysAddr) > 1:
            for mack in PhysAddr:
                cmac = convertOctect(mack)
                if re.search(nmac, cmac, re.IGNORECASE):
		    ipAddr = re.sub("\'|\(|\)|,", "", str(mack[0][0][-4:])).replace(" ", ".")
		    break
    return( ipAddr )


def findMacByIp( nip, IPAddr ):
    """This Function will return the MAC Address and its table"""
    count = 0
    iptm = []
    for ipAddress in IPAddr:
        ipmap = map(hex, map(ord, ipAddress[0][1])) 
        for i in range(len(ipmap)):
            ipmap[i] = int(ipmap[i], 16) 
	ipmap = re.sub("\'|\[|\]", "", re.sub(",\s", ".", str(ipmap)))
	if ( re.search(nip, ipmap) ):
	    count += 1
   	    iptm = list(ipAddress[0][0][-5:])
	    break
    if count == 1:
        errorIndication, errorStatus, errorIndex, \
	    PhysMac1 = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', community), \
	    cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,3,1,1,2,iptm[0],1,iptm[1],iptm[2],iptm[3],iptm[4]))
        Mac = convertOctect(PhysMac1)
        return(PhysMac1, Mac)

def tbltranslate( nmac, mack ):
    """This function will return the ipAddress, Port Description and the VlanID"""
    #ipAddr = re.sub("\'|\(|\)|,", "", str(mack[0][0][-4:])).replace(" ", ".")
    indexId = str(mack[0][0][-6])
    errorIndication, errorStatus, errorIndex, \
        PortDescr = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', community), \
	cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,2,2,1,2,int(indexId)))
    if re.search("\d+", str(PortDescr[0][1])):
        vlanID = re.search("\d+", str(PortDescr[0][1])).group()
        return(vlanID, PortDescr[0][1])
        #return(vlanID, ipAddr, PortDescr[0][1])
    else:
        print "MAC %s does not have a Vlan ID %s " % ( nmac, PortDescr[0][1] )
	sys.exit(1)
    
def findDecMacReverse( communityVlan, vIndex ):
    """This function will return the decimal converted MAC that is tied to the Bridge ID
       dot1dTpFdbPort = 1.3.6.1.2.1.17.4.3.1.2.0"""
    count = 0
    errorIndication, errorStatus, errorIndex, \
        decMacT = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', communityVlan), \
        cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,17,4,3,1,2,0))
    for v in decMacT:
        bridgeId = int(v[0][1])
        if ( bridgeId == vIndex ):
	    count += 1
	    decMac = list(v[0][0][-5:])
	    return( decMac )
    if ( count == 0 ):
        print "Vlan Bridge Index %s is not in this table" % ( vIndex )
	sys.exit(1)

def findMacReverse ( communityVlan, decMac ):
    OID = ( 1,3,6,1,2,1,17,4,3,1,1,0,decMac[0],decMac[1],decMac[2],decMac[3],decMac[4] )
    try:
        errorIndication, errorStatus, errorIndex, \
            macTable = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', communityVlan), \
            cmdgen.UdpTransportTarget((device, 161)), OID )
        return( convertOctect(macTable) )
    except TypeError, e:
        print "This OID %t does not exist in this table\n %s" % ( OID, e )
	sys.exit(1)

def findVlanMac(vlanID, nmac):
    """This function will get you the Converted MAC to Decimal then return it"""
    count = 0
    errorIndication, errorStatus, errorIndex, \
        vtpVlanAddr = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', community+"@"+vlanID), \
        cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,17,4,3,1,1))
    if len(vtpVlanAddr) == 0:
	print "This MAC %s is not part of any Vlan" % ( nmac )
	sys.exit(1)
    for vmac in vtpVlanAddr:
	if re.search(nmac,convertOctect(vmac), re.IGNORECASE):
	    count += 1
	    decVlanMac = re.sub("\(|\)|,", "", str(vmac[0][0][-5:]))
	    listDecVlanMac = list(vmac[0][0][-5:])
            return(decVlanMac, listDecVlanMac)
    if count == 0:
	print "This MAC %s is not part of any Vlan" % ( nmac )
	sys.exit(1)

def findPort(vlanID, vlanM, vlanListMac, nmac):
    """ This function will take in the VlanID and the Decimal Converted MAC of the host
        And make a snmpwalk to dot1dTpFdbPort which will then get the bridge port number.
        Once we have the bridge port number we then need to get the mapping to the ifIndex
        To do that we need to make a snmpget to dot1dBasePortIfIndex"""

    lVlan = vlanListMac
    #Here we do an snmpwalk to dot1dTpFdbPort and get the match to the DecimalvlanMac
    errorIndication, errorStatus, errorIndex, \
        vlanIndex = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', community+"@"+vlanID), \
        cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,17,4,3,1,2,0,lVlan[0],lVlan[1],lVlan[2],lVlan[3],lVlan[4]))
    if re.search(vlanM, re.sub("\(|\)|,", "", str(vlanIndex[0][0][-5:]))):
	    #Here we do a snmpget to dot1dBasePortIfIndex to get the ifIndex
        errorIndication, errorStatus, errorIndex, \
	    PortIndexMap = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', community+"@"+vlanID), \
            cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,17,1,4,1,2,vlanIndex[0][1]))
	if  not re.search("\d+", str(PortIndexMap[0][1])):
	    print "There isn't a PortIndex for this mac %s" % ( nmac )
	    sys.exit(1)
        errorIndication, errorStatus, errorIndex, \
	    PortName = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', community), \
            cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,2,2,1,2,+int(PortIndexMap[0][1])))
        return PortName[0][1]

def findIndex( portName ):
    """This function will find the PortName and PortIndex based on the port number you passed"""
    errorIndication, errorStatus, errorIndex, \
        ifIndexTable = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', community), \
        cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,2,2,1,2,))
    for id in ifIndexTable:
        if re.search("\w+"+"("+pname+"$)", str(id[0][1])):
	   ifName = id[0][1]
           ifIndex = id[0][0][-1]
	   return( ifIndex, ifName )

def findCommunity( ifIndex ):
    """This will return the community string + vlan so for example
       public@175"""
    count = 0
    errorIndication, errorStatus, errorIndex, \
        commTable = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', community), \
        cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,47,1,2,1,1,4))
    communityVlan = ""
    vIndex = ""
    for comm in commTable:
        communityVlan = comm[0][1]
	vIndex = findVlanIndex(communityVlan, ifIndex)
	if isinstance(vIndex, int):
	    count += 1
	    return( communityVlan, vIndex )
 	    sys.exit(0)
    if count == 0:
	   print "Could not find a vlan tagged to this port %s ifIndex.%s" % ( pname, ifIndex )
	   sys.exit(1)

def findVlanIndex( vlanComm, ifIndex ):
    """This function will return the Bridge ifIndex ID that ties to this port"""
    count = 0
    errorIndication, errorStatus, errorIndex, \
        vlanIndexTable = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('test-agent', vlanComm), \
        cmdgen.UdpTransportTarget((device, 161)), (1,3,6,1,2,1,17,1,4,1,2))
    vIndex = ""
    for i in vlanIndexTable:
        if int(i[0][1]) == ifIndex:
	    count += 1
	    vIndex = int(i[0][0][-1])
	    break
    if ( count >= 1 ):
	return( vIndex )
    else:
	vIndex = "None"
	return( vIndex )

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
