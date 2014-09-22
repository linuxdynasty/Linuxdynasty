---
layout: post
status: publish
published: true
title: Check ESX Datastores using Python and CIM
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>Good Afternoon guys, here I created another Python Script. This script
  will check your DataStores aka VMFS. I built this script so that it can be used
  with Nagios and or Zenoss. The purpose of this script is so that you can monitor
  thresholds on a per DataStore/VMFS. You will need to download and install <a href=\"http://pywbem.wiki.sourceforge.net/\">Pywbem</a>
  in order to use this script. You can get it <a href=\"http://pywbem.wiki.sourceforge.net/\">here</a><br
  /> Example below...</p>\r\n<pre>        example below...<br />        python check_datastore.py
  -u \"http://esxhost\" -a \"login passwd\" --d \"Esxtestvol2\" -w 60 -c 73 -m GB<br
  />        Warning Esxtestvol2 189GB Avail 62% used |avail=189<br /><br />        python
  check_datastore.py -u \"http://esxhost\" -a \"login passwd\" --d \"Esxtestvol2\"
  -w 70 -c 85 -m MB<br />        OK Esxtestvol2 194558MB Avail 61% used |avail=194558<br
  /><br />        python check_datastore.py -u \"http://esxhost\" -a \"login passwd\"
  --d \"ISO\" -w 10 -c 21 -m KB<br />        Critical ISO 41867542528KB Avail 21%
  used |avail=41867542528<br /><br />        python check_datastore.py -u \"http://esxhost\"
  -a \"login passwd\" --d \"Esxtestvol2\" -w 70 -c 85<br />        OK Esxtestvol2
  204008849408bytes Avail 61% used |avail=204008849408<br /><br />        -u, --url
  \      This is the URL you will use to connect to the ESX server, \"http://esxhost\"<br
  />        -a, --auth      This is the Login and Passwd you will use, \"login passwd\"<br
  />        -d, --dstore    This is the DataStore aka VMFS to check, \"Esxtestvol2\"<br
  />        -w, --warn      This is the warning threshold that you will set, 70<br
  />        -c, --crit      This is the critical threshold that you will set, 85<br
  />        -m, --metric    This is the metric that you will use, \"KB\", \"MB\",
  \"GB\", The default is Bytes<br /></pre>\r\n<p>You can download this script here
  <a href=\"View-details/VMware/32-check_esx_datastore.py.html\">check_datastore.py
  </a></p>\r\n<div>{quickdown:32}<br />\r\n<br />"
wordpress_id: 187
wordpress_url: http://linuxdynasty.org/?p=187
date: !binary |-
  MjAwOS0wMy0yNSAxNzowNjozMSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wMy0yNSAxNzowNjozMSAtMDQwMA==
categories: []
tags:
- VMware
- Check ESX Datastores/VMFS using Python and CIM
comments:
- id: 7
  author: tlindsay42
  author_email: tlindsay42@hotmail.com
  author_url: ''
  date: !binary |-
    MjAxMS0xMC0xNyAyMTo0NDo0MCAtMDQwMA==
  date_gmt: !binary |-
    MjAxMS0xMC0xNyAxNjo0NDo0MCAtMDQwMA==
  content: The script link above is broken
- id: 24
  author: dynasty
  author_email: asanabria@linuxdynasty.org
  author_url: ''
  date: !binary |-
    MjAxMS0xMi0wOSAyMTo1OToyMCAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0wOSAxNjo1OToyMCAtMDUwMA==
  content: I am working on getting the downloads section working again
---
<p>Good Afternoon guys, here I created another Python Script. This script will check your DataStores aka VMFS. I built this script so that it can be used with Nagios and or Zenoss. The purpose of this script is so that you can monitor thresholds on a per DataStore/VMFS. You will need to download and install <a href="http://pywbem.wiki.sourceforge.net/">Pywbem</a> in order to use this script. You can get it <a href="http://pywbem.wiki.sourceforge.net/">here</a><br /> Example below...</p>
<pre>        example below...<br />        python check_datastore.py -u "http://esxhost" -a "login passwd" --d "Esxtestvol2" -w 60 -c 73 -m GB<br />        Warning Esxtestvol2 189GB Avail 62% used |avail=189<br /><br />        python check_datastore.py -u "http://esxhost" -a "login passwd" --d "Esxtestvol2" -w 70 -c 85 -m MB<br />        OK Esxtestvol2 194558MB Avail 61% used |avail=194558<br /><br />        python check_datastore.py -u "http://esxhost" -a "login passwd" --d "ISO" -w 10 -c 21 -m KB<br />        Critical ISO 41867542528KB Avail 21% used |avail=41867542528<br /><br />        python check_datastore.py -u "http://esxhost" -a "login passwd" --d "Esxtestvol2" -w 70 -c 85<br />        OK Esxtestvol2 204008849408bytes Avail 61% used |avail=204008849408<br /><br />        -u, --url       This is the URL you will use to connect to the ESX server, "http://esxhost"<br />        -a, --auth      This is the Login and Passwd you will use, "login passwd"<br />        -d, --dstore    This is the DataStore aka VMFS to check, "Esxtestvol2"<br />        -w, --warn      This is the warning threshold that you will set, 70<br />        -c, --crit      This is the critical threshold that you will set, 85<br />        -m, --metric    This is the metric that you will use, "KB", "MB", "GB", The default is Bytes<br /></pre>
<p>You can download this script here <a href="View-details/VMware/32-check_esx_datastore.py.html">check_datastore.py </a></p>
<div>{quickdown:32}</p>
<p><a id="more"></a><a id="more-187"></a><br />
ScreenShot below of the script...</div>
<p> </p>
