---
layout: post
status: publish
published: true
title: Screen HowTo Part 2
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>In the the first part of this HowTo,&nbsp; I gave you the bare minimum
  to get Screen working<br />\r\nand how to use it on a day to day basis.... This
  time around I will show you some <br />\r\nof the advanced features of screen that
  may make your life easier in the terminal..</p>\r\n<p>Before continuing this HowTo
  please read <a href=\"screen-howto-part-1.html\" title=\"Screen Part 2\">Part 1</a>
  if you do not have previous experience with screen.<br />\r\nSo lets start this
  HowTo with some more Screen Commands...</p>\r\n<p>&nbsp;</p>\r\n<br />"
wordpress_id: 16
wordpress_url: http://linuxdynasty.org/?p=16
date: !binary |-
  MjAwOC0wNS0xNyAxNTozOToxMSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0xNyAxNTozOToxMSAtMDQwMA==
categories: []
tags:
- Advance Linux HowTo's
- Screen HowTo part 2 Screen HowTo screen howto
comments: []
---
<p>In the the first part of this HowTo,&nbsp; I gave you the bare minimum to get Screen working<br />
and how to use it on a day to day basis.... This time around I will show you some <br />
of the advanced features of screen that may make your life easier in the terminal..</p>
<p>Before continuing this HowTo please read <a href="screen-howto-part-1.html" title="Screen Part 2">Part 1</a> if you do not have previous experience with screen.<br />
So lets start this HowTo with some more Screen Commands...</p>
<p>&nbsp;</p>
<p><a id="more"></a><a id="more-16"></a></p>
<p>&nbsp;<font color="#0000ff"><font color="#000000"><a href="images/stories/screenshots/Screenshot2.png" height="49" width="96" title="Screen Screen shot" rel="shadowbox"><img alt="" title="" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/Screenshot2.png" align="left" height="42" width="81" /></a></font></font></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>1- To start a split screen session in you current screen session...<br />
&nbsp;&nbsp;&nbsp; <font color="#0000ff"><strong><font color="#000000">((</font>ctrl+a<font color="#000000">)</font> S<font color="#000000">)&nbsp;</font></strong><font color="#000000"> </font></font></p>
<p><font color="#0000ff"><font color="#000000">2- To switch between split screens...<br />
</font></font>&nbsp;&nbsp;&nbsp; <font color="#0000ff"><strong><font color="#000000">((</font>ctrl+a<font color="#000000">)</font> &lt;tab button&gt;<font color="#000000">)</font></strong></font>...</p>
<p>3- To copy output from one split screen to the next...<br />
&nbsp;&nbsp;&nbsp; <font color="#0000ff"><strong><font color="#000000">((</font>ctrl+a<font color="#000000">)</font> [<font color="#000000">)</font></strong></font> now using the up and down arrow find the output you want to copy and from where you want to start copying hit the <font color="#0000ff"><strong>&lt;space bar&gt;</strong></font> and keep using the arrows to where you want to stop copying and hit the <font color="#0000ff"><strong>&lt;space bar&gt;</strong></font> again.</p>
<p>4- To paste the output from the previous command...<br />
&nbsp; &nbsp; <font color="#0000ff"><strong><font color="#000000">((</font>ctrl+a) ]<font color="#000000">)</font></strong></font><font color="#000000">&nbsp;</font> <span class="notice"><br />
Now if you want to paste it in the split terminal you would have to do step 2 then step 4.</span> </p>
<p><span class="note"><strong><br />
I use the above commands especially to copy output from one terminal to next without a mouse</strong>.</span></p>
<p>5- Now lets say you want to lock our screen session from private eyes...<br />
&nbsp;&nbsp; <strong>((<font color="#0000ff">ctrl+a</font>) <font color="#0000ff">x</font>)&nbsp;&nbsp; </strong></p>
<p></p>
<p><span class="attention"><br />
To unlock your session just use your password for you account.</span></p>
<p>The following below will make your screen session show all of your sessions in a nice bar below your terminal, show you the current date and time, as well as tell you the host you are in. Check the screenshot above to see what it would look like.</p>
<p>Add the following below to <font color="#0000ff"><strong>.screenrc</strong></font> in your home directory..... Example <font color="#0000ff"><strong>/home/dynasty/.screenrc</strong></font></p>
<pre>hardstatus alwayslastline<br />hardstatus string '%{b}[ %{B}%H %{g}][%= %{wk}%?%-Lw%?%{=b kR}<br />(%{W}%n*%f %t%?(%u)%?%{=b kR})%{= kw}%?%+Lw%?%?%= %{g}][%{Y}%l%{g}]%{=b C}[ %m/%d %c ]%{W}'<br />startup_message off<br />defscrollback 200000<br />shelltitle dynasty<br />caption always</pre>
