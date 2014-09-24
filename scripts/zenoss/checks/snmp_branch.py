#!/usr/bin/env python
#Created by Allen Sanabria aka LinuxDynasty
#Copyright (C) 2009  Allen Sanabria

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

import sys
import re
import string
import getopt
from pysnmp.entity.rfc3413.oneliner import cmdgen

__author__ = "Allen Sanabria"
__copyright__ = "Copyright 2010, LinuxDynasty"
__license__ = "GPL"
__version__ = "1.0.10"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"

def str2int(orig_oid):
    for id in range(len(orig_oid)):
        orig_oid[id] = int(orig_oid[id])
    return tuple(orig_oid)

def main(args):
    if help:
        usage(0)
    elif community and device and oid and port:
        SnmpBranch = initconn()
        printMagic(SnmpBranch, community, device, oid, port, ival, label, length)
    else:
        usage(0)

def initconn():
    oid_pre_check = re.sub("^\.", "", oid)
    oid1 = str2int(list(string.split(oid_pre_check, sep=".")))
    try:
        errorIndication, errorStatus, errorIndex, \
                      SnmpData = cmdgen.CommandGenerator().nextCmd\
	                  (cmdgen.CommunityData('test-agent', community, version),\
				      cmdgen.UdpTransportTarget((device, port)), oid1)
    except (errorIndication, ValueError,TypeError), e:
        print e

    if len(SnmpData) == 0:
        print "No data returned, Empty Tuple"
        sys.exit(1)

    return(SnmpData)
    
def printMagic(SnmpBranch, community, device, oid, port, ival, label, length=None):
    oid_pre_check = re.sub("^\.", "", oid)
    out_oid = []
    i = 0
    if length:
        length = int(length) - len(str(ival))
        length = str(length)
    for leaves in range(len(SnmpBranch)):
        if ival:
            if length:
                mi = re.search(r"\.[0-9]{"+length+"}"+str(ival)+"\)$", re.sub(", ", ".",str(SnmpBranch[leaves][0][0])))
                #print mi, "BAM"
            else:
                mi = re.search(r"\."+ival+"\)$", re.sub(", ", ".",str(SnmpBranch[leaves][0][0])))
            if label:
                if ival and mi and len(label) > 1:
                    out1 = "%s=%s" % (label[i],SnmpBranch[leaves][0][1])
                    out_oid.insert(leaves,out1)
                    i += 1

                elif ival and mi and len(label) == 1:
                    out1 = "%s%s=%s" % (label[0],str(i),SnmpBranch[leaves][0][1])
                    out_oid.insert(leaves,out1)
                    i += 1

            elif ival and mi and not label:
                out1 = "default%s=%s" % (str(i),SnmpBranch[leaves][0][1])
                out_oid.insert(leaves,out1)
                i += 1
        
        elif not ival:
            if fsearch:
                if label and re.search(r"\."+fsearch+"[0-9]+\)$", re.sub(", ", ".",str(SnmpBranch[leaves][0][0]))):
                    if len(label) > 1:
                        out1 = "%s=%s" % (label[i],SnmpBranch[leaves][0][1])
                        out_oid.insert(leaves,out1)
                        i += 1
                    elif len(label) == 1:
                        out1 = "%s%s=%s" % (label[0],str(i),SnmpBranch[leaves][0][1])
                        out_oid.insert(leaves,out1)
                        i += 1
                elif not label and re.search(r"\."+fsearch+"[0-9]+\)$", re.sub(", ", ".",str(SnmpBranch[leaves][0][0]))):
                    out1 = "default%s=%s" % (str(i),SnmpBranch[leaves][0][1])
                    out_oid.insert(leaves,out1)
                    i += 1

            else:
                if label:
                    if len(label) > 1:
                        out1 = "%s=%s" % (label[i],SnmpBranch[leaves][0][1])
                        out_oid.insert(leaves,out1)
                        i += 1
                    elif len(label) == 1:
                        out1 = "%s%s=%s" % (label[0],str(i),SnmpBranch[leaves][0][1])
                        out_oid.insert(leaves,out1)
                        i += 1

                elif not label:
                    out1 = "default%s=%s" % (str(i),SnmpBranch[leaves][0][1])
                    out_oid.insert(leaves,out1)
                    i += 1

    final_out =  re.sub("\[|\]|\'|\"|\,", "",str(string.split(str(out_oid), sep=" ")))
    print "|"+final_out



def usage(code =0):
    print """
    example from Zenoss gui.....
    snmp_branch.py -d ${here/manageIp} -c ${here/zSnmpCommunity} -o 1.3.6.1.4.1.9.9.416.1.3.1.1.5 -p 161 --label="background0, bestEffort0, video0, voice0, background1, bestEffort1, video1, voice1"
    |background0=44896  bestEffort0=739905  video0=0  voice0=1318  background1=3812  bestEffort1=62451  video1=0  voice1=139
    
    example from command line with labels....
    snmp_branch.py -d 127.0.0.1 -c public -o 1.3.6.1.4.1.9.9.416.1.3.1.1.5 -p 161 --label="background0, bestEffort0, video0, voice0, background1, bestEffort1, video1, voice1"
    |background0=44896  bestEffort0=739905  video0=0  voice0=1318  background1=3812  bestEffort1=62451  video1=0  voice1=139
    
    example with out labels....
    snmp_branch.py -d ${here/manageIp} -c ${here/zSnmpCommunity} -o 1.3.6.1.4.1.2334.2.1.2.2.1.14 -p 161 
    |default0=55174635 default1=63348274

    example with one label.....
    snmp_branch.py -d ${here/manageIp} -c ${here/zSnmpCommunity} -o 1.3.6.1.4.1.2334.2.1.2.2.1.14 -p 161 --label="eth"
    |eth0=55174635 eth1=63348274

    example with OID index and labels...
    snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.25.2.3.1 --ival="3" --label="diskIndex,diskType,diskDescr,diskAlloc,diskSize,diskused"
    |diskIndex=3 diskType=(1 3 6 1 2 1 25 2 1 3) diskDescr=Swap Space diskAlloc=1024 diskSize=2096472 diskused=232 

    example wih OID index and a default label...
    snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1 --ival="2" --label="eth0"
    |eth00=2 eth01=eth0 eth02=6 eth03=1500 eth04=100000000 eth05=\\x00\\x02\\xb3\\xb7\\xe3\\xc0 eth06=1 eth07=1 eth08=0 eth09=3100462457 eth010=104425977
    eth011=0 eth012=0 eth013=0 eth014=0 eth015=2258887125 eth016=84531927 eth017=0 eth018=0 eth019=0 eth020=0 eth021=(0 0)

    example with a more then one index value.... This test is on a Cisco Access Point
    snmp_branch.py -d ${here/manageIp} -c ${here/zSnmpCommunity} -o 1.3.6.1.4.1.9.9.416.1.3.1.1 -p 161 --ival="1.1"
    |default0=40 default1=58 default2=32334 default3=18314 default4=760557

    which would be equivalent too
    snmpwalk -v2c -c ${here/zSnmpCommunity} -d ${here/manageIp} 1.3.6.1.4.1.9.9.416.1.3.1.1 |grep -P "1.1 ="
    CISCO-DOT11-QOS-MIB::cdot11QosDiscardedFrames.1.1 = Counter32: 40
    CISCO-DOT11-QOS-MIB::cdot11QosFails.1.1 = Counter32: 58
    CISCO-DOT11-QOS-MIB::cdot11QosRetries.1.1 = Counter32: 32334
    CISCO-DOT11-QOS-MIB::cdot11QosMutipleRetries.1.1 = Counter32: 18314
    CISCO-DOT11-QOS-MIB::cdot11QosTransmittedFrames.1.1 = Counter32: 760557


    -c, --community=   SNMP Community To Use
    -d, --device=      Device Name or IP Address
    -o, --oid=         The SNMP OID To Walk
    -p, --port=        The SNMP Port To Use, usually 161
    -l, --label=       This will be a list of lables that you want applied to each data point "Inside_Link, Outside_link"
    -i, --ival=        This will grab the index specified and all of its oid's related to that index
    -l, --length=      This option with the --ival option will give you an exact match of the indexed OID. In most cases, the indexed oid 
                       is like this .1 or .100, but there are special cases where the indexed OID is .46432510 Now you only want to match 10
                       and you do not care for the rest. Example...
                       snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1.16 --ival="24" --length="9"
    -f, --fsearch      This option does not work with ival or length. This options is for certain special cases where you only wach to match 
                       the begining digits of the last octect of the OID (.1.3.6.1.2.1.2.2.1.16.1073741824). Example...
                       snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1.16 --fsearch="1073"
    -v, --version=     SNMP Version 1 or SNMP Version 2
    """
    return 0

try:
  opts, args = getopt.getopt(sys.argv[1:], "c:d:o:p:l:L:i:f:v:h",
    [ 'community=', 'device=', 'oid=', 'port=', 'label=', 'length=', 'ival=', 'fsearch=', 'version=', 'help' ]
      )
except getopt.error:
  usage()

help = community = device = oid = port = label = length = ival = version = fsearch = None
for opt, val in opts:
    if opt in ('-c', '--community'):
       community = val
    if opt in ('-d', '--device'):
        device = str(val)
    if opt in ('-o', '--oid'):
        oid = val
    if opt in ('-p', '--port'):
        port = int(val)
    if opt in ('-i', '--ival'):
        ival = val
    if opt in ('-f', '--fsearch'):
        fsearch = val
    if opt in ('-L', '--length'):
        length = val
    if opt in ('-v', '--version'):
        version = val
        if version == str(1):
            version = 0
        elif version == str(2):
            version = 1
        else:
            print "For SNMP Version 1, please pass 1. For SNMP v2 pass 2"
            sys.exit(1)
    else:
        version = 1
    if opt in ('-l', '--label'):
	    label = list(string.split(val, sep=","))


if __name__ == "__main__":
    main(sys.argv[1:])

