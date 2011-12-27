#!/usr/bin/env python

import os
import re
import sys
import string
from subprocess import os
from subprocess import Popen
from subprocess import PIPE
from time import ctime
from optparse import OptionParser


session = 'echo "stats()" | nc -w1 '
LOGFILE = '/tmp/stats.log'
DEATHSLOG = '/tmp/deaths.tmp'
STATUS = ''
stats = re.compile(r'(restarts):.*0m ([0-9]+).*\n.*(workers):.*0m ([0-9]+).*\n.*(deaths):.*0m ([0-9]+)'\
                  '.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*(connections total):.*0m ([0-9]+).*\n.'\
                  '*(connections active):.*0m (-?[0-9])+')

def get_status( command ):
    session = Popen([command], stdout=PIPE, stderr=PIPE, shell=True)
    session.wait()
    if session.returncode == 0:
        return(session.stdout.read(), session.returncode)
    else:
        return(None, session.returncode)

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
        try:
            LOG = open(LOGFILE, 'a', 0)
        except Exception, e:
            print e
            sys.exit(2)
        if options.contype == 'tcp':
            host, port = options.connection.split(":")
            session = session + ' '+ host + ' ' + port
            session, code = get_status(session)
            if code == 0:
                output = session
            else:
                print "Can not Connect to the stats() plugin"
                sys.exit(2)
        elif options.contype == 'socket':
            bsd_ncat_session = session + '-U '+ options.connection
            ncat_session = session + ' '+ options.connection
            session, code = get_status(bsd_ncat_session)
            if code == 0:
                output = session
            else:
                session, code = get_status(ncat_session)
                if code == 0:
                    output = session
                else:
                    print "Can not Connect to the stats() plugin"
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
        
