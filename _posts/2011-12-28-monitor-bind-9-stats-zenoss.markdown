---
layout: post
status: publish
published: true
title: How To Monitor and get Bind 9 stats using Zenoss
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Hey guys, here is another Python script by me :-) . The reason for this
  script, is to give you the capabilities to monitor and graph Bind 9 stats. This
  script will be executed through SNMP.. We will be using the UCD-MIB 1.3.6.1.4.1.2021.8.1\r\n<pre>The
  stats are from named.stats... Here is an example of named.stats..\r\ncat /var/cache/bind/named.stats\r\n+++
  Statistics Dump +++ (1325089261)\r\n++ Incoming Requests ++\r\n            83318718
  QUERY\r\n++ Incoming Queries ++\r\n            54293282 A\r\n                1929
  NS\r\n                3186 CNAME\r\n                  27 SOA\r\n            13645272
  PTR\r\n                7921 MX\r\n                 781 TXT\r\n            15224426
  AAAA\r\n                 200 SRV\r\n                   1 NAPTR\r\n               
  1271 A6\r\n                  95 DS\r\n                   2 NSEC\r\n                 
  66 SPF\r\n              140257 ANY\r\n                   2 Others</pre>\r\nYou can
  download the script here .. {filelink=23}\r\n\r\n"
wordpress_id: 415
wordpress_url: http://linuxdynasty.org/?p=415
date: !binary |-
  MjAxMS0xMi0yOCAyMToyNzo0NyAtMDUwMA==
date_gmt: !binary |-
  MjAxMS0xMi0yOCAxNjoyNzo0NyAtMDUwMA==
categories:
- Python
- Zenoss
- SNMP
tags:
- Python
- Zenoss
- Bind9
comments: []
---
<p>Hey guys, here is another Python script by me :-) . The reason for this script, is to give you the capabilities to monitor and graph Bind 9 stats. This script will be executed through SNMP.. We will be using the UCD-MIB 1.3.6.1.4.1.2021.8.1</p>
<pre>The stats are from named.stats... Here is an example of named.stats..
cat /var/cache/bind/named.stats
+++ Statistics Dump +++ (1325089261)
++ Incoming Requests ++
            83318718 QUERY
++ Incoming Queries ++
            54293282 A
                1929 NS
                3186 CNAME
                  27 SOA
            13645272 PTR
                7921 MX
                 781 TXT
            15224426 AAAA
                 200 SRV
                   1 NAPTR
                1271 A6
                  95 DS
                   2 NSEC
                  66 SPF
              140257 ANY
                   2 Others</pre>
<p>You can download the script here .. {filelink=23}</p>
<p><a id="more"></a><a id="more-415"></a><br />
I purposely made this script so that it can be used with snmpd.conf. I made an option called '<strong>-g</strong>', and this option will actualy generate the snmpd.conf file for you with the entries that can be monitored. Example below..</p>
<pre>exec ResolverStatisticsqueries-with-RTT---1600ms /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'queries with RTT &gt; 1600ms'
exec ResolverStatisticsqueries-with-RTT-800-1600ms /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'queries with RTT 800-1600ms'
exec ResolverStatisticsqueries-with-RTT-10-100ms /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'queries with RTT 10-100ms'
exec ResolverStatisticsSERVFAIL-received /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'SERVFAIL received'
exec ResolverStatisticsother-errors-received /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'other errors received'
exec ResolverStatisticsquery-timeouts /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'query timeouts'
exec ResolverStatisticsIPv4-responses-received /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'IPv4 responses received'
exec ResolverStatisticsqueries-with-RTT-500-800ms /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'queries with RTT 500-800ms'
exec ResolverStatisticsqueries-with-RTT---10ms /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'queries with RTT &lt; 10ms'
exec ResolverStatisticsqueries-with-RTT-100-500ms /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'queries with RTT 100-500ms'
exec ResolverStatisticsIPv4-queries-sent /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'IPv4 queries sent'
exec ResolverStatisticsIPv4-NS-address-fetches /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'IPv4 NS address fetches'
exec ResolverStatisticsEDNS(0)-query-failures /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'EDNS(0) query failures'
exec ResolverStatisticsquery-retries /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'query retries'
exec ResolverStatisticslame-delegations-received /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'lame delegations received'
exec ResolverStatisticsFORMERR-received /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'FORMERR received'
exec ResolverStatisticsNXDOMAIN-received /usr/local/bin/getBindStats.py -t 'Resolver Statistics' -s 'NXDOMAIN received'</pre>
<p>That is just a sample above as there is a lot more data from the original output. Here is the output with the '<strong>-h</strong>' option..</p>
<pre>/usr/local/bin/getBindStats.py -h
Usage: getBindStats.py arg --grouptype='Incoming Requests' --printstat='A'

Options:
  -h, --help            show this help message and exit
  -t GTYPE, --grouptype=GTYPE
                        Cache DB RRsets,Incoming Queries,Incoming
                        Requests,Name Server Statistics,Outgoing
                        Queries,Resolver Statistics,Socket I/O Statistics,Zone
                        Maintenance Statistics
  -s PRINT_STAT, --printstat=PRINT_STAT
                        Acceptable Values are these:::TXT,PTR,SPF,queries
                        caused recursion,A,IPv4 NS address fetch
                        failed,mismatch responses received,TCP/IPv4
                        connections established,queries with RTT
                        100-500ms,query timeouts,query retries,NSEC,IPv4
                        responses received,requests with EDNS(0)
                        received,TCP/IPv4 sockets closed,IPv4 IXFR
                        requested,SRV,NOTIFY,queries with RTT
                        10-100ms,TCP/IPv4 connections accepted,lame
                        delegations received,FORMERR received,RRSIG,queries
                        with RTT &gt; 1600ms,UDP/IPv4 recv errors,NS,IPv4
                        notifies sent,queries with RTT 800-1600ms,SERVFAIL
                        received,IPv4 AXFR requested,auth queries
                        rejected,ANY,IPv4 requests received,queries with RTT &lt;
                        10ms,IPv4 notifies received,IPv4 queries sent,queries
                        resulted in referral answer,NXDOMAIN,other errors
                        received,QUERY,truncated responses received,MX,TCP
                        requests received,
  -g, --gensnmp         This will generate in STDOUT the SNMP info you need in
                        snmpd.conf</pre>
<p>&nbsp;</p>
