---
layout: post
status: publish
published: true
title: Python and Expect
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 127
wordpress_url: http://linuxdynasty.org/?p=127
date: !binary |-
  MjAwOS0wOS0yNiAyMzoxMToyMiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wOS0yNiAyMzoxMToyMiAtMDQwMA==
categories:
- Python
- Blog
tags:
- Dynastys Blog
- Python
- Python and Expect
- Expect
- Pexpect
comments: []
---
<div>At the current place that I work at, we are trying to figure out, how much we are logging on a daily basis. Since my manager is thinking of purchasing Splunk ( I hope he does ). But before we make that leap and spend that much money ( Those of you who have splunk know exactly what I am talking about ). We need to know how much we are logging now and how much we would be logging after all of our devices are in Splunk.</div>
<p>The current issue is that we have over 400 Cisco Network devices, and they are not all in the Cisco LMS ( Lan Management Solution ). We also have Solarwind, but we do not have all of our Networking devices in there either. There is only one way I know of doing that with out using multiple tools like Cisco LMS or Func. So I figured, I should go ahead and write a Python tool that can update all of our devices ( Cisco, Nortel, Foundry,  Linux, BSD, you get the idea.. ).</p>
<p>I wrote a Python tool that utilizes pexpect. The tools is almost complete to release on my site, but I still need to add more functionality. Currently, you can pass a device list and a command list to the script. You can also tell the tool to be verbose and print the output. Also you can tell it to use ssh or telnet or both. The tool is smart enogh to use ssh keys or log into a device you never have logged into before, by accepting the key for you.</p>
<p>I'm currently modifying it so that you can just pass one device and not just a list of devices. Also working on a password changer function. I've tested my tool on Linux Servers as well as Cisco devices and so far it works like a charm. I'm thinking about adding threading, but I have not yet decided to do so..</p>
<div>I will post this tool either tonight or tomorrow.. I hope you will find this tool as useful as we do.</div>
