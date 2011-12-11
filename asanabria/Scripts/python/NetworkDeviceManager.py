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

"""
Revision .22 10/02/2009
    * Threading has been implemented into the script. Drastic Speed increase!!
    * Better error checking!

Revision .21 10/01/2009
    * Can now save output to a file. using the --save option

Revision .20 09/27/2009
    * Support for Cisco Devices and Linux Operating Systems
    * Support for telnet and ssh or both
    * Knows if you passed sudo, su, or enable
    * Can pass 1 device or multiple devices through a text file.
    * Can pass 1 command or multiple commands through a text file.
    * When running show commands on Cisco devices, the script will know to send a ( space bar ) to get more info
"""
import os
import sys
import re
import string
import pexpect
import getopt
import threading
from time import ctime
from time import sleep

MAXREAD = 100000
WINDOWSIZE = -1
LOGIN_PROMPT = "\>|\%|\$|\#"
PROMPT = "\>(\s{0,2})?$|\%(\s{0,2})?$|\$(\s{0,2})?$|\#(\s{0,2})?$"
ROOT_PROMPT = "\#"
PERMISSION_DENIED = ".*enied|.*nvalid|.*ailed"
MODULUS_TO_SMALL = "modulus too small"
PROTOCOL_DIFFER = "Protocol major versions differ"
NEWSSHKEY = "Are you sure you want to continue connecting"
INVALID_INPUT = "Invalid input detected"
HOST_KEY_FAILED = "verification failed"
CONNECTION_REFUSED = "Connection refused"
RESET_BY_PEER = "reset by peer|closed by foreign host"
PASS = ".ssword.*|Password:"
USERNAME = ".sername.*"
PRIVALEGE = re.compile(r"^\benable\b|^\ben\b|^\bsu\b")
MORE = "--more--|--More--|^\!"
EOF = pexpect.EOF
tout = 10
term = "both"
good_count = []
unknown_count = []
timeout_count = []
badlp_count = []
key_count = []
reset_count = []
refused_count = []

def main():
    status = 0
    drange = []
    if login and passwd and dlist and clist or \
       login and passwd and device and command or \
       login and passwd and dlist and command or \
       login and passwd and device and clist or \
       login and dlist and clist or \
       login and device and command or \
       login and dlist and command or \
       login and device and clist:
        if dlist:
            print "file list %s" % dlist
            device_list = open(dlist, 'r')
            for line in device_list:
                line = re.sub("\n$", "", line)
                drange.append(line)
            device_list.close()
        else:
            drange.append(device[0])
        threads = []
        nloops = range(len(drange))
        for dline in drange:
            dline = [dline]
            after = thread_command(command_exec, (dline,), command_exec.__name__)
            threads.append(after)

        for i in nloops:
            threads[i].start()
            #sleep(1)
        for i in nloops:
            threads[i].join()

    else:
        usage()

    print "Total host that passed %d" % len(good_count)
    for line in good_count:
        print line
    print "Total host that failed %d" % len(unknown_count)
    for line in unknown_count:
        print line
    print "Total host that had either incorrect login or passwords %d" % len(badlp_count)
    for line in badlp_count:
        print line
    print "Total host that timed out %d" % len(timeout_count)
    for line in timeout_count:
        print line
    print "Total host that were reset by peer or Connection Closed by Peer %d" % len(reset_count)
    for line in reset_count:
        print line
    print "Total host that Host Key Verification Failed on %d" % len(key_count)
    for line in key_count:
        print line
    print "Total host that Connection was refused on %d\n Check Access List" % len(refused_count)
    for line in refused_count:
        print line

def printFormat(variable, width, option="right"):
    if option == "right":
        varOut = variable + ' '  * ( width - len(variable) )
    elif option == "left":
        space = width - len(variable)
        varOut = ' '  * ( len(variable) - width + 1 )  + variable 
    return varOut
    return ' '*space + variable

def escalated_priv(cmd, host):
    try:
        priv = re.sub("\\\\", "", enable)
    except:
        priv = passwd
    status = 0
    if PRIVALEGE.search(cmd):
        if command:
            host.sendline(cmd)
        elif clist:
            host.send(cmd)
        status = host.expect([PASS, PROMPT, EOF], timeout=tout)
        if status == 0:
            host.sendline(priv)
            status = host.expect([LOGIN_PROMPT, PASS,  EOF])
            if status == 0:
                print "I'm in enable mode"
            elif status == 1:
                print "Password Incorrect"
            else:
                print "status ", status
        elif status == 1:
            status = 0
    return( status, host )

def ssh_login( host ):
    host = host[0]
    authorized = False
    status = 0
    session = "ssh " + login+"@"+host
    command = pexpect.spawn( session, maxread=MAXREAD, searchwindowsize=WINDOWSIZE )
    if term == "ssh" or term == "both":
        if verbose:
            print "connecting to %s using %s" % (host, session)
        try:
            status = command.expect( [NEWSSHKEY, PASS, MODULUS_TO_SMALL, PROTOCOL_DIFFER, LOGIN_PROMPT, EOF, HOST_KEY_FAILED, CONNECTION_REFUSED, RESET_BY_PEER], timeout=tout )
        except:
            status = 10
            return( status, command )
        if status == 2:
            if verbose:
                print "Protocol Version 2 failed with host key to small, Trying to connect to host using ssh Protocol version 1"
            session = "ssh -1 " + login+"@"+host
            command = pexpect.spawn( session, maxread=MAXREAD, searchwindowsize=WINDOWSIZE )
            if verbose:
                print "connecting to %s using %s" % (host, session)
            status = command.expect( [NEWSSHKEY, PASS, MODULUS_TO_SMALL, PROTOCOL_DIFFER,  EOF], timeout=tout )
            if status == 3:
                if verbose:
                    print "Protocol MisMatch"
        if status == 0:
            if verbose:
                print "saying yes to accepting ssh key"
            command.sendline("yes")
            status = command.expect( [PASS, LOGIN_PROMPT, EOF] )
            if status == 0:
                command.sendline( passwd )
                status = command.expect( [USERNAME, PASS, PERMISSION_DENIED, LOGIN_PROMPT, EOF], timeout=tout )
                if status == 0 or status == 1 or status == 2:
                    if verbose:
                        print "Password Incorrect %s" % PERMISSION_DENIED
                    status = 9
                elif status == 3:
                    if verbose:
                        print "%s Authenticated, through ssh" % host
                    status = 0
            if status == 1:
                status = 0
                pass
        elif status == 1:
            if verbose:
                print "ssh key already in host file"
            command.sendline('\x03')
            command.close()
            command = pexpect.spawn( session, maxread=MAXREAD, searchwindowsize=WINDOWSIZE )
            status = command.expect( [PASS, EOF] )
            if status == 0:
                command.sendline( passwd )
                status = command.expect( [USERNAME, PASS, PERMISSION_DENIED, LOGIN_PROMPT, EOF], timeout=tout )
                if status == 0 or status == 1 or status == 2:
                    if verbose:
                        print "Password Incorrect %s" % PERMISSION_DENIED
                    status = 9
                elif status == 3:
                    if verbose:
                        print "%s Authenticated, through ssh" % host
                    status = 0
        elif status == 4:
            status = 0
        elif status == 6:
            if verbose:
                print "Host Key Verification Failed for %s" % host
        elif status == 7:
            if verbose:
                print "Connection to %s was refused" % host
        elif status == 8:
            if verbose:
                print "Connection to %s was reset by peer" % host
    return( status, command ) 

def telnet_login(host):
    host = host[0]
    authorized = False
    status = 0
    session = "telnet " + host
    command = pexpect.spawn( session, maxread=MAXREAD, searchwindowsize=WINDOWSIZE  )
    if term == "telnet" or term == "both":
        print "connecting to %s using %s" % ( host, session )
        try:
            status = command.expect( [".sername*", PASS, EOF, CONNECTION_REFUSED, RESET_BY_PEER], timeout=tout )
        except:
            status = 10
            return( status, command )
        if status == 0 or status == 1:
            print "Logging in using telnet", status
            if status == 0:
                command.sendline(login)
                status = command.expect( [PASS, EOF], timeout=tout )
                if status == 0:
                    command.sendline(passwd)
                    status = command.expect( [USERNAME, PASS, PERMISSION_DENIED, LOGIN_PROMPT, EOF], timeout=tout )
            elif status == 1:
                command.sendline(passwd)
                status = command.expect( [USERNAME, PASS, PERMISSION_DENIED, LOGIN_PROMPT, EOF], timeout=tout )
            if status == 0 or status == 1 or status == 2:
                print "Password Incorrect %s" % PERMISSION_DENIED
                status = 9
            elif status == 3:
                print "%s Authenticated, through telnet" % host
                status = 0
        elif status == 3:
            print "Connection to %s was refused" % host
            status = 7
        elif status == 4:
            print "Connection to %s was refused" % host
            status = 8
                    
    return( status, command ) 


def command_exec(dline):
    auth = 0
    if save:
        try:
            save_out = file(dline[0]+".txt", "a")
        except:
            save_out = file(str(dline[0][0])+".txt", "a")
    if term == "ssh":
        auth, host = ssh_login( dline )
    elif term == "telnet":
        auth, host = telnet_login( dline )
    elif term == "both":
        auth, host = ssh_login( dline )
        if auth != 0 and auth != 9:
            auth, host = telnet_login( dline )
            if auth != 0:
                if verbose:
                    print auth, " ssh and telnet failed"
    if auth == 0:
        good_count.append(dline[0])
        if clist:
            command_list = open(clist, 'r')
        else:
            command_list = command
        for cline in command_list:
            if PRIVALEGE.search(cline):
                status, host = escalated_priv(cline, host)
                if save:
                    host.logfile=save_out
                if status != 0:
                    print "Could not get escalated privaleges"
                    sys.exit(1)
                if output:
                    print host.before
            elif re.search(r"\bsudo\b", cline):
                if save:
                    host.logfile=save_out
                if command:
                    host.sendline( cline )
                elif clist:
                    host.send(cline)
                status = host.expect([PASS, LOGIN_PROMPT, EOF], timeout=tout)
                if status == 0:
                    host.sendline(passwd)
                    status = host.expect([LOGIN_PROMPT, EOF], timeout=tout)
                elif status == 1:
                    status = 0
                if output:
                    print host.before, host.after
                            
            else:
                if save:
                    host.logfile=save_out
                if command:
                    host.sendline( cline )
                elif clist:
                    host.send( cline )
                status = host.expect( [INVALID_INPUT, MORE, PROMPT, EOF], timeout=tout )
                if status == 0:
                    print "Command did not run correctly: ", host.before, host.after
                    sys.exit(1)
                if status == 1:
                    print host.before 
                    while status == 1:
                        host.send('\x20')
                        status = host.expect( [INVALID_INPUT, MORE, PROMPT, EOF], timeout=tout )
                        print host.before 
                        print host.match.group() 
                else:
                    if output:
                        print host.before 
                        print host.after 
                            

        if save:
            save_out.close()
    elif auth == 10:
        print "TIMED OUT, could not connect to %s" % dline[0]
        timeout_count.append(dline[0])
    elif auth == 9:
        print "Permission Denied, could not connect to %s" % dline[0]
        badlp_count.append(dline[0])
    elif auth == 6:
        print "Ssh Host Key Verification Failed, could not connect to %s" % dline[0]
        key_count.append(dline[0])
    elif auth == 7:
        print "Could not connect to %s, Connection was refused" % dline[0]
        refused_count.append(dline[0])
    elif auth == 8:
        print "Could not connect to %s,  Because connected was reset by peer" % dline[0]
        reset_count.append(dline[0])
    else:
        print "%s not Authenticated" % dline[0]
        unknown_count.append(dline[0])
    host.close()

class thread_command(threading.Thread):
  def __init__(self, func, args, name=''):
      threading.Thread.__init__( self )
      self.name = name
      self.func = func
      self.args = args

  def run(self):
      apply(self.func, self.args)


            
def usage():
    A = 20
    B = 50

    print printFormat("-l, --login", A)+ printFormat("Your user name to the device. Example below..", B)
    print printFormat(" ", A)+printFormat("-l 'admin', --login='admin'", A)
    print printFormat("-p, --passwd", A)+ printFormat("Your password to the device. Example below..", B)
    print printFormat(" ", A)+printFormat("-p 'passwd', --passwd='pass'", A)
    print printFormat("-e, --enable", A)+ printFormat("Your enable or su or sudo password to the device. Example below..", B)
    print printFormat(" ", A)+printFormat("-e 'passwd', --enable='pass'", A)
    print printFormat("-D, --dlist", A)+ printFormat("List of devices you want to run this script against. Example below..", B)
    print printFormat(" ", A)+printFormat("-D '/home/test/switches.txt', --dlist='/home/test/switches.txt'", A)
    print printFormat("-d, --device", A)+ printFormat("The devices you want to run this script against. Example below..", B)
    print printFormat(" ", A)+printFormat("-d '192.168.101.1', --device='192.168.101.1'", A)
    print printFormat("-C, --clist", A)+ printFormat("List of commands that you want to run ithis script against. Example below..", B)
    print printFormat(" ", A)+printFormat("-C '/home/test/commands.txt', --clist='/home/test/commands.txt'", A)
    print printFormat("-c, --command", A)+ printFormat("The command that you want to run. Example below..", B)
    print printFormat(" ", A)+printFormat("-c '/sbin/netstat -tln', --command='show vlan'", A)
    print printFormat("-t, --term", A)+ printFormat("What terminal you are going to use (ssh or telnet or both) The default is to use both. Example below..", B)
    print printFormat(" ", A)+printFormat("-t 'ssh', --term='ssh'", A)
    print printFormat("-o, --output", A)+ printFormat("The default is to run all the commands with out outputting them, this will enable output", B)
    print printFormat(" ", A)+printFormat("-o, --output", A)
    print printFormat("-T, --tout", A)+ printFormat("The default is to timeout after 10 seconds of no output", B)
    print printFormat(" ", A)+printFormat("-T, --tout", A)
    print printFormat("-s, --save", A)+ printFormat("This option will save the output in a .txt file per host.", B)
    print printFormat(" ", A)+printFormat("-s, --save", A)
    print printFormat("-h, --help", A)+ printFormat("The will display this help file", B)
    print printFormat("\nExamples Below..", A)
    print printFormat("python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -C './cmd.txt' -t ssh -e 'p\@55wd' --output --tout=2", A)
    print printFormat("python ldNetDeviceManager.py --login=dynasty --passwd='passwd' --dlist='./switches' --clist='./cmd.txt' --term=both --enable='p\@55wd' --output --tout=2", A)
    print printFormat("python ldNetDeviceManager.py --login=dynasty --passwd='passwd' --dlist='./switches' --command='service snmpd restart' --term=ssh --enable='p\@55wd' --output --tout=20, --save", A)
    print printFormat("python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -C './cmd.txt' -t ssh  -o --tout=2", A)
    print printFormat("\nIf you have SSH Keys then you do not need to pass a password unless you have to get root access or sudo access. example below..", A)
    print printFormat("python ldNetDeviceManager.py -l dynasty -d 192.168.101.11 -C './cmd.txt' -t ssh  -o --tout=2", A)
    print printFormat("python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -c 'sudo service snmpd restart' --term=ssh  --output --tout=2", A)
    print printFormat("python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -c 'sudo service snmpd restart' --output --save", A)
    sys.exit(0)

try:
     opts, args = getopt.getopt(sys.argv[1:], 'p:C:c:t:T:D:d:l:e:sovh',
     [ 'passwd=', 'command=', 'clist=', 'device=', 'dlist=', 'login=', 'tout=', 'term=', 'enable=', 'save', 'output', 'verbose', 'help' ]
     )
except getopt.error, e:
    print "I did not make it", e
    usage()

help = verbose = save = output = login = command = enable = device = passwd = clist = dlist = None

for opt, val in opts:
    if opt in ('-l', '--login'):
        login = val
    if opt in ('-e', '--enable'):
        enable = re.sub("\\\\", "", val)
    if opt in ('-p', '--passwd'):
        passwd = re.sub("\\\\", "", val)
    if opt in ('-D', '--dlist'):
        dlist = val
    if opt in ('-d', '--device'):
        device = []
        device.append(val)
    if opt in ('-C', '--clist'):
        clist = val
    if opt in ('-c', '--command'):
        command = []
        command.append(val)
    if opt in ('-t', '--term'):
        term = val
    if opt in ('-T', '--tout'):
        tout = int(val)
    if opt in ('-o', '--output'):
        output = True
    if opt in ('-s', '--save'):
        save = True
    if opt in ('-v', '--verbose'):
        verbose = True
    if opt in ('-h', '--help'):
        help = True

if help:
    usage()
if __name__ == "__main__":
    main()
