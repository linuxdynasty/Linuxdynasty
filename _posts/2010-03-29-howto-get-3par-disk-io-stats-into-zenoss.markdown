---
layout: post
status: publish
published: true
title: HowTo get 3par disk IO stats into Zenoss
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "I've come to realize, that CIM is the new SNMP, but on steroids. Most
  new SAN, NAS, Network, and Operating Systems now support <a href=\"http://www.dmtf.org/standards/cim/\">CIM</a>/<a
  href=\"http://www.dmtf.org/standards/wbem/\">WBEM</a>. To me it is easier to gather
  statistics and information through CIM, then it is through SNMP. In this article
  I am going to give you a script that will allow you to query the 3par for Disk IO
  stats. You will be able to grab Disk IO stats on a per Volume, per Port, or per
  Disk basis.You will also be able to search for a Volume, Port, or Disk, instead
  of just dumping all the Volumes, Ports, or Disk.\r\n\r\nBefore you download this
  script, you will need to download <a href=\"http://sourceforge.net/projects/pywbem/\">pywbem</a>
  from sourceforge and install it. .\r\n\r\nget3ParIOstats.py == {filelink=6}\r\n\r\n<span
  class=\"attention\">All the data that you get from the script, must be saved as
  a COUNTER and not a GAUGE.</span>\r\n\r\nHere is an example of searching for statistics
  by DISK for DISK 2:6:1..\r\n<pre>python get3parIOstats.py -u \"http://3par\" -a
  'login passwd' -s '2:6:1' --diskOK|2:6:1_ReadIOs=67236384 2:6:1_WriteIOs=28457131
  2:6:1_TotalIOs=95693515</pre>\r\n"
wordpress_id: 196
wordpress_url: http://linuxdynasty.org/?p=196
date: !binary |-
  MjAxMC0wMy0yOSAwMjoxNToxMyAtMDQwMA==
date_gmt: !binary |-
  MjAxMC0wMy0yOSAwMjoxNToxMyAtMDQwMA==
categories:
- Zenoss
tags:
- Python
- Zenoss
- 3par
- Disk
- IO
- stats
- pywbem
- CIM
comments: []
---
<p>I've come to realize, that CIM is the new SNMP, but on steroids. Most new SAN, NAS, Network, and Operating Systems now support <a href="http://www.dmtf.org/standards/cim/">CIM</a>/<a href="http://www.dmtf.org/standards/wbem/">WBEM</a>. To me it is easier to gather statistics and information through CIM, then it is through SNMP. In this article I am going to give you a script that will allow you to query the 3par for Disk IO stats. You will be able to grab Disk IO stats on a per Volume, per Port, or per Disk basis.You will also be able to search for a Volume, Port, or Disk, instead of just dumping all the Volumes, Ports, or Disk.</p>
<p>Before you download this script, you will need to download <a href="http://sourceforge.net/projects/pywbem/">pywbem</a> from sourceforge and install it. .</p>
<p>get3ParIOstats.py == {filelink=6}</p>
<p><span class="attention">All the data that you get from the script, must be saved as a COUNTER and not a GAUGE.</span></p>
<p>Here is an example of searching for statistics by DISK for DISK 2:6:1..</p>
<pre>python get3parIOstats.py -u "http://3par" -a 'login passwd' -s '2:6:1' --diskOK|2:6:1_ReadIOs=67236384 2:6:1_WriteIOs=28457131 2:6:1_TotalIOs=95693515</pre>
<p><a id="more"></a><a id="more-196"></a></p>
<p><span class="note">Before I continue much further, I would like to say that this script would go great with my <a href="howto-add-multiple-datapoints-to-zenoss-using-the-zenoss-api.html">Zenoss Template Manager</a></span><br />
An example of running get3parIOstats.py with the Zenoss Template Manager..</p>
<pre>python /opt/zenoss/libexec/get3parIOstats.py -u "http://3par" -a "login passwd" -p |
sed -re "s/([0-9]:[0-9]:[0-9]_w+)=w+/"-p1,C"/g" -e "s/^w+|//g" -e "s/:/_/g"|
xargs Zenoss_Template_Manager.py -d "3par" -c 'get3parIOstats.py -u http://3par" -a "login passwd" -p' -t "3parIOStats" --dsource="PortIOstats" -V $1</pre>
<pre>Template 3parIOStats already exists at /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStatsDataSource 
PortIOstats already exists at /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsParser = AutoCommand 
http://3par" -a "login passwd" -p has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsPortIOstats DataSource is EnabledDataPoint  
2_0_1_ReadIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_1_WriteIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_1_TotalIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_2_ReadIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_2_WriteIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_2_TotalIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_3_ReadIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_3_WriteIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_3_TotalIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_4_ReadIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_4_WriteIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_0_4_TotalIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_1_ReadIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_1_WriteIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_1_TotalIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_2_ReadIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_2_WriteIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_2_TotalIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_3_ReadIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_3_WriteIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_3_TotalIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstatsDataPoint  
2_2_4_ReadIOs of type COUNTER has been added to DataSource /zport/dmd/Devices/Storage/3par/devices/3par/3parIOStats/datasources/PortIOstats</pre>
<p><span class="note">Here is an example of searching by VOLUME</span></p>
<pre>python get3parIOstats.py -u "http://3par" -a 'login passwd' --volume -s zenoss
OK|zenoss-perf_ReadIOs=178585316 zenoss-perf_WriteIOs=133818738 zenoss-perf_TotalIOs=312404054 zenoss-perf_ReadHitIOs=391775944 zenoss-perf_
WriteHitIOs=75752999zenoss-mysql_ReadIOs=807053119 zenoss-mysql_WriteIOs=397407133 
zenoss-mysql_TotalIOs=1204460252 zenoss-mysql_ReadHitIOs=893915116 zenoss-mysql_WriteHitIOs=218224301</pre>
<p>As you can see above, I searched for zenoss, and it printed out two volumes that matched zenoss. So you can either be really specific and just print out one volume or be vague and match as many volumes as you can. Or you do not have to search for anything, you just can list all the stats for Volumes, Ports, or Disks..</p>
<p>Here is an example of that...</p>
<pre>python get3parIOstats.py -u "http://172.16.100.73" -a 'login passwd' --port
OK|2:0:1_ReadIOs=1646791211 2:0:1_WriteIOs=833778099 2:0:1_TotalIOs=2480569310 2:0:2_ReadIOs=1652490070 
2:0:2_WriteIOs=838498029 2:0:2_TotalIOs=24909880992:0:3_ReadIOs=1641530849 2:0:3_WriteIOs=825438313 
2:0:3_TotalIOs=2466969162 2:0:4_ReadIOs=1637164097 2:0:4_WriteIOs=826686709 2:0:4_TotalIOs=2463850806
2:2:1_ReadIOs=1823091934 2:2:1_WriteIOs=1048202110 2:2:1_TotalIOs=2871294044 2:2:2_ReadIOs=0 
2:2:2_WriteIOs=0 2:2:2_TotalIOs=0 2:2:3_ReadIOs=0 2:2:3_WriteIOs=02:2:3_TotalIOs=0 
2:2:4_ReadIOs=0 2:2:4_WriteIOs=0 2:2:4_TotalIOs=0 2:3:1_ReadIOs=1012223361 2:3:1_WriteIOs=1291116066 
2:3:1_TotalIOs=2303339427 2:3:2_ReadIOs=02:3:2_WriteIOs=0 2:3:2_TotalIOs=0 2:3:3_ReadIOs=0 
2:3:3_WriteIOs=0 2:3:3_TotalIOs=0 2:3:4_ReadIOs=0 2:3:4_WriteIOs=0 2:3:4_TotalIOs=0 
2:5:1_ReadIOs=11185369362:5:1_WriteIOs=2241831596 2:5:1_TotalIOs=3360368532 2:5:2_ReadIOs=0 
2:5:2_WriteIOs=0 2:5:2_TotalIOs=0 2:5:3_ReadIOs=0 2:5:3_WriteIOs=0 2:5:3_TotalIOs=02:5:4_ReadIOs=0 
2:5:4_WriteIOs=0 2:5:4_TotalIOs=0 3:0:1_ReadIOs=1618784135 3:0:1_WriteIOs=885315727 3:0:1_TotalIOs=2504099862 
3:0:2_ReadIOs=1640576188 3:0:2_WriteIOs=908172240 3:0:2_TotalIOs=25487484283:0:3_ReadIOs=1643215242 
3:0:3_WriteIOs=909195911 3:0:3_TotalIOs=2552411153 3:0:4_ReadIOs=1638896605 3:0:4_WriteIOs=909738643 
3:0:4_TotalIOs=25486352483:2:1_ReadIOs=1820238591 3:2:1_WriteIOs=1140801166 3:2:1_TotalIOs=2961039757 
3:2:2_ReadIOs=0 3:2:2_WriteIOs=0 3:2:2_TotalIOs=0 3:2:3_ReadIOs=0 3:2:3_WriteIOs=0 
3:2:3_TotalIOs=03:2:4_ReadIOs=0 3:2:4_WriteIOs=0 3:2:4_TotalIOs=0 3:3:1_ReadIOs=2444206400 
3:3:1_WriteIOs=1606025077 3:3:1_TotalIOs=4050231477 3:3:2_ReadIOs=0 3:3:2_WriteIOs=0 
3:3:2_TotalIOs=03:3:3_ReadIOs=0 3:3:3_WriteIOs=0 3:3:3_TotalIOs=0 3:3:4_ReadIOs=0 3:3:4_WriteIOs=0 
3:3:4_TotalIOs=0 3:5:1_ReadIOs=268806737 3:5:1_WriteIOs=605936851 3:5:1_TotalIOs=8747435883:5:2_ReadIOs=0 
3:5:2_WriteIOs=0 3:5:2_TotalIOs=0 3:5:3_ReadIOs=0 3:5:3_WriteIOs=0 3:5:3_TotalIOs=0 3:5:4_ReadIOs=0 
3:5:4_WriteIOs=0 3:5:4_TotalIOs=0</pre>
