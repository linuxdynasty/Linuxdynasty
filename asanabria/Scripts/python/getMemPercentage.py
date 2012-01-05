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

def getPercentages(device):
    availSwap = device.getRRDValue('memAvailSwap_memAvailSwap')
    totalSwap = device.os.totalSwap
    if availSwap and totalSwap:
        swapPercentageAvail = availSwap * 1024 / totalSwap * 100
        swapPercentageUsed = 100 - swapPercentageAvail
    else:
        print "Either totalSwap or availSwap is not not in Zenoss for this device %s" % ( device.id )
        sys.exit(2)
    availMem = device.getRRDValue('memAvailReal_memAvailReal')
    totalMem = device.hw.totalMemory
    if availMem and totalMem:
        memPercentageUsed = device.getRRDValue('memAvailReal_memAvailReal') * 1024 / device.hw.totalMemory * 100
        memPercentageAvail = 100 - memPercentageUsed
    else:
        print "Either totalMem or availMem is not not in Zenoss for this device %s" % ( device.id )
        sys.exit(2)
    return(swapPercentageAvail, swapPercentageUsed, memPercentageAvail, memPercentageUsed)

if __name__ == '__main__':
    usage = '%prog -d "nginx-fs-1" -d "nginx-fs-2""'
    parser = OptionParser(usage)
    parser.add_option("-d", "--device", dest="device", 
                     help="The device, you want your template attached to.")
    (options, args) = parser.parse_args()

    
    dmd = ZenScriptBase(connect=True,noopts=True).dmd

    if options.device:
        device = dmd.Devices.findDeviceByIdOrIp(options.device)
        if device:
            swapAvail, swapUsed, memAvail, memUsed  = getPercentages(device)
            print "OK |swapPercentageAvail=%d swapPercentageUsed=%d memPercentageAvail=%d memPercentageUsed=%d" \
                % (swapAvail, swapUsed, memUsed, memAvail)
            sys.exit(0)
        else:
            print 'Critical %s does not exist' % (options.device)
            sys.exit(2)
    else:
        sys.exit(0)
