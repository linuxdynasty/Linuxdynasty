---
layout: post
status: publish
published: true
title: HowTo monitor and add multiple Data Points the easy way in Zenoss
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Recently I had to input quite a few OID's into Zenoss. This meant I had
  to create a Data Source for each OID I wanted to monitor as well as one Data Point.\r\nNow
  I knew this was going to be a hassle!!! So I decided to write a custom Python script
  that uses pysnmp to essentially do a snmpwalk (nextCmd)\r\non a Branch of OID's.
  This means that I can create one Data Source and Mutiple Data Points.\r\nWhich drops
  the amount of time that I have to input into the Zenoss GUI.\r\n\r\nPlease Post
  any questions about this script here <a href=\"http://www.linuxdynasty.org/forums/Scripting/scripting/snmp_branch_help\">http://www.linuxdynasty.org/forums/Scripting/scripting/snmp_branch_help</a>\r\nYou
  can download the script <a href=\"View-details/Zenoss/29-snmp_branch.py.html\">snmp_branch.py</a>\r\n<ul>\r\n\t<li>Update
  1.0.10\r\n<ol>\r\n\t<li>Fixed labeling bug, (Thanks Stephan26 for finding this)</li>\r\n\t<li>Added
  --fsearch option\r\nThanks Stephan26 for suggesting to add a way to find OID's by
  their begining Digits on their last Octect</li>\r\n\t<li>Added --length option\r\nThis
  will allow you to search for an Index on the final Octect of the OID, when the final
  octect is not just the index.\r\nExample.... You want the index OID of 100 but the
  entire last octect of the OID is .6534389100)</li>\r\n</ol>\r\n</li>\r\n</ul>\r\n&nbsp;\r\n\r\nSo
  here is an example below of what the data looks like from SNMP..\r\n<pre>UCD-SNMP-MIB::ssIndex.0
  = INTEGER: 1UCD-SNMP-MIB::ssSwapIn.0 = INTEGER: 0UCD-SNMP-MIB::ssSwapOut.0 = INTEGER:
  0UCD-SNMP-MIB::ssIOSent.0 = INTEGER: 0UCD-SNMP-MIB::ssIOReceive.0 = INTEGER: 1UCD-SNMP-MIB::ssSysInterrupts.0
  = INTEGER: 3|UCD-SNMP-MIB::ssSysContext.0 = INTEGER: 19UCD-SNMP-MIB::ssCpuUser.0
  = INTEGER: 7UCD-SNMP-MIB::ssCpuSystem.0 = INTEGER: 7UCD-SNMP-MIB::ssCpuIdle.0 =
  INTEGER: 84</pre>\r\n&nbsp;\r\n\r\n"
wordpress_id: 77
wordpress_url: http://linuxdynasty.org/?p=77
date: !binary |-
  MjAwOS0wMi0yNyAxOToxMjozNSAtMDUwMA==
date_gmt: !binary |-
  MjAwOS0wMi0yNyAxOToxMjozNSAtMDUwMA==
categories:
- Uncategorized
tags:
- Python HowTo's
- HowTo monitor and add multiple Data Points the easy way in Zenoss
comments: []
---
<p>Recently I had to input quite a few OID's into Zenoss. This meant I had to create a Data Source for each OID I wanted to monitor as well as one Data Point.<br />
Now I knew this was going to be a hassle!!! So I decided to write a custom Python script that uses pysnmp to essentially do a snmpwalk (nextCmd)<br />
on a Branch of OID's. This means that I can create one Data Source and Mutiple Data Points.<br />
Which drops the amount of time that I have to input into the Zenoss GUI.</p>
<p>Please Post any questions about this script here <a href="http://www.linuxdynasty.org/forums/Scripting/scripting/snmp_branch_help">http://www.linuxdynasty.org/forums/Scripting/scripting/snmp_branch_help</a><br />
You can download the script <a href="View-details/Zenoss/29-snmp_branch.py.html">snmp_branch.py</a></p>
<ul>
<li>Update 1.0.10
<ol>
<li>Fixed labeling bug, (Thanks Stephan26 for finding this)</li>
<li>Added --fsearch option<br />
Thanks Stephan26 for suggesting to add a way to find OID's by their begining Digits on their last Octect</li>
<li>Added --length option<br />
This will allow you to search for an Index on the final Octect of the OID, when the final octect is not just the index.<br />
Example.... You want the index OID of 100 but the entire last octect of the OID is .6534389100)</li>
</ol>
</li>
</ul>
<p>&nbsp;</p>
<p>So here is an example below of what the data looks like from SNMP..</p>
<pre>UCD-SNMP-MIB::ssIndex.0 = INTEGER: 1UCD-SNMP-MIB::ssSwapIn.0 = INTEGER: 0UCD-SNMP-MIB::ssSwapOut.0 = INTEGER: 0UCD-SNMP-MIB::ssIOSent.0 = INTEGER: 0UCD-SNMP-MIB::ssIOReceive.0 = INTEGER: 1UCD-SNMP-MIB::ssSysInterrupts.0 = INTEGER: 3|UCD-SNMP-MIB::ssSysContext.0 = INTEGER: 19UCD-SNMP-MIB::ssCpuUser.0 = INTEGER: 7UCD-SNMP-MIB::ssCpuSystem.0 = INTEGER: 7UCD-SNMP-MIB::ssCpuIdle.0 = INTEGER: 84</pre>
<p>&nbsp;</p>
<p><a id="more"></a><a id="more-77"></a></p>
<pre>UCD-SNMP-MIB::ssCpuRawUser.0 = Counter32: 4891073 
UCD-SNMP-MIB::ssCpuRawNice.0 = Counter32: 64793 
UCD-SNMP-MIB::ssCpuRawSystem.0 = Counter32: 4617885 
UCD-SNMP-MIB::ssCpuRawIdle.0 = Counter32: 148113219
UCD-SNMP-MIB::ssCpuRawWait.0 = Counter32: 671245 
UCD-SNMP-MIB::ssCpuRawKernel.0 = Counter32: 4399675 
UCD-SNMP-MIB::ssCpuRawInterrupt.0 = Counter32: 71505 
UCD-SNMP-MIB::ssIORawSent.0 = Counter32: 261953540 
UCD-SNMP-MIB::ssIORawReceived.0 = Counter32: 904164 
UCD-SNMP-MIB::ssRawInterrupts.0 = Counter32: 821108747 
UCD-SNMP-MIB::ssRawContexts.0 = Counter32: 115659352 
UCD-SNMP-MIB::ssCpuRawSoftIRQ.0 = Counter32: 146705 
UCD-SNMP-MIB::ssRawSwapIn.0 = Counter32: 0 
UCD-SNMP-MIB::ssRawSwapOut.0 = Counter32: 0</pre>
<p>Now most people would not want to graph all of these OID's, but hey you never know.... Now for the above you could just enter ONE OID<br />
per Data Source and a Data Point.... Or you can create one Data Source and Multipel Data Points..... Example below...</p>
<pre>/opt/zenoss/libexec/snmp_branch.py -d zenoss -c public -o 1.3.6.1.4.1.2021.11 -p 161 --label="ssIndex, ssErrorName, ssSwapIn, ssSwapOut, ssIOSent, ssIOReceive, ssSysInterrupts, ssSysContext, ssCpuUser, ssCpuSystem, ssCpuIdle, 12, ssCpuRawNice,  ssCpuRawSystem, ssCpuRawIdle, ssCpuRawWait, ssCpuRawKernel, ssCpuRawInterrupt, ssIORawSent, ssIORawReceived,  ssRawInterrupts, ssRawContexts, ssCpuRawSoftIRQ, ssRawSwapIn, ssRawSwapOut"</pre>
<p>Here is the output below. Mind you the output is valid for the Nagios Api. Which means we will be able to create Data Points.</p>
<pre><strong>|ssIndex=1 ssErrorName=systemStats ssSwapIn=0 ssSwapOut=0 ssIOSent=0 ssIOReceive=1 
ssSysInterrupts=3 ssSysContext=19 ssCpuUser=4 ssCpuSystem=3 ssCpuIdle=92 
12=4892383 ssCpuRawNice=64793 ssCpuRawSystem=4619154 ssCpuRawIdle=148138615 
ssCpuRawWait=671279 ssCpuRawKernel=4400910 ssCpuRawInterrupt=71516 
ssIORawSent=261993492 ssIORawReceived=904164 ssRawInterrupts=821253241 
ssRawContexts=115685918 ssCpuRawSoftIRQ=146728 ssRawSwapIn=0 ssRawSwapOut=0</strong></pre>
<p>Now you do not have to create a label for each OID, but I would recommend that you do since I assume you<br />
want labels that actually mean something. But just in case that you do not, the default is to print default and<br />
a number after it. So for example default0=88888. Also lets say you do want to add at least one label,<br />
well you can do just that just add for example --label="cpu".<br />
This will do the same as the default so the output would becpu0=999 cpu1=999.</p>
<p><strong>New Update to the above.... Thanks to a zenoss user named j053ph</strong></p>
<p>The plugin now supports grabbing the index of an OID for instance...</p>
<pre> [root@dynasty ~]# <strong>snmpwalk -v2c -c public localhost .1.3.6.1.2.1.25.2.3 | grep -P ".3"</strong></pre>
<pre>HOST-RESOURCES-MIB::hrStorageIndex.3 = INTEGER: 3
HOST-RESOURCES-MIB::hrStorageType.3 = OID: HOST-RESOURCES-TYPES::hrStorageVirtualMemory
HOST-RESOURCES-MIB::hrStorageDescr.3 = STRING: Swap Space
HOST-RESOURCES-MIB::hrStorageAllocationUnits.3 = INTEGER: 1024 Bytes
HOST-RESOURCES-MIB::hrStorageSize.3 = INTEGER: 2096472
HOST-RESOURCES-MIB::hrStorageUsed.3 = INTEGER: 232</pre>
<p>&nbsp;</p>
<pre>[root@dynasty ~]#/opt/zenoss/libexec/snmp_branch.py -c public -d localhost -p 161 \
-o 1.3.6.1.2.1.25.2.3.1 --ival="3" --label="diskIndex,diskType,diskDescr,diskAlloc,diskSize,diskused"\
|diskIndex=3 diskType=(1 3 6 1 2 1 25 2 1 3) diskDescr=Swap Space diskAlloc=1024 \
diskSize=2096472 diskused=232</pre>
<p>Another example</p>
<pre><span class="postbody"> [root@dynasty ~]#snmpwalk -v2c -c public localhost 1.3.6.1.2.1.2.2.1 | grep -P ".2"
IF-MIB::ifIndex.2 = INTEGER: 2
IF-MIB::ifDescr.2 = STRING: eth0
IF-MIB::ifType.2 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifMtu.2 = INTEGER: 1500
IF-MIB::ifSpeed.2 = Gauge32: 100000000
IF-MIB::ifPhysAddress.2 = STRING: 0:2:b3:b7:e3:c0
IF-MIB::ifAdminStatus.2 = INTEGER: up(1)
IF-MIB::ifOperStatus.2 = INTEGER: up(1)
IF-MIB::ifLastChange.2 = Timeticks: (0) 0:00:00.00
IF-MIB::ifInOctets.2 = Counter32: 3100215763
IF-MIB::ifInUcastPkts.2 = Counter32: 104423294
IF-MIB::ifInNUcastPkts.2 = Counter32: 0
IF-MIB::ifInDiscards.2 = Counter32: 0
IF-MIB::ifInErrors.2 = Counter32: 0
IF-MIB::ifInUnknownProtos.2 = Counter32: 0
IF-MIB::ifOutOctets.2 = Counter32: 2258585248
IF-MIB::ifOutUcastPkts.2 = Counter32: 84530414
IF-MIB::ifOutNUcastPkts.2 = Counter32: 0
IF-MIB::ifOutDiscards.2 = Counter32: 0
IF-MIB::ifOutErrors.2 = Counter32: 0
IF-MIB::ifOutQLen.2 = Gauge32: 0
IF-MIB::ifSpecific.2 = OID: SNMPv2-SMI::zeroDotZero</span></pre>
<p><span class="postbody"><br />
</span></p>
<pre>[root@dynasty ~]#/opt/zenoss/libexec/snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1 --ival="2" --label="ifIndex,ifDescr,ifType,ifMtu,ifSpeed,ifPhysAddress,ifAdminStatus,ifOperStatus,ifLastChange,ifInOctets,ifInUcastPkts,ifInNUcastPkts,ifInDiscards,ifInErrors,ifInUnknownProtos,ifOutOctets,ifOutUcastPkts,ifOutNUcastPkts,ifOutDiscards,ifOutErrors,ifOutQLen,ifSpecific"

|ifIndex=2 ifDescr=eth0 ifType=6 ifMtu=1500 ifSpeed=100000000 ifPhysAddress=\x00\x02\xb3\xb7\xe3\xc0 ifAdminStatus=1ifOperStatus=1 ifLastChange=0 ifInOctets=3100243441 ifInUcastPkts=104423605 ifInNUcastPkts=0 ifInDiscards=0 ifInErrors=0ifInUnknownProtos=0 ifOutOctets=2258608324 ifOutUcastPkts=84530576 ifOutNUcastPkts=0 ifOutDiscards=0 ifOutErrors=0ifOutQLen=0 ifSpecific=(0 0)</pre>
<p>Lets say you do a snmpwalk to a host and you want the OIDS that only match the first few Digits of the final Octets...</p>
<pre>Name/OID: .1.3.6.1.2.1.2.2.1.10.805306369; Value (Counter32): 2566470483     Name/OID: .1.3.6.1.2.1.2.2.1.10.805306370; Value (Counter32):   3179025023   Name/OID: .1.3.6.1.2.1.2.2.1.10.805306371; Value (Counter32): 0   Name/OID: .1.3.6.1.2.1.2.2.1.10.805306372; Value (Counter32): 0   Name/OID: .1.3.6.1.2.1.2.2.1.10.805306373; Value (Counter32):   2395861415   Name/OID: .1.3.6.1.2.1.2.2.1.10.805306374; Value (Counter32): 0   Name/OID: .1.3.6.1.2.1.2.2.1.10.805306375; Value (Counter32): 0   Name/OID: .1.3.6.1.2.1.2.2.1.10.1073741824; Value (Counter32): 0   Name/OID: .1.3.6.1.2.1.2.2.1.10.1073741825; Value (Counter32):   140134400   Name/OID: .1.3.6.1.2.1.2.2.1.10.1073741826; Value (Counter32): 0   Name/OID: .1.3.6.1.2.1.2.2.1.10.1073741827; Value (Counter32):   377893040   Name/OID: .1.3.6.1.2.1.2.2.1.10.1073741825; Value (Counter32):   173081872</pre>
<p>Quoting Stephan26....... But i only wanted to import the OID ending with ...10.1073xxxx into Zenoss (there are hundreds of them), so now all i have to do is use the --fsearch function in the snmp_branch.py script as so:<br />
Here is an example using the --fsearch option..</p>
<pre>[zenoss@lqc90990smon01 libexec]$ python   /opt/zenoss/libexec/snmp_branch_search.py -c public -d swm48_220_sw0 -p   161 -o .1.3.6.1.2.1.2.2.1.10 --fsearch="1073"  |default0=0 default1=2919865312 default2=0 default3=3661123408   default4=2269960320 default5=0 default6=0 default7=0 default8=3135432112   default9=220838336 default10=0 default11=0 default12=3562923072   default13=1742625920 default14=0 default15=3200104576   default16=1732443344 default17=0 default18=3463670544   default19=1132119840 default20=1296033888 default21=0 default22=0   default23=0 default24=220421488 default25=2772715952 default26=0   default27=0 default28=2869249536 default29=2645500784 default30=0   default31=0 default32=4270207264 default33=0 default34=1884162416</pre>
<p>Now lets say you need a Index OID that ends in 25, but the final octect includes more then just the indexed OID...<br />
Example....<br />
Name/OID: .1.3.6.1.2.1.2.2.1.10.1073741825; Value (Counter32): 173081872<br />
As you can see the Final Octect is 10 digits long. If you were to use just the --ival option, it will not work. Because the --ival option matches ".ival" ( Which means it matches the final octect, because ival assumes that the final octect is the ival. With the --length option and --ival option, this is no longer true..</p>
<p>With the --length option it will make sure it just matches the length of the oid minus the length of the ival plus matching ival at the end.<br />
Example...</p>
<pre>snmpwalk -v2c -On -c public localhost 1.3.6.1.2.1.25.4.2.1.1 |grep -P "1045".1.3.6.1.2.1.25.4.2.1.1.1045 = INTEGER: 1045

python snmp_branch.py -c public -d localhost -p 161 -o .1.3.6.1.2.1.25.4.2.1.1 --ival="45" --length=4|default0=1045</pre>
<p>Here is an example using the --length option with the --ival option</p>
<p><a href="images/stories/screenshots/snmp_branch.png" rel="shadowbox[0]"><img style="width: 456px; height: 497px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/snmp_branch.png" alt="" /></a></p>
<p>&nbsp;</p>
<p>Here are more examples below on how you would run the script.....<br />
example from Zenoss gui.....<br />
snmp_branch.py -d ${here/manageIp} -c ${here/zSnmpCommunity} -o 1.3.6.1.4.1.9.9.416.1.3.1.1.5 -p 161 --label="background0,<br />
bestEffort0, video0, voice0, background1, bestEffort1, video1, voice1"<br />
|background0=44896 bestEffort0=739905 video0=0 voice0=1318 background1=3812 bestEffort1=62451 video1=0 voice1=139</p>
<p>example from command line with labels....<br />
snmp_branch.py -d 127.0.0.1 -c public -o 1.3.6.1.4.1.9.9.416.1.3.1.1.5 -p 161 --label="background0, bestEffort0, video0, voice0,<br />
background1, bestEffort1, video1, voice1"<br />
|background0=44896 bestEffort0=739905 video0=0 voice0=1318 background1=3812 bestEffort1=62451 video1=0 voice1=139</p>
<p>example with out labels....<br />
snmp_branch.py -d ${here/manageIp} -c ${here/zSnmpCommunity} -o 1.3.6.1.4.1.2334.2.1.2.2.1.14 -p 161<br />
|default0=55174635 default1=63348274</p>
<p>example with one label.....<br />
snmp_branch.py -d ${here/manageIp} -c ${here/zSnmpCommunity} -o 1.3.6.1.4.1.2334.2.1.2.2.1.14 -p 161 --label="eth"<br />
|eth0=55174635 eth1=63348274</p>
<pre>-c, --community=   SNMP Community To Use -d, --device=      Device Name or IP Address -o, --oid=         The SNMP OID To Walk -p, --port=        The SNMP Port To Use, usually 161 -l, --label=       This will be a list of lables that you want applied to each data point "Inside_Link, Outside_link" -i, --ival=        This will grab the index specified and all of its oid's related to that index -l, --length=      This option with the --ival option will give you an exact match of the indexed OID. In most cases, the indexed oid  is like this .1 or .100, but there are special cases where the indexed OID is .46432510 Now you only want to match 10 and you do not care for the rest. Example... snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1.16 --ival="24" --length="9" -f, --fsearch      This option does not work with ival or length. This options is for certain special cases where you only wach to match  the begining digits of the last octect of the OID (.1.3.6.1.2.1.2.2.1.16.1073741824). Example... snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1.16 --fsearch="1073" -v, --version=     SNMP Version 1 or SNMP Version 2</pre>
<p>&nbsp;</p>
<p>Below is the Screenshot of the template I created... You can see I only created 4 OID's to monitor, but in reality they are 4 branch OID's<br />
which contain 8 child OID's in each one. So all I had to do was create the 8 datapoints and on Data Source for each Branch IOD</p>
<p><a href="images/stories/screenshots/ZenTemplate.png" rel="shadowbox[0]"><img src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/ZenTemplate.png" alt="" width="415" height="254" /></a></p>
