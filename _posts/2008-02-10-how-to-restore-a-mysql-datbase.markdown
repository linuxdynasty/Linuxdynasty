---
layout: post
status: publish
published: true
title: How to restore a MySQL Database
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 6
wordpress_url: http://linuxdynasty.org/?p=6
date: !binary |-
  MjAwOC0wMi0xMCAwNDo1ODoxOSAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAwNDo1ODoxOSAtMDUwMA==
categories: []
tags:
- MySQL HowTo's
- How to restore a MySQL Database in Linux Fedora ubuntu Gentoo Windows
comments: []
---
<p><strong><span style="color: red">Now that you know how to backup your database,I will show you how to restore it on another database.</span></strong> </p>
<ol>
<li>
<ul>
The most common and basic way to restore, is a restore of a database.</p>
<li><span style="color: blue"><strong>mysql -u test1 --password=pass1 world &lt; world.sql</strong></span></li>
</ul>
<p><span style="color: blue"><strong><br />
</strong></span> </li>
<li>
<ul>
How about restoring your database to another database over the network with out logging into that box...</p>
<li><strong><span style="color: blue">mysqldump -u test1 --password=pass1 world | mysql --host=170.20.10.32 -C world</span></strong></li>
</ul>
</li>
</ol>
