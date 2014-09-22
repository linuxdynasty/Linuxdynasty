---
layout: post
status: publish
published: true
title: SSH Blocking How To using Iptables
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 61
wordpress_url: http://linuxdynasty.org/?p=61
date: !binary |-
  MjAwOC0wMi0xMCAyMzo1NToxOCAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAyMzo1NToxOCAtMDUwMA==
categories: []
tags:
- Linux Networking HowTo's
- SSH Blocking How To using Iptables How To Block ssh using iptables
comments: []
---
<p><strong><span style="color: red">This quick how to is for those linux admin/users who have there Linux server accessible to the outside world.</span></strong></p>
<p><strong><span style="color: red">Don't you hate when those bots start hitting you with a ssh dictionary attack??? Well block using IPTABLES.</span></strong></p>
<ol>
<li>
<ul><strong>Here I will show you how to add the first rule in iptables...</strong></p>
<li>The 1st rule we add is where we tell iptables to create a list called ssh_attempt and store the source ip of every recent ssh attempt on port 22 using tcp on interface eth0. </li>
<li><span style="color: blue">&quot;<strong>iptables -A INPUT -i eth0 -p tcp -m tcp --dport 22 -m state --state NEW -m recent --set --name ssh_attempt --rsource</strong>&quot;</span>
</li>
<li>step by step explanation.. </li>
<li>iptables is the command that you use to enter the firewall rules in. </li>
<li>&quot;<strong><span style="color: blue">-A INPUT</span></strong>&quot; means APPEND to the INPUT chain </li>
<li>&quot;<strong><span style="color: blue">-i eth0</span></strong>&quot; means this rule will use the interface eth0 </li>
<li>&quot;<strong><span style="color: blue">-p tcp</span></strong>&quot; means we are using the TCP protocol </li>
<li>&quot;<strong><span style="color: blue">-m tcp</span></strong>&quot; means we are matching the TCP protocol </li>
<li>&quot;<strong><span style="color: blue">--dport 22</span></strong>&quot; means we are matching based on the destination port 22 </li>
<li>&quot;<strong><span style="color: blue">-m state --state NEW</span></strong>&quot; This rule will only apply to NEW incoming ssh connections not ESTABLISHED or RELATED. </li>
<li>&quot;<strong><span style="color: blue">-m recent --set --name ssh_attempt --rsource</span></strong>&quot; allows us to match packets based on recent events that we have previously matched and sets the name of the list , while saving the source ip address and port. </li>
</ul>
</li>
<li>
<ul><strong>In this step we will show you how to deny those bots..</strong></p>
<li><span style="color: blue">&quot;<strong>iptables -A INPUT -i eth0 -p tcp -m tcp --dport 22 -m state --state NEW -m recent --update --seconds 10 --hitcount 2 --name ssh_attempt --rsource -j DROP</strong>&quot;</span></li>
<li>The only difference in this rule is these options. </li>
<li>&quot;<strong><span style="color: blue">--update --seconds 10 --hitcount 1 --name ssh_attempt</span></strong>&quot; This will match true if the source is available in the specified list and it also updates the last-seen time in the list. The &quot;<strong><span style="color: blue">--seconds 10</span></strong>&quot; match is used to specify how long since the &quot;last seen&quot;. The &quot;<strong><span style="color: blue">--hitcount 2</span></strong>&quot; will limit the match to only include packets that have seen at least the hitcount amount of packets.</li>
</ul>
</li>
</ol>
