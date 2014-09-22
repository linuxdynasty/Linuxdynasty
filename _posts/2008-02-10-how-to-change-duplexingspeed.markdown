---
layout: post
status: publish
published: true
title: How to change Duplexing/Speed
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 58
wordpress_url: http://linuxdynasty.org/?p=58
date: !binary |-
  MjAwOC0wMi0xMCAyMzo0Mzo0NCAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAyMzo0Mzo0NCAtMDUwMA==
categories: []
tags:
- Linux Networking HowTo's
- How to change Duplexing/Speed on Linux duplex speed fedora ubuntu linux
comments: []
---
<p><span style="color: rgb(255, 0, 0)">In this tutorial we will show you how to view your speed/duplexing setting and also changing your duplexing/speed settings</span></p>
<ol>
<li>
<ul>
To view you interface settings, run this..<span style="color: rgb(0, 0, 255)">&quot;<strong>ethtool eth0</strong>&quot;</span></p>
<pre><br />Settings for eth0:<br />        Supported ports: [ TP MII ]<br />        Supported link modes:   10baseT/Half 10baseT/Full<br />                                100baseT/Half 100baseT/Full<br />        Supports auto-negotiation: Yes<br />        Advertised link modes:  10baseT/Half 10baseT/Full<br />                                100baseT/Half 100baseT/Full<br />        Advertised auto-negotiation: Yes<br />        Speed: 100Mb/s<br />        Duplex: Full<br />        Port: MII<br />        PHYAD: 1<br />        Transceiver: internal<br />        Auto-negotiation: on<br />        Supports Wake-on: g<br />        Wake-on: g<br />        Current message level: 0x00000007 (7)<br />        Link detected: yes<br />  </pre>
<p>&nbsp;</p>
<li>To change your settings for eth0 you will have to do this...<br />
<span style="color: rgb(0, 0, 255)">&quot;<strong>ethtool -s eth1 speed 100 duplex full autoneg off</strong>&quot;</span> </li>
<li><strong>REDHAT</strong>To make these changes permanently you will have to append this <strong><span style="color: rgb(0, 0, 255)">ETHTOOL_OPTS=&quot;speed 100 duplex full autoneg off&quot;</span></strong>to the /etc/sysconfig/network-scripts/ifcfg-eth0 file
<pre><br />DEVICE=eth0<br />BROADCAST=192.168.101.255<br />BOOTPROTO=static<br />HWADDR=00:E0:81:24:CQ:82<br />IPADDR=192.168.101.5<br />NETMASK=255.255.255.0<br />NETWORK=192.168.101.0<br />ONBOOT=yes<br />TYPE=Ethernet<br />ETHTOOL_OPTS=&quot;speed 100 duplex full autoneg off&quot;<br />  </pre>
</li>
</ul>
</li>
</ol>
