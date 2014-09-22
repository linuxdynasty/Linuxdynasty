---
layout: post
status: publish
published: true
title: Swatch Startup Script
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "I've been using Swatch for quite a while now and I never invested the
  time to  create a quick startup script. Today, I decided to create one and it works
  just fine under Centos and Ubuntu Server. You can download it here..\r\nswatch init
  script == {filelink=11}\r\n\r\n"
wordpress_id: 92
wordpress_url: http://linuxdynasty.org/?p=92
date: !binary |-
  MjAwOS0xMS0xMiAyMTo0Njo1NiAtMDUwMA==
date_gmt: !binary |-
  MjAwOS0xMS0xMiAyMTo0Njo1NiAtMDUwMA==
categories:
- Shell
tags:
- Shell HowTo's
- Swatch Startup Script
comments: []
---
<p>I've been using Swatch for quite a while now and I never invested the time to  create a quick startup script. Today, I decided to create one and it works just fine under Centos and Ubuntu Server. You can download it here..<br />
swatch init script == {filelink=11}</p>
<p><a id="more"></a><a id="more-92"></a></p>
<p>Or you can copy and paste it below..</p>
<pre>#!/bin/bash## /etc/init.d/swatch# init script for Swatch.## chkconfig: 2345 90 60# description: Swatch#November 11th 2009 Allen Sanabria#http://linuxdynasty.org#CONFIG="/etc/swatch/swatch.conf"PID="/var/run/swatch.pid"LOGFILE="/var/log/secure"PIDS="/tmp/pids.txt"RETVAL=0

swatch_start() {if [ -f $PID ] then echo "Swatch is already running"   cat $PID else echo "Starting Swatch" /usr/bin/swatch --config-file=$CONFIG --tail-file=$LOGFILE --pid-file=$PID &gt; /dev/null 2&gt;&amp;1 &amp; RETVAL=$?fi}

swatch_stop() {if [ -f $PID ] then echo "Stopping Swatch" PARENT="$(&lt; "$PID")" INIT_PID=`ps -o ppid $PARENT |awk ' /[0-9]+/ { print $1 } '` CPID1=`ps --ppid $PARENT |awk ' /[0-9]+/ { print $1 } '` kill -9 $INIT_PID $PARENT $CPID1   rm -f $PID $PIDS RETVAL=$? else echo "Swatch is not running!"fi}

swatch_status() {if [ -f $PID ] then echo "Swatch is running" PARENT="$(&lt; "$PID")" INIT_PID=`ps -o ppid $PARENT |awk ' /[0-9]+/ { print $1 } '` ps -o pid -o command --pid $INIT_PID --pid $PARENT --ppid $PARENT else echo "Swatch is not running" RETVAL=$?fi}

case "$1" in start) swatch_start ;; stop) swatch_stop ;; restart) swatch_stop swatch_start ;; status) swatch_status ;; *) echo "Usage: $0 {start|stop|restart|status}" exit 1esac

exit $RETVAL</pre>
