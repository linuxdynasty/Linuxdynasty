---
layout: post
status: publish
published: true
title: Netbackup Troubleshooting How To
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>This is not really a howto but more of a quick lookup on what commands
  to use to debug/troubleshoot.&nbsp; <br />\r\nSo this is not lay out in any order
  what so ever. Just a bunch of random notes.... I hope this helps you the way it
  has helped me..... :)</p>\r\n<p>1. There are 2 directories where logs exist! 1st
  dir is <strong>/usr/openv/logs</strong> (Low level logs) and<br />\r\n2nd dir is
  <strong class=\"highlight\">/usr/openv/netbackup</strong><strong>/logs</strong>
  (Here you will have to create the subdirectories in order <br />\r\nfor logs to
  be created here) BEWARE these logs tend to get huge!</p>\r\n<p>&nbsp;</p>\r\n<br
  />"
wordpress_id: 69
wordpress_url: http://linuxdynasty.org/?p=69
date: !binary |-
  MjAwOC0wMi0xMCAyMzoxMToyOSAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAyMzoxMToyOSAtMDUwMA==
categories: []
tags:
- Netbackup HowTo's
- Netbackup HowTo Troubleshooting Linux Netbackup 6MP Netbackup Debugging Debug Netbackup
comments: []
---
<p>This is not really a howto but more of a quick lookup on what commands to use to debug/troubleshoot.&nbsp; <br />
So this is not lay out in any order what so ever. Just a bunch of random notes.... I hope this helps you the way it has helped me..... :)</p>
<p>1. There are 2 directories where logs exist! 1st dir is <strong>/usr/openv/logs</strong> (Low level logs) and<br />
2nd dir is <strong class="highlight">/usr/openv/netbackup</strong><strong>/logs</strong> (Here you will have to create the subdirectories in order <br />
for logs to be created here) BEWARE these logs tend to get huge!</p>
<p>&nbsp;</p>
<p><a id="more"></a><a id="more-69"></a></p>
<p>&nbsp;</p>
<ol>
<li>
<p>Also if the <strong>/usr</strong> dir becomes a 100% full Netbackup will basically stop functioning!! Always check the logs dir!</p>
</li>
<li>
<p>If DNS goes bad Netbackup will also stop functioning and will need a restart of<strong class="highlight"> </strong>Netbackup!</p>
</li>
<li>
<p>Commands you should use for everyday trouble shooting.</p>
<ol>
<li class="gap">
<p dir="ltr"><strong>/usr/openv/netbackup/bin/</strong><strong>bpclntcmd -hn client</strong> <br />
(This command is extremely helpful, it tells you if Netbackup can do a successful lookup of the dns name)</p>
</li>
<li>
<p><tt><span></span></tt><strong><span></span>bpclntcmd -ip ip_address</strong><br />
 (This command is also very helpfuls, it tells you if Netbackup can do a reverse dns lookup)</p>
</li>
<li>
<p><strong><span>/usr/openv/netbackup/bin/</span></strong><strong>bpexpdate -m 03000I -d 0</strong> <br />
(This command allows you to expire media when needed instead of waiting for it to expire)</p>
</li>
<li>
<p><strong>bpstulist</strong> <br />
(This command will tell you all drives and there hosts connected to the master server)</p>
</li>
<li>
<p><strong><span>/usr/openv/volmgr/bin</span></strong>/<strong>tpautoconf -a</strong> <br />
(This cmd will scan all local device on the media manager)</p>
</li>
<li>
<p><strong><span>/usr/openv/volmgr/bin/</span></strong><strong>vmoprcmd</strong> <br />
(excellent cmd for verifying that all media managers have their drives)</p>
</li>
<li>
<p><strong><span>/usr/openv/netbackup/bin/admincmd/</span></strong><strong>bpmedialist -rl 1</strong> <br />
(This cmd is retrieving all info about media that is available/full/expired/other) NOTE: available_media uses this cmd to get some of its info</p>
</li>
<li>
<p><strong><span>/usr/openv/netbackup/bin/admincmd/</span></strong><strong>bpmedia -unfreeze</strong> <strong>-m 03001</strong> <br />
(This cmd unfreezes the media)</p>
</li>
<li><strong><font face="Arial" size="2">/usr/openv/netbackup/bin/</font></strong><strong>bpadm</strong> <br />
(is a script that runs cmds for you in a easier format and also does about 90% of what the gui does)</p>
<ul>
<li>
<p>example how to change a volume pool for a media;</p>
</li>
<li>
<p>run <strong>bpadm</strong></p>
</li>
<li>
<p>choose option (<strong>e</strong>) media management</p>
</li>
<li>
<p>choose option (<strong>s</strong>) special actions</p>
</li>
<li>
<p>choose option (<strong>p</strong>) Change volume pool for volume pools</p>
</li>
<li>
<p>choose a volume pool from where you are want to move media to, and you are done!</p>
</li>
</ul>
</li>
<li>
<p>Troubleshooting <strong>SYBASE GOING FUBAR</strong>! These are the steps to take to get a clean EMM database up and running with .</p>
<ul>
<li>
<p>Stop Netbackup services.</p>
</li>
<li>
<p>Move the contents our of the <strong>/usr/openv/db/data/</strong> directory.</p>
</li>
<li>
<p>Start the database server up with the command &quot;<strong>nbdbms_start_server</strong>&quot; from the <strong>/usr/openv/db/bin</strong> directory</p>
</li>
<li>
<p>Run a &quot;<strong>nbdbms_start_server -stat</strong>&quot; to make sure the database server was up</p>
</li>
<li>
<p>Run &quot;<strong>create_nbdb</strong>&quot; to created in default locations to database files.</p>
</li>
<li>
<p>Start Netbackup services.</p>
</li>
<li>
<p>Run &quot;<strong>tpext</strong>&quot; from the <strong>/volmgr/bin</strong> directory</p>
</li>
<li>
<p>Then restart Netbackup on all servers!</p>
</li>
<li>
<p>Now scan for all devices on &lt;hostname&gt;.</p>
</li>
</ul>
</li>
<li class="gap">
<p>Check a jukebox at the command line:</p>
<ul>
<li>
<p><strong>/usr/openv/volmgr/bin/vmcheckxxx -rt tld -rn 1 -list</strong></p>
</li>
</ul>
</li>
<li class="gap">
<p>Inventory Jukebox from the command line:</p>
<ul>
<li>
<p><strong>/usr/openv/volmgr/bin/vmupdate -rt tld -rn 1 -full [-interactive] -use_barcode_rules</strong></p>
</li>
</ul>
</li>
<li class="gap">
<p>Check to see which disk are expired, full, available</p>
<ul>
<li>
<p><strong>/usr/openv/</strong><strong class="highlight">netbackup</strong><strong>/bin bpmedialist -rl 1</strong> <br />
(-rl means retention level, the 1 means 2 week retention which is what we are using)</p>
</li>
</ul>
</li>
<li class="gap">
<p>If you notice that you are running out of tapes and you know tapes shouldve expired, <br />
run the previous command and get all of the expire tapes and run this command.</p>
<ul>
<li>
<p>/usr/openv/<strong class="highlight">netbackup</strong>/bin/bpexpdate -m [mediaid] -d 0 (-d means days so 0 means now)</p>
</li>
</ul>
<ol>
<li>
<p>The <strong><span>/usr/openv/netbackup/bin/admincmd/</span></strong><strong>nbemmcmd</strong> (This is the sybase cmd utility<br />
<strong>(PLEASE BE CAREFUL USING THIS CMD!! </strong><br />
This cmd is very useful in situations where you have to remove/add a client/media manager/device. here are some examples:</p>
<ul>
<li>
<p>This deletes a media manger (<strong>nbemmcmd -deletehost -machinename media_server -machinetype media</strong>)</p>
</li>
<li>
<p>This deletes a tape (<strong>nbemmcmd -deletemedia -mediaid 03000I -originhost server</strong>)</p>
</li>
<li>
<p>This tells you if which boxes are have a emmserver and if they are reachable (<strong>nbemmcmd -getemmserver</strong>)</p>
</li>
<li>
<p>This will let you know if there are any media conflicts (<strong>nbemmcmd -listmedia -conflicts</strong>)</p>
</li>
<li>
<p>This will let you know what hosts are seen as media_managers and master servers (<strong>nbemmcmd -listhosts</strong>)</p>
</li>
</ul>
</li>
</ol>
</li>
</ol>
<ul>
<li><strong>&nbsp;/usr/openv/netbackup/bin/bpps -x</strong> (shows all Netbackup process that are running). </li>
</ul>
<ul>
<li>
<pre><font size="2"><strong><span>/usr/openv/netbackup/bin/goodies/available_media <br /></span></strong>(Display all media and its states, and this script does this by <br />running two other commaands and formatting it so it can be seen in a usable format) </font></pre>
</li>
</ul>
<ul>
<li><strong><span>/usr/openv/netbackup/bin/admincmd/</span></strong><strong>bpdbjobs</strong> (This is esentially the activity monitor)</li>
</ul>
</li>
</ol>
<p><script type="text/javascript"><!--<br />
 amzn_cl_tag="linuxd-20";<br />
//--></script><br />
<script type="text/javascript" src="http://cls.assoc-amazon.com/s/cls.js"></script></p>
