---
layout: post
status: publish
published: true
title: Basic Networking HowTo on OpenSolaris
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p><span class=\"dropcap\">I</span>'m a complete NEWBIE to the OpenSolaris
  world!!!! So I am writing this HowTo for all the OpenSolaris NEWBIE'S out there...
  I'll do my best to explain how to setup basic networking on OpenSolaris as I was
  stuck for a good 3 hours trying to get basic networking connectivity working.</p>\r\n<br
  />"
wordpress_id: 200
wordpress_url: http://linuxdynasty.org/?p=200
date: !binary |-
  MjAwOC0wNy0xMyAxOTowMTo1OCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNy0xMyAxOTowMTo1OCAtMDQwMA==
categories: []
tags:
- Beginner OpenSolaris HowTo's
- Basic Networking HowTo on OpenSolaris
comments: []
---
<p><span class="dropcap">I</span>'m a complete NEWBIE to the OpenSolaris world!!!! So I am writing this HowTo for all the OpenSolaris NEWBIE'S out there... I'll do my best to explain how to setup basic networking on OpenSolaris as I was stuck for a good 3 hours trying to get basic networking connectivity working.</p>
<p><a id="more"></a><a id="more-200"></a><br />Now OpenSolaris is not as popular as Linux so there are not as many devices supported as there are for Linux (So bare that in mind). When I first installed OpenSolaris and OpenSolaris booted up just fine, I logged into the nice Gnome Window Manager and opened up a shell. I ran &quot;<font color="#0000ff"><strong>ifconfig -a</strong></font>&quot; and it showed two &quot;<strong>lo</strong>&quot; interfaces(One ipv4 and the other ipv6) and an <strong>nge0</strong> interface (Old Nvidia Drivers).</p>
<p>I had no network connectivity, so I had to google for a few seconds and I found that if you run &quot;<strong><font color="#0000ff">ifconfig</font> &lt;<font color="#0000ff">interface_name</font>&gt; <font color="#0000ff">dhcp start</font></strong>&quot; this will send a DHCP request to the DHCP server. Well I ran this and it just sat there and waited until it exited with no dhcp server response. I did not know if that was the right driver for my network card though I did assume it was why else OpenSolaris choose that driver for me.</p>
<p>My first instinct is how do I found out for sure that &quot;<strong>nge</strong>&quot;&nbsp; was the correct driver for my network card. So I need a utility that is equivalent to &quot;<font color="#0000ff"><strong>lspci</strong></font>&quot; in the OpenSolaris world, after some searching I found &quot;<font color="#0000ff"><strong>scanpci</strong></font>&quot; and &quot;<font color="#0000ff"><strong>prtconf</strong></font>&quot;. Though &quot;<font color="#0000ff"><strong>prtconf</strong></font>&quot; did not give me what I was looking for in this situation but &quot;<font color="#0000ff"><strong>scanpci</strong></font>&quot; did. This is the output of &quot;<font color="#0000ff"><strong>scanpci</strong></font>&quot; for my network controller...</p>
<p>&quot;<strong>/usr/X11R6/bin/<font color="#0000ff">scanpci -v</font></strong>&quot;</p>
<p>pci bus 0x0000 cardnum 0x07 function 0x00: vendor 0x10de device 0x03ef<br />
&nbsp;nVidia Corporation MCP61 Ethernet<br />
&nbsp;CardVendor 0x1565 card 0x2505 (Biostar Microtech Int'l Corp, Card unknown)<br />
&nbsp; STATUS&nbsp;&nbsp;&nbsp; 0x00b0&nbsp; COMMAND 0x0007<br />
&nbsp; CLASS&nbsp;&nbsp;&nbsp;&nbsp; 0x06 0x80 0x00&nbsp; REVISION 0xa2<br />
&nbsp; BIST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0x00&nbsp; HEADER 0x00&nbsp; LATENCY 0x00&nbsp; CACHE 0x00<br />
&nbsp; BASE0&nbsp;&nbsp;&nbsp;&nbsp; 0xfe02d000&nbsp; addr 0xfe02d000&nbsp; MEM<br />
&nbsp; BASE1&nbsp;&nbsp;&nbsp;&nbsp; 0x0000ec01&nbsp; addr 0x0000ec00&nbsp; I/O<br />
&nbsp; MAX_LAT&nbsp;&nbsp; 0x14&nbsp; MIN_GNT 0x01&nbsp; INT_PIN 0x01&nbsp; INT_LINE 0x0b<br />
&nbsp; BYTE_0&nbsp;&nbsp;&nbsp; 0x65&nbsp; BYTE_1&nbsp; 0x15&nbsp; BYTE_2&nbsp; 0x05&nbsp; BYTE_3&nbsp; 0x25</p>
<p>&nbsp;</p>
<p>The info above was a great help, <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1- The type of card we have and its model &quot; <strong>nVidia Corporation MCP61 Ethernet</strong>&quot;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2- The device ID <strong>0x03ef</strong> thought all you really need is <strong>03ef</strong></p>
<p>I found this link on the <a href="http://www.opensolaris.org/os/community/device_drivers/projects/longriver/nic_driver_list/" title="Nic Driver List">OpenSolaris</a> web site. This link will show you all the supported and third party supported drivers for OpenSolaris. I found the <strong>nfo</strong> driver which is for the nforce chipset. Though for the third party drivers, OpenSolaris does not provide you the link to the sources or binaries . So after another search on google I found this link <a href="http://homepage2.nifty.com/mrym3/taiyodo/eng/" title="NFO Drivers for Nvidia">http://homepage2.nifty.com/mrym3/taiyodo/eng/</a>. This site was exactly what I needed, Here is the link for the newest driver for <a href="http://homepage2.nifty.com/mrym3/taiyodo/nfo-2.6.0.tar.gz" title="Latest NFO Driver">nfo</a>.</p>
<p>After I downloaded&nbsp;<a href="http://homepage2.nifty.com/mrym3/taiyodo/nfo-2.6.0.tar.gz" title="Latest NFO Driver">nfo</a> , here are the steps I took ( They were in the Readme.txt ).</p>
<ol>
<li><font color="#0000ff"><strong><span>gunzip nfo-2.6.0.tar.gz</span></strong></font></li>
<li><font color="#0000ff"><strong><span>tar -xvf nfo-2.6.0.tar</span></strong></font></li>
<li><font color="#0000ff"><strong><span>cd nfo-2.6.0</span></strong></font></li>
<li><font color="#0000ff"><strong><span>rm obj Makefile</span></strong></font></li>
<li><font color="#000000"><span><font color="#0000ff"><strong>ln -s Makefile.${KARCH}_${COMPILER} Makefile</strong></font>&nbsp; ( for me it was <font color="#0000ff"><strong>ln -s Makefile.amd64_gcc&nbsp; Makefile</strong></font> )</span></font></li>
<li><font color="#000000"><span><font color="#0000ff"><strong>ln -s ${KARCH} obj</strong></font> ( for me it was </span></font><font color="#000000"><font color="#0000ff"><strong>ln -s amd64 obj</strong></font> )</font></li>
<li><font color="#0000ff"><strong>rm Makefile.config</strong></font></li>
<li><font color="#0000ff"><strong>ln -s Makefile.config_gld3 Makefile.config</strong></font></li>
<li><font color="#0000ff"><strong>/usr/ccs/bin/make</strong></font></li>
<li><font color="#0000ff"><strong>/usr/ccs/bin/make install</strong></font></li>
<li><font color="#0000ff"><strong>cp nfo.conf /kernel/drv/nfo.conf</strong></font></li>
<li><font color="#0000ff"><strong>./adddrv.sh</strong></font></li>
<li><font color="#0000ff"><strong>modload obj/nfo</strong></font></li>
<li><font color="#0000ff"><strong>devfsadm -i nfo</strong></font></li>
<li><font color="#0000ff"><strong>ifconfig nfoN plumb</strong></font> ( where <strong>N</strong> is the device number, for me it was <strong>nfo0</strong> )</li>
<li><font color="#0000ff"><strong>ifconfig nfo0 dhcp start</strong></font> ( this is if you want your interface to use DHCP )</li>
<li><font color="#0000ff"><strong>touch /etc/dhcp.nfo0</strong></font>&nbsp; ( this is if you want your interface to use dhcp when it come back up)</li>
<li>edit <font color="#0000ff"><strong>/etc/nsswitch.conf</strong></font>&nbsp; ( Where it says <strong>host: files</strong>, change it to <strong>host: files dns</strong> )</li>
<li><font color="#0000ff"><strong>reboot -- r</strong></font></li>
</ol>
<p><span class="attention">I am now connected to the internet!!! Everything I did above is what lead me to internet connectivity. The reason I gave you all the steps I had to do is so that you do not have to go through the same pain I did and at the same time learn some Solaris specific commands.Next I will give you the normal steps to get network connectivity. Steps for DHCP and steps for Static network connectivity.</span> </p>
<p>&nbsp;</p>
