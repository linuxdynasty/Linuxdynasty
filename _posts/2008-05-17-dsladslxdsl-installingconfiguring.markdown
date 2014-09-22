---
layout: post
status: publish
published: true
title: DSL/ADSL/XDSL - Installing/Configuring
author:
  display_name: tinkpen
  login: tinkpen
  email: tinkpen@sympatico.ca
  url: ''
author_login: tinkpen
author_email: tinkpen@sympatico.ca
wordpress_id: 62
wordpress_url: http://linuxdynasty.org/?p=62
date: !binary |-
  MjAwOC0wNS0xNyAxNDo0NDo0NyAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0xNyAxNDo0NDo0NyAtMDQwMA==
categories: []
tags:
- Linux Networking HowTo's
- DSL HowTo ADSL HowTo XDSL HowTo on Fedora CentOS RedHat
comments: []
---
<p><font size="3"><strong>To Install/Configure DSL/ADSL On RedHat/Centos Linux</strong>:&nbsp;</font></p>
<p>&nbsp;</p>
<ol style="margin-top: 0cm" start="1" type="1">
<li class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">Check to see if <strong>pppoe</strong> is installed<br />
<strong>rpm –qa | grep rp-pppoe<br />
</strong>if not then:<br />
<strong>yum install rp-pppoe<br />
<o:p></o:p></strong></span></li>
<li class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">After the install, run<span>&nbsp; </span><strong>adsl-setup</strong><br />
     and input your settings<br />
<o:p></o:p></span></li>
<li class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">/sbin/ifup ppp0</span></strong><span style="font-size: 12pt" lang="EN-US"><br />
     or <strong>adsl-start</strong><br />
<o:p></o:p></span></li>
<li class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">To stop your connection: <strong>adsl-stop</strong><br />
<o:p></o:p></span></li>
<li class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">To check the connection’s status: <strong>adsl-status</strong><br />
<o:p></o:p></span></li>
</ol>
<p>&nbsp;</p>
