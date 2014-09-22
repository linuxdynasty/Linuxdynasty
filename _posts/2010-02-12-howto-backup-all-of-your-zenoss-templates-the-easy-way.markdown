---
layout: post
status: publish
published: true
title: HowTo backup all of your Zenoss Templates the easy way.
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Recently I had to prepare for a Zenoss upgrade. During my prep work I
  had to create a zenpack of all of our Templates. For those of you who use Zenoss,
  you know how many templates you can start to accumulate in a short amount of time.
  You can have Templates attached to single Devices, to SubClasses, and to Classes.
  Now if you have a few devices this is not a big deal. But if you have a couple hundred
  to a couple of thousand devices, this could be a real hassle.\r\n\r\nNow you can
  take a ton of your time and review Class by Class and Device by Device until you
  finally finish. You will eventually get it all in a Zenpack....... Well lucky for
  you guys I created a Python Script that runs as the Zenoss user and create a Zenpack
  for you. All you have to do is pick a name for the ZenPack and optionally the Device
  Class you want to scan. The script will scan the Device Class that you specified
  ( or by default scan the entire /Device Class and its Sub Classes). It will then
  create the ZenPack with all the locally attached Device Templates. I am thinking
  of also adding the Events class as part of the next release of this script.\r\n\r\n<span
  class=\"note\">Update 1.0.1, I added the --unique option. If you decide to use this
  option, This Zenpack will only add, The Device Templates that are not already part
  of an existing ZenPack. I also added the --verbose option, so that you can see which
  Device Templates are being added or being dismissed.\r\n</span>\r\n\r\nYou can download
  the script here\r\n{filelink=8}\r\n\r\n"
wordpress_id: 85
wordpress_url: http://linuxdynasty.org/?p=85
date: !binary |-
  MjAxMC0wMi0xMiAyMDoxOTo1OCAtMDUwMA==
date_gmt: !binary |-
  MjAxMC0wMi0xMiAyMDoxOTo1OCAtMDUwMA==
categories:
- Python
- Zenoss
tags:
- Python HowTo's
- Python
- Zenoss
- ZenPacks
comments:
- id: 5
  author: mahimahi
  author_email: mahimahi@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMS0xMC0wOCAwMzoxNjoxMyAtMDQwMA==
  date_gmt: !binary |-
    MjAxMS0xMC0wNyAyMjoxNjoxMyAtMDQwMA==
  content: ! 'Downloads are not working.  Trying to down load this script and all
    I see is: {quickdown:53}'
- id: 27
  author: dynasty
  author_email: asanabria@linuxdynasty.org
  author_url: ''
  date: !binary |-
    MjAxMS0xMi0wOSAyMjowMDowOSAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0wOSAxNzowMDowOSAtMDUwMA==
  content: I switched from Joomla to wordpress, I am working on getting the downloads
    section working again
---
<p>Recently I had to prepare for a Zenoss upgrade. During my prep work I had to create a zenpack of all of our Templates. For those of you who use Zenoss, you know how many templates you can start to accumulate in a short amount of time. You can have Templates attached to single Devices, to SubClasses, and to Classes. Now if you have a few devices this is not a big deal. But if you have a couple hundred to a couple of thousand devices, this could be a real hassle.</p>
<p>Now you can take a ton of your time and review Class by Class and Device by Device until you finally finish. You will eventually get it all in a Zenpack....... Well lucky for you guys I created a Python Script that runs as the Zenoss user and create a Zenpack for you. All you have to do is pick a name for the ZenPack and optionally the Device Class you want to scan. The script will scan the Device Class that you specified ( or by default scan the entire /Device Class and its Sub Classes). It will then create the ZenPack with all the locally attached Device Templates. I am thinking of also adding the Events class as part of the next release of this script.</p>
<p><span class="note">Update 1.0.1, I added the --unique option. If you decide to use this option, This Zenpack will only add, The Device Templates that are not already part of an existing ZenPack. I also added the --verbose option, so that you can see which Device Templates are being added or being dismissed.<br />
</span></p>
<p>You can download the script here<br />
{filelink=8}</p>
<p><a id="more"></a><a id="more-85"></a></p>
<p>Example.....</p>
<pre>python createZenPack.py -p "ZenPacks.Allen.Test1" -a "Allen Sanabria" -v "0.9" -r "/Server/Linux/"

INFO:zen.HookReportLoader:loading reports from:/opt/zenoss/ZenPacks/ZenPacks.Allen.Test1/ZenPacks/Allen/Test1/reportsCreated ZenPack ZenPacks.Allen.Test1Scanning for locally attached TemplatesScanning for locally attached TemplatesObjects Attached to Zenpack ZenPacks.Allen.Test1/zport/dmd/Devices/Server/Linux/foo1.com/foo/zport/dmd/Devices/Server/Linux/DNS/bind/zport/dmd/Devices/Server/Linux/Apache/http</pre>
<p>Another Example, with the unique option and verbose option.</p>
<pre>python createZenPack.py -p "ZenPacks.Allen.Test1" -a "Allen Sanabria" -v "0.9" -u -V 

-INFO:zen.HookReportLoader:loading reports from:/opt/zenoss/ZenPacks/ZenPacks.Allen.Test1/ZenPacks/Allen/Test1/reportsCreated ZenPack ZenPacks.Allen.Test1Scanning for locally attached TemplatesScanning for locally attached TemplatesObjects Attached to Zenpack ZenPacks.Allen.Test1I'm not UNIQUE /zport/dmd/Devices/Server/rrdTemplates/LDAPServerI'm in ZenPacks.zenoss.LDAPMonitorI'm not UNIQUE /zport/dmd/Devices/Server/rrdTemplates/ApacheI'm in ZenPacks.zenoss.ApacheMonitorI'm UNIQUE /zport/dmd/Devices/Server/Linux/foo1.com/foo</pre>
<p>Another Example...</p>
<pre>python createZenPack.py --listHPTemperatureSensorsZenPacks.Allen.Test1ZenPacks.Allen.FullZenPacks.Allen.Tomcat</pre>
<p>Help OutPut...</p>
<pre>python createZenPack.py -husage: createZenPack.py  --packname=ZenPackName --author=name --version=1.0

options: -h, --help            show this help message and exit -p ZPACKNAME,         --packname=ZPACKNAME                       The name of the ZenPack that you want to create -a AUTHOR,            --author=AUTHOR                       Who is creating The ZenPack? -v VERSION,           --version=VERSION                       What Release is this? -r ROOT,              --root=ROOT                         What Device Class You want the Search to begin at? -l,                   --list                       List all the ZenPacks</pre>
<p>&nbsp;</p>
