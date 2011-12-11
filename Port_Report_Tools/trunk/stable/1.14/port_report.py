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

"""Revision 1.14 03/31/10
    * Found out that even though most switches I ran into, use the 
      entLogicalCommunity table to snmpwalk the dot1d snmp tables. Not all do!
      Some actually use the community string that you passed to the script with the
      VlanId that comes with the entLogicalCommunity table.
    * Added support for Cisco Catalyst C3750
"""
"""Revision 1.13 10/01/09
    * Fixed line 348 as per christianha. return nmac.lower()
      This fix will allow you to pass a MAC in all uppercase and still match though the switch is responding in lowercase.
"""    
"""Revision 1.12 09/18/09
    * Added follow switch option. Now when you run the Port Report with the --report option, you an also
      pass the --follow option. This option will follow every dp neighbor connectetd to the switch you are
      scaning as well as the switches it is scanning.
"""
"""Revision 1.11 09/13/09
    * More code clean up and another increase in speed.
    * Also port_report can now follow EtherChannel
    * Fixed issue, where the matching of the cdp neighbor was not matching correctly
"""        
"""Revision 1.10 09/09/09
Code Clean up and a slight increase in speed ( by a few seconds ) during the search by mac or ip
"""

"""Revision 1.9 05/08/2009
Code changes and Added CDP support..

    * Detect CDP Neighbors during the scan for MAC Addresses or IP Addresses
"""

""" Revision 1.7 04/30/09
This is a big update for Port Report.... In this revision the following brands and devices are supported

   1. Cisco
          * Catalyst 6509 w/ Supervisor 720 running IOS
          * Catalyst 3560
          * Catalyst 3550 (SMI)
          * Cisco CIGESM series Chassis Blades
          * Cisco Catalyst 2960
   2. Foundry
          * Foundry Server Iron
   3. Nortel
          * Nortel Passport 8600
          * Nortel 5520 Ethernet Routing Switch
   4. HP
          * HP Procurve 5406xl

""" 
#Now at the 5th revision 1.5 04/21/09
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
from time import ctime
from socket import gethostbyaddr


try:
    from pysnmp.entity.rfc3413.oneliner import cmdgen
except Exception, e:
    print("You need to download pysnmp and pyasn1", e)
    sys.exit(1)

def usage():
    print("""
    -d, --device	This is the device you want to scan
    -c, --community	This is the SNMP community string to use
    -m, --mac 		This is the MAC Address you are using to search foir what port your device is plugged into
    -i, --ip		This is the IP Address you are using to find the MAC Address of the device and The port in the switched it is plugged into
    -n, --pname		This is the Port Name you are searching For
    -v, --verbose	This will print out the time stamps of the for loops and of the functions
    -r, --report	This will print out all the mac addresses on the switch you are scanning and what ports they are connected to.
    -f, --follow	This will follow all the cdp neighbors found per switch when using the -r or --report option.

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

    python port_report.py -d 192.168.101.1 -c public -r -f
    Running Switch Report on 192.168.101.1
    GigabitEthernet1/40,00 1b 90 99 3d 83,None,None,vlan1,up,up,unknown,1000mb,
    GigabitEthernet10/15,00 23 5e ef 34 81,192.168.101.2,Pointer Record Not set for 192.168.101.62,vlan1,up,up,fullDuplex,1000mb,GIG Laser to 71Fifth
    GigabitEthernet1/34,00 01 02 03 03 05,None,None,vlan174,up,up,unknown,1000mb,CCA_CAS Untrusted Interface IP 168.3


    """)
    sys.exit(0)


def main():
    if verbose: print(ctime(), " Main Started") 
    if ( community and device and ( mac or ip or pname or report ) ):
        snmperror, switchtype = get( device, community, oTable["sysDescr"], 0 )
        switchtype = str(switchtype)
        if snmperror:
            print(snmperror, "Either Wrong Community String or Firewall or SNMP Not Running")
            sys.exit(1)
        sbrand = None
        scanned_neighbor = False
        dswitch = device
        switch = followSwitch( dswitch, community )
        entIpList = {}
        ipList = []
        entaddr = walk( device, community, oTable["ipAdEntAddr"] )
        for line in entaddr:
            ipList.append(switch.convertOctectIp( line[0][1] ))
        entIpList[device] = ipList
        nip = ""
        nmac = ""
        count = 0
        if mac or ip:
            switch.set_duplex()
            switch.set_speed()
            switch.set_port_name()
            switch.set_phys_addr()
            if verbose: print(switchtype)
            mTable = ""
            if mac:
                nmac = mac
                nmac, valid = verify_mac( nmac )
                if not valid:
                    print("you mac %s is in the wrong format" % (mac))
                    sys.exit(1)
                nip = switch.findIpByMac( nmac )
            if ip:
                nip = ip
                nmac = switch.findMacByIp( nip )
                if nmac == None:
                    print("This IPAddress is not in the ARP table")
                    sys.exit(1)

            if ( re.search("Cisco|PROCURVE|Nortel|ERS|Foundry", switchtype, re.IGNORECASE ) ):
                mTable, ifIndex = switch.find_mac( nmac, nip )
                count = 0
                sswitch = dswitch
                if (mTable):
                    count += 1
                    for key, val in list(mTable.items()):
                        print("Switch Connected to %s" % ( dswitch ))
                        print("SwitchPort = %s\nSwitchPortSpeed = %s\nSwitchPortDuplex = %s\nSwitchVlan = %s" % \
                              ( val["ifDescr"], val["ifSpeed"], val["ifDuplex"], val["vlan"] ))
                        print("SnmpHostName = %s\nSnmpHostDescr = %s\nHostMAC  = %s\nHostIP = %s\nHostName = %s\n" % \
                              ( val["sysName"], val["sysDescr"], val["nmac"], val["ipAddr"], val["hostName"] ))
                        if re.search("Port-channel", val["ifDescr"]):
                            if verbose: print("ifIndex %d is a %s interface" % ( ifIndex, val["ifDescr"] ))
                            ifIndex_pagp_list = switch.get_pagp_ports( ifIndex )
                            if verbose: print("List of Interfaces is in EtherChannel: ", ifIndex_pagp_list)
                            ifIndex = ifIndex_pagp_list[0]
                neighbor = followSwitch(dswitch, community).get_cdp_neighbor_ip( ifIndex )
                if neighbor:
                    if verbose: print(neighbor)
                    sswitch = dswitch
                    while neighbor:
                        old_neighbor = neighbor
                        new_neighbor = followSwitch(sswitch, community)
                        ifIndex, count1 = new_neighbor.get_mac_from_cdp_neighbor( neighbor, nmac, nip )
                        count += count1
                        sswitch = neighbor
                        neighbor = followSwitch(sswitch, community).get_cdp_neighbor_ip( ifIndex )
                        if neighbor:
                            entaddr = walk( sswitch, community, oTable["ipAdEntAddr"] )
                            iplist = []
                            for line in entaddr:
                                ipList.append(new_neighbor.convertOctectIp( line[0][1] ))
                            entIpList[neighbor] = ipList
                            for key, value in list(entIpList.items()):
                                for line in value:
                                    if line == neighbor:
                                        scanned_neighbor = True
                                        print("this neighbor has already been scanned")
                                        print(line, neighbor)
                                        neighbor = None
                    if ( count >= 1 ):
                        print("This MAC %s was finally traced to this switch %s" % ( nmac, sswitch ))
            if ( count == 0 ):
                print("The Mac Address %s is not on this switch %s" % ( nmac, dswitch ))
            

        if pname:
            count = 0
            switch.set_duplex()
            switch.set_speed()
            switch.set_port_name()
            switch.set_phys_addr()
            switch.find_port_match( pname ) 
            ifIndex = switch.get_ifIndex()
            ifName = switch.get_ifName()
            sbrand = switch.get_sbrand()
            connected_macs = []
            if ( re.search("Cisco|PROCURVE", switchtype, re.IGNORECASE ) ):
                lcomm, lvlan = switch.retreive_communities( )
                if verbose:  print(ctime(), "Retreiving Community Strings\n %s" % ( lcomm ))
                for i in range(len(lcomm)):
                    mdict = switch.return_mac_by_ifIndex( lcomm[i], lvlan[i] )
                    if mdict:
                        connected_macs.append(mdict)
            elif ( re.search("Nortel|ERS|Foundry", switchtype, re.IGNORECASE ) ):
                comm = community
                vlan = None
                mdict = switch.return_mac_by_ifIndex( comm, vlan )
                if mdict:
                    connected_macs.append(mdict)
            if len(connected_macs) > 0:
                for host in connected_macs:
                    for key, val in list(host.items()):
                        count += 1
                        print("SwitchPort = %s\nSwitchPortSpeed = %s\nSwitchPortDuplex = %s\nSwitchVlan = %s" \
                               % ( val["ifDescr"], val["ifSpeed"], val["ifDuplex"], val["vlan"] ))
                        print("SnmpHostName = %s\nHostDescr = %s\nHostMAC  = %s\nHostIP = %s\nHostName = %s\n" \
                               % ( val["sysName"], val["sysDescr"], val["nmac"], val["ipAddr"], val["hostName"] ))
                print("There are %d MAC Addresses connected to port %s" % ( count, pname ))
            else:
                print("There are not any MAC Addresses connected to this %s port" % ( pname ))

        if report:
            dswitch = device
            count = write_report(dswitch, entIpList)
            tcount = 0
            if follow:
                for item in count:
                    tcount += item
                print("Total MAC Addresses found: %d" % tcount)
            
def write_report( dev, entIpList, tcount = [] ):
    print("Running Switch Report on %s" % ( dev ))
    scanned_neighbor = False
    ipList = []
    snmperror, switchtype = get( dev, community, oTable["sysDescr"], 0 )
    switchtype = str(switchtype)
    if snmperror:
        print(snmperror, "Either Wrong Community String or Firewall or SNMP Not Running")
        sys.exit(1)
    switch = followSwitch( dev, community )
    switch.set_duplex()
    switch.set_speed()
    switch.set_port_name()
    switch.set_phys_addr()
    switch.set_oper_status()
    switch.set_admin_status()
    switch.set_alias()
    count = 0
    conn_output = open("connnected_ports_on_"+dev+".csv", "a")
    if ( re.search("Cisco|PROCURVE", switchtype, re.IGNORECASE ) ):
        lcomm, lvlan = switch.retreive_communities( )
        if verbose:  print(ctime(), "Retreiving Community Strings\n %s" % ( lcomm ))
        for i in range(len(lcomm)):
            macout = switch.switch_report( lcomm[i], lvlan[i], conn_output )
            count += macout
            tcount.append(macout)
        print("total MAC Addresses found on %s: %d\n" % ( dev, count ))
    elif ( re.search("Nortel|ERS|Foundry", switchtype, re.IGNORECASE ) ):
        macout = switch.switch_report( community, None, conn_output )
        count += macout
        tcount.append(macout)
        print("total MAC Addresses found on %s: %d\n" % ( dev, count ))
    conn_output.close()
    if follow:
        neighbors = switch.get_cdp_neighbor_ip_table()
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if verbose: "Print neighbor %s " % neighbor
                for key, value in list(entIpList.items()):
                    for line in value:
                        if line == neighbor:
                            scanned_neighbor = True
                            if verbose:
                                print("this neighbor has already been scanned")
                                print(line, neighbor)
                            break
                    if scanned_neighbor:
                        break
                if scanned_neighbor:
                    continue
                else:
                    entaddr = walk( neighbor, community, oTable["ipAdEntAddr"] )
                    if entaddr == "requestTimedOut":
                        continue
                    for line in entaddr:
                        ipList.append(switch.convertOctectIp( line[0][1] ))
                    entIpList[neighbor] = ipList
                    write_report(neighbor, entIpList, tcount)
    else:
        tcount = count
    return tcount    

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
    if verbose: print(ctime(), " Finished Checking for mac") 
    return( nmac, valid )


def walk( dswitch, commVlan, oid  ):
    """This function will return the table of OID's that I am walking"""
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

    if not isinstance(rval, int):
        rval = 0
    oidN = list(oid)
    if isinstance(indexOid, int):
        oidN.append(indexOid)
    elif type(indexOid) == list:
        oidN = oidN + list(map(int, indexOid))
    oidN = tuple(oidN)
    errorIndication, errorStatus, errorIndex, \
        generic = cmdgen.CommandGenerator().getCmd(cmdgen.CommunityData('test-agent', commVlan), \
        cmdgen.UdpTransportTarget((device, 161)), oidN)
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

def alias_name( switch ):
    aliasW = walk( switch, community, oTable['ifAlias'] )
    aliasH = {}
    for i in aliasW:
        aliasH[i[0][0][-1]] = str(i[0][1])
    return aliasH

def admin_settings( switch ):
    adminW = walk( switch , community, oTable['ifAdminStatus'] )
    adminH = {}
    for i in adminW:
        adminH[i[0][0][-1]] = str(ostatus[i[0][1]])
    return adminH

def oper_settings( switch ):
    operW = walk( switch, community, oTable['ifOperStatus'] )
    operH = {}
    for i in operW:
        operH[i[0][0][-1]] = str(ostatus[i[0][1]])
    return operH

def duplex_settings( switch ):
    duplexW = walk( switch, community, oTable['dot3StatsDuplexStatus'] )
    duplexH = {}
    for i in duplexW:
        duplexH[i[0][0][-1]] = str(duplex[i[0][1]])
    return duplexH

def speed_settings( switch ):
    speedW = walk( switch, community, oTable['ifSpeed'] )
    speedH = {}
    for i in speedW:
        speedH[i[0][0][-1]] = str(port_speed(int(i[0][1]) ) )
    return speedH

def port_name( switch ):
    portW = walk( switch, community, oTable['ifDescr'] )
    portH = {}
    for i in portW:
        portH[i[0][0][-1]] = str(i[0][1])
    return portH

def port_speed( speed ):
    speed = speed / 1000000
    speed = str(speed)+"mb"
    return speed

class followSwitch(object):
    def __init__(self, switch, comm="public" ):
        self.community = comm
        self.switch = switch
        self.sbrand = None
        self.snmperror, self.switchtype = get( self.switch, self.community, oTable["sysDescr"], 2)
        if ( re.search("Cisco", self.switchtype, re.IGNORECASE ) ):
            self.sbrand = "Cisco"
        elif ( re.search("PROCURVE", self.switchtype, re.IGNORECASE ) ):
            self.sbrand = "HP"
        elif ( re.search("Nortel|ERS", self.switchtype, re.IGNORECASE ) ):
            self.sbrand = "Nortel"
        elif ( re.search("Foundry", self.switchtype, re.IGNORECASE ) ):
            self.sbrand = "Foundry"

    def get_sbrand( self ):
        return self.sbrand

    def set_duplex( self ):
        try:
            self.duplexH = duplex_settings( self.switch )
        except:
            self.duplexH = None

    def set_speed( self ):
        try:
            self.speedH = speed_settings( self.switch )
        except:
            self.speedH = None

    def set_port_name( self ):
        self.portNameH = port_name( self.switch )

    def set_oper_status( self ):
        self.operH =  oper_settings( self.switch )

    def set_admin_status( self ):
        self.adminH = admin_settings( self.switch )

    def set_alias( self ):
        self.aliasH = alias_name( self.switch )

    def set_phys_addr( self ):
        self.PhysAddr = walk( self.switch, community, oTable["atPhysAddress"] )

    def set_ifIndex_dict( self ):
        self.portNameH = port_name( self.switch )
        self.operH =  oper_settings( self.switch )
        self.adminH = admin_settings( self.switch )
        self.aliasH = alias_name( self.switch )
        self.PhysAddr = walk( self.switch, community, oTable["atPhysAddress"] )
        try:
            self.duplexH = duplex_settings( self.switch )
        except:
            self.duplexH = None
        try:
            self.speedH = speed_settings( self.switch )
        except:
            self.speedH = None


    def findMacByIp( self, nip ):
        """This Function will return the MAC Address if the IPAddress that  was in the ARP table
           if not it will return None"""
        count = 0
        nmac = ""
        for ipAddress in self.PhysAddr:
            ip1 = str(ipAddress[0][0][-4:])
            ipmap = re.sub("\'|\[|\]|\(|\)", "", re.sub(",\s", ".", ip1))
            if ( nip == ipmap ):
                count += 1
                nmac = self.convertOctectMac(ipAddress[0][1])
                break
        if count == 1:
            return( nmac )
        else:
            nmac = None
            return( nmac )

    def findIpByMac( self, nmac  ):
        """This Function will only return the IP Address of the MAC you are searching for if
           the IP Address is in the ARP table.  """
        self.ipAddr = None
        for mack in self.PhysAddr:
            cmac = self.convertOctectMac(mack[0][1])
            if re.search(nmac, cmac, re.IGNORECASE):
                ip1 = str(mack[0][0][-4:])
                self.ipAddr = re.sub("\'|\(|\)|,", "", ip1).replace(" ", ".")
                break
        return self.ipAddr

    def convertOctectMac(self, mack):
        """This Function will convert the OctectString into a Valid MAC Address"""
        mmap = list(map(hex, list(map(ord, mack)) ))
        cmac = mmap
        for i in range(len(mmap)):
            mmap[i] = re.sub("0x", "", mmap[i])
            mmap[i] = mmap[i].zfill(2)
        cmac = re.sub("\'|\,|\[|\]", "", str(mmap) )
        return cmac

    def convertOctectIp(self, hexip):
        """This Function will convert the OctectString into a valid Ip Address"""
        ip = list(map(hex, list(map(ord, hexip)) ))
        ip = list(map(hex2dec, ip))
        ip = re.sub("\,", ".",re.sub("\'|\[|\]|\s","", str(ip)))
        return ip

    def convertDecMac(self, mack):
        """This Function will convert the Decimal into HEX"""
        mmap = list(map(hex, mack)) 
        cmac = mmap
        for i in range(len(mmap)):
            mmap[i] = re.sub("0x", "", mmap[i])
            mmap[i] = mmap[i].zfill(2)
        cmac = re.sub("\'|\,|\[|\]", "", str(mmap) )
        return cmac

    def get_pagp_ports( self, pagp_ifIndex ):
        """get_pagp_ports will return a list of ifIndex ID's, that is associated with 
        the EtherChannel ifIndex. Will return a tuple of ifIndex ID's"""
        pagp_group = walk( self.switch, self.community, pagpTable["pagpGroupIfIndex"] )
        ifIndexList = []
        for line in pagp_group:
            if pagp_ifIndex == int(line[0][1]):
                ifIndexList.append(int(line[0][0][-1]))
        return tuple(ifIndexList)
            

    def retreive_communities( self ):
        """ This function does exactly what it is defined as. It will return a list
            of Community Strings from the entLogicalCommunity OID Table.
            As well as grab the associated vlan ID. Then return both in a tuple"""
        commTable = walk( self.switch, self.community, oTable["entLogicalCommunity"] ) 
        if verbose: print(commTable)
        lcomm = []
        lvlan = []
        for comm in commTable:
            if verbose: print(ctime(), " Looping Through CommTable") 
            vlan = int(comm[0][0][-1])
            comm = str(comm[0][1])
            if len(lcomm) == 0:
                lcomm.append(comm)
                lvlan.append(vlan)
            elif len(lcomm) >= 1:
                if lcomm[:len(comm[-1])].__contains__(comm):
                    if verbose: print("Duplicate Community String")
                    continue
                else:
                    lcomm.append(comm)
                    lvlan.append(vlan)
        return( lcomm, lvlan )

    def find_port_match( self, pname ):
        """ By passing this function the Port Name and The Brand of
            this Switch, you will in return get the ifIndex and the ifName"""
        if verbose: print(ctime(), " In generic_pname Function") 
        self.ifIndex = None
        self.ifName = None
        count = 0
        ifNameTable = walk( self.switch, community, oTable["ifName"] )
        pfield = re.compile("([0-9]{1,2})\\/([0-9]{1,2})")  # "1/9"
        gen_pname = []
        new_pname = ""
        if ( pfield.search(pname) ):
            gen_pname.append(pfield.match(pname).group(1))
            gen_pname.append(pfield.match(pname).group(2))
            if ( self.sbrand == "HP" ):
                new_pname = hpTable[str(gen_pname[0])]+str(gen_pname[1])
                count += 1
                if verbose: print(new_pname)
            if ( self.sbrand == "Nortel" ):
                new_pname = "Slot: %s Port: %s" % ( str(gen_pname[0]), str(gen_pname[1]) )
                count += 1
                if verbose: print(new_pname)
            if (self. sbrand == "Foundry" ):
                new_pname = "FastEthernet%s" % ( str(gen_pname[1]) )
                count += 1
                if verbose: print(new_pname)

        for iface in ifNameTable:
            ifIndex = int(iface[0][0][-1])
            ifName = str(iface[0][1])
            if new_pname:
                if ( re.search(new_pname, ifName) ):
                    count +=1
                    self.ifIndex = ifIndex
                    self.ifName = ifName
                    if verbose: print("Found %s on %s and the ifIndex is %d" % ( new_pname, self.ifName, self.ifIndex ))
                    break
            if ( re.search("[A-Z]+"+pname+"|"+pname, ifName) ):
                count +=1
                self.ifIndex = ifIndex
                self.ifName = ifName
                if verbose: print("Found %s on %s and the ifIndex is %d" % ( pname, ifName, ifIndex ))
                break
    
    def get_ifIndex(self):
        return( self.ifIndex )

    def get_ifName(self):
        return( self.ifName )

    def find_mac(self, nmac, nip=None):
        self.mac = nmac
        snmperror, switchtype = get( self.switch, self.community, oTable["sysDescr"], 2)
        mTable = ifIndex = None
        if ( re.search("Cisco|HP", self.sbrand, re.IGNORECASE) ):
            lcomm, lvlan = self.retreive_communities( )
            if verbose:  print(ctime(), "Retreiving Community Strings\n %s" % ( lcomm ))
            for i in range(len(lcomm)):
                mTable, ifIndex = self.find_mac_or_ip( self.mac, nip, lcomm[i], lvlan[i] )
                if len(mTable) >= 1:
                    break
        elif ( re.search("Nortel|ERS|Foundry", self.sbrand, re.IGNORECASE) ):
                mTable, ifIndex = self.find_mac_or_ip( self.mac, nip, self.community, None )
        return mTable, ifIndex

    def find_mac_or_ip( self, nmac, nip, comm, vlanID ):
        if verbose: print(ctime(), " In generic_mac_or_ip Function") 
        if verbose: print(nmac, nip, self.switch, comm)
        macVlanTable = walk( self.switch, comm, oTable["dot1dTpFdbPort"] )
        if macVlanTable == "requestTimedOut":
            comm = community+"@"+str(vlanID)
            macVlanTable = walk( self.switch, comm, oTable["dot1dTpFdbPort"] )
        if verbose: print(macVlanTable)
        mTable = {}
        count = 0
        ifIndex = None
        if ( len(macVlanTable) > 0 ):
            if verbose: print(ctime(), " First If Statement ") 
            for macVlan in macVlanTable:
                cmac = self.convertDecMac(list(macVlan[0][0][-6:]))
                if re.search(nmac, cmac, re.IGNORECASE):
                    if verbose: print("MAC Addresses Match %s and %s" % ( nmac, cmac ))
                    count += 1
                    bIndex = int(macVlan[0][1])
                    snmperror, ifIndex = get( self.switch, comm, oTable["dot1dBasePortIfIndex"], 2, bIndex )
                    if snmperror:
                        print snmperror
                        sys.exit(1)
                    ifIndex = int(ifIndex)
                    ifSpeed = self.speedH[ifIndex]
                    try:
                        ifDuplex = self.duplexH[ifIndex]
                    except:
                        ifDuplex = None
                    port = self.portNameH[ifIndex]
                    vlan = ""
                    hname = None
                    if vlanID:
                        try:
                            snmperror, vlan = get( self.switch, comm, oTable["entLogicalDescr"], 2, vlanID )
                        except:
                            vlan = None
                    if not nip:
                        ipAddr = str(self.findIpByMac( nmac ))
                    else:
                        ipAddr = nip
                    if re.search("(\d{1,3}\.){3}\d{1,3}", str(ipAddr) ):
                        try:
                            hname = gethostbyaddr(ipAddr)
                            hname = hname[0]
                        except:
                            hname = "Pointer Record Not set for %s" % ( ipAddr )
                        snmperror, sysName = get( ipAddr, community, oTable["sysName"], 2 )
                        if snmperror: sysName = snmperror
                        snmperror, sysDescr = get( ipAddr, community, oTable["sysDescr"], 2 )
                        if snmperror: sysDescr = snmperror
                        mTable[nmac] = {
                                        "ifDescr" : port,
                                        "ifSpeed" : ifSpeed,
                                        "ifDuplex" : ifDuplex,
                                        "vlan" : vlan,
                                        "sysName" : sysName,
                                        "sysDescr" : sysDescr,
                                        "nmac" : nmac,
                                        "ipAddr" : ipAddr,
                                        "hostName" : hname
                                       } 
                        count += 1
                    else:
                        sysName = "None"
                        sysDescr = "None"
                        mTable[nmac] = {
                                        "ifDescr" : port,
                                        "ifSpeed" : ifSpeed,
                                        "ifDuplex" : ifDuplex,
                                        "vlan" : vlan,
                                        "sysName" : "No SNMP Access",
                                        "sysDescr" : "No SNMP Access",
                                        "nmac" : nmac,
                                        "ipAddr" : ipAddr,
                                        "hostName" : hname
                                       }
                    count += 1
                    if verbose: print(ctime(), " Done ") 
                    break

        return mTable, ifIndex
	       

    def return_mac_by_ifIndex( self, comm, vlanID ):
        """ This function will return a list of dictionairies by the port Index
            So lets say you pass this function ifIndex 10, return_mac_by_ifIndex
	        will return any MAC Addresses Associated with that ifIndex."""

        mTable = {}
        sTable = {}
        switch = []
        mcount = 0
        vIfIndexTable = walk( self.switch, comm, oTable["dot1dBasePortIfIndex"] )
        if vIfIndexTable == "requestTimedOut":
            comm = community+"@"+str(vlanID)
            vIfIndexTable = walk( self.switch, comm, oTable["dot1dBasePortIfIndex"] )
        if ( len(vIfIndexTable) > 0 ):
            for v in vIfIndexTable:
                vIndex = int(v[0][1])
                bIndex = int(v[0][0][-1])
                if verbose: print("Now Trying to Match the %d ifIndex to the bridge %d ifIndex table" % ( self.ifIndex, vIndex ))
                if ( self.ifIndex == vIndex ):
                    if verbose: print("Match %d ifIndex to %d BridgeifIndex Table" % ( self.ifIndex, vIndex ))
                    dM = walk( self.switch, comm, oTable["dot1dTpFdbPort"] )
                    for d in dM:
                        decmac = int(d[0][1])
                        if verbose: print("Now Trying to Match the %d bIndex to the decimal bridge %d Index table" % ( bIndex, decmac ))
                        if vlanID:
                            snmperror, vlan = get( self.switch, comm, oTable["entLogicalDescr"], 2, vlanID )
                            print(vlan, "found vlan")
                        else:
                            vlan = None
                        if ( bIndex == decmac ):
                            mcount += 1
                            indexListOid = list(d[0][0][-6:])
                            nmac =  self.convertDecMac( indexListOid )
                            if verbose: print("Found %s Decimal Mac and Coverted into a HEX MAC %s " % ( indexListOid, nmac ))
                            ipAddr = str( self.findIpByMac( nmac ) )
                            hname = None
                            try:
                                ifSpeed = self.speedH[self.ifIndex]
                            except:
                                ifSpeed = None
                            try:
                                ifDuplex = self.duplexH[self.ifIndex]
                            except:
                                ifDuplex = None
                            port = self.portNameH[self.ifIndex]
                            if re.search("(\d{1,3}\.){3}\d{1,3}", ipAddr ):
                                if re.search("127.0.0.\d+", ipAddr ):
                                    pass
                                else:
                                    try:
                                        hname = gethostbyaddr(ipAddr)
                                        hname = hname[0]
                                    except:
                                        hname = "Pointer Record Not set for %s" % ( ipAddr )
                                    snmperror, sysName =  get( ipAddr, community, oTable["sysName"], 2 )
                                    if snmperror: sysName = snmperror
                                    snmperror, sysDescr =  get( ipAddr, community, oTable["sysDescr"], 2 )
                                    sysName = str(sysName)
                                    if snmperror: sysDescr = snmperror
                                    sysDescr = str(sysDescr)
                                    snmperror, sysModel =  get( ipAddr, community, oTable["entPhysicalModelName"], 2 )
                                    if re.search("Cisco|PROCURVE|Nortel|Foundry", sysDescr, re.IGNORECASE):
                                        switch.append(ipAddr)
                                        switch.append(sysName)
                                        switch.append(sysDescr)
                                        switch.append(sysModel)
                                        switch.append(vlan)
                                        switch.append(self.speedH[self.ifIndex])
                                        switch.append(self.portNameH[self.ifIndex])
                                    else:
                                        mTable[nmac] = {
                                                        "ifDescr" : port,
                                                        "ifSpeed" : ifSpeed,
                                                        "ifDuplex" : ifDuplex,
                                                        "vlan" : vlan,
                                                        "sysName" : sysName,
                                                        "sysDescr" : sysDescr,
                                                        "nmac" : nmac,
                                                        "ipAddr" : ipAddr,
                                                        "hostName" : hname
                                                       }
                            else:
                                mTable[nmac] = {
                                                "ifDescr" : port,
                                                "ifSpeed" : ifSpeed,
                                                "ifDuplex" : ifDuplex,
                                                "vlan" : vlan,
                                                "sysName" : "No SNMP Access",
                                                "sysDescr" : "No SNMP Access",
                                                "nmac" : nmac,
                                                "ipAddr" : ipAddr,
                                                "hostName" : hname
                                               }
        return mTable

    def switch_report( self, comm, vlanID, conn_output ):
        """switch_report will write to stdout and to a .csv file
           everytime it finds a mac attached to a specific Interface"""
        vlan = ""
        output = []
        count = 0
        if vlanID:
            snmperror, vlan = get( self.switch, comm, oTable["entLogicalDescr"], 2, vlanID )
        else:
            vlan = None
        bridgeTable = walk( self.switch, comm, oTable['dot1dBasePort'] )
        decMacTable = walk( self.switch, comm, oTable['dot1dTpFdbPort'] )
        if bridgeTable == "requestTimedOut" and decMacTable == "requestTimedOut":
            comm = community+"@"+str(vlanID)
            bridgeTable = walk( self.switch, comm, oTable['dot1dBasePort'] )
            decMacTable = walk( self.switch, comm, oTable['dot1dTpFdbPort'] )
        if verbose: print(decMacTable)
        if verbose: print(bridgeTable)
        if ( len(decMacTable) > 0 ):
            for bindex in bridgeTable:
                bIndex = int(bindex[0][1])
                snmperror, ifIndex = get( self.switch, comm, oTable['dot1dBasePortIfIndex'], 2, int(bIndex) )
                ifIndex = int(ifIndex)
                for dm in decMacTable:
                    if dm[0][1] == bIndex:
                        ifDuplex = ""
                        ifSpeed = self.speedH[ifIndex]
                        try:
                            ifDuplex = self.duplexH[ifIndex]
                        except:
                            ifDuplex = "Not Known"
                        port = self.portNameH[ifIndex]
                        ifOperStatus = self.operH[ifIndex]
                        ifAdminStatus = self.adminH[ifIndex]
                        alias = self.aliasH[ifIndex]
                        decMac = list(dm[0][0][-6:])
                        nmac = self.convertDecMac( decMac )
                        ipAddr = str( self.findIpByMac( nmac ) )
                        hname = None
                        if re.search("(\d{1,3}\.){3}\d{1,3}", ipAddr ):
                            if re.search("127.0.0.\d+", ipAddr ):
                                pass
                            else:
                                try:
                                    hname = gethostbyaddr(ipAddr)
                                    hname = hname[0]
                                except:
                                    hname = "Pointer Record Not set for %s" % ( ipAddr )
                        output = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % ( port,nmac,ipAddr,hname,vlan,ifAdminStatus,ifOperStatus,ifDuplex,ifSpeed,alias )
                        count += 1
                        print(output)
                        conn_output.write(output)
                        conn_output.flush()
                    else:
                        continue
        return count

    def get_cdp_neighbor_ip(self, ifIndex):
        """ This function will grab the cdp neigbor that is attached
        to the ifIndex that is passed to this function
        """
        self.ifIndex = ifIndex
        ctable = walk( self.switch, self.community, cdpTable["cdpCacheAddress"])
        count = 0
        self.ip = None
        for host in ctable:
            match = tuple(host[0])
            if verbose:
                print(self.ifIndex, match[0][-2], self.convertOctectIp(str(host[0][1])))
            if ( self.ifIndex == match[0][-2] ):
                if verbose:
                    print("found ifIndex %s and here is the ip address of the cdpneighbor %s" \
                           % (str(self.ifIndex), self.convertOctectIp(str(host[0][1]))))
                self.ip = self.convertOctectIp(str(host[0][1]))
        return self.ip
 
    def get_cdp_neighbor_ip_table(self):
        """ This function will grab the cdp neigbor table and return a list of neighbors"""
        ctable = walk( self.switch, self.community, cdpTable["cdpCacheAddress"])
        self.ipTable = []
        for host in ctable:
            self.ipTable.append(self.convertOctectIp(str(host[0][1])))
            if verbose:
                print(self.convertOctectIp(str(host[0][1])))
        self.ipTable = tuple(self.ipTable)
        return self.ipTable
 
 
    def get_mac_from_cdp_neighbor( self, cswitch, nmac, nip ):
        self.cswitch = cswitch
        self.nmac = nmac
        self.nip = nip
        snmperror, switchtype = get( self.cswitch, self.community, oTable["sysDescr"], 2)
        if snmperror:
            print("Wrong Community String %s for device %s" % ( self.community, self.cswitch ))
            sys.exit(1)
        get_nmac = followSwitch( self.cswitch, self.community )
        get_nmac.set_duplex()
        get_nmac.set_speed()
        get_nmac.set_port_name()
        if self.nip == None:
            get_nmac.set_phys_addr()
        cTable, self.new_ifIndex = get_nmac.find_mac( self.nmac, self.nip )
        count = 0
        if cTable:
            count += 1
            print("Found %s on %s\n" % ( self.nmac, self.cswitch )) 
            for key, val in list(cTable.items()):
                print("Switch Connected to %s" % ( self.cswitch ))
                print("SwitchPort = %s\nSwitchPortSpeed = %s\nSwitchPortDuplex = %s\nSwitchVlan = %s" % \
                       ( val["ifDescr"], val["ifSpeed"], val["ifDuplex"], val["vlan"] ))
                print("SnmpHostName = %s\nSnmpHostDescr = %s\nHostMAC  = %s\nHostIP = %s\nHostName = %s\n" % \
                       ( val["sysName"], val["sysDescr"], val["nmac"], val["ipAddr"], val["hostName"] ))
                if re.search("Port-channel", val["ifDescr"]):
                    if verbose: print("ifIndex %d is a %s interface" % ( self.new_ifIndex, val["ifDescr"] ))
                    ifIndex_pagp_list = get_nmac.get_pagp_ports( self.new_ifIndex )
                    if verbose: print("List of Interfaces is in EtherChannel: ", ifIndex_pagp_list)
                    self.new_ifIndex = ifIndex_pagp_list[0]
        return (self.new_ifIndex, count)
          

   

cdpTable = {
            "cdpCacheAddress" : (1,3,6,1,4,1,9,9,23,1,2,1,1,4)
           }

pagpTable = {
            "pagpGroupIfIndex" : (1,3,6,1,4,1,9,9,98,1,1,1,1,8)
            }
oTable = { 
           "entLogicalCommunity" : (1,3,6,1,2,1,47,1,2,1,1,4),
           "entPhysicalModelName" : (1,3,6,1,2,1,47,1,1,1,1,13,1),
           "entLogicalDescr" : (1,3,6,1,2,1,47,1,2,1,1,2),
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
           "ifAdminStatus" : (1,3,6,1,2,1,2,2,1,7),
           "ifOperStatus" : (1,3,6,1,2,1,2,2,1,8),
           "atPhysAddress" : (1,3,6,1,2,1,3,1,1,2),
           "ipAdEntAddr" : (1,3,6,1,2,1,4,20,1,1),
           "ipAdEntIfIndex" : (1,3,6,1,2,1,4,20,1,2)
         }

hpTable = {"1" : "A", "2" : "B", "3" : "C", "4" : "D", "5" : "E",
           "6" : "F", "7" : "G", "8" : "H", "9" : "J", "10" : "K"
	  }

duplex = {
          1 : "unknown",
          2 : "halfDuplex",
          3 : "fullDuplex",
          '': "NotSet"
         }


ostatus = {
           1 : "up",
           2 : "down",
           3 : "testing",
           4 : "unknown",
           5 : "dormant",
           6 : "notPresent",
           7 : "lowerLayerDown"
          }

try:
     opts, args = getopt.getopt(sys.argv[1:], "c:d:i:m:n:h:rfv",
     [ 'community=', 'device=', "mac=", 'ip=', 'pname=', 'report', 'verbose', 'follow', 'help' ]
     )
except getopt.error:
     usage()

help = community = device = mac = ip = pname = verbose = report = follow = None

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
    if opt in ('-r', '--report'):
        report = True
    if opt in ('-f', '--follow'):
        follow = True
    if opt in ('-v', '--verbose'):
        verbose = True

   

if __name__ == '__main__':
    main()

