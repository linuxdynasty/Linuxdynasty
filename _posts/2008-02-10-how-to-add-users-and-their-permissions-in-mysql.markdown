---
layout: post
status: publish
published: true
title: How to add users and their permissions in MySQL
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 8
wordpress_url: http://linuxdynasty.org/?p=8
date: !binary |-
  MjAwOC0wMi0xMCAwNToxMTowOSAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAwNToxMTowOSAtMDUwMA==
categories: []
tags:
- MySQL HowTo's
- MySQL User Permissions HowTo
comments: []
---
<p><strong><span style="color: red">Mysql user howto, All these commands were tested on MySQL5</span></strong></p>
<ol>
<li>How to add a user.
<ul>
<li> I am using the user test as a example as well as the host localhost as an example...<strong><br />
<span style="color: blue">&quot;CREATE USER 'test'@'localhost' IDENTIFIED BY 'passwd';&quot;</span></strong> </li>
</ul>
</li>
<li>How to change a users password
<ul>
<li><strong><span style="color: blue">&quot;SET PASSWORD FOR 'test'@'localhost' = PASSWORD('passwd');&quot;</span></strong> </li>
</ul>
</li>
<li>How to delete a user<strong><br />
</strong></p>
<ul>
<li><strong><span style="color: blue">&quot;DROP USER 'test'@'localhost';&quot;</span></strong> </li>
</ul>
</li>
<li>How to rename a users account
<ul>
<li><strong><span style="color: blue">&quot;RENAME USER 'test'@'localhost' TO 'test1'@'localhost';&quot;</span></strong> </li>
</ul>
</li>
<li>How to grant different permissions to users
<ul>
<li>This statement give the SELECT(query) access to the user test on all databases on localhost... <br />
<strong><span style="color: blue">&quot;GRANT SELECT on *.* TO 'test'@'localhost' IDENTIFIED BY 'passwd';&quot;</span></strong> </li>
<li>This statement gives the test user super user privileges on all databases on localhost to user test.... <br />
<strong><span style="color: blue">&quot;GRANT ALL PRIVILEGES on *.* TO 'test'@'localhost' IDENTIFIED BY 'passwd';&quot;</span></strong> </li>
</ul>
</li>
</ol>
