---
layout: post
status: publish
published: true
title: LD Port Report Project aka Switch Port Mapper Tool
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 209
wordpress_url: http://linuxdynasty.org/?p=209
date: !binary |-
  MjAwOS0wNS0wNSAwODoxMDo0MSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNS0wNSAwODoxMDo0MSAtMDQwMA==
categories:
- Port Report Projects
tags:
- Switch Port Report
- LD Switch Port Mapper Project Page
comments: []
---
<p>The Port Report Project is essentially a Switch Port Mapper Tool or a Switch Port Mapping Tool like a few other commercial products out there, except The Port Report Project is free. Right now there is no GUI or WEB interface for the project but it is in the works.</p>
<p>This project started off as being a simple 150 line script that did something quite simple... Its only purpose was to find MAC Addresses on a switch. Then I was asked could you also search by IP, so I added that. Now I was asked to search by Port, so I added that. Well you get where this is all going.... My goal now is to build the equivalent of other commercial port mapping tools, but Open Source....</p>
<p>On this page I will be keeping all the updates to this Project, so please keep checking back every now and again for updates.<br />
You can get any revision of the Port Report tool here <a title="title" href="Port-Report-Project/">http://www.linuxdynasty.org/Port-Report-Project/ </a><br />
{quickdown:39}</p>
<p>Any issues with the LD Port Report Project, please discuss here in the<a href="http://linuxdynasty.org/index.php?option=com_agora&amp;id=7&amp;Itemid=7"> forums</a><br />
This script requires, Pysnmp and Pyasn1. If you have python-setuptools, you can install it by running this..<br />
easy_install pysnmp, easy_install pyasn1</p>
<p>Three things you will need for this script to work..</p>
<ol>
<li>Pysnmp</li>
<li>Pyasn1</li>
<li>SNMP Access to the switch you want to talk too and its community string.</li>
</ol>
<div>To make your life easier you should do the following</div>
<ol>
<li>install <a title="title" href="http://pypi.python.org/pypi/setuptools">python-setuptools</a></li>
<li>then run easy_install pysnmp</li>
<li>and easy_install pyasn1</li>
<li>or you can download the 2 modules manually.<br />
<a title="title" href="http://sourceforge.net/projects/pysnmp/">pysnmp</a> and <a title="title" href="http://sourceforge.net/projects/pyasn1/">pyasn1</a></li>
<li>then unzip the 2 files and in each directory run <strong>python setup.py install</strong></li>
</ol>
<p>I am using the following revisions from the python cheese shop pysnmp 4.1.12a and pyasn1 0.0.9a</p>
<div>For revision 1.12 and above..... If you installed <strong>pyasn1</strong> and <strong>pysnmp</strong> using <strong>easy_install</strong>. Please uninstall it now and install the newest revision and run <strong>python setup.py install</strong> Instead of using <strong>easy_install</strong>.<br />
Revision history and Examples below.....</div>
<dl>
<dd>Revision 1.13 10/01/09</p>
<ul>
<li>Fixed line 348 as per christianha. return nmac.lower()<br />
This fix will allow you to pass a MAC in all uppercase and still match though the switch is responding in lowercase.<br />
00 E0 B8 81 E8 B7 will now match 00 e0 b8 81 e8 b7</li>
</ul>
<p>Revision 1.12 09/18/09</p>
<ul>
<li>The report option of the script can now follow cdp neighbors using the <strong>--follow</strong> option or <strong>-f</strong>.<br />
When you run the command below it will create ONE CSV file per cdp neighbor it scanned.<br />
I was able to scan from my core Switch down to the last neighbor in the line ( 44 Neighbors in just under 20 minutes. )<br />
Which equaled to a little over 4K Mac Addresses<br />
For instance...port_report.py -d 192.168.101.1 -c public -r -f</li>
</ul>
<p>Revision 1.11 09/13/09</p>
<ul>
<li>More code clean up and another increase in speed.</li>
<li>Also port_report can now follow EtherChannel</li>
</ul>
<ul>
<li>Added better verbosity</li>
<li>Added Sanity Checking for cdp neighbors</li>
</ul>
<p>&nbsp;</p>
<p>Revision 1.10 09/09/09</p>
<ul>
<li>Code Clean up and a slight increase in speed ( by a few seconds ) during the search by mac or ip</li>
</ul>
<p>Revision 1.9<br />
Code changes and Added CDP Support</p>
<ul>
<li>Detect CDP Neighbors during the scan for MAC Addresses or IP Addresses</li>
</ul>
<p>Revision 1.8<br />
Here is a quick update.....</p>
<ul>
<li>I just add dns reverse lookups to the output of this script.</li>
</ul>
<p>Revision 1.7<br />
Adds support to the following devices..</p>
<ol>
<li>Cisco
<ul>
<li>Catalyst 6509 w/ Supervisor 720 running IOS</li>
<li>Catalyst 3560</li>
<li>Catalyst 3550 (SMI)</li>
<li>Cisco CIGESM series Chassis Blades</li>
<li>Cisco Catalyst 2960</li>
</ul>
</li>
<li>Foundry
<ul>
<li>Foundry Server Iron</li>
</ul>
</li>
<li>Nortel
<ul>
<li>Nortel Passport 8600</li>
<li>Nortel 5520 Ethernet Routing Switch</li>
</ul>
</li>
<li>HP
<ul>
<li>HP Procurve 5406xl</li>
</ul>
</li>
</ol>
<p>&nbsp;</p>
<p>Revision 1.6<br />
New additions to this revision ....</p>
<ul>
<li>Support for HP Procurve Switches, ( Tested on the newer versions of HP )</li>
<li>combined switch_report.py in port_report.py.</li>
<li>Added --verbose flag</li>
</ul>
<p>Previous Releases....</p>
<ul>
<li>Search by MAC or IP or PORT</li>
</ul>
</dd>
</dl>
<p>&nbsp;</p>
<p><img title="More..." src="http://linuxdynasty.org/wp-includes/js/tinymce/plugins/wordpress/img/trans.gif" alt="" /></p>
<p>EXAMPLES BELOW...</p>
<p><strong>Below is an example of the integrated CDP following of switches using the -m ( --mac ) option</strong><code></code></p>
<p>&nbsp;</p>
<pre>python port_report.py -d switch -c community -m "00 13 20 16 5f f7" 
Switch Connected to 192.168.101.1 
SwitchPort = GigabitEthernet10/3 
SwitchPortSpeed = 1000mb 
SwitchPortDuplex = fullDuplex 
SwitchVlan = vlan176 
SnmpHostName = requestTimedOut 
SnmpHostDescr = requestTimedOut 
HostMAC = 00 13 20 16 5f f7 
HostIP = 192.168.101.101 
HostName = Pointer Record Not set for 192.168.101.101 

Found 00 13 20 16 5f f7 on 192.168.101.5
Switch Connected to 192.168.101.5 
SwitchPort = GigabitEthernet0/24 
SwitchPortSpeed = 1000mb 
SwitchPortDuplex = fullDuplex 
SwitchVlan = vlan176 
SnmpHostName = No SNMP Access 
SnmpHostDescr = No SNMP Access 
HostMAC = 00 13 20 16 5f f7 
HostIP = None 
HostName = None 

Found 00 13 20 16 5f f7 on 192.168.101.6 
Switch Connected to 192.168.101.6 
SwitchPort = GigabitEthernet0/22 
SwitchPortSpeed = 1000mb 
SwitchPortDuplex = fullDuplex 
SwitchVlan = vlan176 
SnmpHostName = No SNMP Access 
SnmpHostDescr = No SNMP Access 
HostMAC = 00 13 20 16 5f f7 
HostIP = None 
HostName = None 

This MAC 00 13 20 16 5f f7 was finally traced to this switch 192.168.101.6</pre>
<p><strong>Below I will show you an example of the listing of MAC Addresses per Port using the n (--pname) option </strong></p>
<pre>python port_report.py -d 192.168.101.1 -c community -n "10/3"
SwitchPort = GigabitEthernet10/3
SwitchPortSpeed = 1000mb
SwitchPortDuplex = fullDuplex
SwitchVlan = vlan176
SnmpHostName = requestTimedOut
HostDescr = requestTimedOut
HostMAC  = 00 22 64 bb 3e 17
HostIP = 192.168.101.146
HostName = Pointer Record Not set for 192.168.101.146

SwitchPort = GigabitEthernet10/3
SwitchPortSpeed = 1000mb
SwitchPortDuplex = fullDuplex
SwitchVlan = vlan176
SnmpHostName = requestTimedOut
HostDescr = requestTimedOut
HostMAC  = 00 0c f1 bb bf eb
HostIP = 192.168.101.147
HostName = Pointer Record Not set for 192.168.101.147

SwitchPort = GigabitEthernet10/3
SwitchPortSpeed = 1000mb
SwitchPortDuplex = fullDuplex
SwitchVlan = vlan176
SnmpHostName = requestTimedOut
HostDescr = requestTimedOut
HostMAC  = 00 20 4a 83 20 97
HostIP = 192.168.101.30
HostName = Pointer Record Not set for 192.168.101.30</pre>
<p><strong>Below is an example of running the --report option.. Also the report option will save the output to disk in a CSV file. </strong></p>
<pre>python port_report.py -d 192.168.101.5 -c community --report
GigabitEthernet0/1,00 1c c0 12 6a 8b,None,None,vlan180,up,up,fullDuplex,1000mb,
GigabitEthernet0/1,00 20 4a 12 2b 68,None,None,vlan180,up,up,fullDuplex,1000mb,
GigabitEthernet0/1,00 12 44 94 dc 40,192.168.101.132,Pointer Record Not set for 192.168.101.132,vlan180,up,up,fullDuplex,1000mb,
GigabitEthernet0/1,00 21 5a c7 81 16,None,None,vlan180,up,up,fullDuplex,1000mb,
GigabitEthernet0/3,00 20 4a 12 2b 71,None,None,vlan180,up,up,halfDuplex,10mb,</pre>
<p><strong>Below is an example of searching by IP Addresses -i (--ip)..</strong></p>
<pre>python port_report.py -d 192.168.101.1 -c ommunity -i "192.168.101.200"
Switch Connected to 192.168.101.1
SwitchPort = GigabitEthernet1/17
SwitchPortSpeed = 1000mb
SwitchPortDuplex = unknown
SwitchVlan = vlan175
SnmpHostName = zenmon.linuxdynasty.org
SnmpHostDescr = Linux zenmon.linuxdynasty.org 2.6.18-92.1.22.el5 #1 SMP Tue Dec 16 12:03:43 EST 2008 i686HostMAC  = 00 14 38 4f 5e 38HostIP = 192.168.101.200HostName = zenmon.linuxdynasty.org</pre>
