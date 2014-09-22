---
layout: post
status: publish
published: true
title: How to setup a network interface
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 60
wordpress_url: http://linuxdynasty.org/?p=60
date: !binary |-
  MjAwOC0wMi0xMCAyMzo1MjozMyAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAyMzo1MjozMyAtMDUwMA==
categories: []
tags:
- Linux Networking HowTo's
- How to setup a network interface on fedora or gentoo
comments: []
---
<p><strong><span style="color: red">I will try to make this tutorial as general as possible, as I can give you the REDHAT way of doing things as concerns to where REDHAT base systems maintain there networking files or Gentoo based systems...etc</span></strong></p>
<ol>
<li>
<ul>
Lets start with the basics....</p>
<li>To view all your active network interface<br />
 run this command <span style="color: blue">&quot;<strong>ifconfig</strong>&quot;</span></li>
<pre>  sabayon-dynasty ~ # ifconfig<br />eth0      <br />Link encap:Ethernet  HWaddr 00:0E:35:94:FB:D9<br />inet addr:192.168.101.5  Bcast:192.168.101.255 Mask:255.255.255.0<br />inet6 addr: fe80::20e:35ff:fe94:fbd9/64 Scope:Link<br />UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1<br />RX packets:2656195 errors:0 dropped:19 overruns:0 frame:0<br />TX packets:1762149 errors:0 dropped:0 overruns:0 carrier:0<br />collisions:0 txqueuelen:1000<br />RX bytes:3593125256 (3426.6 Mb)  TX bytes:144856589 (138.1 Mb)<br />Interrupt:10 Base address:0xe000 Memory:e0200000-e0200fff<br />  </pre>
<li>Or you can be specific and run (ifconfig and the interface name)<span style="color: blue">&quot;<strong>ifconfig  eth0</strong>&quot;</span> </li>
</ul>
</li>
<li>
<ul>
Setup your network interfaces!</p>
<li><strong>REDHAT WAY</strong>For redhat based systems you will have to do this (assuming your network interface is eth0 and using DHCP)..<br />
<span style="color: blue">&quot;<strong>vi /etc/sysconfig/network-scripts/ifcfg-eth0</strong>&quot;</span></p>
<pre>DEVICE=eth0<br />BOOTPROTO=dhcp<br />HWADDR=00:E0:81:24:CQ:82<br />ONBOOT=yes<br />  </pre>
</li>
<li> Now for a static ip setup (assuming eth0)..<br />
<span style="color: blue">&quot;<strong>vi /etc/sysconfig/network-scripts/ifcfg-eth0</strong>&quot;</span></p>
<pre><br />DEVICE=eth0<br />BROADCAST=192.168.101.255<br />BOOTPROTO=static<br />HWADDR=00:E0:81:24:CQ:82<br />IPADDR=192.168.101.5<br />NETMASK=255.255.255.0<br />NETWORK=192.168.101.0<br />ONBOOT=yes<br />TYPE=Ethernet<br /></pre>
</li>
<li>Now run this <span style="color: blue">&quot;<strong>service network restart</strong>&quot;</span> or run this <span style="color: blue">&quot;<strong>ifdown eth0</strong>&quot;</span> to make sure the interface is down, then <span style="color: blue">&quot;<strong>ifup eth0</strong>&quot;</span> </li>
</ul>
</li>
<li>
<ul><strong>GENTOO WAY</strong>For gentoo based systems you will have to do this.</p>
<li>(assuming your network interface is eth0 and using DHCP)..<br />
<span style="color: blue">&quot;<strong>vi /etc/conf.d/net</strong>&quot;</span></p>
<pre><br />config_eth0=( &quot;dhcp&quot; )<br />dhcp_eth0=&quot;nosendhost&quot;<br />dns_domain_eth0=&quot;linuxdynasty&quot;<br />  </pre>
</li>
<li>Now for a static ip setup (assuming eth0)..<br />
<span style="color: blue">&quot;<strong>vi /etc/conf.d/net</strong>&quot;</span></p>
<pre><br />config_eth0=( &quot;192.168.0.2 netmask 255.255.255.0 broadcast 192.168.0.255&quot; )<br />routes_eth0=(&quot;default via 192.168.0.1&quot;)   # IPv4 default route<br />  </pre>
</li>
<li>Now run this <span style="color: blue">&quot;<strong>rc-update add net.eth0 default</strong>&quot;</span> so that it is in the default run level. </li>
<li>Now to get the interface up and running...<br />
<span style="color: blue">&quot;<strong>/etc/init.d/net.eth0 restart</strong>&quot;</span> </li>
</ul>
</li>
</ol>
