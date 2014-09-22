---
layout: post
status: publish
published: true
title: Using netstat to find active network connections
author:
  display_name: admin
  login: admin
  email: admin@linuxdynasty.org
  url: ''
author_login: admin
author_email: admin@linuxdynasty.org
wordpress_id: 25
wordpress_url: http://linuxdynasty.org/?p=25
date: !binary |-
  MjAwOC0wNS0yNCAxMDoyMTozNSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0yNCAxMDoyMTozNSAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- How to use netstat
comments: []
---
<p>To list all open network ports on your machine, run <strong>netstat -lnptu</strong>. Here is a breakdown of the parameters:</p>
<p><strong>l</strong> - List all listening ports<br />
<strong>n</strong> - Display the numeric IP addresses (i.e., don't do reverse DNS lookups)<br />
<strong>p</strong> - List the process name that is attached to that port<br />
<strong>t</strong> - List all TCP connections<br />
<strong>u</strong> - List all UDP connections</p>
<p>&nbsp;</p>
<p><img alt="" title="" src="http://core.dexxtreme.com/temp/netstat-l.png" width="750" height="460" />&nbsp;</p>
<p>In this example, there are a number of open ports. For example, you can see: </p>
<p>print server (lpd on port 515)<br />
 rsync server (rsyncd on port 873)<br />
database server (mysqld on localhost port 3306)<br />
web server (httpd on port 80)<br />
dns server&nbsp; (named on port 53)<br />
openssh (sshd on port 22)<br />
syslog (syslog-ng on port 514)<br />
snmp (snmpd on port 161) <br />
dhcp server (dhcpd on port 67)<br />
tftp server (in.tftpd on port 69)<br />
time server (ntpd on port 123)<br />
several services related to importing an NFS filesystem</p>
<p>You can also change the &quot;<strong>l</strong>&quot; to an &quot;<strong>a</strong>&quot; to list both listening and active ports. </p>
<p><img alt="" title="" src="http://core.dexxtreme.com/temp/netstat-a.png" width="750" height="530" />&nbsp;</p>
<p>You can also use netstat to show the current routing table by running&nbsp; <strong>netstat -rn</strong>:</p>
<p><img alt="" title="" src="http://core.dexxtreme.com/temp/netstat-r.png" width="750" height="105" /><br />
&nbsp;</p>
