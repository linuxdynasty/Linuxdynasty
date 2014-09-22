---
layout: post
status: publish
published: true
title: Introduction to the Alias Command
author:
  display_name: tinkpen
  login: tinkpen
  email: tinkpen@sympatico.ca
  url: ''
author_login: tinkpen
author_email: tinkpen@sympatico.ca
excerpt: ! "<p>&nbsp;<a class=\"wproOver\" href=\"javascript:void(null);\"></a></p>\r\n<p
  class=\"MsoNormal\"><strong><span style=\"font-size: 12pt\" lang=\"EN-US\">alias</span></strong><span
  style=\"font-size: 12pt\" lang=\"EN-US\">\r\n<o:p></o:p></span></p>\r\n<p class=\"LinuxCommandChar\"><strong><span
  style=\"font-size: 12pt\">What:</span></strong><span style=\"font-size: 12pt\">\r\n<o:p></o:p></span></p>\r\n<p
  class=\"LinuxCommandChar\"><span style=\"font-size: 12pt\">-Linux allows a\r\ncomplex
  (or commands with long names) to be given a shorter form using a simple\r\ncharacter
  string\r\n<o:p></o:p></span></p>\r\n<p class=\"LinuxCommandChar\"><span style=\"font-size:
  12pt\">-This is called an <strong>alias</strong>\r\n<o:p></o:p></span></p>\r\n<p
  class=\"LinuxCommandChar\"><span style=\"font-size: 12pt\">-You create aliases\r\nwith
  the <strong>alias</strong> command\r\n<o:p></o:p></span></p>\r\n<p class=\"LinuxCommandChar\"><span
  style=\"font-size: 12pt\">-This command is\r\nbuilt<span>&nbsp; </span>into the
  Bash shell, not a\r\nseparate program<br />\r\n</span></p>\r\n<br />"
wordpress_id: 33
wordpress_url: http://linuxdynasty.org/?p=33
date: !binary |-
  MjAwOC0wNi0xNCAxNDo1NjoxMiAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNi0xNCAxNDo1NjoxMiAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- Alias command HowTo
comments: []
---
<p>&nbsp;<a class="wproOver" href="javascript:void(null);"></a></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US">alias</span></strong><span style="font-size: 12pt" lang="EN-US"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">What:</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-Linux allows a<br />
complex (or commands with long names) to be given a shorter form using a simple<br />
character string<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-This is called an <strong>alias</strong><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-You create aliases<br />
with the <strong>alias</strong> command<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-This command is<br />
built<span>&nbsp; </span>into the Bash shell, not a<br />
separate program<br />
</span></p>
<p><a id="more"></a><a id="more-33"></a></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"></p>
<p>&nbsp;<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">Where:</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-usually set in home ~/.bashrc<br />
file (home/username/.bashrc)<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-this allows alias to<br />
be used by interactive subshells.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">-Aliases that are to<br />
be the defaults for all users are placed in the /etc/bashrc file<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">How (a) The Rules:</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">Syntax</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">alias <em>name-of-alias</em>=<em>value</em><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">alias r=rm<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">Rules:</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">1. No space is allowed<br />
before or after the = (equal sign)<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">2. If spaces/tabs are<br />
needed then quotation marks (usually single quotes) must be used<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>alias cp='cp -i'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">3. Aliases can be<br />
nested, so that you can have aliases that call other aliases.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>You create two aliases:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>alias lll='ls -la'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>alias tdr='cd /home/harry'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>You can now combine these two aliases to<br />
create another alias:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>alias lcd='tdr | lll'<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">4. Aliases are<br />
disabled for noninteractive shells (i.e. shell scripts)<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">HOW (B) – PRATICAL USES</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></strong></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">Adding Aliases</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">1) <strong>Temporary Alias</strong><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">To add an alias that<br />
will only last as your current session:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>alias lll='ls -la'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">2) <strong>Permanent Alias – Single User</strong><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">a) vi /home/<em>user</em>/.bashrc<br />
<span>&nbsp;&nbsp; </span>i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span>vi /home/Harold/.bashrc<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">Note:</span></strong><span style="font-size: 12pt"> The<br />
file is called <strong>.bashrc</strong> not<strong> bashrc</strong>. There is a period (.) at the<br />
beginning of the file<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">name.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">b) Add aliases desired<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp; </span>i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span>alias lll='ls -la'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">c) Save file (ESC,<br />
then qw )<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">3) <strong>Permanent Alias – Root</strong><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">a) As root:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span><span>&nbsp;&nbsp;&nbsp; </span>cd ~<span>&nbsp;</span><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">b) Edit .bashrc file<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span><span>&nbsp;&nbsp;&nbsp; </span>vi .bashrc<span style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span>&nbsp; </span><br />
<o:p></o:p></span></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">c) Add desired aliases<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp; </span>i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span>alias lll='ls -la'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">d) Save file (ESC,<br />
then qw )<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">4) <strong>Permanent Universal Aliases</strong><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">a) As root:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp; </span>vi /etc/bashrc<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp; </span>Note: Unlike the other bashrc files, this<br />
has no dot at the front of the file name<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">b) Go to the end of<br />
the file, put in a comment and add the aliases desired:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span>i.e. <br />
# Custom Alias for this machine<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias rm='rm -i'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias mv='mv -i'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias cp='cp -i'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">c) Save file<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">NOTE: </span></strong><span style="font-size: 12pt"><span>&nbsp;</span>The alias command allows several commands to<br />
be strung together.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">Example</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">As a system<br />
administrator, one of you main jobs will be working with Apache, the main web<br />
server for Linux. As part of this work you will frequently have to look for<br />
Apache (httpd) processes. The standard way to do this is:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">ps -ef | grep httpd<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">Rather than having to<br />
type this over &amp; over again you can create an alias that allows you to do<br />
this in a few key strokes:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias psh='ps -ef | grep httpd'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">List current aliases:</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">alias<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">root@LocalHostSun Jun 01 &gt; alias<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias cp='cp -i'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias l.='ls -d .* --color=tty'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias ll='ls -l --color=tty'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias ls='ls --color=tty'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias mv='mv -i'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias rm='rm -i'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot<br />
--show-tilde'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">Note:</span></strong><span style="font-size: 12pt"> In<br />
this case, nothing follows the alias command. Also some aliases are preset by<br />
the OS.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">List value of a specific alias</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">Type alias <em>alias_name</em><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">root@LocalHostTue Jun 10 &gt; alias rm<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias rm='rm -i'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">Preventing the Shell from Using an Alias</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">Lets say you have an<br />
alias that is the name of a command (only with options):<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias rm='rm -i'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">In this case whenever<br />
you type the <strong>rm</strong> command you will be<br />
prompted for confirmaition (-i).<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">If you want to run the<strong>rm</strong> command with the –i option then<br />
use the full pathname for the command:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">i.e.:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">/bin/rm test2<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">You can also us<span>&nbsp; </span>the  with the command:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">rm test4<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
<p class="LinuxCommandChar"><strong><span style="font-size: 12pt">Removing Aliases</span></strong><span style="font-size: 12pt"><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">1) Temporary Alias<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">Use the <strong>unalias</strong> command, <strong>unalias</strong> <em>alias-name</em><br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">i.e.<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">You have created the<br />
following alias for the current session:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">alias lll='ls -la'<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt">To remove it, do the<br />
following:<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar" style="background: rgb(230, 230, 230) none repeat scroll 0% 50%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial"><span style="font-size: 12pt">unalias lll<br />
<o:p></o:p></span></p>
<p class="LinuxCommandChar"><span style="font-size: 12pt"><br />
<o:p>&nbsp;</o:p></span></p>
