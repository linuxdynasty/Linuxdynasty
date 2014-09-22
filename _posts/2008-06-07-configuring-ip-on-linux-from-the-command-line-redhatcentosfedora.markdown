---
layout: post
status: publish
published: true
title: Configuring IP on Linux from the Command Line (RedHat,CentOS,Fedora)
author:
  display_name: tinkpen
  login: tinkpen
  email: tinkpen@sympatico.ca
  url: ''
author_login: tinkpen
author_email: tinkpen@sympatico.ca
excerpt: ! "<p class=\"MsoNormal\"><strong><span style=\"font-size: 12pt\" lang=\"EN-US\">Configuring
  IP on Linux from the Command Line\r\n(RedHat,CentOS,Fedora)\r\n</span></strong></p>\r\n<p
  class=\"MsoNormal\"><span style=\"font-size: 12pt\">This\r\nguide assumes that you
  are adding an the IP on eth0. If you are doing this on\r\nanother Eth card (i.e.
  eth1) just adjust the eth numbers accordingly\r\n</span></p>\r\n<p class=\"MsoNormal\"> </p>\r\n<br
  />"
wordpress_id: 65
wordpress_url: http://linuxdynasty.org/?p=65
date: !binary |-
  MjAwOC0wNi0wNyAxNDoxMDoyOSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNi0wNyAxNDoxMDoyOSAtMDQwMA==
categories: []
tags:
- Linux Networking HowTo's
- How to setup a static interface on RedHat Centos
comments: []
---
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">Configuring IP on Linux from the Command Line<br />
(RedHat,CentOS,Fedora)<br />
</span></strong></p>
<p class="MsoNormal"><span style="font-size: 12pt">This<br />
guide assumes that you are adding an the IP on eth0. If you are doing this on<br />
another Eth card (i.e. eth1) just adjust the eth numbers accordingly<br />
</span></p>
<p class="MsoNormal"> </p>
<p><a id="more"></a><a id="more-65"></a></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US"><br />
Step 1 -Add IP Address<br />
</span></strong></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">vi /etc/sysconfig/network-scripts/ifcfg-eth0<br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
 </span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">and configure like<br />
the following (pick any IP address available on your network)<br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
 </span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">DEVICE=eth0<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">BOOTPROTO=none<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">BROADCAST=192.168.1.255<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">IPADDR=192.168.1.105<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">NETMASK=255.255.255.0<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">NETWORK=192.168.1.0<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">HWADDR=00:50:FC:4B:B8:98<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">ONBOOT=yes<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">TYPE=Ethernet<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">USERCTL=no<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">IPV6INIT=no<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">PEERDNS=no<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">GATEWAY=192.168.1.1<br />
</span></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt"><br />
 </span></strong></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">Step 2 Restart the NIC<br />
</span></strong></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">service network restart<br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
 </span></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">Step 3 - Add the Default Route:<br />
</span></strong></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">Default Route: </span></strong><span style="font-size: 12pt" lang="EN-US"><br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">route add default<br />
gw <em>ip_address_of_your_default_gateway</em><br />
eth0<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">route add default gw 192.168.1.1 eth0<br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
 </span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">To make gw/route<br />
permanent:<br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">vi /etc/sysconfig/network<br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
 </span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">to make look like<br />
this:<br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
 </span></p>
<p class="MsoNormal"><span style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; font-size: 12pt; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial" lang="EN-US">NETWORKING=yes<br />
HOSTNAME= localhost.localdomain<br />
GATEWAY=192.168.1.1<br />
</span><span style="font-size: 12pt" lang="EN-US"><span> </span><span> </span><br />
</span></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">Step 4 - Add DNS Servers<br />
</span></strong></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><span> </span><br />
</span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">vi /etc/resolv.conf<br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
 </span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">so it looks like<br />
this:<br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
 </span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">search yourdomain.com<br />
nameserver 192.168.1.37<br />
nameserver 192.168.1.36<br />
nameserver 192.168.1.38<br />
</span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><span> </span><br />
</span></p>
<p> </p>
