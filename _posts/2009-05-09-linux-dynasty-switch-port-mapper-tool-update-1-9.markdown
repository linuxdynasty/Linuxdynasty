---
layout: post
status: publish
published: true
title: Linux Dynasty Switch Port Mapper Tool Update 1.9
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>I'm really excited to introduce Port Report Update 1.9  aka the Switch
  Port Mapper Tool. We've done quite a few code modifications to the previous release
  of Port Report. The most important feature we just finish adding to Port Report,
  is to detect CDP Neighbors during the scan for MAC Addresses or IP Addresses. We
  are still adding features as the days pass, so please stay tuned....</p>\r\n<p>Revision
  1.9<br /> Code changes and Added CDP support..</p>\r\n<ul>\r\n<li>Detect CDP Neighbors
  during the scan for MAC Addresses or IP Addresses </li>\r\n</ul>\r\n<p>You can download
  the script <a href=\"Port-Report-Project/\">http://www.linuxdynasty.org/Port-Report-Project/<br
  /></a>{quickdown:39}</p>\r\n<br />"
wordpress_id: 210
wordpress_url: http://linuxdynasty.org/?p=210
date: !binary |-
  MjAwOS0wNS0wOSAwMToyODozNSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNS0wOSAwMToyODozNSAtMDQwMA==
categories: []
tags:
- Switch Port Report
- Linux Dynasty Switch Port Mapper Toool
comments: []
---
<p>I'm really excited to introduce Port Report Update 1.9  aka the Switch Port Mapper Tool. We've done quite a few code modifications to the previous release of Port Report. The most important feature we just finish adding to Port Report, is to detect CDP Neighbors during the scan for MAC Addresses or IP Addresses. We are still adding features as the days pass, so please stay tuned....</p>
<p>Revision 1.9<br /> Code changes and Added CDP support..</p>
<ul>
<li>Detect CDP Neighbors during the scan for MAC Addresses or IP Addresses </li>
</ul>
<p>You can download the script <a href="Port-Report-Project/">http://www.linuxdynasty.org/Port-Report-Project/<br /></a>{quickdown:39}</p>
<p><a id="more"></a><a id="more-210"></a></p>
<p> </p>
<p> Here is an example below..</p>
<pre><pre><code>python port_report.py -d switch -c community -m "00 13 20 16 5f f7"<br />Switch Connected to 192.168.101.1<br />SwitchPort = GigabitEthernet10/3<br />SwitchPortSpeed = 1000mb<br />SwitchPortDuplex = fullDuplex<br />SwitchVlan = vlan176<br />SnmpHostName = requestTimedOut<br />SnmpHostDescr = requestTimedOut<br />HostMAC  = 00 13 20 16 5f f7<br />HostIP = 192.168.101.101<br />HostName = Pointer Record Not set for 192.168.101.101<br /><br />Found 00 13 20 16 5f f7 on 192.168.101.5<br /><br />Switch Connected to 192.168.101.5<br />SwitchPort = GigabitEthernet0/24<br />SwitchPortSpeed = 1000mb<br />SwitchPortDuplex = fullDuplex<br />SwitchVlan = vlan176<br />SnmpHostName = No SNMP Access<br />SnmpHostDescr = No SNMP Access<br />HostMAC  = 00 13 20 16 5f f7<br />HostIP = None<br />HostName = None<br /><br />Found 00 13 20 16 5f f7 on 192.168.101.6<br /><br />Switch Connected to 192.168.101.6<br />SwitchPort = GigabitEthernet0/22<br />SwitchPortSpeed = 1000mb<br />SwitchPortDuplex = fullDuplex<br />SwitchVlan = vlan176<br />SnmpHostName = No SNMP Access<br />SnmpHostDescr = No SNMP Access<br />HostMAC  = 00 13 20 16 5f f7<br />HostIP = None<br />HostName = None<br /><br />This MAC 00 13 20 16 5f f7 was finally traced to this switch 192.168.101.6</code> </pre>
<p></p>
