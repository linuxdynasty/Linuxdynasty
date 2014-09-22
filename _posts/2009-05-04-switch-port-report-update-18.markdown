---
layout: post
status: publish
published: true
title: Switch Port Report Update 1.8
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 126
wordpress_url: http://linuxdynasty.org/?p=126
date: !binary |-
  MjAwOS0wNS0wNCAxMTo0NDoxMSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNS0wNCAxMTo0NDoxMSAtMDQwMA==
categories: []
tags:
- Dynastys Blog
- Switch Port Report Update 1.8
comments: []
---
<p>The Port Report Project is essentially a Switch Port Mapper Tool or a Switch Port Mapping Tool like a few other commercial products out there, except The Port Report Project is free.  Right now there is no GUI or WEB interface for the project but it is in the works.</p>
<p>Here is a quick update..... I just add dns reverse lookups to the output of this script.. So if you have Pointer Records set on a good part of your infrastructure, you will get the host name to those MAC Addresses that have the IP addresses in the ARP table.</p>
<p>You can download Port Report 1.8 here <a href="View-details/Port-Report-Project/43-Port-Report-1.8.html" title="title">http://www.linuxdynasty.org/View-details/Python-Scripts/39-port_report.py.htmll<br /> </a>{quickdown:39}<br />Example below...</p>
<p> </p>
<p>Here is an example from running port_report.py with the --report option..</p>
<pre><small>GigabitEthernet3/2,00 50 56 aa 06 63,192.168.101.64,lists.linuxdynasty.org,vlan32,up,up,fullDuplex,1000mb,conan vmnic6<br />GigabitEthernet3/2,00 50 56 aa 1e 9b,192.168.101.54,Pointer Record Not set for 192.168.101.54,vlan32,up,up,fullDuplex,1000mb,conan vmnic6<br />GigabitEthernet2/28,00 11 21 35 1d da,The IP Address for 00 11 21 35 1d da is not in the ARP Table,None,vlan15,up,up,fullDuplex,1000mb,<br /> </small></pre>
<p>Here is an example running  with the --pname option..</p>
<pre>SwitchPort = GigabitEthernet3/2<br />SwitchPortSpeed = 1000mb<br />SwitchPortDuplex = fullDuplex<br />SwitchVlan = vlan32<br />SnmpHostName = requestTimedOut<br />HostDescr = requestTimedOut<br />HostMAC  = 00 50 56 aa 06 63<br />HostIP = 192.168.101.64<br />HostName = lists.linuxdynasty.org<br /><br />SwitchPort = GigabitEthernet3/2<br />SwitchPortSpeed = 1000mb<br />SwitchPortDuplex = fullDuplex<br />SwitchVlan = vlan32<br />SnmpHostName = requestTimedOut<br />HostDescr = requestTimedOut<br />HostMAC  = 00 50 56 aa 1e 9b<br />HostIP = 192.168.101.54<br />HostName = Pointer Record Not set for 192.168.101.54<br /><br />SwitchPort = GigabitEthernet3/2<br />SwitchPortSpeed = 1000mb<br />SwitchPortDuplex = fullDuplex<br />SwitchVlan = vlan5<br />SnmpHostName = No SNMP Access<br />HostDescr = No SNMP Access<br />HostMAC  = 00 50 56 aa 51 6a<br />HostIP = The IP Address for 00 50 56 aa 51 6a is not in the ARP Table<br />HostName = None<br /> </pre>
