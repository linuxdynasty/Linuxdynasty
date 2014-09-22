---
layout: post
status: publish
published: true
title: Creating a virtual loopback device
author:
  display_name: admin
  login: admin
  email: admin@linuxdynasty.org
  url: ''
author_login: admin
author_email: admin@linuxdynasty.org
excerpt: ! "<p>Sometimes you will need to create a virtual loopback device for whatever
  reason. One possible need would be for a temporary filesystem to do some quick testing,
  or maybe to set up a larger /tmp partition on a server where /tmp is too small.
  To initially create the loopback device, run:</p>\r\n<p>&nbsp;# <font color=\"#0000ff\"><strong>dd</strong></font>
  <strong>if=/dev/zero of=/usr/local/tmpfs bs=50M count=10<br />\r\ndd if=&lt;<font
  color=\"#ff0000\">file to read from</font>&gt; of=&lt;<font color=\"#ff0000\">file
  to write to</font>&gt; bs=&lt;<font color=\"#ff0000\">byte size</font>&gt; count=&lt;<font
  color=\"#ff0000\">count to loop</font>&gt;<br />\r\n</strong></p>\r\n<br />"
wordpress_id: 27
wordpress_url: http://linuxdynasty.org/?p=27
date: !binary |-
  MjAwOC0wNS0yNCAxMTo1NTo1MSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0yNCAxMTo1NTo1MSAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- How to create a virtual loop back device
comments: []
---
<p>Sometimes you will need to create a virtual loopback device for whatever reason. One possible need would be for a temporary filesystem to do some quick testing, or maybe to set up a larger /tmp partition on a server where /tmp is too small. To initially create the loopback device, run:</p>
<p>&nbsp;# <font color="#0000ff"><strong>dd</strong></font> <strong>if=/dev/zero of=/usr/local/tmpfs bs=50M count=10<br />
dd if=&lt;<font color="#ff0000">file to read from</font>&gt; of=&lt;<font color="#ff0000">file to write to</font>&gt; bs=&lt;<font color="#ff0000">byte size</font>&gt; count=&lt;<font color="#ff0000">count to loop</font>&gt;<br />
</strong></p>
<p><a id="more"></a><a id="more-27"></a></p>
<p># <font color="#0000ff"><strong>losetup</strong></font> <strong>/dev/loop0 /usr/local/tmpfs<br />
losetup &lt;<font color="#ff0000">loopback device</font>&gt; &lt;<font color="#ff0000">file</font>&gt;</strong></p>
<p># <font color="#0000ff"><strong>mkfs</strong></font> <strong>-t ext3 /dev/loop0<br />
mkfs -t &lt;<font color="#ff0000">file system type</font>&gt; &lt;<font color="#ff0000">file system</font>&gt;</strong> </p>
<p># <font color="#0000ff"><strong>mount</strong></font> <strong>/dev/loop0 /path/to/dir<br />
mount &lt;<font color="#ff0000">file system</font>&gt; &lt;<font color="#ff0000">dir to mount filesystem</font>&gt;</strong> </p>
<p><span class="attention">You should now have a 500MB loopback filesystem (minus the standard filesystem overhead) mounted under /path/to/dir. You can change the size of the device by modifying the &quot;<strong>bs</strong>&quot; and &quot;<strong>count</strong>&quot; arguments in the &quot;<strong>dd</strong>&quot; command. On every reboot,you will need to do the following to make the device available again:</span></p>
<p># <font color="#0000ff"><strong>losetup</strong></font> <strong>/dev/loop0 /usr/local/tmpfs</strong></p>
<p># <strong><font color="#0000ff">mount</font> /dev/loop0 /path/to/dir </strong></p>
<p>&nbsp;</p>
