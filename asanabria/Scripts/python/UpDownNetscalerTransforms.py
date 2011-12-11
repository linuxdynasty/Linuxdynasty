# 1.1.1 - 2010/01/18 (Allen)
# Transforms for enable/disable of serviceGroups in the Netscaler

import re

# True in the transform; False to test in a script.
tlc_prod = True
#tlc_prod = False
tlc_summary = None
tlc_desc = None
tlc_service = None
tlc_vserver = None
tlc_group = None
tlc_component = None
tlc_severity = None
tlc_message = None
# Production:
if tlc_prod:
    # Get the summary attribute from the event object:
    # Use this Format, if you have the Netscaler MIB loaded into Zenoss
    tlc_desc  = getattr(evt, "entityName",None)
    tlc_service = getattr(evt, "svcServiceName", None)
    tlc_vserver = getattr(evt, "vsvrName", None)
    tlc_group = getattr(evt, "svcGrpMemberName", None)
    # Use this Format, if you DO NOT have the SNMPv2-SMI MIB loaded into Zenoss
    #tlc_desc = getattr(evt, "1.3.6.1.4.1.5951.4.1.10.2.5.0", None)

    # Use this Format, if you have the SNMPv2-SMI MIB loaded into Zenoss
    #tlc_desc = getattr(evt, "enterprises.5951.4.1.10.2.5.0", None)

# Testing:
else:
    pass
    #tlc_group = "\"Foo Barr\""
    #tlc_desc = "disable serviceGroup testforzenoss 0 0 -delay 0"
    #tlc_desc = "server_serviceGroup_NSSVC_HTTP_172.16.50.31:8080(Foo Bar_172.16.50.31_8080)_UP"
    #tlc_desc = "disable serviceGroup "Foo Bar" billy 4545 0 -delay 0"
    #tlc_desc = "enable serviceGroup testforzenoss"
    #tlc_desc = "enable serviceGroup testforzenoss billy 1234"
    #tlc_desc = "disable serviceGroup testforzenoss billy 1234 0 -delay 0"

if tlc_desc:
    # Set state ("enable"/"disable"), summary, and component.
    tlc_state = re.search(r"_(\w+$)",tlc_desc).group(1)
    if tlc_service:
        tlc_summary = "Service %s is %s" % (tlc_service, tlc_state)
        tlc_component = "NS_Service"
    elif tlc_vserver:
        tlc_summary = "Site %s is %s" % (tlc_vserver, tlc_state)
        tlc_component = "NS_VirtualServer"
    elif tlc_group:
        tlc_summary = "Service Group %s is %s"  % (tlc_group, tlc_state)
        tlc_component = "NS_Group"
    else:
        tlc_summary = "Service Group %s is %s"  % (tlc_group, tlc_state)

    if tlc_state == "UP":
        tlc_severity = 0
    elif tlc_state == "DOWN":
        tlc_severity = 5

    tlc_message = "%s\nOriginal Message:\n%s" % (tlc_summary, tlc_desc)

	# Production:
    if tlc_prod:
        # Modify the event.
        evt.summary     = tlc_summary
        evt.message    	= tlc_summary
        evt.component   = tlc_component
        evt.severity    = tlc_severity
    # Testing:
    else:
        print "Summary = %s" % tlc_summary
        print "Message = %s" % tlc_message
        print "Component = %s" % tlc_component
        print "Severity = %d" % tlc_severity

