---
layout: post
status: publish
published: true
title: Run Levels In Linux
author:
  display_name: tinkpen
  login: tinkpen
  email: tinkpen@sympatico.ca
  url: ''
author_login: tinkpen
author_email: tinkpen@sympatico.ca
excerpt: ! "<p class=\"MsoNormal\"><strong><span style=\"font-size: 14pt\" lang=\"EN-US\">RUN
  LEVELS</span></strong><strong><span style=\"font-size: 12pt\" lang=\"EN-US\">\r\n<o:p></o:p></span></strong></p>\r\n<p
  class=\"MsoNormal\"><span style=\"font-size: 12pt\" lang=\"EN-US\">\r\n<o:p>&nbsp;</o:p></span></p>\r\n<p
  class=\"MsoNormal\"><strong><span style=\"font-size: 12pt\" lang=\"EN-US\">Background</span></strong><span
  style=\"font-size: 12pt\" lang=\"EN-US\">\r\n<o:p></o:p></span></p>\r\n<p class=\"MsoNormal\"><span
  style=\"font-size: 12pt\" lang=\"EN-US\">-Linux can boot\r\ninto various configurations
  (much like with what you get with Windows when\r\nhitting <strong>F8</strong> while
  booting)\r\n<o:p></o:p></span></p>\r\n<p class=\"MsoNormal\"><span style=\"font-size:
  12pt\" lang=\"EN-US\">-Linux has 6 boot\r\nlevels but outside of specialized situations,
  only levels 3 &amp; 5 are useful\r\n<o:p></o:p></span></p>\r\n<p class=\"MsoNormal\"><span
  style=\"font-size: 12pt\" lang=\"EN-US\">-Runlevel 3 boots\r\nto a command prompt
  –this is the default Runlevel for most servers\r\n<o:p></o:p></span></p>\r\n<p class=\"MsoNormal\"><span
  style=\"font-size: 12pt\" lang=\"EN-US\">-Runlevel 5 boots\r\nto a GUI interface
  similar to Windows – this is the default Runlevel for most\r\nworkstations\r\n<o:p></o:p></span></p>\r\n<p
  class=\"MsoNormal\"><span style=\"font-size: 12pt\" lang=\"EN-US\">\r\n<o:p>\r\n<br
  />"
wordpress_id: 32
wordpress_url: http://linuxdynasty.org/?p=32
date: !binary |-
  MjAwOC0wNi0wNyAxNDozODoxMSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNi0wNyAxNDozODoxMSAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- Linux boot levels for beginners
comments: []
---
<p class="MsoNormal"><strong><span style="font-size: 14pt" lang="EN-US">RUN LEVELS</span></strong><strong><span style="font-size: 12pt" lang="EN-US"><br />
<o:p></o:p></span></strong></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">Background</span></strong><span style="font-size: 12pt" lang="EN-US"><br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">-Linux can boot<br />
into various configurations (much like with what you get with Windows when<br />
hitting <strong>F8</strong> while booting)<br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">-Linux has 6 boot<br />
levels but outside of specialized situations, only levels 3 &amp; 5 are useful<br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">-Runlevel 3 boots<br />
to a command prompt –this is the default Runlevel for most servers<br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">-Runlevel 5 boots<br />
to a GUI interface similar to Windows – this is the default Runlevel for most<br />
workstations<br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
<o:p><br />
<br /><a id="more"></a><a id="more-32"></a><br />&nbsp;</o:p></span></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">Linux RunLevel Chart</span></strong><span style="font-size: 12pt" lang="EN-US"><br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
<o:p>&nbsp;</o:p></span></p>
<table class="MsoNormalTable" style="border: 1pt solid windowtext; margin-left: 31.05pt" border="1" cellpadding="0" cellspacing="0">
<thead>
<tr>
<td colspan="5" style="border: 1pt solid windowtext; padding: 3.75pt">
<p class="MsoNormal"><strong><span style="font-size: 12pt">Runlevels<br />
<o:p></o:p></span></strong></p>
</td>
</tr>
<tr>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="bottom">
<p class="MsoNormal"><strong><span style="font-size: 12pt">Number<br />
<o:p></o:p></span></strong></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="bottom">
<p class="MsoNormal"><strong><span style="font-size: 12pt">Name<br />
<o:p></o:p></span></strong></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="bottom">
<p class="MsoNormal"><strong><span style="font-size: 12pt">Login<br />
<o:p></o:p></span></strong></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="bottom">
<p class="MsoNormal"><strong><span style="font-size: 12pt">Network<br />
<o:p></o:p></span></strong></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="bottom">
<p class="MsoNormal"><strong><span style="font-size: 12pt">Filesystems<br />
<o:p></o:p></span></strong></p>
</td>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">0<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Halt<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">&nbsp;<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">&nbsp;<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">&nbsp;<br />
<o:p></o:p></span></p>
</td>
</tr>
<tr>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">1<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Single<br />
  user<br />
  (Very Useful for Troubleshooting)<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Textual<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Down<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Mounted<br />
<o:p></o:p></span></p>
</td>
</tr>
<tr>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">2<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Multiuser<br />
  without NFS<br />
  (Network File System)<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Textual<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Up<br />
  (partially)<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Mounted<br />
<o:p></o:p></span></p>
</td>
</tr>
<tr>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">3<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Multiuser</span></p>
<p class="MsoNormal"><span style="font-size: 12pt">(Standard boot level for servers)&nbsp;</span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Textual<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Up<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Mounted<br />
<o:p></o:p></span></p>
</td>
</tr>
<tr>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">4<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">User<br />
  defined<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">&nbsp;<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">&nbsp;<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">&nbsp;<br />
<o:p></o:p></span></p>
</td>
</tr>
<tr>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">5<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Multiuser<br />
  with X Windows/GUI</span></p>
<p class="MsoNormal"><span style="font-size: 12pt">(Standard boot level for desktops)&nbsp;</span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Graphical<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Up<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Mounted<br />
<o:p></o:p></span></p>
</td>
</tr>
<tr>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">6<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">Reboot<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">&nbsp;<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">&nbsp;<br />
<o:p></o:p></span></p>
</td>
<td style="border: 1pt solid windowtext; padding: 3.75pt" valign="top">
<p class="MsoNormal"><span style="font-size: 12pt">&nbsp;<br />
<o:p></o:p></span></p>
</td>
</tr>
</tbody>
</table>
<p class="MsoNormal"><span lang="EN-US"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US"><br />
<o:p>&nbsp;</o:p></span></strong></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US"><br />
<o:p>&nbsp;</o:p></span></strong></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">How to change a Run Level</span></strong><span style="font-size: 12pt" lang="EN-US"><br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">1. Make sure you<br />
are logged in as root<br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">2. <strong>init <em>runlevel</em></strong><span>&nbsp; </span><br />
<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>i.e.<br />
<o:p></o:p></span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt" lang="EN-US">init 6<br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US">reboot the system<br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">How to change The Default Run Level</span></strong><span style="font-size: 12pt" lang="EN-US"><br />
<o:p></o:p></span></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">NOTE: </span></strong><span style="font-size: 12pt" lang="EN-US"><span>&nbsp;</span>Be VERY care with this – DO NOT<br />
set your run levels to 6 (forever rebooting) or 0 (your machine halts every<br />
time you try and start it.<strong><br />
<o:p></o:p></strong></span></p>
<p class="MsoNormal"><span style="font-size: 12pt" lang="EN-US"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar" style="margin-left: 0cm"><strong><span style="font-size: 12pt">Steps:</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="margin-left: 0cm"><span style="font-size: 12pt">1.<br />
vi /etc/inittab<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="margin-left: 0cm"><span style="font-size: 12pt">2.<br />
Look for a line the ends with <strong>initdefault</strong><br />
i.e.:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; margin-left: 0cm; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>id:3:initdefault:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="margin-left: 0cm"><span style="font-size: 12pt">3.<br />
Change the number. Unless you are troubleshooting you should only use a value<br />
of 3 or 5 in this line<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="margin-left: 0cm"><span style="font-size: 12pt">4.<br />
Save<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="margin-left: 0cm"><span style="font-size: 12pt">5.<br />
Reboot system to test.<br />
<o:p></o:p></span></p>
<p>&nbsp;</p>
