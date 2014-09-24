# 2010/01/18 LinuxDynasty
# Transforms for enable/disable of serviceGroups in the Netscaler

import re

# True in the transform; False to test in a script.
zprod = True
#zprod = False

zdesc = None
zgroup = None

# Production:
if zprod:
    # Get the summary attribute from the event object:
    # Use this Format, if you have the Netscaler MIB loaded into Zenoss
    zdesc = getattr(evt, "configurationCmd", None)
    
    # Use this Format, if you DO NOT have the SNMPv2-SMI MIB loaded into Zenoss
    #zdesc = getattr(evt, "1.3.6.1.4.1.5951.4.1.10.2.5.0", None)

    # Use this Format, if you have the SNMPv2-SMI MIB loaded into Zenoss
    #zdesc = getattr(evt, "enterprises.5951.4.1.10.2.5.0", None)

# Testing:
else:
    pass
    #uncomment any of the following to test
    #zdesc = "disable serviceGroup testforzenoss 0 0 -delay 0"
    #zdesc = "enable serviceGroup testforzenoss"
    #zdesc = "enable serviceGroup testforzenoss billy 1234"
    #zdesc = "disable serviceGroup testforzenoss billy 1234 0 -delay 0"

if zdesc:
    
    zstate = None
    zsummary = None
    zcomponent = None
    zseverity = None
    zmessage = None
    node_message = re.search(r"(?P<state>^disable|enable)\s+(?P<prop>\w+)\s+(?P<sgroup>\w+|\"\w+.*\")\s+(?P<node>[a-zA-Z]\w+)(\s+[0-9]+\s+[0-9]+\s+-delay\s+[0-9]+)?", zdesc)
    sg_message = re.search(r"(?P<state>^disable|enable)\s+(?P<prop>\w+)\s+(?P<sgroup>\w+|\"\w+.*\")(\s+[0-9]+\s+[0-9]+\s+-delay\s+[0-9]+)?", zdesc)
    if node_message:
        zstate          = node_message.group('state')
        zsummary	= "%s node %s on %s %s" % ( node_message.group('state'), node_message.group('node'), node_message.group('prop'), node_message.group('sgroup') )
        zcomponent	= node_message.group('sgroup')
    elif sg_message:
        zstate          = sg_message.group('state')
        zsummary	= "%s %s %s" % ( sg_message.group('state'), sg_message.group('prop'), sg_message.group('sgroup') )
        zcomponent	= sg_message.group('sgroup')
    else:
        zsummary = zdesc


    if zstate == "enable":
        zseverity = 0
    elif zstate == "disable":
        zseverity = 4


    zmessage = "%s\nOriginal Message:\n%s" % (zsummary, zdesc)

	# Production:
    if zprod:
        evt.summary     = zsummary
        evt.message    	= zmessage
        evt.component   = zcomponent
        evt.severity    = zseverity
    # Testing:
    else:
        print "Summary = %s" % zsummary
        print "Message = %s" % zmessage
        print "Component = %s" % zcomponent
        print "Severity = %d" % zseverity

