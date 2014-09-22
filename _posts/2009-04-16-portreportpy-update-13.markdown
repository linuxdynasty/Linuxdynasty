---
layout: post
status: publish
published: true
title: port_report.py update 1.3
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 120
wordpress_url: http://linuxdynasty.org/?p=120
date: !binary |-
  MjAwOS0wNC0xNiAxNTo0NToxNiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNC0xNiAxNTo0NToxNiAtMDQwMA==
categories: []
tags:
- Dynastys Blog
- port_report.py update 1.3
comments: []
---
<p><span>Update 1.3 </span></p>
<ul>
<li><span>You are now able to pass 4 different mac formats.. For instance<br />
00 14 38 4f 5e 39 or 00-14-38-4f-5e-39 or 00:14:38:4f:5e:39 or<br />
0014.384f.5e39"</span></li>
<li><span>More information is printed out when you pass the mac or ip</span></li>
<li><span>Further Testing shows the script runs on Cisco Switches only so far. </span></li>
</ul>
<p>I trying very hard to get this script to work with non Cisco device, but since I do not have any other networking device besides Cisco available to me, I am limited.I am working with Kshort to assist me in trying to add Nortel and Foundry, but I can user more help from the community. If you can assist with this please let me know..</p>
<p>Example below...</p>
<pre>python port_report.py -d 192.168.101.1 -c public -m "0014.384f.5e38"<br />MAC  = 00 14 38 4f 5e 38<br />Port = GigabitEthernet1/17<br />Speed = 1gbps<br />Duplex = unknown<br />Vlan = 175<br />IPAddr = 192.168.101.200<br /> </pre>
<p>You can download the script here <a href="http://www.linuxdynasty.org/Port-Report-Project/" title="title">port_report.py </a></p>
<p> </p>
