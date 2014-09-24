#!/usr/bin/env python
#Created by Allen Sanabria aka LinuxDynasty

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

try:
    import pywbem
except:
    print "You need to download Pywbem from http://pywbem.wiki.sourceforge.net/"
    sys.exit(1)

def main():
    exitval = {
            "OK" : 0,
        "WARNING" : 1,
        "CRITICAL" : 2,
        "UNKNOWN" : 3
       }
    vm_namespace = "vmware/esxv2"
    client = pywbem.WBEMConnection(url, auth, vm_namespace)
    vms = client.EnumerateInstances('VMWARE_StoragePool')
    count = 0
    metrics = metric
    if not metric:
        metrics = "bytes"
    else:
        metrics = metric
    for vm in vms:
        vmname = vm['ElementName']
        total = DmetricCalc(vm['TotalManagedSpace'], metrics)
        remaining = DmetricCalc(vm['RemainingManagedSpace'], metrics)
        used = total - remaining
        percent_used = (used * 100) / total
        if dstore:
            dsmatch = "^"+dstore+"$"
            if re.search(dsmatch, vmname):
                rval = threshold(percent_used)
                count += 1
                print rval, dstore, str(remaining)+metrics+" Avail",str(percent_used)+"% used "+ "|avail="+str(remaining)
                sys.exit(exitval[rval])
    if count == 0:
        print "DataStore %s Does Not Exists on %s"  % ( dstore, url )
        
def DmetricCalc(val, metrics):
    if re.search("GB", metrics):
        return(val / 1024 / 1024 / 1024)
    elif re.search("MB", metrics):
        return(val / 1024 / 1024)
    elif re.search("KB", metrics):
        return(val / 1024)
    else:
        return(val)

def threshold(percent_used):
    if percent_used < warn:
       return("OK")
    if percent_used >= warn and percent_used < crit:
       return("WARNING")
    if percent_used >= crit:
       return("CRITICAL")
    if crit < warn:
       print "Crit Value is Greater Then Warn"
       sys.exit(1)

def usage():
    print """
        example below...
    python check_datastore.py -u "http://esxhost" -a "login passwd" --d "Esxtestvol2" -w 60 -c 73 -m GB
    Warning Esxtestvol2 189GB Avail 62% used |avail=189

    python check_datastore.py -u "http://esxhost" -a "login passwd" --d "Esxtestvol2" -w 70 -c 85 -m MB
    OK Esxtestvol2 194558MB Avail 61% used |avail=194558

    python check_datastore.py -u "http://esxhost" -a "login passwd" --d "ISO" -w 10 -c 21 -m KB
    Critical ISO 41867542528KB Avail 21% used |avail=41867542528

    python check_datastore.py -u "http://esxhost" -a "login passwd" --d "Esxtestvol2" -w 70 -c 85
    OK Esxtestvol2 204008849408bytes Avail 61% used |avail=204008849408

    -u, --url	This is the URL you will use to connect to the ESX server, "http://esxhost"
    -a, --auth	This is the Login and Passwd you will use, "login passwd"
    -d, --dstore	This is the DataStore aka VMFS to check, "Esxtestvol2"
    -w, --warn	This is the warning threshold that you will set, 70
    -c, --crit	This is the critical threshold that you will set, 85
    -m, --metric	This is the metric that you will use, "KB", "MB", "GB", The default is Bytes
    
    """
    sys.exit(0)

try:
    opts, args = getopt.getopt( sys.argv[1:], "u:h:a:d:w:c:m:",
    [ 'url=', 'help', 'auth=', 'dstore=', 'warn=', 'crit=', 'metric=' ]
    )
except getopt.error:
    usage()


url = help = auth = dstore = warn = crit = metric =  None
for opt, val in opts:
    if opt in ('-u', '--url'):
        url = val
    if opt in ('-a', '--auth'):
        auth = list(string.split(val, sep=" "))
        auth[1] = re.sub("\\\\", "", auth[1])
        auth = tuple(auth)
    if opt in ('-d', '--dstore'):
        dstore = val
    if opt in ('-h', '--help'):
        help = usage()
    if opt in ('-w', '--warn'):
        warn = int(val)
    if opt in ('-c', '--crit'):
        crit = int(val)
    if opt in ('-m', '--metric'):
        metric = val


if __name__ == "__main__" and url and auth and dstore and warn and crit:
    main()
else:
    usage()
