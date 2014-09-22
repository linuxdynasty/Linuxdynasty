---
layout: post
status: publish
published: true
title: Discovered Zenoss Devices
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 192
wordpress_url: http://linuxdynasty.org/?p=192
date: !binary |-
  MjAwOC0wNC0yNiAwNDoyNToxNyAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNC0yNiAwNDoyNToxNyAtMDQwMA==
categories:
- Zenoss
tags:
- Zenoss
- Discovered Zenoss Devices Python Zenoss Scripting Python howto
comments: []
---
<h3><strong>For those Zenoss users out there, this script will send a emailof devices that are in the discovered class.</strong></h3>
<h3><strong>So once you receive this email you will know that you need to move those devices into there appropriate classes.</strong></h3>
<pre><br />#!/bin/env python<br /><span>#Copyright (C) 2008  Allen Sanabria<br /><br />#This program is free software; you can redistribute it and/or modify<br />#it under the terms of the GNU General Public License as published by<br />#the Free Software Foundation; either version 2 of the License, or<br />#(at your option) any later version.<br /><br />#This program is distributed in the hope that it will be useful,<br />#but WITHOUT ANY WARRANTY; without even the implied warranty of<br />#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the<br />#GNU General Public License for more details.<br /><br />#You should have received a copy of the GNU General Public License along<br />#with this program; if not, write to the Free Software Foundation, Inc.,<br />#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.</span><br />##############################################################<br />#Created by Allen Sanabria aka LinuxDynasty aka PrNino69<br />#This script is to check how many devices are in the<br />#Discovered Class<br />#Started Nov 28th<br />#Completed, Nov 28th<br />##############################################################<br /><br />import os, sys<br />from re import sub<br />from string import split<br />from string import join<br />from urllib import urlopen<br />from smtplib import SMTP<br />from time import sleep<br /><br /><br />user = &quot;zenoss&quot;<br />passwd = 'zenoss'<br />util = '@zenoss'<br />base = &quot;http://%s:%s%s:8080&quot; % (user,passwd,util)<br />discovered_url = urlopen(base+'/zport/dmd/Devices/Discovered/getSubDevices').read()<br />discovered_sub = sub(&quot;&lt;Device at /zport/dmd/Devices/Discovered/devices/|&gt;|^[|]$|,&quot;, &quot;&quot;, discovered_url)<br />discovered_list = list(split(discovered_sub))<br /><br /><br />message = &quot;&quot;&quot;nThe boxes below were discovered in the last run of zendisc.nThey are all located under /Devices/Discovered Class.n<br />                     Please move Devices to appropriate Device class, if one does not exist please create one.n<br />                     This script runs on the zenoss (cc17-22) server.&quot;&quot;&quot;<br />devices = sub(&quot;,|[|]&quot;, &quot;n&quot;, str(discovered_list))<br />BODY = join((message, devices),&quot;n&quot;)<br />print BODY<br />FROM = &quot;zenoss@linuxdynasty.org&quot;<br />TO = &quot;sa@linuxdynasty.org&quot;<br />SUBJECT = &quot;Devices That Were Discovered During The Network Scan!&quot;<br />body = join((&quot;From: %s&quot; % FROM, &quot;To: %s&quot; % TO, &quot;Subject: %s&quot; % SUBJECT, &quot;&quot;, BODY), &quot;n&quot;)<br />server = SMTP('localhost')<br />server.set_debuglevel(1)<br />server.sendmail(FROM, [TO], body)<br />sleep(10)<br />server.quit()<br /></pre>
