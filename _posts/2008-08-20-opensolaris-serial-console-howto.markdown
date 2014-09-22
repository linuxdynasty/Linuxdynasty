---
layout: post
status: publish
published: true
title: OpenSolaris serial console howto
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>The other day I was ripping at my hair because I could not figure out
  how to console into OpenSolaris on my X86 box at home. I had my serial connection
  connected correctly.... But, I just could not figure out what command to use to
  console into Solaris as I always used minicom for Linux.</p>\r\n<p>After much searching
  I found the command <font color=\"#0000ff\"><strong>tip</strong></font>, which is
  the Solaris command equivalent to Linux's <font color=\"#0000ff\"><strong>minicom</strong></font>.&nbsp;
  The command <font color=\"#0000ff\"><strong>tip</strong></font> is actually quite
  easy to use, you just need to know some basics and modify your <font color=\"#ff0000\"><strong>/etc/remote</strong></font>
  configuration file if you are running on a x86 system.</p>\r\n<br />"
wordpress_id: 202
wordpress_url: http://linuxdynasty.org/?p=202
date: !binary |-
  MjAwOC0wOC0yMCAxNTowNTo0MSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wOC0yMCAxNTowNTo0MSAtMDQwMA==
categories: []
tags:
- Beginner OpenSolaris HowTo's
- OpenSolaris serial console howto
comments: []
---
<p>The other day I was ripping at my hair because I could not figure out how to console into OpenSolaris on my X86 box at home. I had my serial connection connected correctly.... But, I just could not figure out what command to use to console into Solaris as I always used minicom for Linux.</p>
<p>After much searching I found the command <font color="#0000ff"><strong>tip</strong></font>, which is the Solaris command equivalent to Linux's <font color="#0000ff"><strong>minicom</strong></font>.&nbsp; The command <font color="#0000ff"><strong>tip</strong></font> is actually quite easy to use, you just need to know some basics and modify your <font color="#ff0000"><strong>/etc/remote</strong></font> configuration file if you are running on a x86 system.</p>
<p><a id="more"></a><a id="more-202"></a></p>
<p>Follow the steps below....</p>
<ol>
<li>Verify that you have configured your system so that it can be serial console into.. Here is a tutorial that I have created on how to setup serial console on Linux <br />
 ( <a href="(%20http://www.linuxdynasty.org/how-to-setup-serial-console-on-linux.html%20)" title="">http://www.linuxdynasty.org/how-to-setup-serial-console-on-linux.html</a> )</p>
</li>
<li>Make sure you have a serial cable and that it is appropriately connected to what ever Unix/Linux server that you are using.
</li>
<li>Before modifying anything please make sure you are logged in as root or have sudo privileges.<br />
Example.. { <font color="#0000ff"><strong>su -</strong></font> } or { <font color="#0000ff"><strong>sudo su -</strong></font> } to gain root access.</p>
</li>
<li>Modify <font color="#ff0000"><strong>/etc/remote</strong></font>&nbsp; by adding the line below into it... But before you add the line below into the <font color="#ff0000"><strong>/etc/remote file</strong></font>, you should understand why you are doing so. The reason is that by default Solaris install has a entry in <font color="#ff0000"><strong>/etc/remote</strong></font> that is called hardwire with almost the exact same entry as below except it is using Serial B instead of Serial A, and this is an issue if you are running on an x86 box with only one Serial connection. So by adding the below, this will fix your dillema. 
<pre>serial1:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :dv=/dev/term/a:br#9600:el=^C^S^Q^U^D:ie=%$:oe=^D:</pre>
</li>
<li>Now type the command <font color="#0000ff"><strong>tip</strong></font> with the entry name of the above... Example { <strong><font color="#0000ff">tip</font> <font color="#ff0000">serial1</font></strong> }
<pre>-bash-3.2$ tip ser1<br />connected<br /><br />opensolaris console login:</pre>
</li>
</ol>
<p>&nbsp;</p>
<p>You should now be at the login prompt of what ever Unix/Linux system you are trying to connect to. Here are some extra command sequences that are extremely helpful while using <font color="#0000ff"><strong>tip</strong></font>.. </p>
<ul>
<li>You can logout of a tip session by typing the following key sequence... { <font color="#0000ff"><strong>~~.</strong></font> }
<pre>opensolaris console login: ~<br /><br />[EOT]<br /></pre>
<p>
</li>
<li>You can transfer a file from the console session that you are connected to back to the system you are consoleing from like this.. { <font color="#0000ff"><strong>~t</strong></font> }
<pre>-bash-3.2$ tip ser1<br />connected<br />opensolaris console login: root<br />Password: <br />Last login: Wed Aug 20 07:37:46 on console<br />Sun Microsystems Inc.&nbsp;&nbsp; SunOS 5.11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; snv_95&nbsp; January 2008<br />You have mail.<br /># bash<br />bash-3.2# ls<br />WE_NEED<br />{ here is where you type ~t and will look like the following }<br />bash-3.2# ~[take] WE_NEED    <br />{ Once the lines stop increasing you can run ( ctrl+c ), <br />then you will see right after the line number the following below }<br />2 lines transferred in 51 seconds   <br />!<br />bash-3.2# <br /></pre>
</li>
</ul>
