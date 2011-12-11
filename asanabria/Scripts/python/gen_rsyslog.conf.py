#!/usr/bin/env python

import os
import sys
import re
import string

from optparse import OptionParser
usage = "usage: %prog arg --file"
parser = OptionParser(usage)
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-t", "--template", dest="template_name",
                  help="Template name template=NAME")
parser.add_option("-c", "--cluster", dest="cluster_name",
                  help="Cluster name cluster=NAME")
(options, args) = parser.parse_args()

var_dir = '/var/log/remote'
hosts = open(options.filename, 'r')
lsys = []
for i in hosts:
  lsys.append(re.sub(r'\n','',i))
val = lsys.pop(0)
template = '$template %s,\"%s/%s/%sprogramname%s.log\"' % (options.template_name, var_dir, options.cluster_name, "%", "%")
base_text = 'if $source == \'%s\' \\ \n' % (val)
for i in lsys:
  base_text += '    or $source == \'%s\' \\ \n' % (i)
base_text += 'then ?%s' % (options.template_name)
print template
print base_text
