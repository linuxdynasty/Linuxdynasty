---
layout: post
status: publish
published: true
title: HowTo monitor the Netscaler using Python and Soap instead of SNMP
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "In this HowTo, I will show you how you can get statistics off of the Netscaler
  without using SNMP. You might be asking why would I want to do that?? Well like
  many other devices that support SNMP, the Netscaler makes use of dynamic OID creation.
  For those of you that do not understand what I mean. Dynamic OID creation, is the
  way that Networking devices give OID's to variables that are not static in the device
  itself.\r\n\r\nHere are some common static variables/OID's, amongst most devices
  out there.\r\n<ul>\r\n\t<li>CPU Utilization</li>\r\n\t<li>Disk Utilization</li>\r\n\t<li>Memory
  Utilization</li>\r\n\t<li>TCP Statistics</li>\r\n</ul>\r\nHere are some common,
  non-static variables/OID's..\r\n<ul>\r\n\t<li>A Load Balanced Virtual Server</li>\r\n\t<li>Statistics
  about LUNS</li>\r\n\t<li>Statistics about Services</li>\r\n</ul>\r\nNow you can
  get these statistics off of the SNMP based device. But if and when this device is
  rebooted, more then likely the OID has changed. Now you are stuck with the task,
  of finding the new OID. Since the Netscalers have a SOAP Based API, we can get those
  same statistics with out ever needing to know the OID.\r\n\r\nHere I have attached
  a script that I wrote, using Python and Suds to connect to the Netscaler. This script
  works perfectly with <a href=\"http://www.zenoss.com/\">Zenoss</a> and its DataPoint
  structure. {filelink=9}\r\n\r\n"
wordpress_id: 84
wordpress_url: http://linuxdynasty.org/?p=84
date: !binary |-
  MjAxMC0wMi0wNyAyMToyOToxNyAtMDUwMA==
date_gmt: !binary |-
  MjAxMC0wMi0wNyAyMToyOToxNyAtMDUwMA==
categories:
- Python
- Zenoss
- Netscaler
tags:
- Python HowTo's
- Netscaler
- Python
- Suds.
- SNMP
- OID
- SOAP
comments:
- id: 2
  author: bassbonerocks
  author_email: nogoal4u@pacbell.net
  author_url: ''
  date: !binary |-
    MjAxMS0xMC0wNiAwMDo0NDowNiAtMDQwMA==
  date_gmt: !binary |-
    MjAxMS0xMC0wNSAxOTo0NDowNiAtMDQwMA==
  content: You mention a getns_stats.py script, but I see no download for this script.
    Is this a modified version of some FOSS script? Or is the download link just missing?
- id: 3
  author: bassbonerocks
  author_email: nogoal4u@pacbell.net
  author_url: ''
  date: !binary |-
    MjAxMS0xMC0wNiAwMDo0NzozMCAtMDQwMA==
  date_gmt: !binary |-
    MjAxMS0xMC0wNSAxOTo0NzozMCAtMDQwMA==
  content: I guess I should mention why I'm looking for the script, I'm in the process
    of writing a zenpack for this. If I can get a copy of this script I hope to create
    a nice zenpack for all of this instead of having to hack it together every time
    :)
- id: 28
  author: dynasty
  author_email: asanabria@linuxdynasty.org
  author_url: ''
  date: !binary |-
    MjAxMS0xMi0wOSAyMjowMDozOSAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0wOSAxNzowMDozOSAtMDUwMA==
  content: I switched from Joomla to wordpress, I am working on getting the downloads
    section working again
---
<p>In this HowTo, I will show you how you can get statistics off of the Netscaler without using SNMP. You might be asking why would I want to do that?? Well like many other devices that support SNMP, the Netscaler makes use of dynamic OID creation. For those of you that do not understand what I mean. Dynamic OID creation, is the way that Networking devices give OID's to variables that are not static in the device itself.</p>
<p>Here are some common static variables/OID's, amongst most devices out there.</p>
<ul>
<li>CPU Utilization</li>
<li>Disk Utilization</li>
<li>Memory Utilization</li>
<li>TCP Statistics</li>
</ul>
<p>Here are some common, non-static variables/OID's..</p>
<ul>
<li>A Load Balanced Virtual Server</li>
<li>Statistics about LUNS</li>
<li>Statistics about Services</li>
</ul>
<p>Now you can get these statistics off of the SNMP based device. But if and when this device is rebooted, more then likely the OID has changed. Now you are stuck with the task, of finding the new OID. Since the Netscalers have a SOAP Based API, we can get those same statistics with out ever needing to know the OID.</p>
<p>Here I have attached a script that I wrote, using Python and Suds to connect to the Netscaler. This script works perfectly with <a href="http://www.zenoss.com/">Zenoss</a> and its DataPoint structure. {filelink=9}</p>
<p><a id="more"></a><a id="more-84"></a></p>
<p><span class="attention">Before you proceeed any further, you will need to download SUDS from here <a href="https://fedorahosted.org/suds/">https://fedorahosted.org/suds/</a>.</span><br />
You should also check this HowTo that I wrote, it contains some examples on how to connect to the Netscaler using the Python Virtual Shell.<br />
<a href="http://www.linuxdynasty.org/how-to-get-information-from-the-netscaler-using-python-and-suds.html">http://www.linuxdynasty.org/how-to-get-information-from-the-netscaler-using-python-and-suds.html</a></p>
<p>Here are some examples on how you will run the script...</p>
<pre>python getns_stats.py -t http -i "nsip" -u "login" -p "passwd"OK|httptotrxresponsebytes=116454007709 httpresponsesrate=0 httppostsrate=0 httptotposts=3960332 httptotgets=5621562 httperrserverbusy=9540 httprequestsrate=0 httprxresponsebytesrate=0 httptotothers=3505 httptxresponsebytesrate=0 httptotrequests=9585399 httperrserverbusyrate=0 httprxrequestbytesrate=0 httptotresponses=9569809 httpgetsrate=0 httptottxresponsebytes=0 httpothersrate=0 httptotrxrequestbytes=21823753173

python getns_stats.py -t tcp -i "nsip" -u "login" -p "passwd"OK|tcpcurserverconn=379 tcpcurclientconnclosing=4 tcptotrxbytes=169757271745 tcpclientconnopenedrate=0 tcpcurserverconnopening=0 tcptottxpkts=497006339 tcprxpktsrate=25 tcpactiveserverconn=4 tcpcurserverconnclosing=374 tcptxbytesrate=1902 tcprxbytesrate=1641 tcpcurclientconnopening=0 tcpcurclientconn=16 tcpcurserverconnestablished=5 tcptotrxpkts=460755860 tcptxpktsrate=31 tcpcurclientconnestablished=12 tcpserverconnopenedrate=10 tcptottxbytes=108830467243</pre>
<p>Both the Stats, above are actually static in The Netscaler. But I actually included them in the script, because I can. The stats I will show you below are not static..</p>
<pre>python getns_stats.py -n test_vs -t lbvserver -i "nsip" -u "login" -p "passwd"OK|totalresponses=18238 establishedconn=0 pktssentrate=0 totalrequestbytes=18807153 hitsrate=0 totalrequests=18299 requestbytesrate=0 requestsrate=0 totalpktsrecvd=25490 pktsrecvdrate=0 curclntconnections=0 totalresponsebytes=815662173 totalpktssent=70190 responsebytesrate=0 tothits=18303 cursrvrconnections=0 responsesrate=0

python getns_stats.py -n test_svc -t service -i "nsip" -u "login" -p "passwd"OK|totalresponses=2070 throughputrate=0 totalrequestbytes=3309175 totalrequests=2071 svrestablishedconn=0 surgecount=0 requestbytesrate=0 requestsrate=0 activetransactions=0 throughput=0 curclntconnections=0 totalresponsebytes=25849781 responsebytesrate=0 cursrvrconnections=8 responsesrate=0

python getns_stats.py Please provide the Netscaler IPAddress and username/password pass the --help for more options

python getns_stats.py -husage: getns_stats.py [options] arg --username=username --password=password --netscaler=netscalerip

options:-h, --help                          show this help message and exit                                    -i HOSTNAME, --hostname=HOSTNAME                                    Here you will put the netscaler IPAddress or the                                    netscaler hostname

-u USERNAME, --username=USERNAME    Your username

-p PASSWORD, --password=PASSWORD    Your password

-l LIST, --list=LIST                List all the names of the Virtual Servers and                                    Services. Example --list=lbvserver, --list=service

-n NAME, --name=NAME                Virtual Server that you want to grab statistics for.

-t TYPE, --type=TYPE                Here you either pass service, lbvserver, tcp or http.                                    example... --name=foobar --type=lbvserver  or                                    --type=tcp or --type=http or --name=foobar                                    --type=service</pre>
<p>&nbsp;</p>
