---
layout: post
status: publish
published: true
title: Today's task!
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 128
wordpress_url: http://linuxdynasty.org/?p=128
date: !binary |-
  MjAwOS0xMC0wNSAxOTowODozMSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0xMC0wNSAxOTowODozMSAtMDQwMA==
categories:
- Python
- Blog
- VMware
tags:
- Dynastys Blog
- Today's task!
comments:
- id: 16
  author: complicated
  author_email: complicatedspirit@hotmail.com
  author_url: ''
  date: !binary |-
    MjAxMS0xMS0yMCAyMjoyMzoxNyAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMS0yMCAxNzoyMzoxNyAtMDUwMA==
  content: ! "Download link does not work. Can you please fix it.\r\n\r\nThanks."
- id: 17
  author: exacon
  author_email: af@exacon.at
  author_url: ''
  date: !binary |-
    MjAxMS0xMS0yNSAxNDoyMjoyNyAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMS0yNSAwOToyMjoyNyAtMDUwMA==
  content: ! "hello,\r\n\r\ni would like to get these interesting scripts, but it
    seemed that the links are broken..\r\n\r\nso, plz. help..\r\n\r\nthanks.."
- id: 23
  author: dynasty
  author_email: asanabria@linuxdynasty.org
  author_url: ''
  date: !binary |-
    MjAxMS0xMi0wOSAyMTo1ODo0MSAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0wOSAxNjo1ODo0MSAtMDUwMA==
  content: I will work on getting the upload section back up soon
---
<p>Today I was given a task to have my manager emailed once a day. If any of our Data Stores in ESX 3.5 are over 80% utilized. So I said to my self. What would be the easiest way to do this???? Well I've written two scripts in the past, that could help me accomplish that. The first script VMstoragePool.py will list all of the Data Stores in Vmware and its utilization. The 2nd script is check_datastore.py, and this script will return OK, WARNING, or CRITICAL, depending on the thresholds you set. So by effectively combining the 2 scripts I was able to get what I want. Example below...</p>
<pre>python VMstoragePool.py -u "https://esxhostA" -a "login passwd" |grep "DataStore Name" |awk {'print $3'} |for line in `xargs`;do python check_datastore.py -u "https://esxhostA" -a "login passwd" -d $line -w 80 -c 90 -m "GB"|grep -P "WARNING|CRITICAL";done|mail user@domain.com
CRITICAL XythosVol2 57GB Avail 94% used |avail=57
WARNING XythosVol1 62GB Avail 87% used |avail=62
WARNING LinuxVol1 57GB Avail 88% used |avail=57
WARNING WinVol1 75GB Avail 84% used |avail=75
WARNING BBSCVOL1 122GB Avail 88% used |avail=122
CRITICAL NSSharedVOL1 46GB Avail 95% used |avail=46</pre>
<p>&nbsp;</p>
<p>So I can run this script in cron once a day and pipe the output to email him directly. Simple yet effective! On a side note, I fixed both chec_datastore.py and VMstoragePool.py to effectivly parse passwd's that used characters like !@#$%^.</p>
<p>Both scripts can be downlaoded here..<br />
check_datastore.py == {filelink=12}</p>
<p>VMstoragePool.py == {filelink=13}</p>
