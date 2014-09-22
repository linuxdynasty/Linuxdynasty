---
layout: post
status: publish
published: true
title: Syncing up Zenoss with the Citrix Netscaler using Python
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p><span class=\"dropcap\">T</span>he script below I created to sync up
  Zenoss with the Citrix Netscalers. What this will do essentially is make sure that
  all of our devices in Zenoss are in the correct Systems in Zenoss. So for instance
  lets say we have a cluster called Foo-Cluster and we have 100 devices that are in
  that cluster as per the netscaler. This script will move those 100 devices into
  that System aka {Cluster} in Zenoss.</p>\r\n<p>\r\n<p>The reason this is so important
  is that when you update the Citrix Netscaler you will also have to update Zenoss,
  but if you run this script in cron then you will not have to update Zenoss at all.
  This script was written in <a type=\"amzn\" search=\"Python Core\">Python</a> <span
  class=\"attention\">This script was tested with Zenoss 2.0.2, Also some modifications
  may have to be made to fit your environment.</span></p>\r\n<p>Please post any questions
  to this script here <a href=\"http://linuxdynasty.org/phpBB3/viewtopic.php?f=5&amp;t=3\"
  title=\"\">http://linuxdynasty.org/phpBB3/viewtopic.php?f=5&amp;t=3</a> <br />\r\nYou
  can download the script here&nbsp; ... <a href=\"http://www.linuxdynasty.org/View-details/Zenoss/20-zenoss_netscaler_snmp.py.html\"
  title=\"\">zenoss_netscaler_snmp.py</a><br />\r\n</p></p>\r\n<p>\r\n<p><br />\r\n<br
  />&nbsp;</p></p>\r\n<br />"
wordpress_id: 193
wordpress_url: http://linuxdynasty.org/?p=193
date: !binary |-
  MjAwOC0wNi0xNyAxOTo0ODoyOCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNi0xNyAxOTo0ODoyOCAtMDQwMA==
categories:
- Zenoss
tags:
- Zenoss
- Syncing up Zenoss with the Citrix Netscaler using Python
comments: []
---
<p><span class="dropcap">T</span>he script below I created to sync up Zenoss with the Citrix Netscalers. What this will do essentially is make sure that all of our devices in Zenoss are in the correct Systems in Zenoss. So for instance lets say we have a cluster called Foo-Cluster and we have 100 devices that are in that cluster as per the netscaler. This script will move those 100 devices into that System aka {Cluster} in Zenoss.</p>
<p><p>The reason this is so important is that when you update the Citrix Netscaler you will also have to update Zenoss, but if you run this script in cron then you will not have to update Zenoss at all. This script was written in <a type="amzn" search="Python Core">Python</a> <span class="attention">This script was tested with Zenoss 2.0.2, Also some modifications may have to be made to fit your environment.</span></p>
<p>Please post any questions to this script here <a href="http://linuxdynasty.org/phpBB3/viewtopic.php?f=5&amp;t=3" title="">http://linuxdynasty.org/phpBB3/viewtopic.php?f=5&amp;t=3</a> <br />
You can download the script here&nbsp; ... <a href="http://www.linuxdynasty.org/View-details/Zenoss/20-zenoss_netscaler_snmp.py.html" title="">zenoss_netscaler_snmp.py</a></p></p>
<p>
<p>&nbsp;</p></p>
<p><a id="more"></a><a id="more-193"></a></p>
