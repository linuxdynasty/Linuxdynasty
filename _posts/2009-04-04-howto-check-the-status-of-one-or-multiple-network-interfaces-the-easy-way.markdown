---
layout: post
status: publish
published: true
title: HowTo check the status of one or multiple network interfaces the easy way
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>Today a friend of mine wanted to know how he can check the status and
  or speed of multiple Network Interfaces/Ports on a device ( Switch, Router, Server,
  etcc ) using SNMP. Specifically he wanted to know if the Interfaces/Ports are Operationally
  Up or Down and also if it is Administratively. Then he also wanted to know the speed
  of the Interfaces/Ports that were Up or Down.</p>\r\n<p>Now you can easily get this
  information through SNMP or if you have a monitoring tool like <a href=\"http://zenoss.com\"
  title=\"\" target=\"_blank\">Zenoss.</a> But he wanted a command line script that
  would run fairly quickly and either print the results to STDOUT or that he can pipe
  the ouput in an email.</p>\r\n<p>So I decided, ok I'll wite you a quick script in
  Python that will get you that information. FYI, I'm thinking of making this script
  compatible with the Nagios API. If you want this feature please let me know... Below
  I will give you some examples of the script....&nbsp; </p>\r\n<pre>    python check_int_speed.py
  --device zenoss --community &quot;public&quot; --astatus &quot;Up&quot; --ostatus
  &quot;Up&quot;<br />    lo is Administratively  Up and Operationally Up and running
  at 10mbs<br />    eth0 is Administratively  Up and Operationally Up and running
  at 1gbps<br /></pre>\r\n<br />"
wordpress_id: 79
wordpress_url: http://linuxdynasty.org/?p=79
date: !binary |-
  MjAwOS0wNC0wNCAwMjowMDo1MSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNC0wNCAwMjowMDo1MSAtMDQwMA==
categories: []
tags:
- Python HowTo's
- HowTo check the status of one or multiple network interfacese the easy way
comments: []
---
<p>Today a friend of mine wanted to know how he can check the status and or speed of multiple Network Interfaces/Ports on a device ( Switch, Router, Server, etcc ) using SNMP. Specifically he wanted to know if the Interfaces/Ports are Operationally Up or Down and also if it is Administratively. Then he also wanted to know the speed of the Interfaces/Ports that were Up or Down.</p>
<p>Now you can easily get this information through SNMP or if you have a monitoring tool like <a href="http://zenoss.com" title="" target="_blank">Zenoss.</a> But he wanted a command line script that would run fairly quickly and either print the results to STDOUT or that he can pipe the ouput in an email.</p>
<p>So I decided, ok I'll wite you a quick script in Python that will get you that information. FYI, I'm thinking of making this script compatible with the Nagios API. If you want this feature please let me know... Below I will give you some examples of the script....&nbsp; </p>
<pre>    python check_int_speed.py --device zenoss --community &quot;public&quot; --astatus &quot;Up&quot; --ostatus &quot;Up&quot;<br />    lo is Administratively  Up and Operationally Up and running at 10mbs<br />    eth0 is Administratively  Up and Operationally Up and running at 1gbps<br /></pre>
<p><a id="more"></a><a id="more-79"></a></p>
<pre>    python check_int_speed.py --device zenoss --community &quot;public&quot; --astatus &quot;Up&quot; --ostatus &quot;Up&quot; --speed &quot;1gbps&quot;<br />    eth0 is Administratively  Up and Operationally Up and running at 1gbps<br /><br />    python check_int_speed.py --device switch --community &quot;public&quot; --astatus &quot;Down&quot; --ostatus &quot;Down&quot; --pname &quot;GigabitEthernet10/23&quot;<br />    GigabitEthernet10/23 is Administratively Down and Operationally Down and running at 1gbps<br /></pre>
<p></p>
<pre>    python check_int_speed.py --device switch --community &quot;public&quot; --astatus &quot;Up&quot; --ostatus &quot;Up&quot; --speed &quot;1gbps&quot;<br />    GigabitEthernet1/31 is Administratively  Up and Operationally Up and running at 1gbps<br />    GigabitEthernet1/37 is Administratively  Up and Operationally Up and running at 1gbps<br />    GigabitEthernet1/34 is Administratively  Up and Operationally Up and running at 1gbps<br /></pre>
<p></p>
<pre>    python check_int_speed.py --device switch --community &quot;public&quot; --astatus &quot;Down&quot; --ostatus &quot;Down&quot;<br />    GigabitEthernet2/36 is Administratively  Down and Operationally Down and running at 1gbps<br />    Vlan1 is Administratively  Down and Operationally Down and running at 1gbps<br />    GigabitEthernet2/30 is Administratively  Down and Operationally Down and running at 1gbps<br />    GigabitEthernet10/20 is Administratively  Down and Operationally Down and running at 1gbps<br />    GigabitEthernet10/21 is Administratively  Down and Operationally Down and running at 1gbps<br /><br /><p><br />You can download the script here <a href="http://www.linuxdynasty.org/View-details/Python-Scripts/37-Check-Interface-Status-Script.html" title="">check_int_status.py</a><br /></p></pre>
