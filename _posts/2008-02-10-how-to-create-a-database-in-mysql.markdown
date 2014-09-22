---
layout: post
status: publish
published: true
title: How to create a database in MySQL
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 7
wordpress_url: http://linuxdynasty.org/?p=7
date: !binary |-
  MjAwOC0wMi0xMCAwNTowMjo0OCAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAwNTowMjo0OCAtMDUwMA==
categories: []
tags:
- MySQL HowTo's
- How to create a database in MySQL on Linux Windows Fedora ubuntu Gentoo
comments: []
---
<p><span style="color: red">How to create a database?</span></p>
<ol>
<li> By default mysql installs as the root user with no passwd (unless noted otherwise)
<ul>
<li> Verify that mysql is running by one way (out of many ways). This is the command....<strong><br />
<span style="color: blue">&quot;ps -fe |grep mysqld |grep -v grep&quot;</span></strong>The output should be similiar to this... /(usr/libexec/mysqld --defaults-file=/etc/my.cnf --basedir=/usr --datadir=/var/lib/mysql --user=mysql --pid-file=/var/run/mysqld/mysqld.pid --skip-locking --socket=/var/lib/mysql/mysql.sock)</li>
</ul>
</li>
<li>Once you verified that mysql is running, log in to mysql using this command
<ul>
<li>Run this command...<strong><br />
<span style="color: blue">&quot;mysql&quot;</span>.</strong>... (This should suffice unless your installation of mysql required a username and password) </li>
<li>The output should be similar to this..
<pre><br />Welcome to the MySQL monitor.  Commands end with ; or g.<br />Your MySQL connection id is 24365 to server version: 4.1.20<br /><br />Type 'help;' or 'h' for help. Type 'c' to clear the buffer.<br /><br />mysql&gt; <br /></pre>
</li>
</ul>
</li>
<li>Run this command..
<ul>
<li><strong><span style="color: blue">&quot;Create database TEST;&quot;</span></strong>....Output should look like this...
<pre><br />       Query OK, 1 row affected (0.02 sec)<br /></pre>
</li>
</ul>
</li>
</ol>
<p><strong>Now for the all in one Feature......</strong></p>
<pre><br />[root@s15261720 wiki]# ps -e |grep mysqld<br /> 7209 ?        00:00:00 mysqld_safe<br /> 7242 ?        00:00:12 mysqld<br /><br /># mysql  <br />Enter password: <br />Welcome to the MySQL monitor.  Commands end with ; or g.<br />Your MySQL connection id is 24415 to server version: 4.1.20<br /><br />Type 'help;' or 'h' for help. Type 'c' to clear the buffer.<br /><br />mysql&gt; <br /><br />mysql&gt; create database test;<br />Query OK, 1 row affected (0.00 sec)<br /><br />mysql&gt;<br /></pre>
