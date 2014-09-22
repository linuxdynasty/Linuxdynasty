---
layout: post
status: publish
published: true
title: How to mount an ISO image under Linux
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p><span>Another quick and dirty HowTo, this time we are showing you how
  to mount an ISO image under Linux. If you are just getting into Linux you will see
  that you will have to do this quite often as a Linux Admin/Engineer. In the example
  below I will use a CentOS ISO Image as an example.<br />\r\n</span></p>\r\n<br />"
wordpress_id: 35
wordpress_url: http://linuxdynasty.org/?p=35
date: !binary |-
  MjAwOC0wOC0xMyAxODozODozMSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wOC0xMyAxODozODozMSAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- How to mount an ISO image under Linux
comments: []
---
<p><span>Another quick and dirty HowTo, this time we are showing you how to mount an ISO image under Linux. If you are just getting into Linux you will see that you will have to do this quite often as a Linux Admin/Engineer. In the example below I will use a CentOS ISO Image as an example.<br />
</span></p>
<p><a id="more"></a><a id="more-35"></a></p>
<ol>
<li>
<p><span>Make sure you are root or have root privileges.. Example { &quot;<font color="#0000ff"><strong>su -</strong></font>&quot; or &quot;<font color="#0000ff"><strong>sudo su -</strong></font>&quot; }</span></p>
</li>
<li>Make the directory where you want to mount the image to.. Example { &quot;<font color="#0000ff"><strong>mkdir</strong></font> <font color="#ff0000"><strong>/mnt/Centos5_2</strong></font>&quot; }
<p><span></span></p>
</li>
<li>
<p><span>Mount the image under the directory you created under the previous step.. Example { &quot;<strong><font color="#0000ff">mount -o loop</font> CentOS-5.2-i386-netinstall.iso <font color="#ff0000">/mnt/Centos5_2/</font></strong>&quot; }</span></p>
</li>
<li><span>Now you can verify that the ISO image is mounted under&nbsp; </span><span><strong><font color="#ff0000">/mnt/Centos5_2/</font></strong>... Example { &quot;<font color="#0000ff"><strong>df -h&quot;</strong></font> or &quot;<font color="#0000ff"><strong>ls</strong></font> </span><span><strong><font color="#ff0000">/mnt/Centos5_2/</font></strong></span><span>&quot; or &quot;<font color="#0000ff"><strong>cd</strong></font> </span><span><strong><font color="#ff0000">/mnt/Centos5_2/</font></strong></span><span>&quot; }</span></li>
</ol>
<p><span>So here is the syntax with out the explanation...</span></p>
<ol>
<li><span>&quot;<font color="#0000ff"><strong>su -</strong></font>&quot; or &quot;<font color="#0000ff"><strong>sudo su -</strong></font>&quot; </span></li>
<li><span></span><span> </span>&quot;<font color="#0000ff"><strong>mkdir</strong></font> <font color="#ff0000"><strong>/mnt/Centos5_2</strong></font>&quot; </li>
<li><span>&quot;<strong><font color="#0000ff">mount -o loop</font> CentOS-5.2-i386-netinstall.iso <font color="#ff0000">/mnt/Centos5_2/</font></strong>&quot;</span></li>
<li><span>&quot;<font color="#0000ff"><strong>df -h&quot;</strong></font> or &quot;<font color="#0000ff"><strong>ls</strong></font> </span><span><strong><font color="#ff0000">/mnt/Centos5_2/</font></strong></span><span>&quot; or &quot;<font color="#0000ff"><strong>cd</strong></font> </span><span><strong><font color="#ff0000">/mnt/Centos5_2/</font></strong></span><span> and then run a &quot;<font color="#0000ff"><strong>ls</strong></font>&quot; &quot;</span></li>
</ol>
