#!/usr/bin/env python

import os
import re
import sys
import string
import subprocess
from time import ctime
from optparse import OptionParser


session = 'echo "stats()" | nc -q1 '
LOGFILE = '/tmp/stats.log'
DEATHSLOG = '/tmp/deaths.tmp'
STATUS = ''
stats = re.compile(r'(restarts):.*0m ([0-9]+).*\n.*(workers):.*0m ([0-9]+).*\n.*(deaths):.*0m ([0-9]+)'\
                  '.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*(connections total):.*0m ([0-9]+).*\n.'\
                  '*(connections active):.*0m (-?[0-9])+')

if __name__ == '__main__':
    usage = "usage: %prog arg --contype=socket|tcp --connection=pathto socket|host:port"
    parser = OptionParser(usage)
    parser.add_option("-t", "--contype", dest="contype",
                     help="socket or tcp")
    parser.add_option("-c", "--connection", dest="connection",
                     help="/tmp/cluster-repl.sock or localhost:8888")
    parser.add_option("-w", "--timeout", dest="timeout", default=5,
                     help="int of how long you want this script to wait until it times out")
    (options, args) = parser.parse_args()

    if options.contype and options.connection:
        if options.contype == 'tcp':
            host, port = options.connection.split(":")
            session = session + ' '+ host + ' ' + port
        elif options.contype == 'socket':
            session = session + ' '+ options.connection
        try:
            LOG = open(LOGFILE, 'a', 0)
        except Exception, e:
            print e
            sys.exit(2)
        try:
            output = subprocess.os.popen(session).read()
        except Exception, e:
            print e
            LOG.write(output)
            sys.exit(2)
        restarts = [stats.search(output).group(1), stats.search(output).group(2)]
        workers = [stats.search(output).group(3), stats.search(output).group(4)]
        deaths = [stats.search(output).group(5), stats.search(output).group(6)]
        connections_total = [re.sub(r'\s+', '_', stats.search(output).group(7)), stats.search(output).group(8)]
        connections_active = [re.sub(r'\s+', '_', stats.search(output).group(9)), stats.search(output).group(10)]
        if os.path.isfile(DEATHSLOG):
           tmp = open(DEATHSLOG, 'r')
           deathstmp = tmp.read()
           tmp.close()
           if deathstmp == deaths[1]:
               print 'Deaths Has not increased, Deaths count is %s NodeJS cluster OK |%s=%s %s=%s %s=%s %s=%s %s=%s' % \
               ( deaths[1], restarts[0], restarts[1], workers[0], workers[1], deaths[0], deaths[1],
               connections_total[0], connections_total[1], connections_active[0], connections_active[1])
               STATUS = 0
           elif deaths < deaths[1]:
               print 'Deaths Has increased, Deaths count is %s NodeJS cluster CRITICAL |%s=%s %s=%s %s=%s %s=%s %s=%s' % \
               ( deaths[1], restarts[0], restarts[1], workers[0], workers[1], deaths[0], deaths[1],
               connections_total[0], connections_total[1], connections_active[0], connections_active[1])
               STATUS = 2
           elif deaths > deaths[1]:
               print 'Deaths Has decreased, Deaths count is %s NodeJS cluster OK |%s=%s %s=%s %s=%s %s=%s %s=%s' % \
               ( deaths[1], restarts[0], restarts[1], workers[0], workers[1], deaths[0], deaths[1],
               connections_total[0], connections_total[1], connections_active[0], connections_active[1])
               STATUS = 0
        else:
               print 'NodeJS cluster OK, deaths tmp file initialized |%s=%s %s=%s %s=%s %s=%s %s=%s' % \
               ( restarts[0], restarts[1], workers[0], workers[1], deaths[0], deaths[1],
               connections_total[0], connections_total[1], connections_active[0], connections_active[1])
               STATUS = 0
        deathswritetmp = open(DEATHSLOG, 'w', 0)
        deathswritetmp.write(deaths[1])
        deathswritetmp.close()
        LOG.write(output)
        LOG.close()
        sys.exit(STATUS)
        
