---
layout: post
status: publish
published: true
title: How to setup serial console on linux
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 21
wordpress_url: http://linuxdynasty.org/?p=21
date: !binary |-
  MjAwOC0wMi0xMCAwNTozNjozOCAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAwNTozNjozOCAtMDUwMA==
categories: []
tags:
- Beginner Linux HowTo's
- howto
- linux
- serial console howto
- serial
- console
- ubuntu
- fedora
comments: []
---
<p><b><span style="color: red;">This tutorial is for those Admins who need to setup serial console on there LINUX servers</span></b></p>
<p> <strong>Section-1</strong></p>
<ol>
<li>
<ul>
In this first part of of the how to I will show you how to setup serial console on a <br /><strong>RedHat(Fedora,CentOS)</strong> based systems<strong>(Does work on other systems as well)</strong>.</p>
<li>First step is to make sure you have a serial port. </li>
<li>Second step is to make sure you have a console cable. You can do this by running this..
<pre>linuxdynasty.org]# dmesg |grep ttyS0<br />ttyS0 at I/O 0x3f8 (irq = 4) is a 16550A<br />  </pre>
</li>
</ul>
</li>
<li>
<ul>
Once you verified you have the necessary <strong>hardware</strong> configuration, <br />we are on to configuring the server.</p>
<li>Add this <b><span style="color: blue;">co:2345:respawn:/sbin/agetty ttyS0 9600 vt100-nav</span></b> to <b><span style="color: green;">/etc/inittab</span></b> <br />using your favorite editor. (mine is vi :) ) This is how mine looks like..
<pre># Run gettys in standard runlevels<br />co:2345:respawn:/sbin/agetty ttyS0 57600 vt100-nav<br />1:2345:respawn:/sbin/mingetty tty1<br />2:2345:respawn:/sbin/mingetty tty2<br />3:2345:respawn:/sbin/mingetty tty3<br />4:2345:respawn:/sbin/mingetty tty4<br />5:2345:respawn:/sbin/mingetty tty5<br />6:2345:respawn:/sbin/mingetty tty6<br /> </pre>
</li>
</ul>
</li>
<li>
<ul>
Now it is time to edit <b><span style="color: green;">/boot/grub.conf</span></b>. These two entries need to be added into grub.conf<br /><b><span style="color: blue;">serial --unit=0 --speed=57600</span><br /><span style="color: blue;">terminal --timeout=5 serial console</span></b><br />And append this to <b><span style="color: blue;">console=ttyS0,57600n8</span></b> to your kernel entry.</p>
<li>Here is the all in one solution..
<p> <small></small></p>
<pre><small><br />serial --unit=0 --speed=57600<br />terminal --timeout=5 serial console<br />title CentOS (2.6.9-55.0.2.EL)<br />   root (hd1,0)<br />   kernel /vmlinuz-2.6.9-55.0.2.EL ro root=/dev/VolGroup00/LogVol00 console=tty0 console=ttyS0,57600n8<br />   initrd /initrd-2.6.9-55.0.2.EL.img<br />  </small></pre></p>
</li>
<li>Now reboot your server and from another box console in. </li>
</ul>
</li>
</ol>
<p> <strong>Section-2</strong></p>
<ol>
<li>
<ul>
Now we will show you how to setup a serial console for <strong>Ubuntu Feisty 7.0.4</strong>, <br />(Reason I chose Feisty is that Feisty no longer uses the <b><span style="color: green;">/etc/inittab</span></b> . <br />Instead uses upstart for its init functions)</p>
<li>First step, follow the First step in Section-1 of this tutorial.</li>
</ul>
</li>
<li>
<ul>
Once you verified you have the necessary <strong>hardware</strong> configuration, <br />we are on to configuring the server.</p>
<li>Add this <b><span style="color: blue;">exec /sbin/getty -L 57600 ttyS0 vt102</span></b> to <b><span style="color: green;">/etc/event.d/ttyS0</span></b> (<b><br />If this file does not exist please create it</b>) using your favorite editor. (mine is vi :) ) <br />This is how mine looks like..
<pre># tty0 - getty<br />#<br /># This service maintains a getty on tty1 from the point the system is<br /># started until it is shut down again.<br /><br />start on runlevel 2<br />start on runlevel 3<br />start on runlevel 4<br />start on runlevel 5<br /><br />stop on runlevel 0<br />stop on runlevel 1<br />stop on runlevel 6<br /><br />respawn<br />exec /sbin/getty -L 57600 ttyS0 vt102<br />  </pre>
</li>
</ul>
</li>
<li>
<ul>
Now proceed to third step of Section-1 of this tutorial.
</ul>
</li>
</ol>
