---
layout: post
status: publish
published: true
title: Ideas for expanding the current port_report Python Script
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 119
wordpress_url: http://linuxdynasty.org/?p=119
date: !binary |-
  MjAwOS0wNC0xNSAxMjowNzowMiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNC0xNSAxMjowNzowMiAtMDQwMA==
categories: []
tags:
- Dynastys Blog
- Ideas for expanding the current port_report Python Script
comments: []
---
<p>Since I've been working on this script, I see a lot of possibilities. The only draw back so far is that it has only worked on Cisco Switches. Unless other users who have other switches tell me otherwise. One of the features I want to add hopefully this week is to pass the cdp option. So if you run the script like this <strong>port_report.py -d switch -c community -n "1/1"</strong> and in return you get like 20 different MAC addresses. More then likely that port is connected to another switch. Lets say that you run the script again to one of those MAC addresses <strong>port_report.py -d switch -c community -m "00 16 cb b6 ac a3"</strong> and the script as you expected return port 1/1. Now you know that physically that MAC is not connected to that port but a switch is connected to that port and the MAC that you are searching is connected to that switch. So my idea is that if you pass the CDP option, the script will check the cdp snmp table and see if that port is connected to another switch and if so stop scanning the current switch and follow the next switch and find the MAC there.</p>
<p>Also I'm thinking of building a GUI app for this script, which will in return become a program and no longer a script. If you have ideas to add to this, please leave a comment. </p>
