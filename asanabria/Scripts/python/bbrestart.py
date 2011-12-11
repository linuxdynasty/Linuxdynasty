#!/usr/bin/env python
#Created by Allen Sanabria on Aug 18 2009
#Restart list of BlackBoard Web Servers as the bbexec user.
#Essentially ssh as the bbexec user (ssh key ) to the webserver
#and restart BlackBoard. There is some error checking..

import os
import subprocess
import string
import time

bbweb = [ "eagle.newschool.edu", "falcon.newschool.edu", "hawk.newschool.edu" ]
bbuser = "bbexec"
scontroller = "sudo /usr/local/blackboard/tools/admin/ServiceController.sh"
date = string.split(time.ctime(), " ")
outlog = "output-"+date[1]+"-"+date[2]+"-"+date[4]+".log"
errorlog = "error-"+date[1]+"-"+date[2]+"-"+date[4]+".log"
bbretval = []
logdir = "/var/log/"
host_retval = []
outFile = os.path.join(logdir, outlog)
outptr = file(outFile, "a", 0)
errFile = os.path.join(logdir, errorlog)
errptr = file(errFile, "a", 0)

for host in bbweb:
    bblogin = bbuser+"@"+host
    bbstop = ["ssh", bblogin, scontroller + " services.stop"]
    bbstart = ["ssh", bblogin, scontroller + " services.start"]
    outptr.write("beginning Shutdown of Blackboard on " + host)
    stopbb_retval = subprocess.call(bbstop, 0, None, None, outptr, errptr)
    outptr.write("beginning Startup of Blackboard on " + host)
    startbb_retval = subprocess.call(bbstart, 0, None, None, outptr, errptr)
    if stopbb_retval == 0 and startbb_retval == 0:
        print "BlackBoard has been successfully restarted on " + host
    elif stopbb_retval == 1 or startbb_retval == 1:
        if stopbb_retval == 1:
            print "Issues stoping BlackBoard on " + host
        elif startbb_retval == 1:
            print "Issues starting BlackBoard on " + host
        else:
            print "Can not stop or start BlackBoard on " + host

errptr.close()
outptr.close()
