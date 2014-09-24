#!/usr/bin/python
#Created by Allen Sanabria aka LinuxDynasty
#!/usr/bin/python

#This script will reorder your vmnics for you
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
#        Name   PCI   Driver  Link  Speed  Duplex MTU    Description
#vmnic = [0]    [1]   [2]     [3]   [4]    [5]    [6]    [7]
#Last Modified 03/11/2009
import os
import sys
import re
import string
import getopt


try:
  opts, args = getopt.getopt(sys.argv[1:], "v",[ 'verbose' ])
except getopt.error:
  usage() 
verbose = None
for opt, val in opts:
  if opt in ('-v', '--verbose'):
    verbose = True


def case_match(vmnic):
  s1 = re.compile("(\/device\/)(\w+\:\w+\.\w+)(\/vmkname \= )\"vmnic[0-9]+\"")
  sub1 = s1.search(vmnic)
  for i in range(len(nics)):
    if sub1:
      if sub1.group(2) == nics[i][0]:
        match0 = re.sub(sub1.group(),
                 sub1.group(1)+nics[i][0]+sub1.group(3)+"\""+nics[i][1]+"\"", vmnic)
        return match0

esxcfg_nics = os.popen("/usr/sbin/esxcfg-nics -l").readlines()
esxcfg_nics.pop(0)
def hex2dec(h):
  d =  int(h, 16)
  return str(d)

vmnic = []
nics = []
nicname = "vmnic"

for line in range(len(esxcfg_nics)):
  vmnic = string.split(esxcfg_nics[line])
  nics.append([vmnic[1], vmnic[0], vmnic[2], vmnic[3]])

if verbose:
  print "Pre Sort"

for line in range(len(nics)):
  match = re.search("(^\w+)\:(\w+)\.(\w+)", nics[line][0])
  if match:
    nics[line][0] = hex2dec(match.group(1)).zfill(3)+":"+match.group(2)+"."+hex2dec(match.group(3))
  if verbose:
    print nics[line][0]

if verbose:
  print "\nPost Sort"

nics.sort()
for line in range(len(nics)):
  nics[line][1] = "vmnic"+str(line)
  if verbose:
    print nics[line][0]

esxcfg = open("/etc/vmware/esx.conf", "r")
esxcfg_new = open("/etc/vmware/esx.conf.new", "a")

for line in esxcfg:
  match = case_match(str(line))
  if match:
    esxcfg_new.write(match)
    if verbose:
      print "Original Line: "+line,
      print "New Line: "+match
  else:
    esxcfg_new.write(line)

esxcfg.close()
esxcfg_new.close()

os.rename("/etc/vmware/esx.conf", "/etc/vmware/esx.conf.orig")
os.rename("/etc/vmware/esx.conf.new", "/etc/vmware/esx.conf")
