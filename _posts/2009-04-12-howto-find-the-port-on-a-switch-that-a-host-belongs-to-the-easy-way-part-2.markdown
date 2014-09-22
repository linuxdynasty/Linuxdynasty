---
layout: post
status: publish
published: true
title: HowTo find the port on a switch that a host belongs to, the easy way, part
  2
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p> </p>\r\n<p>In my previous <a href=\"howto-find-the-port-on-a-switch-that-a-host-belongs-to-the-easy-way-part-1.html\"
  title=\"title\">HowTO</a>, I created the <a href=\"View-details/Python-Scripts/38-get_port.py.html\"
  title=\"title\">get_port.py</a> script. Now this script did the job, but had a few
  faults in it.</p>\r\n<ul>\r\n<li>Major fault was the fact that the script could
  not match multiple MAC<br /> Addresses per port</li>\r\n<li>Also if the port had
  multiple MAC Addresses it usually would fail while doing the search</li>\r\n<li>Better
  error checking. For example if you searched by IP Address before, the error was
  ambiguous.<br /> Now the error will say the IP Address you are looking for is not
  in the ARP Table</li>\r\n</ul>\r\n<p>This script has been heavily tested on Cisco
  Core Switches and on Cisco Catalyst Switches. So far no issues like in the previous
  one. <br /> I will post some of my output below so you can get an idea on how the
  script works.<br /> <br />Also to see the script in action immediately, you should
  run the command like this..</p>\r\n<pre>python port_report.py -d 192.168.101.1 -c
  public -n \"1/40\"</pre>\r\n<p><span class=\"attention\">The reason you should run
  the above first, is that if the ip address you are searching for is not in the ARP
  table you will not get any results. Also I have already seen instance where a someone
  runs the script and uses the search for mac function and it does not return a mac.
  One reason this happens, is because the mac you are searching for is not on the
  switch you are walking or not part of any vlan.So by passing a port, the script 
  will scan every vlan on the switch for MAC Addresses connected to that port.This
  script uses the dot1d tables to get the MAC info as per the CISCO website.</span></p>\r\n<p>Update
  1.1</p>\r\n<ul>\r\n<li>Fixed Port Matching... </li>\r\n<li>Now for the -n option
  you can pass the port number '1/1' or the Port Name as per ifName \"Gi1/1\"<ol>\r\n<li>Pysnmp</li>\r\n<li>Pyasn1</li>\r\n<li>SNMP
  Access to the switch you want to talk too and its community string.</li>\r\n</ol></li>\r\n<br
  />\r\n<p>Three things you will need for this script to work..</p>\r\n</ul>\r\n<div></div>\r\n<ul>\r\n<li>
  <ol>\r\n<li>install <a href=\"http://pypi.python.org/pypi/setuptools\" title=\"title\">python-setuptools<br
  /> </a></li>\r\n<li>then run easy_install pysnmp<a href=\"http://pypi.python.org/pypi/setuptools\"
  title=\"title\"></a></li>\r\n<li>and easy_install pyasn1</li>\r\n</ol></li>\r\nTo
  make your life easier you should do the following<br />\r\n<p>I am using the following
  revisions from the python cheese shop <span>pysnmp 4.1.7a  and pyasn1 0.0.6a</span></p>\r\nYou
  can download the script here<br /> <a href=\"Port-Report-Project/\" title=\"title\">port_report.py</a><br
  />\r\n<p>{quickdown:39}<br />Please post anything related to this script on this
  forum link <a href=\"forums/Scripting/scripting/port_report\">http://www.linuxdynasty.org/forums/Scripting/scripting/port_report</a>
  <br /> Unless it is just a comment, thank you...</p>\r\n<p>Also if you download
  this script on other Platforms besides Cisco, please let me know if it works, so
  I can added under platforms supported.</p>\r\n<br />"
wordpress_id: 81
wordpress_url: http://linuxdynasty.org/?p=81
date: !binary |-
  MjAwOS0wNC0xMiAyMjowNzoyNyAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNC0xMiAyMjowNzoyNyAtMDQwMA==
categories: []
tags:
- Python HowTo's
- HowTo find the port on a switch that a host belongs to
- the easy way
- part 2
comments: []
---
<p> </p>
<p>In my previous <a href="howto-find-the-port-on-a-switch-that-a-host-belongs-to-the-easy-way-part-1.html" title="title">HowTO</a>, I created the <a href="View-details/Python-Scripts/38-get_port.py.html" title="title">get_port.py</a> script. Now this script did the job, but had a few faults in it.</p>
<ul>
<li>Major fault was the fact that the script could not match multiple MAC<br /> Addresses per port</li>
<li>Also if the port had multiple MAC Addresses it usually would fail while doing the search</li>
<li>Better error checking. For example if you searched by IP Address before, the error was ambiguous.<br /> Now the error will say the IP Address you are looking for is not in the ARP Table</li>
</ul>
<p>This script has been heavily tested on Cisco Core Switches and on Cisco Catalyst Switches. So far no issues like in the previous one. <br /> I will post some of my output below so you can get an idea on how the script works.</p>
<p>Also to see the script in action immediately, you should run the command like this..</p>
<pre>python port_report.py -d 192.168.101.1 -c public -n "1/40"</pre>
<p><span class="attention">The reason you should run the above first, is that if the ip address you are searching for is not in the ARP table you will not get any results. Also I have already seen instance where a someone runs the script and uses the search for mac function and it does not return a mac. One reason this happens, is because the mac you are searching for is not on the switch you are walking or not part of any vlan.So by passing a port, the script  will scan every vlan on the switch for MAC Addresses connected to that port.This script uses the dot1d tables to get the MAC info as per the CISCO website.</span></p>
<p>Update 1.1</p>
<ul>
<li>Fixed Port Matching... </li>
<li>Now for the -n option you can pass the port number '1/1' or the Port Name as per ifName "Gi1/1"
<ol>
<li>Pysnmp</li>
<li>Pyasn1</li>
<li>SNMP Access to the switch you want to talk too and its community string.</li>
</ol>
</li>
<p></p>
<p>Three things you will need for this script to work..</p>
</ul>
<div></div>
<ul>
<li>
<ol>
<li>install <a href="http://pypi.python.org/pypi/setuptools" title="title">python-setuptools<br /> </a></li>
<li>then run easy_install pysnmp<a href="http://pypi.python.org/pypi/setuptools" title="title"></a></li>
<li>and easy_install pyasn1</li>
</ol>
</li>
<p>To make your life easier you should do the following</p>
<p>I am using the following revisions from the python cheese shop <span>pysnmp 4.1.7a  and pyasn1 0.0.6a</span></p>
<p>You can download the script here<br /> <a href="Port-Report-Project/" title="title">port_report.py</a></p>
<p>{quickdown:39}<br />Please post anything related to this script on this forum link <a href="forums/Scripting/scripting/port_report">http://www.linuxdynasty.org/forums/Scripting/scripting/port_report</a> <br /> Unless it is just a comment, thank you...</p>
<p>Also if you download this script on other Platforms besides Cisco, please let me know if it works, so I can added under platforms supported.</p>
<p><a id="more"></a><a id="more-81"></a></p>
<pre>python port_report.py -d 192.168.101.1 -c public -i "192.168.101.201"<br />This IPAddress is not in the ARP table<br /><br />python port_report.py -d 192.168.101.1 -c public -i "192.168.101.209"<br />MAC  = 00 14 38 7f 6e 38<br />Port = GigabitEthernet1/17<br />Vlan = 175<br />IPAddr = 192.168.101.209<br /><br />python port_report.py -d 192.168.101.1 -c public -m "00 14 38 4f 5e 39"<br />MAC  = 00 14 38 4f 5e 39<br />Port = GigabitEthernet1/17<br />Vlan = 175<br />IPAddr = 192.168.101.201<br /><br />python port_report.py -d 192.168.101.1 -c public -n "1/40"<br />Port 1/40 has the below MAC Addresses associated with it<br />MAC  = 00 1b 95 97 3c 81<br />Port = GigabitEthernet1/40<br />Vlan = 1<br />IPAddr = The IP Address for this MAC is not in the ARP Table<br /><br />MAC  = 00 15 fa b4 10 06<br />Port = GigabitEthernet1/40<br />Vlan = 174<br />IPAddr = The IP Address for this MAC is not in the ARP Table<br /><br />Total MAC Addresses associated with this interface 2<br /><br />python port_report.py -d 192.168.101.1 -c public -n "1/2"<br />Port 1/2 has the below MAC Addresses associated with it<br />MAC  = 08 00 0f 20 b3 aa<br />Port = GigabitEthernet1/2<br />Vlan = 176<br />IPAddr = 192.168.101.104<br /><br />MAC  = 08 00 0f 21 d3 78<br />Port = GigabitEthernet1/2<br />Vlan = 173<br />IPAddr = 192.168.101.105<br /><br />MAC  = 08 00 0f 20 b3 aa<br />Port = GigabitEthernet1/2<br />Vlan = 175<br />IPAddr = 192.168.101.115<br /><br /></pre>
<p> </p>
</ul>
