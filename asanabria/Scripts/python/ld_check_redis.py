#!/usr/bin/env python

import sys
import re
import string
import os
from optparse import OptionParser


try:
    import redis
except Exception as e:
    print e
    sys.exit(2)


usage = '%prog -d "device id or device ip" -l password '
parser = OptionParser(usage)
parser.add_option("-d", "--device", dest="device", 
    help="The redis server you want to connect to")
parser.add_option("-p", "--passwd", dest="passwd", 
    help="The password used to connect to the redis server")
parser.add_option("-n", "--port", dest="port", default=6379,
    help="The port the redis server is using")
parser.add_option("-t", "--timeout", dest="timeout", default=10,
    help="socket timeout to redis server")
(options, args) = parser.parse_args()

if __name__ == '__main__':
    db = ''
    info_cmd = ''
    perfout = '|'
    if options.device and options.passwd:
        try:
            db = redis.Redis(host="%s" % (options.device), password="%s" % (options.passwd), \
                port=int(options.port), socket_timeout=int(options.timeout))
        except Exception as e:
            print 'CRITICAL %s' % (e)
            sys.exit(2)
        try:
            info_cmd = db.info()
        except Exception as e:
            print 'CRITICAL %s' % (e)
            sys.exit(2)
        count = 0
        for key in info_cmd.keys():
            ktype = type(info_cmd[key])
            if ktype is int:
                perfout = perfout + ' %s=%d'% (key, info_cmd[key])
            elif ktype is float:
                perfout = perfout + ' %s=%f' % (key, info_cmd[key])
            elif ktype is dict:
                for k, v in info_cmd[key].items():
                    if type(v) is int:
                        perfout = perfout + ' %s_%s=%d'% (key, k, v)
                    elif type(v) is float:
                        perfout = perfout + ' %s_%s=%f' % (key, k, v)

        if info_cmd['role'] == 'master':
            print 'OK Master Redis Server %s is Running %s %s' % \
                ( options.device, info_cmd['redis_version'], perfout )
            sys.exit(0)
        elif info_cmd['role'] == 'slave':
            if info_cmd['master_link_status'] == 'up' and info_cmd['master_sync_in_progress'] == 0:
                print 'OK Master %s is up and Slave %s is in sync %s' % \
                    ( info_cmd['master_host'], options.device, perfout )
                sys.exit(0)
            elif info_cmd['master_link_status'] == 'up' and info_cmd['master_sync_in_progress'] == 1:
                print 'WARNING Master %s is up and Slave %s is out of sync %s' % \
                    ( info_cmd['master_host'], options.device, perfout )
                sys.exit(1)
            elif info_cmd['master_link_status'] == 'down':
                print 'CRITICAL Master %s is down and Slave %s is out of sync %s' %  \
                    ( info_cmd['master_host'], options.device, perfout )
                sys.exit(2)


    else:
        print 'You did not either pass the redis server or redis password'

