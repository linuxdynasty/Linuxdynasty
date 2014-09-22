---
layout: post
status: publish
published: true
title: Port Report Update 1.6
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 122
wordpress_url: http://linuxdynasty.org/?p=122
date: !binary |-
  MjAwOS0wNC0yNCAxODo0MDo1NiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNC0yNCAxODo0MDo1NiAtMDQwMA==
categories: []
tags:
- Dynastys Blog
- Cisco
- Find
- Port
- Mac
- IP
comments: []
---
<p>Let me make this one thing clear about port_report.py and one limitation it has when searching for IP Addresses on a switch ( not really a limitation of the script ). When searching by IP address, the IP Address has to be in the ARP table, if the IP is not in the ARP table then the script will report that the IP Address is not in the ARP table. I know I sound redundant but I have been asked this question alot. The better thing to do is to search by MAC Address as this is more then likely to be on the switch. That is all depending on how often the table gets clean.</p>
<p>Currently, the newest revision, is revision 1.6. <br /> New additions to this revision ....</p>
<ul>
<li>Support for HP Procurve Switches, ( Tested on the newer versions of HP )</li>
<li>combined switch_report.py in port_report.py.</li>
<li>Added --verbose flag</li>
</ul>
<p>Previous Releases....</p>
<ul>
<li>All Cisco Switches supported...</li>
<li>Search by MAC or IP or PORT </li>
</ul>
<div>You can get the newest revision Here ... <a href="View-details/Python-Scripts/39-port_report.py.html">http://www.linuxdynasty.org/View-details/Python-Scripts/39-port_report.py.html</a><br />{quickdown:39}</div>
