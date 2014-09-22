---
layout: post
status: publish
published: true
title: Monitoring RabbitMQ with Zenoss
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 198
wordpress_url: http://linuxdynasty.org/?p=198
date: !binary |-
  MjAxMC0wOS0xMCAxNjoxNzowMyAtMDQwMA==
date_gmt: !binary |-
  MjAxMC0wOS0xMCAxNjoxNzowMyAtMDQwMA==
categories:
- Zenoss
tags:
- Zenoss
- Monitoring RabbitMQ with Zenoss
comments: []
---
<p>RabbitMQ was recently deployed in the company I currently work for. At the last minute ( as always ) they came to me and ask me to please add RabbitMQ monitoring to Zenoss. They said here is the url and now please monitor for a few stats ( <a href="http://www.lshift.net/blog/2009/11/30/introducing-rabbitmq-status-plugin">using the RabbitMQ Status Plugi</a>n ). So I said to myself, I could easily just write a quick shell script to get the 3 stats that they needed and add them into Zenoss. After thinking about it.... In the near future they might ask for more than those 3 stats. So I decided to write a quick python script ( Zenoss Compatible ) to get all the stats from that status page and input them into Zenoss...</p>
<p>Prerequisites</p>
<ol>
<li>Zenoss 2.5 and above ( I have not tested on 3.+ or &lt;2 .4 )</li>
<li>lxml Python module    "<strong>easy_install lxml</strong>" as the zenoss user</li>
<li>"<strong><a href="View-details/Zenoss/54-Zenoss_Template_Manager.html">Zenoss_Template_Manager.py</a></strong>" Optional, Only needed if you do not want to add all the datapoints manually... I DON'T!!!!</li>
<li>RabbitMQ Installed</li>
<li>RabbitMQ Status Plugin from <a href="http://www.lshift.net/blog/2009/11/30/introducing-rabbitmq-status-plugin">http://www.lshift.net/blog/2009/11/30/introducing-rabbitmq-status-plugin</a></li>
<li>"<strong><a href="View-details/LD-Network-Manager-Project/60-RabiitMQ-monitoring-Zenoss-Style.html">check_rabbitmq.py</a></strong>"</li>
</ol>
<p>Zenoss Template Manager = {filelink=3}</p>
<p>CheckRabbitMQ.py = {filelink=2}</p>
<p>Once you have all the above, we are ready to go..</p>
<ol>
<li>copy both Python Scripts above into the /opt/zenoss/libexec/ folder  ( If you are using RedHat/CentOS ) and make sure they are executable.</li>
</ol>
<p>As the Zenoss user run the script ....<br />
/opt/zenoss/libexec/check_rabbitmq.py -u 'http://rabbitmq-server:55672' -a 'mon-user mon-passwd' |sed -re "s/^OK|/ /g" |sed -re "s/([A-Za-z0-9_.]+*)?=[0-9]+/-p "1,G"/g" |xargs /opt/zenoss/libexec/Zenoss_Template_Manager.py -o "/Devices/Server/Linux/RabbitMQ" -c '/opt/zenoss/libexec/check_rabbitmq.py -u "http://rabbitmq-server:55672" -a "mon-user mon-passwd"' --template=RabbitMQ --dsource=RabbitMQStats -V $1</p>
<p>If you need to know how to use the Zenoss_Template_Manager.y script, check here <a href="howto-add-multiple-datapoints-to-zenoss-using-the-zenoss-api.html">http://www.linuxdynasty.org/howto-add-multiple-datapoints-to-zenoss-using-the-zenoss-api.html</a></p>
<p>So let me explain what the sed statements above are doing...</p>
<ul>
<li>"sed -re "s/^OK|/ /g"" This sed statement is removing the OK| from the beginning of the line</li>
<li>"sed -re "s/([A-Za-z0-9_.]+*)?=[0-9]+/-p "1,G"/g"<br />
This 1st part of the sed statement is matching any letter,number,underscore, and period, any number of times until it reaches the equal "="  "<strong>[A-Za-z0-9_.]+*)?=</strong>"<br />
The  2nd part of this statement is going to match the "=" and any number of integers after it. "<strong>[0-9]+</strong>"<br />
Now we need to make the substitution.... So we are going to substitute, every match with a -p,  then a space and then the 1st group match in escaped quotes, then a comma and G for GAUGE.</li>
</ul>
<p>The 2 sed statements above will do that for every match it finds. If you were to add each datapoint by hand, it would look like this....<br />
/opt/zenoss/libexec/Zenoss_Template_Manager.py -o "/Devices/Server/Linux//RabbitMQ" -c '/opt/zenoss/libexec/check_rabbitmq.py -u "http://rabbitmq-server:55672" -a "mon-user mon-passwd"' --template=RabbitMQ --dsource=RabbitMQStats -V -p "queue.conversion.event.tracking_msg_unack,G" -p "connections,G" -p "erlang_processes_used,G" -p "erlang_processes_avail,G" -p "file_descriptors_used,G" -p "file_descriptors_avai,G" -p "binary_memory,G" -p "memory_used,G" -p "memory_avail,G"</p>
<p>I hope the above scripts will save someone time and frustration......</p>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 162px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">connections=26 erlang_processes_used=252 erlang_processes_avail=1048576 file_descriptors_used=1 file_descriptors_avail=1024 pid=3167  binary_memory=0 ets_memory=0  memory_used=27 memory_avail=99</div>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 162px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">3</div>
<p>&nbsp;</p>
