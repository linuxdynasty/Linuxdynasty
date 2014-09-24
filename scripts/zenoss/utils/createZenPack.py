#!/opt/zenoss/bin/python
""" This Script will scan either the default /Device Class and all its subOrganizers/Devices
    Or a specified Device Class like /Server/Linux
"""

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
__version__ = "1.0.1"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"

ignore_templates = re.compile(r"""
       ^\/zport\/dmd\/Devices\/Network\/Router\/Cisco\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Ping\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Power\/UPS\/APC\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Power\/rrdTemplates\/APC%20PDU$|
       ^\/zport\/dmd\/Devices\/Server\/Cmd\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Server\/Cmd\/rrdTemplates\/FileSystem$|
       ^\/zport\/dmd\/Devices\/Server\/Cmd\/rrdTemplates\/ethernetCsmacd$|
       ^\/zport\/dmd\/Devices\/Server\/Linux\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Server\/SSH\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Server\/Scan\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Server\/Solaris\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Server\/Windows\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Server\/Windows\/rrdTemplates\/HardDisk$|
       ^\/zport\/dmd\/Devices\/Server\/rrdTemplates\/Device$|
       ^\/zport\/dmd\/Devices\/Server\/rrdTemplates\/FileSystem$""", re.VERBOSE)

def scanAndAddToZenPack(zpackname, root, dlist, olist, author, version):
    
    def scanLoop(objectlist, zlist=dmd.ZenPackManager.packs()):
        print "Scanning for locally attached Templates"
        for i in objectlist:
            name = i.id
            templates = i.getRRDTemplates()
            for j in templates:
                if re.search(name, j.getRRDPath()):
                    ppath = j.getPrimaryUrlPath()
                    if options.unique:
                        if ignore_templates.search(ppath):
                            if options.verbose:
                                print "Skipping %s" % (ppath)
                            continue
                        else:
                            pack_count = 0
                            for pack in zlist:
                                pack_list = pack.list('')[0][1]
                                for object in pack_list:
                                    dsource = ppath+"/datasources/"
                                    gdef = ppath+"/graphDefs/"
                                    tholds = ppath+"/thresholds/"
                                    if re.search(dsource+"|"+gdef+"|"+tholds, object):
                                        if options.verbose:
                                            print "I'm not UNIQUE %s" % (ppath)
                                            print "I'm in %s" % (pack.id)
                                        pack_count +=1
                                        break
                                    elif pack_list.__contains__(ppath):
                                        if options.verbose:
                                            print "I'm not UNIQUE %s" % (ppath)
                                            print "I'm in %s" % (pack.id)
                                        pack_count +=1
                                        break
                                if pack_count > 0:
                                    break
                            if pack_count == 0:
                                if options.verbose:
                                    print "I'm UNIQUE %s" % (ppath)
                                tplate = j
                                tplate.addToZenPack(pack=zpack.id)
                    else:
                        tplate = j
                        tplate.addToZenPack(pack=zpack.id)

    zpack = None
    try:
        zpack = dmd.ZenPackManager.manage_addZenPack(zpackname)
        print "Created ZenPack %s" % (zpack.id)
    except Exception, e:
        print e
        sys.exit(1)
    zpack.author = author
    zpack.version = version
    zlist = dmd.ZenPackManager.packs()
    scanLoop(dlist, zlist)
    scanLoop(olist, zlist)
    commit()

    return(zpack)

if __name__ == '__main__':
    usage = "usage: %prog arg --packname=ZenPackName --author=name --version=1.0"
    parser = OptionParser(usage)
    parser.add_option("-p", "--packname", dest="zpackname", 
                     help="The name of the ZenPack that you want to create")
    parser.add_option("-a", "--author", dest="author", default="Automator", 
                     help="Who is creating The ZenPack?")
    parser.add_option("-v", "--version", dest="version", default="1.0", 
                     help="What Release is this?")
    parser.add_option("-V", "--verbose", action="store_true", dest="verbose", 
                     default=False, help="Print output")
    parser.add_option("-u", "--unique", action="store_true", dest="unique", 
                     default=False, help="Only add unique Device Templates \
                     that are not part of other zenPacks")
    parser.add_option("-r", "--root", dest="root", help="What Device Class You\
                     want the Search to begin at?")
    parser.add_option("-l", "--list", action="store_true", dest="list", 
                     default=False, help="List all the ZenPacks")
    (options, args) = parser.parse_args()

    
    dmd = ZenScriptBase(connect=True,noopts=True).dmd
    if options.zpackname:
        if options.root:
            try:
                root = dmd.Devices.getOrganizer(options.root)
            except Exception, e:
                print "Device Class %s does not Exist" % (e)
                print "Example of Device Class \"Server/Linux\" or \"Network/Switch\""
                sys.exit(1)
        else:
            root = dmd.Devices

        dlist = root.getSubDevices()
        olist = root.getSubOrganizers()

        zenPack = scanAndAddToZenPack(options.zpackname, options.root, dlist, olist, options.author, options.version)
        print "Objects Attached to Zenpack %s" % (zenPack.id)
        for line in zenPack.list("")[0][1]:
            print line
    elif options.list:
        zlist = dmd.ZenPackManager.packs()
        for zpack in zlist:
            print zpack.id
    else:
        print "Pass the --help for more options"
