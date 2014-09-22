---
layout: post
status: publish
published: true
title: How to mount an ISO image under Solaris or OpenSolaris
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>Whats up guys here is another quick and simple, yet necessary HowTo...&nbsp;
  Since as most of you know, I come from a Linux background and mounting an ISO image
  under linux is as simple as .... Ok, follow the link HAHAHAHA <a href=\"http://www.linuxdynasty.org/how-to-mount-an-iso-image-under-linux.html\"
  title=\"\">http://www.linuxdynasty.org/how-to-mount-an-iso-image-under-linux.html</a>.</p>\r\n<br
  />"
wordpress_id: 201
wordpress_url: http://linuxdynasty.org/?p=201
date: !binary |-
  MjAwOC0wOC0xMyAxODo1OTo0NCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wOC0xMyAxODo1OTo0NCAtMDQwMA==
categories: []
tags:
- Beginner OpenSolaris HowTo's
- How to mount an ISO image under Solaris or OpenSolaris
comments: []
---
<p>Whats up guys here is another quick and simple, yet necessary HowTo...&nbsp; Since as most of you know, I come from a Linux background and mounting an ISO image under linux is as simple as .... Ok, follow the link HAHAHAHA <a href="http://www.linuxdynasty.org/how-to-mount-an-iso-image-under-linux.html" title="">http://www.linuxdynasty.org/how-to-mount-an-iso-image-under-linux.html</a>.</p>
<p><a id="more"></a><a id="more-201"></a></p>
<p>For me it feels like Solaris tries to make our lives a tad bit more complicated then it needs to be by adding another step to mount an iso image and ahemm quite a few other things as well which I will not get into right now... </p>
<p>So in order to mount an ISO image under Solaris you will need to use the lofiadm command. The lofiadm command adminsters the loopback file driver aka <strong>lofi</strong>. lofi allows a file ( in this case an ISO image ) to be associated with a block device. That file then can be accessed though the block device ( such as a disk ).</p>
<p></p>
<ol>
<li>
<p><span>Here we use lofiadm to associate the file to a block device.. Example { &quot;<strong><font color="#0000ff">lofiadmin -a</font> <font color="#ff0000">/var/tmp/sol-nv-b95-x86-dvd.iso</font>&quot; </strong>}<br />
By default Solaris will use the next available block device, Example of the output of lofiadm { <font color="#ff0000"><strong>/dev/lofi/1</strong></font></span> }</p>
</li>
<li>You now can run <font color="#0000ff"><strong>lofiadm</strong></font> to verify that the block device was created successfully.. Example { &quot;<font color="#0000ff"><strong>lofiadm</strong></font>&quot; }
<p><span></span></p>
</li>
<li>
<p><span>Now you will need to mount the block device as ReadOnly and specify the File System.. Example { <strong>&quot;<font color="#0000ff">mount -o ro -F hsfs</font> /dev/lofi/1 <font color="#ff0000">/mnt</font></strong>&quot; }<br />
</span></p>
</li>
<li>
<p><span>Finally all you need or better yet may want to do is run a <br />
{ &quot;<font color="#0000ff"><strong>df -k</strong></font>&quot; or &quot;<font color="#0000ff"><strong>df -h</strong></font>&quot;&nbsp; To verify that the device is mounted and then run a &quot;<font color="#0000ff"><strong>ls</strong></font>&quot; to view the contents of the directory}<br />
</span></p>
</li>
</ol>
