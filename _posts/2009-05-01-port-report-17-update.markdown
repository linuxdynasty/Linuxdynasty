---
layout: post
status: publish
published: true
title: Port Report 1.7 Update
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>This is a big update for Port Report.... In this revision the following
  brands and devices are supported</p>\r\n<ol>\r\n<li>Cisco<br /> \r\n<ul>\r\n<li>Catalyst
  6509 w/ Supervisor 720 running IOS</li>\r\n<li>Catalyst 3560</li>\r\n<li>Catalyst
  3550 (SMI)</li>\r\n<li>Cisco CIGESM series Chassis Blades</li>\r\n<li>Cisco Catalyst
  2960</li>\r\n</ul>\r\n</li>\r\n<li>Foundry<br /> \r\n<ul>\r\n<li>Foundry Server
  Iron</li>\r\n</ul>\r\n</li>\r\n<li>Nortel<br /> \r\n<ul>\r\n<li>Nortel Passport
  8600</li>\r\n<li>Nortel 5520 Ethernet Routing Switch</li>\r\n</ul>\r\n</li>\r\n<li>HP<br
  /> \r\n<ul>\r\n<li>HP Procurve 5406xl</li>\r\n</ul>\r\n</li>\r\n</ol>\r\n<p>The
  Script has been tested with the above devices... If you have run this script against
  other devices, please let us know. Also the speed in the report function has drastically
  increased. I ran this script against a 6509 with 800+ devices connected to it in
  just over 2 minutes.</p>\r\n<p>The main article for this script is located here
  <a href=\"howto-find-the-port-on-a-switch-that-a-host-belongs-to-the-easy-way-part-1.html\"
  title=\"title\">http://www.linuxdynasty.org/howto-find-the-port-on-a-switch-that-a-host-belongs-to-the-easy-way-part-1.html
  </a></p>\r\n<p>You can download the script here <a href=\"View-details/Python-Scripts/39-port_report.py.html\">http://www.linuxdynasty.org/View-details/Python-Scripts/39-port_report.py.html</a><br
  />{quickdown:39}</p>\r\n<br />"
wordpress_id: 125
wordpress_url: http://linuxdynasty.org/?p=125
date: !binary |-
  MjAwOS0wNS0wMSAwMTo1Njo0MyAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNS0wMSAwMTo1Njo0MyAtMDQwMA==
categories: []
tags:
- Dynastys Blog
- Port Report 1.7 Update
comments: []
---
<p>This is a big update for Port Report.... In this revision the following brands and devices are supported</p>
<ol>
<li>Cisco<br /> 
<ul>
<li>Catalyst 6509 w/ Supervisor 720 running IOS</li>
<li>Catalyst 3560</li>
<li>Catalyst 3550 (SMI)</li>
<li>Cisco CIGESM series Chassis Blades</li>
<li>Cisco Catalyst 2960</li>
</ul>
</li>
<li>Foundry<br /> 
<ul>
<li>Foundry Server Iron</li>
</ul>
</li>
<li>Nortel<br /> 
<ul>
<li>Nortel Passport 8600</li>
<li>Nortel 5520 Ethernet Routing Switch</li>
</ul>
</li>
<li>HP<br /> 
<ul>
<li>HP Procurve 5406xl</li>
</ul>
</li>
</ol>
<p>The Script has been tested with the above devices... If you have run this script against other devices, please let us know. Also the speed in the report function has drastically increased. I ran this script against a 6509 with 800+ devices connected to it in just over 2 minutes.</p>
<p>The main article for this script is located here <a href="howto-find-the-port-on-a-switch-that-a-host-belongs-to-the-easy-way-part-1.html" title="title">http://www.linuxdynasty.org/howto-find-the-port-on-a-switch-that-a-host-belongs-to-the-easy-way-part-1.html </a></p>
<p>You can download the script here <a href="View-details/Python-Scripts/39-port_report.py.html">http://www.linuxdynasty.org/View-details/Python-Scripts/39-port_report.py.html</a><br />{quickdown:39}</p>
<p><a id="more"></a><a id="more-125"></a></p>
<p>Examples below...</p>
<pre>python port_report.py -d 192.168.101.1 -c public --report <br />GigabitEthernet1/11,00 21 5a 80 0b a6,192.168.101.23,vlan51,up,up,fullDuplex,1gbps,<br />GigabitEthernet1/12,00 12 79 83 3b f3,192.168.101.24,vlan51,up,up,fullDuplex,1gbps,<br /><br />python port_report.py -d 192.168.101.1 -c public -i "192.168.101.201"<br />This IPAddress is not in the ARP table<br /><br />python port_report.py -d 192.168.101.1 -c public -i "192.168.101.202"--verbose<br />Fri Apr 24 15:15:41 2009  Main Started<br />Fri Apr 24 15:15:41 2009  In snmpget function <br />Fri Apr 24 15:15:42 2009  Out of snmpget function <br />Cisco Internetwork Operating System Software <br />IOS (tm) s72033_rp Software (s72033_rp-JK9S-M), Version 12.2(17d)SXB7, RELEASE SOFTWARE (fc2)<br />Technical Support: http://www.cisco.com/techsupport<br />Copyright (c) 1986-2005 by cisco Systems, Inc.<br />Compiled Thu<br />Fri Apr 24 15:15:42 2009  Finished Checking for mac<br />Fri Apr 24 15:15:42 2009  Found IP<br />Fri Apr 24 15:15:42 2009  192.168.101.202 is a Cisco Switch <br />Fri Apr 24 15:15:42 2009  In generic_mac_or_ip Function<br />00 14 38 4f 5e 38 <br />Fri Apr 24 15:15:42 2009  Looping Through CommTable<br />Fri Apr 24 15:15:42 2009  In CommTable For Loop<br />Fri Apr 24 15:15:42 2009  First If Statement <br />Fri Apr 24 15:15:42 2009  Looping Through CommTable<br />Fri Apr 24 15:15:42 2009  In CommTable For Loop<br />Fri Apr 24 15:15:42 2009  Looping Through CommTable<br />Fri Apr 24 15:15:42 2009  In CommTable For Loop<br /><br /><br />python port_report.py -d 192.168.101.1 -c public -i "192.168.101.209"<br />MAC  = 00 14 38 7f 6e 38<br />Port = GigabitEthernet1/17<br />Vlan = 175<br />IPAddr = 192.168.101.209<br /><br />python port_report.py -d 192.168.101.1 -c public -m "00 14 38 4f 5e 39"<br />MAC  = 00 14 38 4f 5e 39<br />Port = GigabitEthernet1/17<br />Vlan = 175<br />IPAddr = 192.168.101.201<br /><br />python port_report.py -d 192.168.101.1 -c public -n "1/40"<br />Port 1/40 has the below MAC Addresses associated with it<br />MAC  = 00 1b 95 97 3c 81<br />Port = GigabitEthernet1/40<br />Vlan = 1<br />IPAddr = The IP Address for this MAC is not in the ARP Table<br /><br />MAC  = 00 15 fa b4 10 06<br />Port = GigabitEthernet1/40<br />Vlan = 174<br />IPAddr = The IP Address for this MAC is not in the ARP Table<br /><br />Total MAC Addresses associated with this interface 2<br /><br />python port_report.py -d 192.168.101.1 -c public -n "1/2"<br />Port 1/2 has the below MAC Addresses associated with it<br />MAC  = 08 00 0f 20 b3 aa<br />Port = GigabitEthernet1/2<br />Vlan = 176<br />IPAddr = 192.168.101.104<br /><br />MAC  = 08 00 0f 21 d3 78<br />Port = GigabitEthernet1/2<br />Vlan = 173<br />IPAddr = 192.168.101.105<br /><br />MAC  = 08 00 0f 20 b3 aa<br />Port = GigabitEthernet1/2<br />Vlan = 175<br />IPAddr = 192.168.101.115<p><br /><br /> </p></pre>
<p> </p>
