---
layout: post
status: publish
published: true
title: Verify current RX Descriptors on all NICS using Python and ethtool
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p><span>The reason I wrote this script was because someone requested
  that I write it for them so that they can run it through all of our servers and
  see what the settings are set to....</span></p>\r\n<p><span>A brief explanation
  of what RX Descriptors are....&nbsp;</span></p>\r\n<p><span>Rx Descriptors is the
  Number of receive descriptors. A receive descriptor is a data structure that describes
  a receive buffer and its attributes to the network controller. The data in the descriptor
  is used by the controller to write data from the controller to host memory.</span></p>\r\n<p><span>Example
  below from ethtool</span></p>\r\n<p><span>&nbsp;</span></p>\r\n<br />"
wordpress_id: 73
wordpress_url: http://linuxdynasty.org/?p=73
date: !binary |-
  MjAwOC0wNS0xNiAyMDowNDoyNyAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0xNiAyMDowNDoyNyAtMDQwMA==
categories: []
tags:
- Python HowTo's
- Verify current RX Descriptors on all NICS using python ethtool -g
comments: []
---
<p><span>The reason I wrote this script was because someone requested that I write it for them so that they can run it through all of our servers and see what the settings are set to....</span></p>
<p><span>A brief explanation of what RX Descriptors are....&nbsp;</span></p>
<p><span>Rx Descriptors is the Number of receive descriptors. A receive descriptor is a data structure that describes a receive buffer and its attributes to the network controller. The data in the descriptor is used by the controller to write data from the controller to host memory.</span></p>
<p><span>Example below from ethtool</span></p>
<p><span>&nbsp;</span></p>
<p><a id="more"></a><a id="more-73"></a></p>
<p><span>&nbsp;</span></p>
<p><span># ethtool -g eth0<br />
Ring parameters for eth0:<br />
Pre-set maximums:<br />
RX:             511<br />
RX Mini:        0<br />
RX Jumbo:       255<br />
TX:             0<br />
Current hardware settings:<br />
RX:             511<br />
RX Mini:        0<br />
RX Jumbo:       100<br />
TX:             511</span></p>
<p><span>&nbsp;</span></p></p>
<p><span>Output of script below... run as root</span></p>
<p><span>python nic_rx_check.py<br />
[FAIL] Current RX value = 128 (Required RX value = 16384)<br />
</span></p>
<p><span><br />
</span></p>
<p><span>#!/usr/bin/env python<br />
#Create by Allen Sanabria<br />
#To verify that the current RX Descriptors are set to the MAX of what it can handle.<br />
#To set this value all you have to do is &quot;ethtool -G &lt;device&gt; &lt;MAX&gt;&quot;&nbsp; ethtool -G eth0 511<br />
</span></p>
<p><span>#This script will reorder your vmnics for you<br />
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
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.</span></p>
<p><span></p>
<p>import os, re</p>
<p>eth = []<br />
cur_rx = {}<br />
max_rx = {}<br />
devices = open('/proc/net/dev', 'r').readlines()</p>
<p>root = 0<br />
uid = os.getuid()<br />
login = os.getlogin()</p>
<p>if uid == root:<br />
&nbsp; for lines in devices:<br />
&nbsp;&nbsp;&nbsp; match1 = re.search(&quot;(eth[0-9]+):&quot;, lines)<br />
&nbsp;&nbsp;&nbsp; if match1:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; eth.append(match1.group(1))<br />
&nbsp;&nbsp;&nbsp; else:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue</p>
<p>&nbsp; for iface in eth:<br />
&nbsp;&nbsp;&nbsp; ethtool = 'ethtool -g %s' % (iface)<br />
&nbsp;&nbsp;&nbsp; ethtool_exec = os.popen(ethtool).readlines()<br />
&nbsp;&nbsp;&nbsp; for line in range(len(ethtool_exec)):<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; match_max = re.search(&quot;^Pre-sets+maximums:&quot;, ethtool_exec[line])<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; match_cur = re.search(&quot;^Currents+hardwares+settings:&quot;, ethtool_exec[line])<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if match_max:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; match_value = re.search(&quot;(d+)&quot;, ethtool_exec[line+1])<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; max_rx[iface] = match_value.group(1)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; elif match_cur:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; match_value = re.search(&quot;(d+)&quot;, ethtool_exec[line+1])<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cur_rx[iface] = match_value.group(1)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br />
&nbsp; for key in cur_rx.keys():<br />
&nbsp;&nbsp;&nbsp; if cur_rx[key] == max_rx[key]:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;[PASS] &quot;+key+&quot; rx value = &quot;+max_rx[key]<br />
&nbsp;&nbsp;&nbsp; else:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;[FAIL] Current RX value = &quot; +cur_rx[key]+ &quot; (Required RX value = &quot; +max_rx[key]+ &quot;)&quot;<br />
else:<br />
&nbsp; print &quot;Only root can run this, and you are %s with a id of %s&quot; % (login, uid <br />
</span></p>
