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
import getopt
import pywbem



def main():
    vm_namespace = "vmware/esxv2"
    client = pywbem.WBEMConnection(url, auth, vm_namespace)
    vms = client.EnumerateInstances('VMWARE_StoragePool')
    vispc = client.EnumerateInstances('VMWARE_VirtualInitiatorSCSIProtocolController')
    print "Available DataStores on %s\n" % (url)
    count = 0
    for vm in vms:
        vmname = vm['ElementName']
	vsname = "^\["+vmname+"\]"
        total = vm['TotalManagedSpace'] /1024 /1024 /1024
	remaining = vm['RemainingManagedSpace'] /1024 /1024 /1024
	used = total - remaining
	percent_used = (used * 100) / total
	if dstore:
	    dsmatch = "^"+dstore+"$"
	    if re.search(dsmatch, vmname):
	        printDstore(total, remaining, used, percent_used, vmname, vispc )
	        count += 1
	        sys.exit(0)
        elif not dstore:
	    printDstore(total, remaining, used, percent_used, vmname, vispc )
	    count += 1
    if count == 0:
        print "DataStore %s Does Not Exists on %s"  % ( dstore, url )
        
def printDstore(total, remaining, used, percent_used, vmname, vispc ):
    vsmatch = "^\["+vmname+"\]"
    count = 0
    print "DataStore Name \t\t\t %s" % (vmname)
    print "Total Disk Space \t\t %sG" % (total)
    print "Remaining Disk Space \t\t %sG" % (remaining)
    print "Used Disk Space \t\t %sG" % (used)
    print "Percentage Used \t\t %s" % (percent_used) + "%"
    print "VMX files that belong to this DataStore::"
    for vmx in vispc:
         if re.search(vsmatch, vmx['SystemName']):
	     print "  " + vmx['SystemName']
	     count += 1
    if count == 0:
        print "  None Exist"
    print "\n"

def usage():
    print """
        example below...
	python VMdataStorePool.py -u "http://esxhost" -a "login passwd"
	Available DataStores on http://esxhost

	DataStore Name                   Esxtestvol2
	Total Disk Space                 499G
	Remaining Disk Space             189G
	Used Disk Space                  310G
	Percentage Used                  62%
	VMX files that belong to this DataStore::
	  [Esxtestvol2] Win2003test3/Win2003test3.vmx
	  [Esxtestvol2] netwaretest/netwaretest.vmx
	  [Esxtestvol2] RHEL 4 NFS test/RHEL 4 NFS test.vmx
	  [Esxtestvol2] RHEL 5 NFS test/RHEL 5 NFS test.vmx
	  [Esxtestvol2] RHEL 3 NFS test/RHEL 3 NFS test.vmx
	  [Esxtestvol2] vicfg/vicfg.vmx

	DataStore Name                   ISO
	Total Disk Space                 49G
	Remaining Disk Space             38G
	Used Disk Space                  11G
	Percentage Used                  22%
	VMX files that belong to this DataStore::
  	  None Exist


	python VMdataStorePool.py -u "http://esxhost" -a "login passwd" --dstore="KodakVol1"
	Available DataStores on http://esxhost

	DataStore Name                   KodakVol1
	Total Disk Space                 499G
	Remaining Disk Space             379G
	Used Disk Space                  120G
	Percentage Used                  24%
	VMX files that belong to this DataStore::
  	  [KodakVol1] Kojak/Kojak.vmx
    	  [KodakVol1] Sakai/Sakai.vmx
      	  [KodakVol1] bbtest2.vmx
          [KodakVol1] bbtest.vmx

	-u, --url       This is the URL you will use to connect to the ESX server, "http://esxhost"
        -a, --auth      This is the Login and Passwd you will use, "login passwd"
        -d, --dstore    This is the DataStore aka VMFS to check, "Esxtestvol2"
	
    """
    sys.exit(0)

try:
    opts, args = getopt.getopt( sys.argv[1:], "u:h:a:d:",
    [ 'url=', 'help', 'auth=', 'dstore=' ]
    )
except getopt.error:
    usage()


url = help = auth = dstore = None
for opt, val in opts:
    if opt in ('-u', '--url'):
        url = val
    if opt in ('-a', '--auth'):
        auth = list(string.split(val, sep=" "))
        auth[1] = re.sub("\\\\", "", auth[1])
        auth = tuple(auth)
        print auth
        print type(auth)
    if opt in ('-d', '--dstore'):
        dstore = val
    if opt in ('-h', '--help'):
        help = usage()


if __name__ == "__main__" and url and auth:
    main()
else:
    usage()
