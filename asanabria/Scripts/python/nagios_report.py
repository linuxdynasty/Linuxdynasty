#!/usr/bin/env python
#Copyright (C) 2008 Allen Sanabria

#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import os
import re
import string
import sys
from time import ctime

t = re.compile("^(\w+)\s+(\w+)\s+(\d+)")
month = t.match(ctime()).group(2)
day = t.match(ctime()).group(3)
log = str(sys.argv[1])
print log
status_report = "/export/home/nagios/log/daily_report-"+month+"-"+day+".txt"
nagios_log = open(log, 'r')
log_list = []
for line in nagios_log:
    log_list.append(line)
nagios_log.close
log_list.pop(0)
log_list.pop(1)
log_list.pop()
hosts_done = []
hosts_alert = []
linem = re.compile("^\[(\d+)\]\s+(\w+.*?\:)\s+(\D+\w+|\w+\-\w+)\;(\w+)\;(\w+)") ##[1223956800] CURRENT HOST STATE: host-301;UP;HARD;1;PING OK - Packet loss = 0%, RTA = 34.94 ms
linel = re.compile("^\[(\d+)\]\s+(\w+.*?\:|Auto|Caught|Nagios|Successfully|Local|LOG|Finished)")

def uniq_host():
    for line in log_list:
        ignorem = linel.search(line).group(2)
        if re.match("HOST ALERT",ignorem):
	    ignores = linem.search(line).group(5)
	    ignoret = linem.search(line).group(4)
            hostn = linem.search(line).group(3)
	    if re.match("HARD", ignores) and re.match("HOST ALERT",ignorem):
                hosts_alert.append(line)
            if hosts_done.__contains__(hostn):
                continue
            elif re.match("HARD", ignores) and re.match("HOST ALERT",ignorem) and re.match("DOWN", ignoret):
                hosts_done.append(hostn)
        elif re.match("LOG|Auto|Caught|Nagios|Successfully|Local|LOG|Finished",ignorem):
	    log_list.remove(line)

def count_alerts():
    thdown = 0
    host_down = []
    status_count = []
    properf = re.compile("(^\w+.*)\s+(\w+)\s+(\d+)\s+(\w+\s+\w+)")
    report = open(status_report, 'a', 0)
    for host in hosts_done:
        host_down, status_count = track_alerts(host)
        report.write("Host " + host + " Status Report\n")
	report.write("-----------------------------------------------------------------\n")
	report.write("Total Times Down = " + str(status_count[0]) + "\n")
	for single in host_down:
	    hstatus = properf.match(single).group(2)
	    htime = properf.match(single).group(3)
	    report.write(host + " went " + hstatus + "  at " + ctime(int(htime)) + "\n")
	report.write("-----------------------------------------------------------------\n\n")
    report.close()	
        

def track_alerts(host):
	host_status = []
	status_count = [0, 0, 0]   #DOWN, UP, TOTAL
        for line in hosts_alert:
            hostm = linem.search(line).group(3)
            daten = int(linem.search(line).group(1))
            status = linem.search(line).group(4)
            hstate = linem.search(line).group(2)
            state = linem.search(line).group(5)
            if re.match(hostm,host):
	        host_status.append(host+" "+status+" "+str(daten)+" "+hstate)
	        print hostm+ " Went "+status+" at "+ctime(daten)
	        if re.match('DOWN', status):
		    status_count[0] += 1
	        elif re.match('UP', status):
		    status_count[1] += 1
        return host_status, status_count 

if __name__ == '__main__':
    uniq_host()
    count_alerts()
