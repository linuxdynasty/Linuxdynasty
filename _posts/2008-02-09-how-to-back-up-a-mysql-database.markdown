---
layout: post
status: publish
published: true
title: How to Back up a MySQL database
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 5
wordpress_url: http://linuxdynasty.org/?p=5
date: !binary |-
  MjAwOC0wMi0wOSAxODoyOTozMSAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0wOSAxODoyOTozMSAtMDUwMA==
categories: []
tags:
- MySQL HowTo's
- How to Back up a MySQL database
comments: []
---
<p><strong><span style="color: red">If you've got a website with a database or a custom database running for your applications, it is imperative that you make regular backups of the database...</span></strong></p>
<p>
 <strong>Following examples are using <span style="color: blue">mysqldump</span></strong> </p>
<ol>
<li>
<ul>
You can use mysqldump to create a simple backup of your database. Here is an example..<strong><span style="color: blue">mysqldump -u username --password=password databasename &gt; backup.sql</span></strong></p>
<li><strong>username </strong>- this is your database username<strong> </strong></li>
<li><strong>password </strong>- this is the password for your database<strong> </strong></li>
<li><strong>databasename </strong>- the name of your database<strong> </strong></li>
<li><strong>backupfile.sql </strong>- the file to which the backup should be written. </li>
</ul>
</li>
<p></p>
<li>
<ul>
To backup multiple databases, you will have to do the following example.   </p>
<li><strong><span style="color: blue">mysqldump -u test1 --password=pass1 --databases world universe &gt;world_and_universe.sql</span></strong> </li>
</ul>
</li>
<p></p>
<li>
<ul>
Now what if we want to back up all of our databases. To do that follow the next example.</p>
<li><strong><span style="color: blue">mysqldump -u test1 --password=pass1 --all-databases &gt;alldb.sql</span></strong> </li>
</ul>
</li>
<p></p>
<li>
<ul>
Here we are going to show you another way of backing up a databases and certain tables using the --add-drop-table. This essentially adds a drop table statement before every create statement. The purpose of this is so that it will remove any previous copies of the table before recreating it.</p>
<li>This example will add a drop statement before every create statement.<strong><br />
<span style="color: blue">mysqldump --add-drop-table -u test1 --password=pass1 world &gt; world.sql</span></strong> </li>
<li>This statement will add a drop statement before the following tables only.<strong><br />
<span style="color: blue">mysqldump --add-drop-table -u test1 --password=pass1 Customers world_users world_passwd&gt; world.sql</span></strong> </li>
</ul>
</li>
</ol>
