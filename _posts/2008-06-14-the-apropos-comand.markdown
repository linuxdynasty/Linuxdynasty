---
layout: post
status: publish
published: true
title: The apropos Comand
author:
  display_name: tinkpen
  login: tinkpen
  email: tinkpen@sympatico.ca
  url: ''
author_login: tinkpen
author_email: tinkpen@sympatico.ca
excerpt: ! "<p class=\"MsoNormal\"><strong><span style=\"font-size: 12pt\">apropos:\r\n<o:p></o:p></span></strong></p>\r\n<p
  class=\"MsoNormal\"><span style=\"font-size: 12pt\"><span></span>-Searches\r\nfor
  a given keyword in the top line (description) of all man pages then displays\r\nall
  that\r\n<o:p></o:p><span> </span><span></span>match\r\n<o:p></o:p></span></p>\r\n<p
  class=\"MsoNormal\"><span style=\"font-size: 12pt\"><span></span>-Useful\r\nif you
  do not know the name of a command but you have a specific task you want\r\nto&nbsp;<span></span><span></span>perform\r\n<o:p></o:p></span><strong><span
  style=\"font-size: 12pt\">\r\n<o:p></o:p>\r\n<p class=\"MsoNormal\"><span style=\"font-size:
  12pt\"><span>&nbsp;</span></span></p>\r\n<br />"
wordpress_id: 34
wordpress_url: http://linuxdynasty.org/?p=34
date: !binary |-
  MjAwOC0wNi0xNCAxNTo1MjowNSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNi0xNCAxNTo1MjowNSAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- The apropos Comand
comments: []
---
<p class="MsoNormal"><strong><span style="font-size: 12pt">apropos:<br />
<o:p></o:p></span></strong></p>
<p class="MsoNormal"><span style="font-size: 12pt"><span></span>-Searches<br />
for a given keyword in the top line (description) of all man pages then displays<br />
all that<br />
<o:p></o:p><span> </span><span></span>match<br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt"><span></span>-Useful<br />
if you do not know the name of a command but you have a specific task you want<br />
to&nbsp;<span></span><span></span>perform<br />
<o:p></o:p></span><strong><span style="font-size: 12pt"><br />
<o:p></o:p></p>
<p class="MsoNormal"><span style="font-size: 12pt"><span>&nbsp;</span></span></p>
<p><a id="more"></a><a id="more-34"></a></p>
<p class="MsoNormal"><span style="font-size: 12pt"><span>&nbsp;</span></span></p>
<p></span></strong></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt">Format</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>apropos<em>keyword</em><br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>i.e.<br />
<o:p></o:p></span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>apropos locate<span>&nbsp; </span><br />
<o:p></o:p></span></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt"></p>
<p>&nbsp;</p>
<p></span></strong></p>
<p class="MsoNormal"><span style="font-size: 12pt"><span><strong>Note:</strong> </span>man<br />
–k <em>keyword</em><br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>i.e.<br />
<o:p></o:p></span></p>
<p class="MsoNormal" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; font-size: 12pt; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>man –k who </span><strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></strong></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">will give the same<br />
result as<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">apropos who<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p><br />
</span><strong><span style="font-size: 12pt">Whatis Database</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-Database used by<br />
apropos is called <strong>whatis</strong><br />
<o:p></o:p> </span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-created by a cron job<br />
that runs weekly using a utility called <strong>makewhatis</strong><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-<a id="iddle9960" name="iddle9960"></a><a id="iddle9958" name="iddle9958"></a><a id="iddle9782" name="iddle9782"></a><a id="iddle9764" name="iddle9764"></a><a id="iddle9501" name="iddle9501"></a><a id="iddle9460" name="iddle9460"></a><a id="iddle9190" name="iddle9190"></a><a id="iddle6026" name="iddle6026"></a><a id="iddle5773" name="iddle5773"></a><a id="iddle5771" name="iddle5771"></a><a id="iddle2940" name="iddle2940"></a><a id="iddle2920" name="iddle2920"></a>The cron utility runs the<br />
/etc/cron.weekly/makewhatis.cron script to build/update the whatis database<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-If <span>&nbsp;</span>the system is turned off periodically (as with<br />
a laptop/desktop), the script may not run. <br />
-To keep <strong>apropos</strong> updated run command,<br />
as root run:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp; </span>makewhatis -w<br />
<o:p></o:p></span></p>
<p class="MsoNormal"><span><br />
<o:p>&nbsp;</o:p></span></p>
<p>&nbsp;</p>
