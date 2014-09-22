---
layout: post
status: publish
published: true
title: Screen HowTo Part 1
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>I've been using screen for the past 3 years and for the first time
  I've decided to seek out more functionality out of it.&nbsp; So last week I spent
  about 2 hours looking up some of the different functionality that I can use in the
  day to day. Let me tell you I found a bunch of goodies that I use now religiously
  (For a week now ;) ).</p>\r\n<p>So for those of you who do not know what a screen
  session is... (STRAIGHT FROM THE MAN PAGES) Screen is a full-screen window manager
  that multiplexes a physical terminal between several processes (typically interactive
  shells).&nbsp; Essentially you can have 30 terminal sessions inside one terminal
  and much more.....</p>\r\n<p>&nbsp;</p>\r\n<br />"
wordpress_id: 15
wordpress_url: http://linuxdynasty.org/?p=15
date: !binary |-
  MjAwOC0wNS0xMSAyMjo0NjowMCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0xMSAyMjo0NjowMCAtMDQwMA==
categories: []
tags:
- Advance Linux HowTo's
- Screen Screen howto screen how to Screen split screen
comments: []
---
<p>I've been using screen for the past 3 years and for the first time I've decided to seek out more functionality out of it.&nbsp; So last week I spent about 2 hours looking up some of the different functionality that I can use in the day to day. Let me tell you I found a bunch of goodies that I use now religiously (For a week now ;) ).</p>
<p>So for those of you who do not know what a screen session is... (STRAIGHT FROM THE MAN PAGES) Screen is a full-screen window manager that multiplexes a physical terminal between several processes (typically interactive shells).&nbsp; Essentially you can have 30 terminal sessions inside one terminal and much more.....</p>
<p>&nbsp;</p>
<p><a id="more"></a><a id="more-15"></a></p>
<p>&nbsp;</p>
<p>To run Screen all you need to do is type &quot;<strong><font color="#0000ff">screen</font></strong>&quot; in your terminal. You more then likely do not have it installed by default. So for those of you who have the distributions below...&nbsp; </p>
<ol>
<li>Fedora/CentOS/RHE/ or any RedHat based system, you will need to run &quot;<strong><font color="#0000ff">yum install screen</font></strong>&quot;</li>
<li>Ubuntu/Debian based systems, you will need to run <font color="#0000ff"><strong>&quot;apt-get install screen</strong></font>&quot;</li>
<li>Gentoo based systems, you will need to run &quot;<font color="#0000ff"><strong>emerge screen</strong></font>&quot;</li>
</ol>
<p>&nbsp;</p>
<p>To start a new screen session all you have to do is type <strong><font color="#0000ff">&quot;screen&quot;</font></strong><br />
Now that you are in a screen session, the fun begins now...</p>
<p><a href="images/stories/screenshots/Screenshot-screen.png" height="49" width="96" title="Screen Screen shot" rel="shadowbox"><img alt="" title="" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/Screenshot-screen.png" align="left" height="42" width="81" /></a></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>1- To start a new sub session (Virtual Session) type <br />
&nbsp;&nbsp; <strong><font color="#0000ff"><font color="#000000">((</font>ctrl+a<font color="#000000">)</font> c<font color="#000000">)</font></font></strong><br />
&nbsp;&nbsp; <span class="attention">Please ignore the plus (+)symbol, this essentially means &quot;ctrl a then c&quot;</span></p>
<p>2- To switch between sessions... <br />
&nbsp;&nbsp;<font color="#0000ff"><strong> <font color="#000000">((</font>ctrl+a<font color="#000000">)</font> &lt;space bar&gt;<font color="#000000">)</font></strong></font></p>
<p>3- To switch between your previous session and the current one..<br />
&nbsp;&nbsp; <font color="#0000ff"><strong><font color="#000000">((</font>ctrl+a<font color="#000000">)</font> a<font color="#000000">)</font></strong></font></p>
<p>4- To kill a frozen session...<br />
&nbsp;&nbsp; <font color="#0000ff"><strong><font color="#000000">((</font>ctrl+a<font color="#000000">)</font> k<font color="#000000">) </font></strong></font></p>
<p>5- To see a list of available commands...<br />
&nbsp;&nbsp;&nbsp;<font color="#0000ff"><strong><font color="#000000">((</font>ctrl+a<font color="#000000">)</font> ?<font color="#000000">)</font><br />
</strong></font></p>
<p>6- To see a list of virtual terminals you have open..<br />
&nbsp;&nbsp; <font color="#0000ff"><strong><font color="#000000">((</font>ctrl</strong></font><font color="#0000ff"><strong>+a<font color="#000000">)</font> &quot;<font color="#000000">)</font></strong></font></p>
<p>7- To Detach from a screen session and not lose any of your virtual terminals...<br />
&nbsp;&nbsp; <font color="#0000ff"><strong><font color="#000000">((</font>ctrl+a<font color="#000000">)</font> d<font color="#000000">)</font></strong></font> <span class="approved">( This is one of the best features of screen!! )</span></p>
<p>8- To view&nbsp; current screen sessions once you are logged out of screen..<br />
&nbsp;&nbsp; <font color="#0000ff"><strong>&quot;screen -list&quot;</strong></font></p>
<p>9- To reattach to an Attached session (Session that was not detached properly)<br />
&nbsp;&nbsp; <font color="#0000ff"><strong>&quot;screen -D -r &lt;11546.pts-5.hostname&gt;&quot;</strong></font> (session name from the output of the screen -list command)</p>
<p>10- To reattach to a detached session..<br />
&nbsp;&nbsp; <font color="#0000ff"><strong>&quot;screen -r &lt;11546.pts-5.hostname&gt;&quot; </strong></font>(session name from the output of the screen -list command)</p>
<p>10- To end that session you can either type <br />
&nbsp; <font color="#0000ff"><strong>&quot;exit&quot; </strong><font color="#000000">or a</font><strong> <font color="#000000">(</font>ctrl+d<font color="#000000">)</font></strong></font></p>
<p><span class="notice">The above commands are the most <strong>BASIC/COMMON</strong> for screen and its everyday use.</span></p>
<p>Now time for a little more advance functionality.. Off to <a href="screen-howto-part-2.html" title="Screen Part 2">Part 2</a> of this HowTo</p>
