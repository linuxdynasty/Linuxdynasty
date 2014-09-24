#!/usr/bin/env python
#Created by Allen Sanabria aka LinuxDynasty

#This script will rst all Virtual Machines in an ESX Server
#Copyright (C) 2008  Allen Sanabria

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

import os
import sys
import re
import string
import pywbem
import getopt

def main():
    vm_namespace = "vmware/esxv2"
    client = pywbem.WBEMConnection(url, auth, vm_namespace)
    vms = client.EnumerateInstances('VMWARE_VMComputerSystem')
    count = 0

    for vm in vms:
        if name:
            dsmatch = "^"+name+"$"
	    if re.search(dsmatch, vm['ElementName']):
	        printVminfo(vm)
		count += 1
		sys.exit(0)
        elif not name:
	    printVminfo(vm)
	    count += 1
    if count == 0:
        print "VirtualMachine %s Does Not Exists on %s"  % ( name, url )

def printVminfo(vm):
    states = {
	      0:"Uknown",
	      1:"Other",
	      2:"Enabled",
	      3:"Disabled",
	      4:"Shutting Down",
	      5:"Not Applicable",
	      6:"Enabled But Offline",
	      7:"In Test",
	      8:"Deferred",
	      9:"Quiesce",
	      10:"Starting",
	      11:"DMTF Reserved",
          12:"Vendor Reserved"
	     }
    vmname = vm['ElementName']
    osystem = vm['OtherIdentifyingInfo'][1]
    hname = ipaddr = None
    dstore = vm['Name']
    rstate = vm['RequestedState']
    if len(vm['OtherIdentifyingInfo']) >= 3:
        hname = vm['OtherIdentifyingInfo'][2]
	ipaddr = vm['OtherIdentifyingInfo'][3]
    print "VM Name \t\t %s" % (vmname)
    print "Operating System \t %s" % (osystem)
    print "Host Name \t\t %s" % (hname)
    print "IP Address \t\t %s" % (ipaddr)
    print "DataStore Used \t\t %s" % (dstore)
    print "Requested State \t %s" % (states[rstate])
    print "Operational Status \t %s" % (states[vm['OperationalStatus'][0]])
    print "Enabled by Default \t %s" % (states[vm['EnabledDefault']])
    print "Enabled State \t\t %s\n" % (states[vm['EnabledState']])

try:
    opts, args = getopt.getopt( sys.argv[1:], "u:a:n:h:",
    [ 'url=', 'auth=', 'help', 'name=' ] )

except getopt.error:
    usage() 


def usage():
    print """
    example below...
    python listVMsInfo.py -u "http://esxhost" -a "login passwd"

    VM Name                  Linux DP Client (tail)
    Operating System         Red Hat Enterprise Linux 5 (32-bit)
    Host Name                dpclient.linuxdynasty
    IP Address               192.168.101.124
    DataStore Used           [Esxtestvol2] Linux Data Protector Install Ser/Linux Data Protector Install Ser.vmx
    Requested State          Not Applicable
    Operational Status       Enabled
    Enabled by Default       Enabled
    Enabled State            Not Applicable

    another example....
    python listVMsInfo.py -u  "http://esxhost" -a "login passwd" --name "bbtest"
    VM Name                  bbtest
    Operating System         Red Hat Enterprise Linux 4 (64-bit)
    Host Name is             None
    IP Address is            None
    DataStore Used           [KodakVol1] bbtest/bbtest.vmx
    Requested State          Not Applicable
    Operational Status       Enabled
    Enabled by Default       Enabled
    Enabled State            Not Applicable

    -u, --url       This is the URL you will use to connect to the ESX server, "http://esxhost"
    -a, --auth      This is the Login and Passwd you will use, "login passwd"
    -n, --dstore    This is the VirtualMachine to check, "bbtest"


    """
    sys.exit(0)

url = auth = help = name = None
for opt, val in opts:
    if opt in ('-u', '--url'):
        url = val
    if opt in ('-a', '--auth'):
        auth = tuple(string.split(val, sep=" "))
    if opt in ('-n', '--name'):
        name = val
    if opt in ('-h', '--help'):
        usage()

if __name__ == "__main__" and url and auth:
    main()

else:
    usage()
