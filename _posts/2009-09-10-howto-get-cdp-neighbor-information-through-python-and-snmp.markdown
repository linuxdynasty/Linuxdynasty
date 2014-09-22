---
layout: post
status: publish
published: true
title: HowTo get CDP neighbor information through Python and SNMP
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<div>This new script is for Network Engineers and System Engineers a like.
  Though I must admit it is more for the System Engineers who do not have access to
  the command line on the CDP enabled device. Have you ever wanted to know what CDP
  enabled devces ( and info related to those devices ) that were directly connected
  to your your Core Switch? But you just do not have the access to get that info.
  But you do have access to the monitoring system, which has SNMP access to the Core
  Switch.</div>\r\n<code>Well this is where my script comes into play... Stay tuned
  for updates, as I'm planning on adding to this script. So you can run it with the
  detail option and a detail port option. Please post any support related question
  in the forums here..</code><a href=\"forums/Scripting/scripting/sh_cdp_neighbor_help\">http://www.linuxdynasty.org/forums/Scripting/scripting/sh_cdp_neighbor_help</a>\r\n<div>Revision
  1.2 9/13/2009</div>\r\n<ul>\r\n\t<li>Catch all CDP connected switches, even if there
  is more then 1 switch seen through 1 port.</li>\r\n</ul>\r\nRevision 1.1 9/11/2009\r\n<ul>\r\n\t<li>Added
  --type option ( --type=detail )</li>\r\n</ul>\r\n<div>Revision 1.0 9/10/2009</div>\r\n<div>\r\n<ul>\r\n\t<li>This
  script is the equivalent of sho cdp nei on a cisco switch, but this is using snmp.</li>\r\n</ul>\r\n</div>\r\n<pre><code>When
  you log into a switch and run a show cdp neighbor, your info might look a little
  like this.. <strong><span style=\"color: #0000ff;\">show cdp neighbor</span></strong>Capability
  Codes: R - Router, T - Trans Bridge, B - Source Route Bridge S - Switch, H - Host,
  I - IGMP, r - Repeater, P - Phone Device ID Local Intrfce Holdtme Capability Platform
  Port ID71_5th_SW1 Gig 10/15 145 S I WS-C2960G-Gig 0/48D_M1001_V180_SW1 Gig 1/42
  132 S I WS-C2960G-Gig 0/1D_M1001_V181_SW1 Gig 1/46 136 S I WS-C2960G-Gig 0/1D_M1001_V181_SW2
  Gig 1/47 166 S I WS-C2960G-Gig 0/1D_M1001_V180_SW3 Gig 1/43 147 S I WS-C2960G-Gig
  0/1D_M1001_V181_SW3 Gig 1/48 158 S I WS-C2960G-Gig 0/1D_M1001_V180_SW2 Gig 1/41
  141 S I WS-C2960G-Gig 0/1D_M1001_V181_SW4 Gig 1/44 179 S I WS-C2960G-Gig 0/1D_M1001_V180_SW4
  Gig 1/40 145 S I WS-C3560G-Gig 0/1D_M701_V177_SW4 Gig 10/7 174 S I WS-C2970G-Gig
  0/25D_M701_V177_SW1 Gig 10/6 154 S I WS-C2970G-Gig 0/25Router Gig 10/1 162 R S WS-C6513
  Gig 9/9Router1 Gig 10/14 168 R S WS-C6513 Gig 9/1679_18th_Fl_SW1 Gig 10/12 174 S
  I WS-C2960G-Gig 0/48D_1700_V187_SW1 Gig 10/13 129 S I WS-C3560G-Gig 0/28D_1700_V187_SW3
  Gig 10/10 146 S I WS-C2960G-Gig 0/48D_1700_V187_SW2 Gig 10/9 148 S I WS-C2960G-Gig
  0/48D_522_V176_SW1 Gig 10/3 121 S I WS-C2970G-Gig 0/25D_522_V176_SW4 Gig 10/4 125
  S I WS-C2970G-Gig 0/25D_CL001_V200_SW1 Gig 10/11 125 S I WS-C2960G-Gig 0/242W_4507R
  Gig 7/2 147 R S I WS-C4507R Gig 3/9</code></pre>\r\nNow this is how it will look
  if you run sh_cdp_neighbor.py script...\r\n\r\n"
wordpress_id: 82
wordpress_url: http://linuxdynasty.org/?p=82
date: !binary |-
  MjAwOS0wOS0xMCAyMzo1NzoxOCAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wOS0xMCAyMzo1NzoxOCAtMDQwMA==
categories:
- Python
- Cisco
- SNMP
tags:
- Python HowTo's
- HowTo get CDP neighbor information through Python and SNMP
comments:
- id: 9
  author: mfieldhouse
  author_email: fieldhouse@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMS0xMC0yNSAyMDozMjozNCAtMDQwMA==
  date_gmt: !binary |-
    MjAxMS0xMC0yNSAxNTozMjozNCAtMDQwMA==
  content: Hey again, I've just been looking through all your Python projects after
    searching for a Python switchport discovery tool. This also looks like a great
    tool that I'd like to use.
---
<div>This new script is for Network Engineers and System Engineers a like. Though I must admit it is more for the System Engineers who do not have access to the command line on the CDP enabled device. Have you ever wanted to know what CDP enabled devces ( and info related to those devices ) that were directly connected to your your Core Switch? But you just do not have the access to get that info. But you do have access to the monitoring system, which has SNMP access to the Core Switch.</div>
<p><code>Well this is where my script comes into play... Stay tuned for updates, as I'm planning on adding to this script. So you can run it with the detail option and a detail port option. Please post any support related question in the forums here..</code><a href="forums/Scripting/scripting/sh_cdp_neighbor_help">http://www.linuxdynasty.org/forums/Scripting/scripting/sh_cdp_neighbor_help</a></p>
<div>Revision 1.2 9/13/2009</div>
<ul>
<li>Catch all CDP connected switches, even if there is more then 1 switch seen through 1 port.</li>
</ul>
<p>Revision 1.1 9/11/2009</p>
<ul>
<li>Added --type option ( --type=detail )</li>
</ul>
<div>Revision 1.0 9/10/2009</div>
<div>
<ul>
<li>This script is the equivalent of sho cdp nei on a cisco switch, but this is using snmp.</li>
</ul>
</div>
<pre><code>When you log into a switch and run a show cdp neighbor, your info might look a little like this.. <strong><span style="color: #0000ff;">show cdp neighbor</span></strong>Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone Device ID Local Intrfce Holdtme Capability Platform Port ID71_5th_SW1 Gig 10/15 145 S I WS-C2960G-Gig 0/48D_M1001_V180_SW1 Gig 1/42 132 S I WS-C2960G-Gig 0/1D_M1001_V181_SW1 Gig 1/46 136 S I WS-C2960G-Gig 0/1D_M1001_V181_SW2 Gig 1/47 166 S I WS-C2960G-Gig 0/1D_M1001_V180_SW3 Gig 1/43 147 S I WS-C2960G-Gig 0/1D_M1001_V181_SW3 Gig 1/48 158 S I WS-C2960G-Gig 0/1D_M1001_V180_SW2 Gig 1/41 141 S I WS-C2960G-Gig 0/1D_M1001_V181_SW4 Gig 1/44 179 S I WS-C2960G-Gig 0/1D_M1001_V180_SW4 Gig 1/40 145 S I WS-C3560G-Gig 0/1D_M701_V177_SW4 Gig 10/7 174 S I WS-C2970G-Gig 0/25D_M701_V177_SW1 Gig 10/6 154 S I WS-C2970G-Gig 0/25Router Gig 10/1 162 R S WS-C6513 Gig 9/9Router1 Gig 10/14 168 R S WS-C6513 Gig 9/1679_18th_Fl_SW1 Gig 10/12 174 S I WS-C2960G-Gig 0/48D_1700_V187_SW1 Gig 10/13 129 S I WS-C3560G-Gig 0/28D_1700_V187_SW3 Gig 10/10 146 S I WS-C2960G-Gig 0/48D_1700_V187_SW2 Gig 10/9 148 S I WS-C2960G-Gig 0/48D_522_V176_SW1 Gig 10/3 121 S I WS-C2970G-Gig 0/25D_522_V176_SW4 Gig 10/4 125 S I WS-C2970G-Gig 0/25D_CL001_V200_SW1 Gig 10/11 125 S I WS-C2960G-Gig 0/242W_4507R Gig 7/2 147 R S I WS-C4507R Gig 3/9</code></pre>
<p>Now this is how it will look if you run sh_cdp_neighbor.py script...</p>
<p><a id="more"></a><a id="more-82"></a></p>
<pre>python <span style="color: #0000ff;"><strong>sh_cdp_neighbor.py -d 192.168.1.1 -c public</strong></span>Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge S - Switch, H - Host, I - IGMP, r - Repeater, P - PhoneDevice ID                  Local Interface      Capability           Platform                       Remote Interface    D_M1001_V181_SW3           Gi1/48               S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/1  Router1                    Gi10/14              R S                  cisco WS-C6513                 GigabitEthernet9/16 D_M1001_V181_SW1           Gi1/46               S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/1  D_M1001_V181_SW2           Gi1/47               S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/1  D_M1001_V181_SW4           Gi1/44               S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/1  D_M1001_V180_SW1           Gi1/42               S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/1  D_M1001_V180_SW3           Gi1/43               S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/1  D_M1001_V180_SW4           Gi1/40               S I                  cisco WS-C3560G-24PS           GigabitEthernet0/1  D_M1001_V180_SW2           Gi1/41               S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/1  71_5th_SW1                 Gi10/15              S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/48 2W_4507R                   Gi7/2                R S I                cisco WS-C4507R                GigabitEthernet3/9  D_1700_V187_SW2            Gi10/9               S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/48 D_CL001_V200_SW1           Gi10/11              S I                  cisco WS-C2960G-24TC-L         GigabitEthernet0/24 D_1700_V187_SW3            Gi10/10              S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/48 D_1700_V187_SW1            Gi10/13              S I                  cisco WS-C3560G-24PS           GigabitEthernet0/28 79_18th_Fl_SW1             Gi10/12              S I                  cisco WS-C2960G-48TC-L         GigabitEthernet0/48 D_522_V176_SW1             Gi10/3               S I                  cisco WS-C2970G-24TS-E         GigabitEthernet0/25 Router                     Gi10/1               R S                  cisco WS-C6513                 GigabitEthernet9/9  D_M701_V177_SW1            Gi10/6               S I                  cisco WS-C2970G-24TS-E         GigabitEthernet0/25 D_M701_V177_SW4            Gi10/7               S I                  cisco WS-C2970G-24TS-E         GigabitEthernet0/25 D_522_V176_SW4             Gi10/4               S I                  cisco WS-C2970G-24TS-E         GigabitEthernet0/25</pre>
<p>As you can see I was able to get about 99% of what the command line version of <span style="color: #0000ff;"><strong>show cdp neighbor</strong></span> was able to retrieve.<br />
Here is another example of the newest feature.....</p>
<pre>python sh_cdp_neighbor.py -d 192.168.1.1 -c public --type=detail
------------------------------
Device ID: Network_5Entry address(es):
IP address:  192.186.1.15Platform: cisco WS-C2950T-24,  Capabilities: S IInterface: Gi3/16,
Port ID (outgoing port): GigabitEthernet0/1
Version :Cisco Internetwork Operating System SoftwareIOS (tm) C2950 Software (C2950-I6K2L2Q4-M), Version 12.1(22)EA11, RELEASE SOFTWARE (fc2)Copyright (c) 1986-2008 by cisco Systems, Inc.Compiled Tue 08-Jan-08 11:12 by amvarmaVTP
Management Domain: testDuplex: fullDuplexManagement address(es):
 IP address:  192.186.1.15

------------------------------

------------------------------
Device ID: I_811_V53_SW1Entry address(es):
 IP address:  192.186.1.16Platform: cisco WS-C2970G-24TS-E,  Capabilities: S IInterface: Gi9/1,
 Port ID (outgoing port): GigabitEthernet0/25</pre>
<p>As you can see I was able to get about 99% of what the command line version of <span style="color: #0000ff;"><strong>show cdp neighbor detail</strong></span> was able to retrieve.</p>
<div>You will need the two python modules to run this script. which are pysnmp and pyasn1.<br />
To make your life easier you should do the following...</div>
<ol>
<li>install <a title="title" href="http://pypi.python.org/pypi/setuptools">python-setuptools<br />
</a></li>
<li>then run easy_install pysnmp</li>
<li>and easy_install pyasn1</li>
<li>or you can download the 2 modules manually.<br />
<a title="title" href="http://voxel.dl.sourceforge.net/sourceforge/pysnmp/pysnmp-4.1.10a.tar.gz">pysnmp</a> and <a title="title" href="http://voxel.dl.sourceforge.net/sourceforge/pyasn1/pyasn1-0.0.8a.tar.gz">pyasn1</a></li>
<li>then unzip the 2 files and in each directory run <strong>python setup.py install</strong></li>
</ol>
<p>I am using the following revisions from the python cheese shop pysnmp 4.1.7a and pyasn1 0.0.6</p>
<p>You can download the script here... <a href="View-details/LinuxDynasty/48-Show-CDP-Neighbor-using-SNMP-and-Python.html">sho_cdp_neighbor.py</a><br />
{filelink=16}</p>
