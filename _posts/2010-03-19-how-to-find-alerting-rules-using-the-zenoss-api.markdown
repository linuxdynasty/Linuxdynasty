---
layout: post
status: publish
published: true
title: How to find Alerting Rules using the Zenoss API
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Good Afternoon my fellow Zenoss users. here I bring you another Python
  tool to use with Zenoss. This tool will allow you to list all of your alerting rules,
  either by Group, User, or Query. If you are like me and have over 100 Alerting Rules.
  Managing these rules are more then a pain in the butt. Especially when you create
  a new rule and you know you created it correctly, but it just does not work... Well
  you might have another conflicting rule. Well what do you do in this situation??
  You can go through each rule manually and sooner or later you will find it.\r\n\r\nOr
  you can use my tool to find it for you. You might ask... How will yout tool find
  the conflicting rule for me??? Well to be honest it will not find the rule for you.
  What it can do is search all the rules for a certain query. Which can return one
  or more alerting rules if they are similiar in nature. or you can have the tool,
  list all of your Alerting rules. Or you can have the script list all of your alerting
  rules by group or user. The toll will report back to you The Group/User, The Alerting
  Rules attached to that Group/user, and the Schedules Attached to that Alerting Rules.\r\n\r\nWhere
  this tool really helped me, was when the DST changed happened. None of my schedules
  were working anymore, so the work around is to move all the schedules ahead of time.
  Using this script I found all my schedules very quickly, with out haveing to go
  through each of my alerting rules one by one.\r\n\r\n{filelink=7}\r\n\r\n"
wordpress_id: 195
wordpress_url: http://linuxdynasty.org/?p=195
date: !binary |-
  MjAxMC0wMy0xOSAxOTozMToxMSAtMDQwMA==
date_gmt: !binary |-
  MjAxMC0wMy0xOSAxOTozMToxMSAtMDQwMA==
categories:
- Zenoss
tags:
- Python
- Zenoss
- API
- Alerting Rules
comments: []
---
<p>Good Afternoon my fellow Zenoss users. here I bring you another Python tool to use with Zenoss. This tool will allow you to list all of your alerting rules, either by Group, User, or Query. If you are like me and have over 100 Alerting Rules. Managing these rules are more then a pain in the butt. Especially when you create a new rule and you know you created it correctly, but it just does not work... Well you might have another conflicting rule. Well what do you do in this situation?? You can go through each rule manually and sooner or later you will find it.</p>
<p>Or you can use my tool to find it for you. You might ask... How will yout tool find the conflicting rule for me??? Well to be honest it will not find the rule for you. What it can do is search all the rules for a certain query. Which can return one or more alerting rules if they are similiar in nature. or you can have the tool, list all of your Alerting rules. Or you can have the script list all of your alerting rules by group or user. The toll will report back to you The Group/User, The Alerting Rules attached to that Group/user, and the Schedules Attached to that Alerting Rules.</p>
<p>Where this tool really helped me, was when the DST changed happened. None of my schedules were working anymore, so the work around is to move all the schedules ahead of time. Using this script I found all my schedules very quickly, with out haveing to go through each of my alerting rules one by one.</p>
<p>{filelink=7}</p>
<p><a id="more"></a><a id="more-195"></a></p>
<p>If you need help, please post your questions here...<br />
<a href="forums/Scripting/scripting/ZalertingRule_Manager">http://www.linuxdynasty.org/forums/Scripting/scripting/ZalertingRule_Manager</a><br />
Example below...</p>
<pre>[zenoss@zenoss ~]$ python ZalertingRules_Manager.py --type="users" --search="asanabria"q################################################################################Alerting Rules for asanabria ************************************************************ Alerting Rule:        foo SQL Query:    severity &gt;= 4 and eventState = 0 and prodState = 1000

 Windows for Alerting Rule foo Window:      yee Start time:  Thu Mar 18 14:40:30 2010 Duration:    days 0 hours 1 minutes 0 ************************************************************

[zenoss@zenoss ~]$ python ZalertingRules_Manager.py --type="groups" --search="Escalation 0"################################################################################Alerting Rules for Escalation 0************************************************************ Alerting Rule:        Server - QA SQL Query:    (prodState = 1000) and (deviceClass like '/Server/Linux/QA Servers%') and (eventState = 0) and (severity &gt;= 4)

 ************************************************************ Alerting Rule:        Email - Downgrade SQL Query:    (prodState = 1000) and (eventClass like '/App/Email/Downgrade%') and (eventState = 0) and (severity &gt;= 4)

 ************************************************************ Alerting Rule:        Email - Job Alerts SQL Query:    (prodState = 1000) and (eventClass like '/App/Email/Job Alerts%') and (eventState = 0) and (severity &gt;= 4)

 Windows for Alerting Rule Email - Job Alerts Window:      0700-0701 Start time:  Sat Mar 13 07:00:00 2010 Duration:    days 0 hours 0 minutes 1 ***********************************************************</pre>
<p>As you can see it will get you a wealth of data.. You can also search by query..</p>
<pre>[zenoss@zenoss ~]$ python ZalertingRules_Manager.py --type="query" --search="/App/Log/Java"################################################################################Owner = App - Tomcat Alerting Rule Tomcat Java Log Matching Query = (prodState = 1000) and (eventClassKey not like '%Java Self Axis Scorer Infinite Loop%') and (eventState = 0) and (severity &gt;= 3) and (eventClass like '/App/Log/Java/US/') Window:      0100-2355 Start time:  Thu Mar 18 01:00:00 2010 Duration:    days 0 hours 22 minutes 55 ************************************************************

################################################################################Owner = Java Self Axis Scorer Infinite Loop Alerting Rule Java Self Axis Scorer Infinite Loop Matching Query = (prodState = 1000) and (eventClassKey like '%Java Self Axis Scorer Infinite Loop%') and (deviceClass like '/Server/Linux/Tomcat/%') and (eventClass like '/App/Log/Java/%') and (eventState = 0) and (severity &gt;= 3)</pre>
<p>Many more features to come.....</p>
