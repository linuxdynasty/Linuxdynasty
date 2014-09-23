---
layout: post
status: publish
published: true
title: How To Monitor Http Status Codes using Zenoss and Snmp.
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 402
wordpress_url: http://linuxdynasty.org/?p=402
date: !binary |-
  MjAxMS0xMi0yNyAxOTo1MjowNCAtMDUwMA==
date_gmt: !binary |-
  MjAxMS0xMi0yNyAxNDo1MjowNCAtMDUwMA==
categories:
- Python
- Zenoss
- HowTo
tags:
- Python
- Zenoss
- HTTP Codes
- Monitor 404
comments: []
---
<p>We needed a way to monitor a few different type of HTTP Status Codes, specifically... ( 400, 404, 500, 503, 504, 200 ). This list is modifiable within the script. Though I'm thinking of turning this list into an option, since everyone might not one to gather the count just for those mentioned above.</p>
<p>So In order to get this data, you will need to use SNMP and install logtail. To make this script work you will need to have an snmpd exec statement in the snmpd.conf file and a crontab entry for the script to run as often as you like.</p>
<p>This script has been tested, using Nginx and Ruby On Rails.<br />
You can download the script here.. {filelink=21}</p>
<ul>
<li>On cron, remember this is modifiable '<strong>* * * * * /usr/local/bin/get_http_codes.py -d "/var/log/nginx" -f "www-access.log" &gt;/tmp/errorcount.txt'</strong></li>
<li>In snmpd.conf without quotes '<strong>exec GetHttpStats /bin/cat /tmp/errorcount.txt</strong>'</li>
</ul>
<p>In Zenoss you will have to use the check_snmp nagios command or the inherent snmp check from zenoss. The oid you need to use is the UCDavis OID. For instance I'm using 2 exec statements in snmpd.conf, so the OID I am using for this check is this one '<strong>.1.3.6.1.4.1.2021.8.1.101.2</strong>' The command I'm using in zenoss is like this <strong>'check_snmp -H ${dev/manageIp} -C readonly -P 2c -o .1.3.6.1.4.1.2021.8.1.101.2</strong>'</p>
<p>The current options for get_http_codes.py is '<strong>-d</strong>' which is the directory where the log file is located and '<strong>-f</strong> ' the name of the logfile. This script uses logtail so that I can always get the difference from the last time I scanned the log file.</p>
<p>The purpose of this script is so that you can graph or create a threshold of how many of the below Http Error Codes you are getting between every check. For instance we run this check every 30 seconds in Cron and in Zenoss and we divide the results by 30 so we can get how many of the error codes are happening per second.<br />
Example of the output of the script is 'SNMP OK - "<strong>Nginx Codes OK|count200=181 count400=1 count404=0 count500=0 count503=0 count504=0" |</strong> '</p>
<p>If you have any feature request or have any questions, please leave a comment. Thank you</p>
