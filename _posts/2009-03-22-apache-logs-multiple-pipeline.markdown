---
layout: post
status: publish
published: true
title: ! 'Apache Logs: Multiple Pipeline'
author:
  display_name: admin
  login: admin
  email: admin@linuxdynasty.org
  url: ''
author_login: admin
author_email: admin@linuxdynasty.org
excerpt: ! "<p>Apache, among many other httpds, can be configured to log to an executable's
  <em>STDIN </em>instead of a file. But older Apaches, again like other httpds, won't
  let you pipe <em>that</em> programme's output to another's input, so you're limited
  to whatever the one was made to do.* </p>\r\n<p>httpd error logs often contain error
  conditions one wants to be alerted about, but for most people that means either
  monitoring it with some variant of tailf running on the host, or <code>ssh</code>ing
  to the host to run <code>tail</code> (or <code>tail -f</code>) on the log, piped
  to <code>egrep</code>, etcetera. This kind of set-up can work fine for one or two
  web servers, but gets cumbersome when you have more than just a few, and can become
  impracticable when dealing with many or when the error logs are being written to
  frequently.</p>\r\n<p>Well, I sometimes have to deal with six hundred or more. Screw
  <code>ssh 'tailf | egrep' ...</code></p>\r\n<br />"
wordpress_id: 78
wordpress_url: http://linuxdynasty.org/?p=78
date: !binary |-
  MjAwOS0wMy0yMiAxNzo1NTo0NiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wMy0yMiAxNzo1NTo0NiAtMDQwMA==
categories: []
tags:
- Python HowTo's
- ! 'Apache Logs: Multiple Pipeline'
comments: []
---
<p>Apache, among many other httpds, can be configured to log to an executable's <em>STDIN </em>instead of a file. But older Apaches, again like other httpds, won't let you pipe <em>that</em> programme's output to another's input, so you're limited to whatever the one was made to do.* </p>
<p>httpd error logs often contain error conditions one wants to be alerted about, but for most people that means either monitoring it with some variant of tailf running on the host, or <code>ssh</code>ing to the host to run <code>tail</code> (or <code>tail -f</code>) on the log, piped to <code>egrep</code>, etcetera. This kind of set-up can work fine for one or two web servers, but gets cumbersome when you have more than just a few, and can become impracticable when dealing with many or when the error logs are being written to frequently.</p>
<p>Well, I sometimes have to deal with six hundred or more. Screw <code>ssh 'tailf | egrep' ...</code></p>
<p><a id="more"></a><a id="more-78"></a></p>
<p><a href="http://www.linuxdynasty.org/View-details/Python-Scripts/30-tailcast-=-tailf-+-datagrams.html">This Python script/module (tailcast.py)</a> will monitor a file or <em>STDIN</em> (a la <code>tailf</code>) and send UDP datagrams to a specified address. The datagrams can be restricted to only those input lines that match a regular expression, and every line of input still becomes a line of output. The result?</p>
<blockquote>
<pre>ErrorLog &quot;| /usr/bin/python /usr/local/bin/tailcast.py -a 224.168.2.9 -p 5664 -r interestingerror|otherbadness | cronolog ...&quot;</pre>
</blockquote>
<p>Now all that my co-workers and I need to do is listen in on the multicast group and we'll have access to every <code>interestingerror</code> or <code>otherbadness</code> that might be going into Apache's error log, without each of us opening six hundred SSh connections, running six hundred <code>tailf</code>s, six hundred <code>egrep</code>s, on six hundred servers that are already being pounded.</p>
<p>It should be noted though that this script suffers from the very same limitation Apache imposes: you get only one pipe. I'll fix that, and the <code>subprocess</code> module will make it easy, but even then you shouldn't be putting too many progs in the pipeline. Think Performance.</p>
<p>[1] Note that later Apache httpds will run the pipe target through <code>/bin/sh -c</code> if the string specifying the target contains any shell metacharacters, like '<code>|</code>'. That may seem like a great thing, but it can actually complicate things when you want your metacharacters to be treated as arguments to the command (i.e. the old behaviour). Although the '<code>|</code>' treatment makes no effective difference to the piping specification to <code>tailcast</code> (other than that <code>tailcast</code> needn't arrange for pipelining), yet it can still have unfortunate effects on the regular expression you're matching, especially if it contains any '<code>|</code>' (or) regex metacharacters...</p>
