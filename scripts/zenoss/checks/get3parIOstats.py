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
import pywbem

from optparse import OptionParser


__author__ = "Allen Sanabria"
__copyright__ = "Copyright 2010, LinuxDynasty"
__license__ = "GPL"
__version__ = "0.0.10"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"

exitval = { 
          "OK" : 0,
          "WARNING" : 1,
          "CRITICAL" : 2,
          "UNKNOWN" : 3 
          }   

def main():
    par_namespace = "root/tpd"
    client = pywbem.WBEMConnection(options.url, options.auth, par_namespace)
    stats = None
    if options.volume:
        stats = client.EnumerateInstances('TPD_VolumeStatisticalData')
    elif options.port:
        stats = client.EnumerateInstances('TPD_PortStatisticalData')
    elif options.disk:
        stats = client.EnumerateInstances('TPD_DiskStatisticalData')
    else:
        print "Pass -h for help with this script"
        sys.exit(0)

    count = 0
    nstats = []
    for stat in stats:
        if options.volume or options.port or options.disk:
            if options.search:
                if re.search(options.search, stat["ElementName"].split(" ")[1]):
                    nstats.append(storeNagiosValues(nstats, stat))
            else:
                nstats.append(storeNagiosValues(nstats, stat))
        else:
            print "Pass -h for help with this script"
            sys.exit(0)

    pstats = re.sub(r"u\'|\"|\,|\'|\(|\)|\[|\]","",str(nstats))
    if len(pstats) > 0:
        print "OK|"+pstats
        sys.exit(exitval["OK"])
    else:
        print "Critical, no stats found"
        sys.exit(exitval["CRITICAL"])

def storeNagiosValues(nstats, stat):
    name = stat["ElementName"].split(" ")[1]
    if options.volume:
        pstats = name+"-ReadIOs="+str(stat['ReadIOs']), name+"-WriteIOs="+str(stat['WriteIOs']),\
                name+"-TotalIOs="+str(stat['TotalIOs']), name+"-ReadHitIOs="+ str(stat['ReadHitIOs']),\
                name+"-WriteHitIOs="+str(stat['WriteHitIOs'])
    elif options.port or options.disk:
        pstats = name+"-ReadIOs="+str(stat['ReadIOs']), name+"-WriteIOs="+str(stat['WriteIOs']),\
                name+"-TotalIOs="+str(stat['TotalIOs'])
    return str(pstats)

if __name__ == "__main__":

    usage = 'python %prog -u "http://3par" -a \'login passwd\' -v\n\
    OK|ubi-depot-1_ReadIOs=175937733 ubi-depot-1_WriteIOs=130875128 ubi-depot-1_TotalIOs=306812861\n\
    ubi-depot-1_ReadHitIOs=383455509 ubi-depot-1_WriteHitIOs=73948920 ubi-depot-10_ReadIOs=6318168\n\
    ubi-depot-10_WriteIOs=19538494 ubi-depot-10_TotalIOs=25856662 ubi-depot-10_ReadHitIOs=11654102\n\
    ubi-depot-10_WriteHitIOs=16343935\n\n\
    python %prog -u "http://3par" -a \'login passwd\' -s \'vol_test\' -v \n\
    OK|vol_test-1_ReadIOs=175937733 vol_test-1_WriteIOs=130875128 vol_test-1_TotalIOs=306812861\n\
    vol_test-1_ReadHitIOs=383455509 vol_test-1_WriteHitIOs=73948920\n'
    parser = OptionParser(usage)
    parser.add_option("-u", "--url", dest="url", 
                     help="This is the URL you will use to connect to the 3Par")
    parser.add_option("-s", "--search", dest="search", 
                     help="regular expression of what Volume you are searching for")
    parser.add_option("-a", "--auth", dest="auth", 
                     help='This is the Login and Passwd you will use,\n \
                     Example.. --auth=\'login passwd\'')
    parser.add_option("-v", "--volume", action="store_true", dest="volume", 
                     help="Use this option if you want to print all volumes IO stats")
    parser.add_option("-p", "--port", action="store_true", dest="port", 
                     help="Use this option if you want to print all port IO stats")
    parser.add_option("-d", "--disk", action="store_true", dest="disk", 
                     help="Use this option if you want to print all disk IO stats")
    (options, args) = parser.parse_args()

    if options.auth and options.url:
        options.auth = tuple(string.split(options.auth, sep=" "))
        main()
