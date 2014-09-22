---
layout: post
status: publish
published: true
title: OpenSolaris and customizing my bashrc
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>I've been using/learning OpenSolaris for the past week and WoW it is
  a complete different world then Linux.. For example I miss my GNU commands.</p>\r\n<ol>\r\n<li>Non
  GNU grep does not have the -r option that I use in the gnu version which is <font
  color=\"#0000ff\"><strong>ggrep</strong></font></li>\r\n<li>Non GNU sed compared
  to <font color=\"#0000ff\"><strong>gsed</strong></font>.</li>\r\n<li>Non GNU tar
  does not have <font color=\"#0000ff\"><strong>gzip</strong></font> integrated as
  the <font color=\"#0000ff\"><strong>gtar</strong></font> does have it.\r\n<br />"
wordpress_id: 107
wordpress_url: http://linuxdynasty.org/?p=107
date: !binary |-
  MjAwOC0wOC0wNyAxNzoxNzo1MCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wOC0wNyAxNzoxNzo1MCAtMDQwMA==
categories: []
tags:
- Dynastys Blog
- OpenSolaris and customizing my bashrc
comments: []
---
<p>I've been using/learning OpenSolaris for the past week and WoW it is a complete different world then Linux.. For example I miss my GNU commands.</p>
<ol>
<li>Non GNU grep does not have the -r option that I use in the gnu version which is <font color="#0000ff"><strong>ggrep</strong></font></li>
<li>Non GNU sed compared to <font color="#0000ff"><strong>gsed</strong></font>.</li>
<li>Non GNU tar does not have <font color="#0000ff"><strong>gzip</strong></font> integrated as the <font color="#0000ff"><strong>gtar</strong></font> does have it.<br />
<br /><a id="more"></a><a id="more-107"></a></li>
</ol>
<p>In order to get my OpenSolaris behave like my Baby Linux does :)... I had to added a few aliases like so to my <font color="#0000ff"><strong>.bashrc</strong></font> file as so... <br />
<strong><font color="#0000ff">alias</font> <font color="#ff0000">vi</font>=&quot;<font color="#0000ff">vim</font>&quot;<br />
<font color="#0000ff">alias</font> <font color="#ff0000">grep</font>=&quot;<font color="#0000ff">ggrep</font>&quot;<br />
</strong><strong><font color="#0000ff">alias</font> <font color="#ff0000">egrep</font>=&quot;<font color="#0000ff">gegrep</font>&quot;</strong><br />
<strong><font color="#0000ff">alias</font> <font color="#ff0000">sed</font>=&quot;<font color="#0000ff">gsed</font>&quot;</strong><br />
<strong><font color="#0000ff">alias</font> <font color="#ff0000">tar</font>=&quot;<font color="#0000ff">gtar</font>&quot;</strong></p>
<p>I am still adding more as I get frustrated.... :(</p>
<p>Also I added more paths to my PATH environment variable in<font color="#0000ff"><strong> .bashrc</strong></font> as well...</p>
<p><strong>PATH=/usr/sbin:/usr/bin:/opt/csw/sbin:/opt/csw/bin:/usr/X11R6/bin<br />
export PATH</strong></p>
<p>&nbsp;</p>
