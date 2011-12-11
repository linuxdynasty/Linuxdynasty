#!/bin/env python
##############################################################
#Created by Allen Sanabria aka LinuxDynasty aka PrNino69
#This script is to check how many devices are in the
#Discovered Class
#Started Nov 28th
#Completed, Nov 28th
##############################################################

import os, sys
from re import sub
from string import split
from string import join
from urllib import urlopen
from smtplib import SMTP
from time import sleep


user = "zenoss"
passwd = 'zenoss'
util = '@zenoss'
base = "http://%s:%s%s:8080" % (user,passwd,util)
discovered_url = urlopen(base+'/zport/dmd/Devices/Discovered/getSubDevices').read()
discovered_sub = sub("<Device at /zport/dmd/Devices/Discovered/devices/|>|^\[|\]$|,", "", discovered_url)
discovered_list = list(split(discovered_sub))


message = "\nThe boxes below were discovered in the last run of zendisc.\nThey are all located under /Devices/Discovered Class.\nPlease move Devices to appropriate Device class, if one does not exist please create one.\nThis script runs on the zenoss (cc17-22) server."
devices = sub(",|\[|\]", "\n", str(discovered_list))
BODY = join((message, devices),"\n")
print BODY
FROM = "zenoss@communityconnect.com"
TO = "sa@communityconnect.com"
SUBJECT = "Devices That Were Discovered During The Network Scan!"
body = join(("From: %s" % FROM, "To: %s" % TO, "Subject: %s" % SUBJECT, "", BODY), "\n")
server = SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(FROM, [TO], body)
sleep(10)
server.quit()
