---
layout: post
status: publish
published: true
title: HowTo add Multiple DataPoints to Zenoss using the Zenoss API
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "I've seen a few people in the Zenoss community forums asking for an easier
  way to add multiple Datapoints into Zenoss, instead of adding 1 by 1. Well, I've
  decided to try and build such a tool today. Now even though the tool is not complete
  (IN MY EYES). It is already has been helpful to me! As of right now the script can
  List Templates in a Organizer ( aka /Devices/Server/Linux ) or in a Device ( zenoss1.linuxdynasty
  ).\r\n\r\nIt can also create a Template, with a Command DataSource, with Multiple
  DataPoints. This means you can now automate the creation of Templates and DataSources
  and DataPoints. So if you are using a tool like Puppet, Cfengine, Bcfg2, or Chef,
  this process can be automated. I will be adding more features in the next few weeks.\r\n\r\nAny
  question or help about this script, please post them here <a href=\"forums/Scripting/scripting/ZenossTemplateManager\">http://www.linuxdynasty.org/forums/Scripting/scripting/ZenossTemplateManager</a>\r\n<span
  style=\"text-decoration: underline;\"><strong>UPDATES!!!!!!</strong></span>\r\n<ul>\r\n\t<li>Update
  1.0.6, Fixed an issue where if youdo not pass the -G option for graph it will fail.</li>\r\n\t<li>Update
  1.0.5, Now have the ability to add multiple graphs with multiple datapoints</li>\r\n\t<li>Update
  1.0.4, Now have the ability to create thresholds, bind templates to class or device,
  set severities on thresholds and\r\ndatasources, attach datapoints to thresholds.</li>\r\n\t<li>Update
  1.0.3, I broke down the templateManager function into 3 smaller functions. You also
  can now list templates and datasources for either device or organizer, and list
  datapoints for a device. I also added more verbosity with the -V option.</li>\r\n\t<li>Update
  1.0.2, You now do not have to pass a command with the script. So i f you already
  have a command in the DataSource, it wll not get overwritten.. Thank you Eangel,
  for telling me about this issue..</li>\r\n</ul>\r\nUpcoming Features such as....\r\n<ul>\r\n\t<li>Deleteing
  Templates, DataSources, and DataPoints</li>\r\n\t<li>Copying Templates</li>\r\n\t<li>Adding
  Graphs</li>\r\n</ul>\r\nThe tool is called Zenoss_Template_Manager.py. You can download
  it here..\r\n{filelink=3}\r\n\r\n"
wordpress_id: 194
wordpress_url: http://linuxdynasty.org/?p=194
date: !binary |-
  MjAxMC0wMy0wNSAwNDoxMjoyNiAtMDUwMA==
date_gmt: !binary |-
  MjAxMC0wMy0wNSAwNDoxMjoyNiAtMDUwMA==
categories:
- Zenoss
tags:
- Zenoss
- API
- Zenoss Device Templates
comments: []
---
<p>I've seen a few people in the Zenoss community forums asking for an easier way to add multiple Datapoints into Zenoss, instead of adding 1 by 1. Well, I've decided to try and build such a tool today. Now even though the tool is not complete (IN MY EYES). It is already has been helpful to me! As of right now the script can List Templates in a Organizer ( aka /Devices/Server/Linux ) or in a Device ( zenoss1.linuxdynasty ).</p>
<p>It can also create a Template, with a Command DataSource, with Multiple DataPoints. This means you can now automate the creation of Templates and DataSources and DataPoints. So if you are using a tool like Puppet, Cfengine, Bcfg2, or Chef, this process can be automated. I will be adding more features in the next few weeks.</p>
<p>Any question or help about this script, please post them here <a href="forums/Scripting/scripting/ZenossTemplateManager">http://www.linuxdynasty.org/forums/Scripting/scripting/ZenossTemplateManager</a><br />
<span style="text-decoration: underline;"><strong>UPDATES!!!!!!</strong></span></p>
<ul>
<li>Update 1.0.6, Fixed an issue where if youdo not pass the -G option for graph it will fail.</li>
<li>Update 1.0.5, Now have the ability to add multiple graphs with multiple datapoints</li>
<li>Update 1.0.4, Now have the ability to create thresholds, bind templates to class or device, set severities on thresholds and<br />
datasources, attach datapoints to thresholds.</li>
<li>Update 1.0.3, I broke down the templateManager function into 3 smaller functions. You also can now list templates and datasources for either device or organizer, and list datapoints for a device. I also added more verbosity with the -V option.</li>
<li>Update 1.0.2, You now do not have to pass a command with the script. So i f you already have a command in the DataSource, it wll not get overwritten.. Thank you Eangel, for telling me about this issue..</li>
</ul>
<p>Upcoming Features such as....</p>
<ul>
<li>Deleteing Templates, DataSources, and DataPoints</li>
<li>Copying Templates</li>
<li>Adding Graphs</li>
</ul>
<p>The tool is called Zenoss_Template_Manager.py. You can download it here..<br />
{filelink=3}</p>
<p><a id="more"></a><a id="more-194"></a></p>
<p>Here are some examples....</p>
<pre>Examples: python Zenoss_Template_Manager.py -d "zenoss.linuxdynasty" -c'/opt/zenoss/libexec/snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1 --ival="1" --label="ifIndex,ifDescr,ifType,ifMtu,ifSpeed,ifPhysAddress,ifAdminStatus,ifOperStatus,ifLastChange,ifInOctets,ifInUcastPkts,ifInNUcastPkts,InDiscards,ifInErrors,ifInUnknownProtos,ifOutOctets,ifOutUcastPkts,ifOutNUcastPkts,ifOutDiscards,ifOutErrors,ifOutQLen,ifSpecific"'--template=TESTER4LIFE2 -p "ifSpeed,G" -p "ifInOctets,C" -p "ifInUcastPkts,C" -p "ifInNUcastPkts,C" -p "ifInDiscards,C" -p "ifInErrors,C" -p "ifOutOctets,C" -p "ifOutUcastPkts,C" -p "ifOutNUcastPkts,C" -p "ifOutDiscards,C" -p "ifOutErrors,C" --dsource="WoW2</pre>
<p>If you already have the command in place for that DataSource, then run the script with out the -c option...</p>
<p>Examples:</p>
<pre>python Zenoss_Template_Manager.py -d "zenoss.linuxdynasty" --template=TESTER4LIFE2 \
-p "ifSpeed,G" -p "ifInOctets,C" -p "ifInUcastPkts,C" -p "ifInNUcastPkts,C" -p "ifInDiscards,C" \
-p "ifInErrors,C" -p "ifOutOctets,C" -p "ifOutUcastPkts,C" -p "ifOutNUcastPkts,C" -p "ifOutDiscards,C" \
-p "ifOutErrors,C" --dsource="WoW2"</pre>
<p>Another Example With The Verbose Option..</p>
<pre>[zenoss@zenoss2 ~]$ python Zenoss_Template_Manager.py -o "/Devices/Server/Linux" \
-c '/opt/zenoss/libexec/snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1 --ival="1"
--label="ifIndex,ifDescr,ifType,ifMtu,ifSpeed,ifPhysAddress,ifAdminStatus,ifOperStatus,ifLastChange,ifInOctets,ifInUcastPkts,
ifInNUcastPkts,InDiscards,ifInErrors,ifInUnknownProtos,ifOutOctets,ifOutUcastPkts,ifOutNUcastPkts,ifOutDiscards,ifOutErrors,ifOutQLen,ifSpecific"' \
-t FooYoo -p "ifSpeed,G" -p "ifInOctets,C" -p "ifInUcastPkts,C" -p "ifInNUcastPkts,C" -p "ifInDiscards,C" -p "ifInErrors,C" -p "ifOutOctets,C" -p "ifOutUcastPkts,C" \
-p "ifOutNUcastPkts,C" -p "ifOutDiscards,C" -p "ifOutErrors,C" -s "eth0" -S "Critical" -P "Nagios" -b -V

Template FooYoo already exists at /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYooBinded Templates : ['Shaolin', 'Device', 'NtpMonitor', 'TESTER4L1F3', 'TESTER', 'FooYoo', 'FooYoo']DataSource eth0 already exists at /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0Command /opt/zenoss/libexec/snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1 --ival="1" --label="ifIndex,ifDescr,ifType,ifMtu,ifSpeed,ifPhysAddress,ifAdminStatus,ifOperStatus,ifLastChange,ifInOctets,ifInUcastPkts,ifInNUcastPkts,InDiscards,ifInErrors,ifInUnknownProtos,ifOutOctets,ifOutUcastPkts,ifOutNUcastPkts,ifOutDiscards,ifOutErrors,ifOutQLen,ifSpecific" has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0Parser = NagiosSeverity = 5eth0 DataSource is EnabledDataPoint ifSpeed of type GAUGE has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifInOctets of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifInUcastPkts of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifInNUcastPkts of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifInDiscards of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifInErrors of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifOutOctets of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifOutUcastPkts of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifOutNUcastPkts of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifOutDiscards of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint ifOutErrors of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0</pre>
<p>I also added the ability to list templates, datasources, and datapoints...<br />
Examples Below...</p>
<pre>python Zenoss_Template_Manager.py -d "qazenoss" --list="datapoints" -t "TESTER4LIFE2"
ifInDiscards /zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifInDiscardsifInErrors
/zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifInErrorsifInNUcastPkts
/zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifInNUcastPktsifInOctets
/zport/dmd/Devices/Server/Tomcat/qdevices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifInOctetsifInUcastPkts
/zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifInUcastPktsifOutDiscards
/zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifOutDiscardsifOutErrors
/zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifOutErrorsifOutNUcastPkts
/zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifOutNUcastPktsifOutOctets
/zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifOutOctetsifOutUcastPkts
/zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifOutUcastPktsifSpeed
/zport/dmd/Devices/Server/Tomcat/devices/qazenoss/TESTER4LIFE2/datasources/WoW2/datapoints/ifSpeed</pre>
<p>&nbsp;</p>
<pre>python Zenoss_Template_Manager.py -o "/Devices/Server/Tomcat" -l "datasources" -t "Tomcat Thread Pool"
Tomcat Current Thread Count
/zport/dmd/Devices/Server/Tomcat/rrdTemplates/Tomcat%20Thread%20Pool/datasources/Tomcat%20Current%20Thread%20CountTomcat
Current Threads Busy /zport/dmd/Devices/Server/Tomcat/rrdTemplates/Tomcat%20Thread%20Pool/datasources/Tomcat%20Current%20Threads%20Busy

python Zenoss_Template_Manager.py -o "/Devices/Server/Tomcat" -l "templates"
DigMonitor
/zport/dmd/Devices/Server/rrdTemplates/DigMonitorFtpMonitor
/zport/dmd/Devices/rrdTemplates/FtpMonitorJava
/zport/dmd/Devices/rrdTemplates/Java</pre>
<p>Example of creating a Threshold..</p>
<pre>[zenoss@zenoss ~]$ python Zenoss_Template_Manager.py -o "/Devices/Server/Linux" -t FooYoo -T FooYee -p "eth0_ifInOctets" -s "eth0" -S "Warning" -m 0 -M 20 -V

Template FooYoo already exists at /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYooDataSource
eth0 already exists at /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0FooYee
threshold created at /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/thresholds/FooYeeminval = 0maxval = 20Severity = 3
eth0_ifInOctets datapoint added to threshold /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/thresholds/FooYeeFooYee
Threshold is Enabled</pre>
<p>Now here is an example of Adding Graphs..</p>
<p><span class="attention"> Remember, when adding DataPoints to your graphs, you are adding the name of the DataSource_Datapoint. You can see what the names of the DataPoints you have available by using the --list="datapoints" option with the --template=TEMPLATE_NAME option</span></p>
<pre>python Zenoss_Template_Manager.py -d "zenoss.linuxdynasty" -t "TESTER" -G "eth0 Discards, eth0_ifInDiscards, eth0_ifOutDiscards, units=discards"</pre>
<p>here is an example of adding graphs with a template and a datasource and multiple datapoints..</p>
<pre>python Zenoss_Template_Manager.py -o "/Devices/Server/Linux" -c '/opt/zenoss/libexec/snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1 --ival="1" \
--label="ifIndex,ifDescr,ifType,ifMtu,ifSpeed,ifPhysAddress,ifAdminStatus,ifOperStatus,ifLastChange,ifInOctets,ifInUcastPkts,ifInNUcastPkts,InDiscards,ifInErrors,ifInUnknownProtos,ifOutOctets,ifOutUcastPkts,ifOutNUcastPkts,ifOutDiscards,ifOutErrors,ifOutQLen,ifSpecific"' \
-t FooYoo -p "ifSpeed,G" -p "ifInOctets,C" -p "ifInUcastPkts,C" -p "ifInNUcastPkts,C" -p "ifInDiscards,C" -p "ifInErrors,C" -p "ifOutOctets,C" -p "ifOutUcastPkts,C" -p "ifOutNUcastPkts,C" -p "ifOutDiscards,C" -p "ifOutErrors,C"\
 -s "eth0" -S "Critical" -P "Nagios" -b -G "eth0 Discards, eth0_ifInDiscards, eth0_ifOutDiscards, units=discards" -G "eth1 Discards, eth0_ifInDiscards, eth0_ifOutDiscards, units=discards" -V

Template FooYoo created at /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYooBinded Templates : ['Shaolin', 'Device', 'NtpMonitor', 'TESTER4L1F3', 'TESTER', 'FooYoo', 'FooYoo']
DataSource eth0 created at /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0Parser = NagiosCommand /opt/zenoss/libexec/snmp_branch.py -c public -d localhost -p 161 -o 1.3.6.1.2.1.2.2.1 --ival="1" --label="ifIndex,ifDescr,ifType,ifMtu,ifSpeed,ifPhysAddress,ifAdminStatus,ifOperStatus,ifLastChange,ifInOctets,ifInUcastPkts,ifInNUcastPkts,InDiscards,ifInErrors,ifInUnknownProtos,ifOutOctets,ifOutUcastPkts,ifOutNUcastPkts,ifOutDiscards,ifOutErrors,ifOutQLen,ifSpecific" has been added to DataSource 
/zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0Severity = 5
eth0 DataSource is EnabledDataPoint 
ifSpeed of type GAUGE has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifInOctets of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifInUcastPkts of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifInNUcastPkts of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifInDiscards of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifInErrors of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifOutOctets of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifOutUcastPkts of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifOutNUcastPkts of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifOutDiscards of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0DataPoint 
ifOutErrors of type COUNTER has been added to DataSource /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/datasources/eth0
eth0 Discards graph was created with ['eth0_ifInDiscards', 'eth0_ifOutDiscards'] 
DataPoints attached at /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/graphDefs/eth0%20Discards
eth1 Discards graph was created with ['eth0_ifInDiscards', 'eth0_ifOutDiscards'] 
DataPoints attached at /zport/dmd/Devices/Server/Linux/rrdTemplates/FooYoo/graphDefs/eth1%20Discards</pre>
<p>To see the Help output, just run it like this <strong><span style="text-decoration: underline;">python Zenoss_Template_Manager.py -h</span></strong></p>
