---
layout: post
status: publish
published: true
title: HowTo find the port on a switch that a host belongs to, the easy way, part
  1
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 80
wordpress_url: http://linuxdynasty.org/?p=80
date: !binary |-
  MjAwOS0wNC0wNyAxNTo1MjoyNiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNC0wNyAxNTo1MjoyNiAtMDQwMA==
categories:
- Python
- Port Report Projects
tags:
- Python HowTo's
- HowTo find the port on a switch that a host belongs to
- the easy way
- part 1
comments: []
---
<p>&nbsp;</p>
<p>The Port Report Project is essentially a Switch Port Mapper Tool or a Switch Port Mapping Tool like a few other commercial products out there, except The Port Report Project is free. Right now there is no GUI or WEB interface for the project but it is in the works.</p>
<p>The other day I was speaking to a buddy of mine. I asked him how cool would it be, if you could just get the port on a switch that you are plugged into, in one line?? So since I thought about it... I figured why not.... I just finished writing the first revision ( I'm assuming more to come). I must say that I am quite pleased with it. Right now you can pass the switch you want to talk too, the community string, and either the MAC or IP address of the host device. In return you will get the MAC Address, IP Address, Port Description (VLAN), and Port you are plugged into.</p>
<p>This script requires, Pysnmp and Pyasn1. If you have python-setuptools, you can install it by running this..<br />
easy_install pysnmp, easy_install pyasn1</p>
<p>&nbsp;</p>
<p>Three things you will need for this script to work..</p>
<ol>
<li>Pysnmp</li>
<li>Pyasn1</li>
<li>SNMP Access to the switch you want to talk too and its community string.</li>
</ol>
<div>To make your life easier you should do the following</div>
<ol>
<li>install <a title="title" href="http://pypi.python.org/pypi/setuptools">python-setuptools<br />
</a></li>
<li>then run easy_install pysnmp</li>
<li>and easy_install pyasn1</li>
<li>or you can download the 2 modules manually.<br />
<a title="title" href="http://voxel.dl.sourceforge.net/sourceforge/pysnmp/pysnmp-4.1.10a.tar.gz">pysnmp</a> and <a title="title" href="http://voxel.dl.sourceforge.net/sourceforge/pyasn1/pyasn1-0.0.8a.tar.gz">pyasn1</a></li>
<li>then unzip the 2 files and in each directory run <strong>python setup.py install</strong></li>
</ol>
<p>I am using the following revisions from the python cheese shop pysnmp 4.1.7a  and pyasn1 0.0.6a</p>
<p>&nbsp;</p>
<p>Revision 2, will even add more features like...</p>
<ul>
<li>Trying to find out what is plugged into a certain Port.</li>
<li>Passing a list of switches</li>
<li>follow chained switches</li>
<li>Gettinginfo from non vlan ports.</li>
<li>If you have more ideas, please let me know..</li>
</ul>
<p><strong><span class="attention">Update 1.7....This is a big update for Port Report.... In this revision the following brands and devices are supported</span></strong></p>
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
<p>The Script has been tested with the above devices... If you have run this script against other devices, please let us know. Also the speed in the report function has drastically increased. I ran this script against a 6509 with 800+ devices connected to it in just over 2 minutes.</p>
<div>You can download the script here {quickdown:44}</div>
<p>Update..  revision 1.6 has been released.</p>
<ul>
<li>Support for HP PROCURVE switches</li>
<li>Added Verbose option</li>
<li>Combined switch_report.py in port_report.py</li>
</ul>
<p>Update, version 1.4...<br />
Only changes that have been made are below..</p>
<ul>
<li>Code Clean up</li>
<li>added check by port name</li>
<li>Added Error Checking</li>
<li>fixed a few bugs with matching the ifIndex port to the bridgeport</li>
</ul>
<p>So from the looks of it this script does work on Cisco Switches,which has been tested. But does not work on HP Procurve switches. I would like to add this feature to this script but I do not have HP switches to test on.  If anyone would like me to add this feature to HP switches oranyother manufacturer please let me know and maybe we can work together to get it working.</p>
<pre>     example below...    python get_port.py -d "switch" -c "community" -m "mac address"

    MAC Address = 00 14 28 1f 2d 38    IP Address = 192.168.101.100    PortDescr = Vlan175    Port = GigabitEthernet1/17

    python get_port.py -d "switch" -c "community" -i "ip address"

    MAC Address = 00 14 28 1f 2d 38    IP Address = 192.168.101.100    PortDescr = Vlan175    Port = GigabitEthernet1/17</pre>
<p>Please post any questions related to this script here.. <a href="forums/Scripting/scripting/port_report">http://www.linuxdynasty.org/forums/Scripting/scripting/port_report</a><br />
You can download the script here... <a title="title" href="Port-Report-Project/">get_port.py </a></p>
<pre>python port_report.py -d 192.168.101.1 -c public --report GigabitEthernet1/11,00 21 5a 80 0b a6,192.168.101.23,vlan51,up,up,fullDuplex,1gbps,GigabitEthernet1/12,00 12 79 83 3b f3,192.168.101.24,vlan51,up,up,fullDuplex,1gbps,

python port_report.py -d 192.168.101.1 -c public -i "192.168.101.201"This IPAddress is not in the ARP table

python port_report.py -d 192.168.101.1 -c public -i "192.168.101.202"--verboseFri Apr 24 15:15:41 2009  Main StartedFri Apr 24 15:15:41 2009  In snmpget function Fri Apr 24 15:15:42 2009  Out of snmpget function Cisco Internetwork Operating System Software IOS (tm) s72033_rp Software (s72033_rp-JK9S-M), Version 12.2(17d)SXB7, RELEASE SOFTWARE (fc2)Technical Support: http://www.cisco.com/techsupportCopyright (c) 1986-2005 by cisco Systems, Inc.Compiled ThuFri Apr 24 15:15:42 2009  Finished Checking for macFri Apr 24 15:15:42 2009  Found IPFri Apr 24 15:15:42 2009  192.168.101.202 is a Cisco Switch Fri Apr 24 15:15:42 2009  In generic_mac_or_ip Function00 14 38 4f 5e 38 Fri Apr 24 15:15:42 2009  Looping Through CommTableFri Apr 24 15:15:42 2009  In CommTable For LoopFri Apr 24 15:15:42 2009  First If Statement Fri Apr 24 15:15:42 2009  Looping Through CommTableFri Apr 24 15:15:42 2009  In CommTable For LoopFri Apr 24 15:15:42 2009  Looping Through CommTableFri Apr 24 15:15:42 2009  In CommTable For Loop

python port_report.py -d 192.168.101.1 -c public -i "192.168.101.209"MAC  = 00 14 38 7f 6e 38Port = GigabitEthernet1/17Vlan = 175IPAddr = 192.168.101.209

python port_report.py -d 192.168.101.1 -c public -m "00 14 38 4f 5e 39"MAC  = 00 14 38 4f 5e 39Port = GigabitEthernet1/17Vlan = 175IPAddr = 192.168.101.201

python port_report.py -d 192.168.101.1 -c public -n "1/40"Port 1/40 has the below MAC Addresses associated with itMAC  = 00 1b 95 97 3c 81Port = GigabitEthernet1/40Vlan = 1IPAddr = The IP Address for this MAC is not in the ARP Table

MAC  = 00 15 fa b4 10 06Port = GigabitEthernet1/40Vlan = 174IPAddr = The IP Address for this MAC is not in the ARP Table

Total MAC Addresses associated with this interface 2

python port_report.py -d 192.168.101.1 -c public -n "1/2"Port 1/2 has the below MAC Addresses associated with itMAC  = 08 00 0f 20 b3 aaPort = GigabitEthernet1/2Vlan = 176IPAddr = 192.168.101.104

MAC  = 08 00 0f 21 d3 78Port = GigabitEthernet1/2Vlan = 173IPAddr = 192.168.101.105

MAC  = 08 00 0f 20 b3 aaPort = GigabitEthernet1/2Vlan = 175IPAddr = 192.168.101.115</pre>
