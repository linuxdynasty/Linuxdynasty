#!/usr/bin/env python
""" 
    The goal of Zenoss_Template_Manager.py is to
    gives you the ability to automate the management
    of Templates and everything pertaining to
    Templates. This Script will allow you to do 
    the following..
      * List Templates in a Device or Device Class
      * List DataSources in a Device or Device Class
      * List DataPoints in a Device or Device Class
      * Create Templates in a Device or Device Class
      * Create DataSource in a Device or Device Class
        * Set Severities
        * Set Parser
      * Create DataPoints in a Device or Device Class
        * Set Data Types
      * Create Thresholds in a Device or Device Class
        * Set Severities
        * Set MinMaxThresholds
      * Create Graphs in a Device or Device Class

    More to come......
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
__version__ = "1.0.6"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"

def findOrganizerTemplate(obj):
    tmpT = obj.getRRDTemplates()
    template = None
    for i in tmpT:
        if i.id == options.template:
            template = i
            break
    return template

def graphCreator(template):
    graph_list = []
    for line in options.graphs:
        graph = None
        datapoint_names = line.split(',')
        for i in xrange(len(datapoint_names)):
            datapoint_names[i] = re.sub(r"^\s+|\s+$", "",datapoint_names[i])
        graph_name = datapoint_names.pop(0)
        current_graphs = template.getGraphDefs()
        if len(current_graphs) >0:
            for line in current_graphs:
                if graph_name == line.id:
                    graph = line
        else:
            graph = template.manage_addGraphDefinition(graph_name)
        if re.search("units=", datapoint_names[len(datapoint_names) -1]):
            graph.units = datapoint_names.pop().split('=')[1]
        graph.manage_deleteGraphPoints(graph.getGraphPointsNames())
        graph.manage_addDataPointGraphPoints(datapoint_names)
        graph_list.append(graph)
        if options.verbose:
            print "%s graph was created with %s DataPoints attached at %s" \
            % (graph.id, datapoint_names, graph.getPrimaryUrlPath())
    commit()
    return graph_list

    
def thresholdCreator(template, gclass='MinMaxThreshold'):
    threshold = None
    if options.gclass:
        gclass = options.gclass
    try:
        threshold = template.manage_addRRDThreshold(options.threshold, gclass)
    except Exception, e:
        print e
    if options.verbose:
        print "%s threshold created at %s" % \
        (threshold.id, threshold.getPrimaryUrlPath())
    commit()
    return threshold


def datapointCreator(dsource):
    for line in options.dpoints:
        line = line.split(',')
        dpoint = dsource.manage_addRRDDataPoint(line[0])
        dpoint.rrdtype = dtype[line[1]]
        if options.verbose:
            print "DataPoint %s of type %s has been added to DataSource %s" % \
            (dpoint.id, dtype[line[1]], dsource.getPrimaryUrlPath())
    commit()
    return dpoint

def datasourceCreator(template):
    dsource = None
    dsources = template.getRRDDataSources()
    for i in dsources:
        if i.id == options.dsource:
            dsource = i
            break
    if dsource:
        if options.verbose:
            print "DataSource %s already exists at %s" % (dsource.id, dsource.getPrimaryUrlPath())
        return dsource
    if not dsource:
        dsource = template.manage_addRRDDataSource(options.dsource, 'BasicDataSource.COMMAND')
        if dsource and options.verbose:
            print "DataSource %s created at %s" % (dsource.id, dsource.getPrimaryUrlPath())
    commit()
    return dsource

def templateCreator(dmd):
    obj = None
    template = None
    if options.device:
        obj = dmd.Devices.findDevice(options.device)
        if not obj:
            print '%s device does not exist" ' % (options.obj)
            sys.exit(1)
    elif options.organizer:
        try:
            obj = dmd.Devices.getOrganizer(options.organizer)
        except Exception, e:
            print '%s Organizer does not exist, Please put Full Path to Organizer' % (e)
            print 'Example... -o "/Devices/Server/Linux"' 
            sys.exit(1)

    if options.device:
        template = obj.getRRDTemplateByName(options.template)
    elif options.organizer:
        template = findOrganizerTemplate(obj)

    if template:
        if options.verbose:
            print "\nTemplate %s already exists at %s" % (template.id, template.getPrimaryUrlPath())
        return template

    if not template:
        if options.device:
            obj.addLocalTemplate(options.template)
            template = obj.getRRDTemplateByName(options.template)
            if options.verbose:
                print "\nTemplate %s created at %s" % (template.id, template.getPrimaryUrlPath())
        elif options.organizer:
            obj.manage_addRRDTemplate(options.template)
            template = findOrganizerTemplate(obj)
            if options.verbose:
                print "\nTemplate %s created at %s" % (template.id, template.getPrimaryUrlPath())

    if options.bind:
        binded_templates = obj.zDeviceTemplates
        binded_templates.append(options.template)
        obj.bindTemplates(binded_templates)
        if options.verbose:
            print "Binded Templates :", binded_templates
    commit()
    return template


if __name__ == '__main__':
    usage = 'Examples: python %prog -d "zenoss.linuxdynasty" -c \'/opt/zenoss/libexec/snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1 --ival="1" --label="ifIndex,ifDescr,ifType,ifMtu,ifSpeed,ifPhysAddress,ifAdminStatus,ifOperStatus,ifLastChange,ifInOctets,ifInUcastPkts,ifInNUcastPkts,InDiscards,ifInErrors,ifInUnknownProtos,ifOutOctets,ifOutUcastPkts,ifOutNUcastPkts,ifOutDiscards,ifOutErrors,ifOutQLen,ifSpecific"\' --template=TESTER4LIFE2 -p "ifSpeed,G" -p "ifInOctets,C" -p "ifInUcastPkts,C" -p "ifInNUcastPkts,C" -p "ifInDiscards,C" -p "ifInErrors,C" -p "ifOutOctets,C" -p "ifOutUcastPkts,C" -p "ifOutNUcastPkts,C" -p "ifOutDiscards,C" -p "ifOutErrors,C" --dsource="WoW2"\n\n\
    python %prog -o "/Devices/Server/Linux" -c \'/opt/zenoss/libexec/snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1 --ival="1" --label="ifIndex,ifDescr,ifType,ifMtu,ifSpeed,ifPhysAddress,ifAdminStatus,ifOperStatus,ifLastChange,ifInOctets,ifInUcastPkts,ifInNUcastPkts,InDiscards,ifInErrors,ifInUnknownProtos,ifOutOctets,ifOutUcastPkts,ifOutNUcastPkts,ifOutDiscards,ifOutErrors,ifOutQLen,ifSpecific"\' --template=TESTER4LIFE2 -p "ifSpeed,G" -p "ifInOctets,C" -p "ifInUcastPkts,C" -p "ifInNUcastPkts,C" -p "ifInDiscards,C" -p "ifInErrors,C" -p "ifOutOctets,C" -p "ifOutUcastPkts,C" -p "ifOutNUcastPkts,C" -p "ifOutDiscards,C" -p "ifOutErrors,C" --dsource="WoW2"\n\n'
    parser = OptionParser(usage)
    parser.add_option("-d", "--device", dest="device", 
                     help="The device, you want your template attached to.")
    parser.add_option("-o", "--organizer", dest="organizer",
                     help="The Organizer you want your template attached to.")
    parser.add_option("-e", "--enabled", dest="enabled", type="int", default=1,
                     help="1 = Enabled and 0 = Disabled, Default is 1")
    parser.add_option("-s", "--dsource", dest="dsource", 
                     help="Name of the DataSource you want to create or use.")
    parser.add_option("-S", "--severity", dest="severity", 
                     help="Critical|Error|Warning|Info|Debug|Clear")
    parser.add_option("-V", "--verbose", action="store_true", dest="verbose", 
                     default=False, help="Print output")
    parser.add_option("-b", "--bind", action="store_true", dest="bind", 
                     default=False, help="Bind The Template you just created.")
    parser.add_option("-p", "--dpoints", action="append", 
                     help='If you are passing this option to create a DataPoint\n\
                     You will need to pass the DataPoint Name and its type.\n\
                     for every -p you will pass either a\n \
                     DataPoint Name and Type C|G|D|A\n \
                     Example.. -p "ifOutDiscards, C", -p "ifInDiscards, C"\n\
                     Or if you are adding DataPoints to a Threshold, you will\n \
                     need to pass the datapoint name and not the id\n\
                     Example.. -p "eth0_ifOutDiscards"')
    parser.add_option("-t", "--template", dest="template", 
                     help="The name of template you want to create or use.")
    parser.add_option("-T", "--threshold", dest="threshold", 
                     help="The name of threshold you want to create or use.")
    parser.add_option("-g", "--gclass", dest="gclass", 
                     help="I'm using this option as a placeholder\n\
                     for generic class names that I might need")
    parser.add_option("-G", "--graphs", action="append", 
                     help='Here you will pass the graph name and the\n\
                     DataPoint name associated with it. You can this option\n\
                     multiple times. Example...\n\
                     -G "eth0 Discards, eth0_ifInDiscards, eth0_ifOutDiscards, units=discards"\n\
                     -G "eth1 Discards, eth1_ifInDiscards, eth1_ifOutDiscards, units=discards"')
    parser.add_option("-c", "--command", dest="command", 
                     help="The Nagios Command you want to add to this template")
    parser.add_option("-m", "--minval", dest="minval", type="int",
                     help="The minimum value that you want to set")
    parser.add_option("-M", "--maxval", dest="maxval", type="int",
                     help="The maximum value that you want to set")
    parser.add_option("-P", "--parser", dest="parser", default="Auto",
                     help='Which Parser you want to use\n \
                     Example.. -P "Nagios" The default is Auto')
    parser.add_option("-l", "--list", dest="list", 
                     help='List either the DataSources, Templates, or DataPoints\n \
                    Example.. --list="templates", or --list="datasources" or\n \
                    --list="datapoints"')
    (options, args) = parser.parse_args()

    dtype = {
            "G" : "GAUGE",
            "C" : "COUNTER",
            "D" : "DERIVE",
            "A" : "ABSOLUTE"
            }
    stype = {
            "Critical" : 5,
            "Error"    : 4,
            "Warning"  : 3,
            "Info"     : 2,
            "Debug"    : 1,
            "Clear"    : 0
            }

    
    dmd = ZenScriptBase(connect=True,noopts=True).dmd
    if options.list:
        obj = None
        if options.device:
            obj = dmd.Devices.findDevice(options.device)
        elif options.organizer:
            obj = dmd.Devices.getOrganizer(options.organizer)
        else:
            print "Pass --help for help"
            sys.exit(1)

        if re.search(r"\bdatasources\b",options.list) and options.template:
            if options.device:
                template = obj.getRRDTemplateByName(options.template)
            elif options.organizer:
                template = findOrganizerTemplate(obj)
            if template:
                for ds in template.getRRDDataSources():
                    print ds.id, ds.getPrimaryUrlPath()

        elif re.search(r"\bdatapoints\b",options.list) and options.template:
            if options.device:
                template = obj.getRRDTemplateByName(options.template)
            elif options.organizer:
                template = findOrganizerTemplate(obj)
            if template:
                for dp in template.getRRDDataPoints():
                    print dp.name(), dp.getPrimaryUrlPath()

        elif options.list == "templates":
            for template in obj.getRRDTemplates():
                print template.id, template.getPrimaryUrlPath()

        else:
            print "Pass --help for help"
            sys.exit(1)

    elif options.device or options.organizer:
        
        if options.template:
            template = templateCreator(dmd)
            if options.dsource:
                dsource = datasourceCreator(template)
                if dsource and not options.threshold:
                    if options.parser:
                        dsource.parser = options.parser
                        if options.verbose:
                            print "Parser = %s" % (options.parser)
                    if options.command:
                        dsource.commandTemplate = options.command
                        if options.verbose:
                            print "Command %s has been added to DataSource %s" \
                            % (options.command, dsource.getPrimaryUrlPath())
                    if options.severity:
                        dsource.severity = stype[options.severity]
                        if options.verbose:
                            print "Severity = %d" % (dsource.severity)
                    if options.enabled == 1:
                        dsource.enabled = True
                        if options.verbose:
                            print "%s DataSource is Enabled" % (dsource.id)
                    else:
                        dsource.enabled = False
                        if options.verbose:
                            print "%s DataSource is Disabled" % (dsource.id)
                    commit()
 
                if options.dpoints and not options.threshold:
                    if len(options.dpoints) >=1:
                        dpoint = datapointCreator(dsource)

            if options.threshold:
                threshold = thresholdCreator(template)
                if type(options.minval) == int:
                    threshold.minval = options.minval
                    if options.verbose:
                        print "minval = %d" % (threshold.minval)
                if type(options.maxval) == int:
                    threshold.maxval = options.maxval
                    if options.verbose:
                        print "maxval = %d" % (threshold.maxval)
                if options.severity:
                    threshold.severity = stype[options.severity]
                    if options.verbose:
                        print "Severity = %d" % (threshold.severity)
                if options.dpoints:
                    threshold.dsnames = []
                    for dpoint in options.dpoints:
                        threshold.dsnames.append(dpoint)
                    if options.verbose:
                        print "%s datapoint added to threshold %s" % \
                              (dpoint, threshold.getPrimaryUrlPath())
                if options.enabled == 1:
                    threshold.enabled = True
                    if options.verbose:
                        print "%s Threshold is Enabled" % (threshold.id)
                else:
                    threshold.enabled = False
                    if options.verbose:
                        print "%s Threshold is Disabled" % (threshold.id)
                commit()
            if options.graphs:    
                if len(options.graphs) >=1:
                    graphs = graphCreator(template)

    else:
        print "Pass the --help for more options"
        sys.exit(1)


