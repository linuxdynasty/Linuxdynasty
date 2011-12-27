#!/usr/bin/env python

import sys
import re
import string
from subprocess import os
from subprocess import Popen
from subprocess import PIPE
from optparse import OptionParser

LOGTAIL = '/usr/sbin/logtail'
TMPDIR = '/tmp'
ERRORCODES = ['400', '404', '500', '503', '504', '200']

codes = re.compile(r'HTTP\/1.[0-9]\s+([0-9]{3})\s+')
stats = { '400' : 0, '404' : 0, '500' : 0, 
          '503' : 0, '504' : 0, '200' : 0
        }
if not os.path.exists(LOGTAIL):
    print "Please install logtail"
    sys.exit(1)

if __name__ == '__main__':
    usage =''
    parser = OptionParser(usage)
    parser.add_option("-d", "--directory", dest="directory",
                     help = "The directory where the access logs exist")
    parser.add_option("-f", "--file", dest="file",
                     help = "name of the access log")
    (options, args) = parser.parse_args()

    if options.directory and options.file:
        if os.path.exists(os.path.join(options.directory, options.file)):
            fpath = os.path.join(options.directory, options.file)
            command = Popen([LOGTAIL, '-f', fpath, '-o', os.path.join(TMPDIR, options.file)], stdout=PIPE)
            tmpfile = command.stdout.readlines()
            count = 0
            for code in ERRORCODES:
                for i in tmpfile:
                    if re.search(r'HTTP\/1.[0-9]\"\s+('+code+')\s+', i):
                        count = count +1
                        stats[code] = count
    print 'Nginx Codes OK|count200=%d count400=%d count404=%d count500=%d count503=%d count504=%d' %\
          (stats['200'], stats['400'], stats['404'], stats['500'], stats['503'], stats['504'])
