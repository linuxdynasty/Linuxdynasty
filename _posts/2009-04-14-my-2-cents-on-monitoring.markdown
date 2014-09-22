---
layout: post
status: publish
published: true
title: My 2 cents on Monitoring..
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 117
wordpress_url: http://linuxdynasty.org/?p=117
date: !binary |-
  MjAwOS0wNC0xNCAwMDoyNjo0NiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNC0xNCAwMDoyNjo0NiAtMDQwMA==
categories: []
tags:
- Dynastys Blog
- My 2 cents on Monitoring..
comments: []
---
<p>My 2 cents on Monitoring... I'm a huge advocate of Monitoring properly... And what I mean by that is monitoring every aspect of your Production environment that means anything to your environment. </p>
<p>Now to break it down even further.... Besides monitoring the basics like DiskIO, Memory, CPU, Dropped Packets, Error in the interfaces.. Monitoring of all the services you are running, either through snmp, scripts, api's, etc.. Also which to me is very important is the monitoring of the log files ( This has saved us a tremendous amount of time ). I've been using Zenoss for the past 2 years and I can not say how much that product has help the companies I worked for and not to mention the time it has saved. </p>
<p>I had Zenoss as the central syslog server, snmpd trap server, monitoring, and trending . You can raise email alerts based on the logs that come in and correlate those events with other alerts from the system.If you prefer not to use a system like zenoss for your central logging then use a system like splunk which to me is the best central syslogging system hands down. then create custom alerting rules based on the criteria you passed and then have it email out or send the alert to a monitoring system like zenoss.</p>
<p>Also, I have met quite a few admins who feel that monitoring is something you can setup once in about a weeks time and let it do its job. I on the other hand feel the complete opposite. I feel that monitoring is a ongoing process and  takes a minimum of 3 months to setup properly. This is the time it takes to research every part of the environment and to properly adjust the values of what you are monitoring, so you do not get email/page bombed.. </p>
<p>I know quite a few of you have received those email bombs before.</p>
<p>For me to be completely satisfied with the monitoring that I put in play. A few things has to be done 1st</p>
<ul>
<li>Work with anyone that is involve with a Production Server/App/Device and find as much as possible about those Services/Devices</li>
<li>Setup a central syslogging system like Splunk that can send alerts based on what ever criteria you set or use a system like Zenoss which you can map alerts to different events. You may not belive me but there is a wealth of important information, that can speedly help you find a issue with a device.</li>
<li>Trending of the systems/devices/services that you are monitoring. So use a system like Cacti or dare I say it... Zenoss</li>
<li>And the most import part... Choose your monitoring tool carefully... Again my personal opinion is to use to most flexible monitoring tool out there. A tool that can use snmp, nagios commands, custom API Scripting, and the ability to automate as much of the monitoring as possible.... Like Zenoss!!! </li>
<li>Time, TIme, Time....Proper monitoring takes alot of research and testing.... But the rewards are 10 fold... </li>
</ul>
<p>No I'm not a Zenoss Sales rep and no I do not work for them. But their product to me as a Systems Engineer is that amazing... I can grab data from a cmdb and pass it to zenoss or grab data from syslog or from splunk or in that fact VMware. I can even automate the grouping in Zenoss..  </p>
<p>Basically when it comes down to it, DO YOUR RESEARCH.... </p></p>
<p> </p>
