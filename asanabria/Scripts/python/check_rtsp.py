#!/usr/bin/env python
"""
    A simple way to provide monitoring and statistics using the
    openRTSP command and Zenoss
"""

__author__ = "Allen Sanabria"
__copyright__ = "Copyright 2010, LinuxDynasty"
__license__ = "Apache 2"
__version__ = "0.0.1"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"

import re
import string
import sys
from subprocess import Popen
from subprocess import PIPE
from optparse import OptionParser


def parse_stats(output):
    lslice = 0
    for i in xrange(len(output)):
        if re.search(r'begin_QOS_statistics', output[i]):
            lslice = i
            break
    lslice = lslice + 2
    output.__delslice__(0,lslice)
    output.pop(-1)
    statsout = ''
    for i in output:
        statsout = statsout + re.sub(r'\t', '=', re.sub(r'\n', ' ', i))
    return statsout


command = 'openRTSP -Q -d 3 -D 1 -V rtsp://'
if __name__ == '__main__':
    usage = "usage: %prog arg --grouptype=\'Incoming Requests\' --printstat=\'A\'"
    parser = OptionParser(usage)
    parser.add_option("-d", "--device", dest="device",
                     help="The device you are going to run this against")
    parser.add_option("-p", "--path", dest="path",
                     help='The rtsp url you are going to run this against \
                     Example.. "/livestream/2012"')
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False,
                     help='Increase verbosity')
    parser.add_option("-s", "--stats", dest="stats", action="store_true", default=False,
                     help='retrieve performance stats')
    (options, args) = parser.parse_args()

    if options.device and options.path:
        command ='%s%s%s' % ( command, options.device, options.path )
        if options.verbose:
            print 'Executing %s' % ( command )
        command_output = Popen([command], shell=True, stdout=PIPE, stderr=PIPE)
        stdout = command_output.stdout.readlines()
        stderr = command_output.stderr.readlines()
        command_output.poll()
        command_output.wait()
        if command_output.returncode == 0 and options.stats:
            stats = parse_stats(stderr)
            print 'OK %s, test completed successfull against %s |status=%s %s' % ( options.path, options.device, command_output.returncode, stats )
            if options.verbose:
                print stderr
        else:
            print 'CRITICAL %s, test failed against %s |status=%s' % ( options.path, options.device, command_output.returncode)
            if options.verbose:
                print stderr
