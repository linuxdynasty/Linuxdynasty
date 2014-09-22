---
layout: post
status: publish
published: true
title: How to store encrypted passwords in MySQL
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 9
wordpress_url: http://linuxdynasty.org/?p=9
date: !binary |-
  MjAwOC0wMi0xMCAwNToxNjo0MSAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAwNToxNjo0MSAtMDUwMA==
categories: []
tags:
- MySQL HowTo's
- MySQL Encryption HowTo Store
comments: []
---
<p><strong>Mysql storing encrypted passwords howto, All these commands were tested on MySQL5</strong></p>
<ol>
<li>
<ul>
<span style="color: #ff0000;"><strong>This example we will create a MD5 encrypted password</strong></span></p>
<li>We need to create a table called user_md5, (The value is returned as a binary string of 32 hex digits)<span style="color: #0000ff;"><br /><strong>"CREATE TABLE user_md5 (user_name VARCHAR(16), password VARCHAR(32));"</strong></span><br />Query OK, 0 rows affected (0.10 sec)</li>
<li>Now we need to insert a user into the table<span style="color: #0000ff;"><br /><strong>"INSERT INTO user_md5 VALUES ('test',MD5('test') );"</strong></span><br />Query OK, 1 row affected (0.00 sec)</li>
<li>Now lets see if we query the user with the unencrypted password will it work<span style="color: #0000ff;"><br /><strong>"SELECT * FROM user_md5 where user_name = 'test' AND password=MD5('test');"</strong></span></li>
<pre><br />+-----------+----------------------------------+<br />| user_name | password                         |<br />+-----------+----------------------------------+<br />| test      | 098f6bcd4621d373cade4e832627b4f6 | <br />+-----------+----------------------------------+<br />1 row in set (0.00 sec)<br /></pre>
</ul>
<p> </p>
</li>
<li>
<ul>
<span style="color: #ff0000;"><strong>This example we will create a SHA1 encrypted password</strong></span></p>
<li>We need to create a table called user_sha1 ((Secure Hash Algorithm). The value is returned as a binary string of 40 hex digits)<span style="color: #0000ff;"><br /><strong>"CREATE TABLE user_sha1 (user_name VARCHAR(16), password VARCHAR(40));"</strong></span><br />Query OK, 0 rows affected (0.10 sec)</li>
<li>Now we need to insert a user into the table<span style="color: #0000ff;"><br /><strong>"INSERT INTO user_sha1 VALUES ('test',SHA1('test') );"</strong></span><br />Query OK, 1 row affected (0.00 sec)</li>
<li>Now lets see if we query the user with the unencrypted password will it work<span style="color: #0000ff;"><br /><strong>"SELECT * FROM user_sha1 where user_name = 'test' AND</strong> password=SHA1('test');"</span></li>
<pre><br />+-----------+------------------------------------------+<br />| user_name | password                                 |<br />+-----------+------------------------------------------+<br />| test      | a94a8fe5ccb19ba61c4c0873d391e987982fbbd3 | <br />+-----------+------------------------------------------+<br />1 row in set (0.00 sec)<br /></pre>
</ul>
<p> </p>
<p> </p>
</li>
<li>
<ul>
<span style="color: #ff0000;"><strong>This example we will create a AES encrypted password</strong></span></p>
<p> </p>
<li>We need to create a table called user_aes, ((Advanced Encryption Standard) encryption, you will need to specify the password field to be of type BLOB)<span style="color: #0000ff;"><br /><strong>"CREATE TABLE user_aes (user_name VARCHAR(16), password BLOB);"</strong></span><br />Query OK, 0 rows affected (0.10 sec)</li>
<li>Now we need to insert a user into the table<span style="color: #0000ff;"><br /><strong>"INSERT INTO user_aes VALUES('test', AES_ENCRYPT('password', 'key') );"</strong></span><br />Query OK, 1 row affected (0.00 sec)</li>
<li>Now lets see the results<span style="color: #0000ff;"><br /><strong>"SELECT * FROM user_aes WHERE user_name='test' AND</strong> password=AES_ENCRYPT('password','key');"</span></li>
<pre><br />+-----------+------------------+<br />| user_name | password         |<br />+-----------+------------------+<br />| test      | ��}��� ���n�<br />                          &lt;-� | <br />+-----------+------------------+<br />1 row in set (0.00 sec)<br /></pre>
<p> </p>
<li>AES provides reversible encryption (provided you have the key), we can obtain the password in plain text format./ </li>
<li><br type="_moz" /></li>
<li>Now lets see the unecrypted password<br /><b><span style="color: #0000ff;">"SELECT AES_DECRYPT(password,'key') FROM user_aes;"</span></b></li>
<pre><br />+-----------------------------+<br />| AES_DECRYPT(password,'key') |<br />+-----------------------------+<br />| password                    | <br />+-----------------------------+<br />1 row in set (0.00 sec)<br /></pre>
</ul>
</li>
</ol>
<p><a href="http://dev.mysql.com/doc/refman/4.1/en/encryption-functions.html"><br />For further info on encryption in MySQL</a></p>
