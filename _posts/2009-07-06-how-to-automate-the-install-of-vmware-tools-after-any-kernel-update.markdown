---
layout: post
status: publish
published: true
title: How To automate the install of vmware-tools after any kernel update
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 191
wordpress_url: http://linuxdynasty.org/?p=191
date: !binary |-
  MjAwOS0wNy0wNiAxNTowNjozNyAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNy0wNiAxNTowNjozNyAtMDQwMA==
categories: []
tags:
- VMware
- vmware-tools
- kernel update
- How To automate the install of vmware-tools
- vmware-tools not running after kernel update
comments: []
---
<p>The other day I was installing kernel updates on a few of my Red Hat servers and I ran into a minor nuisance.&nbsp; After each reboot, I no longer had network connectivity on the hosts, that has the updated kernel. I then realized, that vmware-tools was not running on all of those hosts. So after a few manual instance of me running &quot;<strong>vmware-tools-config.pl -d</strong>&quot; and &quot;<strong>/etc/init.d/network restart</strong>&quot;....I decided to automate that, by adding the below into &quot;<strong>/etc/rc.local</strong>&quot; </p>
<pre>rkernel=`uname -r`<br />if [ -e /etc/vmware-tools/not_configured ]; then<br />    echo &quot;vmware-tools not configured for running kernel $rkernel&quot;<br />    echo &quot;running vmware-config-tools.pl&quot;<br />    /usr/bin/vmware-config-tools.pl -d<br />    echo &quot;vmware-tools now compiled for running kernel $rkernel&quot;<br />    echo &quot;restarting networking&quot;<br />    /etc/init.d/network restart<br />    echo &quot;network restarted&quot;<br />    exit 0<br />fi<br />&nbsp;</pre>
<p>&nbsp;After each host rebooted, I now had network connectivity and vmware-tools was running. I hope the above will save you some time. </p>
