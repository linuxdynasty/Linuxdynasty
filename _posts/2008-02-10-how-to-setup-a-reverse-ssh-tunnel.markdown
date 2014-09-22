---
layout: post
status: publish
published: true
title: How to setup a reverse ssh tunnel
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 12
wordpress_url: http://linuxdynasty.org/?p=12
date: !binary |-
  MjAwOC0wMi0xMCAwNTozMDozNSAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAwNTozMDozNSAtMDUwMA==
categories: []
tags:
- Advance Linux HowTo's
- How to setup a reverse ssh tunnel on Linux Fedora ubuntu Gentoo
comments: []
---
<p><strong><span style="color: rgb(255, 0, 0)">Ever wanted to know how you can ssh into your work desktop/server? Well do not worry any longer.....</span></strong></p>
<ol>
<li>
<ul>
All you need to do is create a reverse tunnel from your Work Desktop/Server to your home server.<br />
<strong><br />
</strong></p>
<li><strong><span style="color: rgb(0, 0, 255)">ssh -nNT -R 5000:local_server:22 username@remote_server</span></strong> </li>
<li>Now from the <strong><span style="color: rgb(0, 0, 255)">remote_server</span></strong> run this<br />
<strong><span style="color: rgb(0, 0, 255)">ssh -p5000 localhost</span></strong>.... now we are in our work desktop/server. </li>
</ul>
</li>
<li>
<ul><strong>Lets brake this down a bit..</strong></p>
<li>The <strong><span style="color: rgb(0, 0, 255)">-n</span></strong> option Redirects stdin from /dev/null. This must be used when ssh is run in the background. </li>
<li>The <strong><span style="color: rgb(0, 0, 255)">-N</span></strong> option does not execute a remote command. This is useful for just forwarding ports. </li>
<li>The <strong><span style="color: rgb(0, 0, 255)">-T</span></strong> option disables pseudo-tty allocation. </li>
<li>The <strong><span style="color: rgb(0, 0, 255)">-R</span></strong> option does tha job of setting up the reverse tunnel. </li>
<li>Port <strong><span style="color: rgb(0, 0, 255)">5000</span></strong> is the port that will be listening on the remote_server (this can be any random port over 1024, if you want to run this as a non-root user). </li>
<li><strong><span style="color: rgb(0, 0, 255)">local_server</span></strong> is the desktop/server that you are creating the connection from. </li>
<li>Port <strong><span style="color: rgb(0, 0, 255)">22</span></strong> is the port that you are making the ssh connection to. </li>
<li><strong><span style="color: rgb(0, 0, 255)">user_name@remote_server</span></strong> is where you are making the ssh connection to for the reverse tunnel. </li>
</ul>
</li>
<li>
<ul><strong>We need to make sure we keep this connection open</strong>.</p>
<li>In <strong><span style="color: rgb(0, 0, 255)">/etc/ssh/sshd_config</span></strong> we need to make sure this is set <strong><span style="color: rgb(0, 0, 255)">TCPKeepAlive yes</span></strong>. </li>
</ul>
</li>
</ol>
