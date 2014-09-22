---
layout: post
status: publish
published: true
title: Daily Nagios Report Python Script Part One
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>I had to create a script that will output every host that has went
  down in the past day and how many times that host went down and at what times did
  that host go down and when it came back up in a nice readable format ( Executives
  who do not know what they are looking at ). Now this is the first release of my
  script and I do mean first release as I really want to expand it to not just do
  daily reports from nagios.log but as well as get the archives and any to pass it
  dates.</p>\r\n<div></div>\r\n<p>I hope you Nagios users who have to send reports
  to your executives find this script useful but check back soon as I'm going to be
  adding more to it or even changing it into its own class. As of right now it consist
  of three functions. The only draw back of the script is that it takes a while to
  parse the log file since it has to find all the uniq hosts in nagios.log and find
  only the hard down and hard up events compared to the uniq hosts.</p>\r\n<p>For
  now I run this script in cron at 6AM and have the txt file that it creates sent
  to a list of users at 7AM on a daily basis.  Again this is my first revision it
  will go through alot more and if you have suggestions or you have expanded on this
  script by all means let me know so I can post it up here or you can become a member
  and post it yourself. Also if you have request please become a member and ask in
  the forums section.</p>\r\n<p><strong>UPDATE!!!</strong><br /> Cambid, fixed the
  regex in the script. It  should now match correctly in all environments!</p>\r\n<br
  />"
wordpress_id: 75
wordpress_url: http://linuxdynasty.org/?p=75
date: !binary |-
  MjAwOC0xMC0wMSAxODoxMToyNiAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0xMC0wMSAxODoxMToyNiAtMDQwMA==
categories: []
tags:
- Python HowTo's
- Daily Nagios Report Python Script Part One
comments: []
---
<p>I had to create a script that will output every host that has went down in the past day and how many times that host went down and at what times did that host go down and when it came back up in a nice readable format ( Executives who do not know what they are looking at ). Now this is the first release of my script and I do mean first release as I really want to expand it to not just do daily reports from nagios.log but as well as get the archives and any to pass it dates.</p>
<div></div>
<p>I hope you Nagios users who have to send reports to your executives find this script useful but check back soon as I'm going to be adding more to it or even changing it into its own class. As of right now it consist of three functions. The only draw back of the script is that it takes a while to parse the log file since it has to find all the uniq hosts in nagios.log and find only the hard down and hard up events compared to the uniq hosts.</p>
<p>For now I run this script in cron at 6AM and have the txt file that it creates sent to a list of users at 7AM on a daily basis.  Again this is my first revision it will go through alot more and if you have suggestions or you have expanded on this script by all means let me know so I can post it up here or you can become a member and post it yourself. Also if you have request please become a member and ask in the forums section.</p>
<p><strong>UPDATE!!!</strong><br /> Cambid, fixed the regex in the script. It  should now match correctly in all environments!</p>
<p><a id="more"></a><a id="more-75"></a></p>
<p>The output looks like this</p>
<pre>Host host1 Status Report<br />-----------------------------------------------------------------<br />Total Times Down = 1<br />host1 went DOWN  at Thu Oct  2 01:34:31 2008<br />-----------------------------------------------------------------<br /><br />Host host2 Status Report<br />-----------------------------------------------------------------<br />Total Times Down = 1<br />host2 went DOWN  at Thu Oct  2 03:16:11 2008<br />host2 went UP    at Thu Oct  2 03:26:51 2008<br />-----------------------------------------------------------------<br /><br />Host host3 Status Report<br />-----------------------------------------------------------------<br />Total Times Down = 1<br />host3 went DOWN  at Thu Oct  2 04:16:31 2008<br />-----------------------------------------------------------------<br /><br />Host host4 Status Report<br />-----------------------------------------------------------------<br />Total Times Down = 3<br />host4 went DOWN  at Tue Oct  2 04:13:58 2008<br />host4 went DOWN  at Tue Oct  2 08:50:28 2008<br />host4 went DOWN  at Tue Oct  2 12:17:08 2008<br />host4 went UP    at Tue Oct  2 07:28:38 2008<br />host4 went UP    at Tue Oct  2 10:53:08 2008<br />host4 went UP    at Tue Oct  2 12:43:48 2008 <br /></pre>
<p>You can download the script <a href="View-details/Linux-Dynasty-Scripts-and-Programs/2-Daily-Nagios-Report.html" title="title">here. </a> To download the script you must become a member first<br />{quickdown:2}</p>
<p><a href="images/stories/Scripts/nagios_report.png" rel="shadowbox[0]"><img alt="alt" style="width: 274px; height: 224px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/Scripts/nagios_report.png" /></a></p>
