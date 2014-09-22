---
layout: post
status: publish
published: true
title: How to generate MAC Addresses for XEN
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 70
wordpress_url: http://linuxdynasty.org/?p=70
date: !binary |-
  MjAwOC0wNC0yMyAwMToxODo0NSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNC0yMyAwMToxODo0NSAtMDQwMA==
categories:
- Blog
tags:
- Python HowTo's
- How to generate MAC Addresses for XEN using Python on Linux Fedora Ubuntu Centos
comments: []
---
<pre>#!/usr/bin/env python# Quick Python script to generate random valid MAC address for XEN Domains#Copyright (C) 2008 Allen Sanabria #This program is free software; you can redistribute it and/or modify#it under the terms of the GNU General Public License as published by#the Free Software Foundation; either version 2 of the License, or#(at your option) any later version. #This program is distributed in the hope that it will be useful,#but WITHOUT ANY WARRANTY; without even the implied warranty of#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the#GNU General Public License for more details. #You should have received a copy of the GNU General Public License along#with this program; if not, write to the Free Software Foundation, Inc.,#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.# This address range is reserved for use by Xen 00:16:3E# I'm importing the function choice of the random module# The reason for this is so that it will pick a random character from the string I gave it to generate a valid MAC for XEN</pre>
<pre>from random import choice
from sys import stdin

def x():  
    X = choice("0123456789ABCDEF")  
    return str(X)

print "Enter how many MAC Addresses do you want me to generate: "
mac = stdin.readline()
mac_list = []
for i in range(int(mac)):  
    mac_list.append("00:16:3E"+":"+x()+x()+":"+x()+x()+":"+x()+x())
for con in range(len(mac_list)):  
    while mac_list.count(mac_list[con]) &gt; 1:    
        print "OH NOOO DUPPPE "+mac_list[con]    
    mac_list.pop(con)    
    mac_list.insert(con, "00:16:3E"+":"+x()+x()+":"+x()+x()+":"+x()+x())  
    print mac_list[con]</pre>
<p>&nbsp;</p>
<p><span style="text-decoration: underline;">OUTPUT</span></p>
<div>python random1.py</div>
<div>Enter how many MAC Addresses do you want me to generate:</div>
<div>5</div>
<div>00:16:3E:09:EB:6F</div>
<div>00:16:3E:5E:4B:AE</div>
<div>00:16:3E:E0:EC:F9</div>
<div>00:16:3E:CF:2A:AE</div>
<div>00:16:3E:A9:D8:DB</div>
