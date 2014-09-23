---
layout: post
status: publish
published: true
title: How To monitor NodeJS using the Stats plugin that comes with Cluster using
  Zenoss.
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 408
wordpress_url: http://linuxdynasty.org/?p=408
date: !binary |-
  MjAxMS0xMi0yOCAwMDozMToyOCAtMDUwMA==
date_gmt: !binary |-
  MjAxMS0xMi0yNyAxOTozMToyOCAtMDUwMA==
categories:
- Python
- Zenoss
- HowTo
- NodeJS
tags: []
comments: []
---
<p>We needed a way to monitor all of our NodeJS instances in Zenoss and not just a simple TCP connection. Since we were already using the Cluster plugin for NodeJS 'http://learnboost.github.com/cluster/' and we are using the stats plugin for Cluster 'http://learnboost.github.com/cluster/docs/stats.html'. We decided to write a quick python script to connect to the stats plugin and parse that data to represent it to Zenoss.</p>
<p>You have 2 options... Run this script by itself using Zenoss to connect to the host or if you are using a socket connection or connecting to localhost only then use SNMP.</p>
<p>Download Here .. {filelink=22}</p>
<ul>
<li>( IN SNMP ) Options are modifiable <strong>'exec CheckClusterLiveStats /usr/local/bin/check_clusterlive_stats.py -t tcp -c localhost:8888</strong>'</li>
<li>Or directly in Zenoss '<strong>/usr/local/bin/check_clusterlive_stats.py -t tcp -c remotehost:8888'</strong></li>
</ul>
<p>This script can be used to connect to a TCP socket or to a local file socket. Example output from Zenoss Test Command...</p>
<pre>Using SNMP Preparing Command...
Executing command /usr/local/zenoss/libexec/check_snmp -H 127.0.0.1 -o .1.3.6.1.4.1.8072.1.3.2.3.1.1.21.67.104.101.99.107.67.108.117.115.116.101.114.76.105.118.101.83.116.97.116.115 -C readonly -R OK against 127.0.0.1
SNMP OK - "Deaths Has not increased, Deaths count is 0 NodeJS cluster OK |restarts=0 workers=4 deaths=0 connections_total=193463 connections_active=0" |

Using Command only...</pre>
<pre>Preparing Command...
Executing command /usr/local/zenoss/libexec/check_clusterlive_stats.py -t tcp -c remotehost:8888
"Deaths Has not increased, Deaths count is 0 NodeJS cluster OK |restarts=0 workers=4 deaths=0 connections_total=193463 connections_active=0" |</pre>
<p>The command above you can run with out snmp. The reason we use snmp because we only allow the stats plugin to run on the localhost interface. So we use snmp to execute the script and in return, it returns the results.</p>
<pre>Here is the help output..
check_clusterlive_stats.py -h
Usage: check_clusterlive_stats.py arg --contype=socket|tcp --connection=pathto socket|host:port

Options:
  -h, --help            show this help message and exit
  -t CONTYPE, --contype=CONTYPE
                        socket or tcp
  -c CONNECTION, --connection=CONNECTION
                        /tmp/cluster-repl.sock or localhost:8888
  -w TIMEOUT, --timeout=TIMEOUT
                        int of how long you want this script to wait until it
                        times out</pre>
<p>&nbsp;</p>
