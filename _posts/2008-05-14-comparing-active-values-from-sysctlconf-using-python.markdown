---
layout: post
status: publish
published: true
title: Comparing active values from sysctl.conf using Python
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p><span>I was told the other day to write a script that will compare
  a set of predefined values&nbsp; to active values from &quot;sysctl -a&quot;<br
  />\r\nSo here it is.... Some people might ask why did I not do this in shell or
  even perl??? The answer is simple I love PYTHON!!! :)<br />\r\n</span></p>\r\n<p><span>Example
  below..... Make sure to run as root&nbsp;</span></p>\r\n<p><span>python sysctl_verify.py
  <br />\r\n[FAIL] net.core.rmem_max = 131071 (Required value = 20971520)<br />\r\n[FAIL]
  net.ipv4.tcp_mem = 374304 (Required value = 32768 32768 32768)<br />\r\n[FAIL] net.ipv4.tcp_rmem
  = 4096 (Required value = 4096 87380 8388608)<br />\r\n[FAIL] net.ipv4.tcp_retries2
  = 15 (Required value = 5)<br />\r\n[FAIL] net.ipv4.tcp_wmem = 4096 (Required value
  = 4096 16384 8388608)<br />\r\n[FAIL] net.core.wmem_max = 131071 (Required value
  = 20971520)<br />\r\n[FAIL] net.core.netdev_max_backlog = 1000 (Required value =
  3000)<br />\r\n[FAIL] net.ipv4.route.flush = Does not Exist!! (Required value =
  1)<br />\r\n[FAIL] Current RX value = 128 (Required RX value = 16384)<br />\r\n</span></p>\r\n<p><span><br
  />\r\n</span></p>\r\n<p><span><br />\r\n#!/usr/bin/env python<br />\r\n#This script
  will will compare a set of predefined values&nbsp; to active values from &quot;sysctl
  -a&quot;<br />\r\n#Copyright (C) 2008  Allen Sanabria<br />\r\n<br />#This program
  is free software; you can redistribute it and/or modify<br />\r\n#it under the terms
  of the GNU General Public License as published by<br />\r\n#the Free Software Foundation;
  either version 2 of the License, or<br />\r\n#(at your option) any later version.<br
  />\r\n<br />#This program is distributed in the hope that it will be useful,<br
  />\r\n#but WITHOUT ANY WARRANTY; without even the implied warranty of<br />\r\n#MERCHANTABILITY
  or FITNESS FOR A PARTICULAR PURPOSE.  See the<br />\r\n#GNU General Public License
  for more details.<br />\r\n<br />#You should have received a copy of the GNU General
  Public License along<br />\r\n#with this program; if not, write to the Free Software
  Foundation, Inc.,<br />\r\n#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301
  USA.<br />\r\nimport os, sys, re, string<br />\r\n#Created by Allen Sanabria<br
  />\r\n#Verify these parameters are whats running in sysctl<br />\r\n# net.core.rmem_max
  = 20971520<br />\r\n# net.core.wmem_max = 20971520<br />\r\n# net.ipv4.tcp_mem =
  32768 32768 32768<br />\r\n# net.ipv4.tcp_rmem = 4096 87380 8388608<br />\r\n# net.ipv4.tcp_wmem
  = 4096 16384 8388608<br />\r\n# net.ipv4.tcp_retries2 = 5<br />\r\n# net.core.netdev_max_backlog
  = 3000<br />\r\n# net.ipv4.route.flush = 1<br />\r\n</span>\r\n<br />"
wordpress_id: 72
wordpress_url: http://linuxdynasty.org/?p=72
date: !binary |-
  MjAwOC0wNS0xNCAyMDowMTozMSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0xNCAyMDowMTozMSAtMDQwMA==
categories: []
tags:
- Python HowTo's
- Comparing active values from sysctl.conf using Python
comments: []
---
<p><span>I was told the other day to write a script that will compare a set of predefined values&nbsp; to active values from &quot;sysctl -a&quot;<br />
So here it is.... Some people might ask why did I not do this in shell or even perl??? The answer is simple I love PYTHON!!! :)<br />
</span></p>
<p><span>Example below..... Make sure to run as root&nbsp;</span></p>
<p><span>python sysctl_verify.py <br />
[FAIL] net.core.rmem_max = 131071 (Required value = 20971520)<br />
[FAIL] net.ipv4.tcp_mem = 374304 (Required value = 32768 32768 32768)<br />
[FAIL] net.ipv4.tcp_rmem = 4096 (Required value = 4096 87380 8388608)<br />
[FAIL] net.ipv4.tcp_retries2 = 15 (Required value = 5)<br />
[FAIL] net.ipv4.tcp_wmem = 4096 (Required value = 4096 16384 8388608)<br />
[FAIL] net.core.wmem_max = 131071 (Required value = 20971520)<br />
[FAIL] net.core.netdev_max_backlog = 1000 (Required value = 3000)<br />
[FAIL] net.ipv4.route.flush = Does not Exist!! (Required value = 1)<br />
[FAIL] Current RX value = 128 (Required RX value = 16384)<br />
</span></p>
<p><span><br />
</span></p>
<p><span><br />
#!/usr/bin/env python<br />
#This script will will compare a set of predefined values&nbsp; to active values from &quot;sysctl -a&quot;<br />
#Copyright (C) 2008  Allen Sanabria</p>
<p>#This program is free software; you can redistribute it and/or modify<br />
#it under the terms of the GNU General Public License as published by<br />
#the Free Software Foundation; either version 2 of the License, or<br />
#(at your option) any later version.</p>
<p>#This program is distributed in the hope that it will be useful,<br />
#but WITHOUT ANY WARRANTY; without even the implied warranty of<br />
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the<br />
#GNU General Public License for more details.</p>
<p>#You should have received a copy of the GNU General Public License along<br />
#with this program; if not, write to the Free Software Foundation, Inc.,<br />
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.<br />
import os, sys, re, string<br />
#Created by Allen Sanabria<br />
#Verify these parameters are whats running in sysctl<br />
# net.core.rmem_max = 20971520<br />
# net.core.wmem_max = 20971520<br />
# net.ipv4.tcp_mem = 32768 32768 32768<br />
# net.ipv4.tcp_rmem = 4096 87380 8388608<br />
# net.ipv4.tcp_wmem = 4096 16384 8388608<br />
# net.ipv4.tcp_retries2 = 5<br />
# net.core.netdev_max_backlog = 3000<br />
# net.ipv4.route.flush = 1<br />
</span><br />
<br /><a id="more"></a><a id="more-72"></a><br /><span><br />
uid = os.getuid()<br />
root = 0<br />
login = os.getlogin()<br />
eth = []<br />
max_rx = {}<br />
cur_rx = {}</p>
<p>if uid == root:<br />
  sysctl_out = {'net.core.rmem_max' : '20971520',<br />
                'net.core.wmem_max' : '20971520',<br />
                'net.ipv4.tcp_mem' : '32768 32768 32768',<br />
                'net.ipv4.tcp_rmem' : '4096 87380 8388608',<br />
                'net.ipv4.tcp_wmem' : '4096 16384 8388608',<br />
                'net.ipv4.tcp_retries2' : '5',<br />
                'net.core.netdev_max_backlog' : '3000',<br />
                'net.ipv4.route.flush' : '1'}</p>
<p>
  for key in sysctl_out.keys():<br />
    sysctl = 'sysctl -a | grep %s' % (key)<br />
    sysctl_exec = os.popen(sysctl).readline()<br />
    sysctl_exec = re.sub('n', '', sysctl_exec)<br />
    sysctl_exec = re.sub('s+', ' ', sysctl_exec)<br />
    sysctl_match = re.search(key+' = '+sysctl_out[key], sysctl_exec)<br />
    sysctl_line = re.search((key)+' = (d+)', sysctl_exec)<br />
    sysctl_first = re.search((key), sysctl_exec)<br />
    if sysctl_match:<br />
      print &quot;[PASS] &quot;+key+ &quot; = &quot; +sysctl_out[key]<br />
    elif not sysctl_first:<br />
      print &quot;[FAIL] &quot; +key+ &quot; = Does not Exist!! (Required value = &quot; +sysctl_out[key]+ &quot;)&quot;<br />
    else:<br />
      print &quot;[FAIL] &quot; +key+ &quot; = &quot; +sysctl_line.group(1)+ &quot; (Required value = &quot; +sysctl_out[key]+ &quot;)&quot;<br />
else:<br />
  print &quot;Only root can run this, and you are %s with a id of %s&quot; % (login, uid)</span></p>
