#!/usr/bin/env python

import os
import sys
import re

from optparse import OptionParser

#libs
import Globals
import Acquisition

from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from transaction import commit

__author__ = "Allen Sanabria"
__copyright__ = "Copyright 2010, LinuxDynasty"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"

def getAggregate(devices, dpoints):
    count = 0
    for device in devices:
        if device.getRRDValue(dpoints):
            dpoint  = device.getRRDValue(dpoints)
            count = count + dpoint
    return count

if __name__ == '__main__':
    usage = '%prog -d "nginx-1" -d "nginx-2" -p "nginx_codes_count200"\n\
    %prog -o "/Server/Linux/Nginx/" -p "nginx_codes_count200"'
    parser = OptionParser(usage)
    parser.add_option("-d", "--device", action="append", 
                     help="The device you want to grab the datapoints from.")
    parser.add_option("-o", "--organizer", dest="organizer",
                     help="The Class you want to get your list of devices from.")
    parser.add_option("-p", "--dpoints", dest="dpoints", 
                     help='Name of DataPoint nginx_codes_count200')
    (options, args) = parser.parse_args()

    
    dmd = ZenScriptBase(connect=True,noopts=True).dmd

    if options.organizer and options.dpoints:
        try:
            oclass = dmd.Devices.getOrganizer(options.organizer)
        except:
            print 'CRITICAL %s does not exist' % ( options.organizer )
            sys.exit(1)
        devices = oclass.getSubDevices()
        count = getAggregate(devices, options.dpoints)
        print "OK Aggregate for %s class is %d|aggregate=%d" % (options.organizer, count, count)
        sys.exit(0)

    elif options.device and options.dpoints:
        if len(options.device) > 1:
           devices = []
           deviceId = ''
           for i in options.device:
                device = dmd.Devices.findDeviceByIdOrIp(i)
                if not device:
                    print 'CRITICAL %s does not exist' % ( i )
                    sys.exit(1)
                else:
                    devices.append(device)
                    deviceId += ' %s' % (device.id)
           count = getAggregate(devices, options.dpoints)
           print "OK Aggregate for devices %s is %d|aggregate=%d" % (deviceId, count, count)
           sys.exit(0)
    else:
        sys.exit(0)

