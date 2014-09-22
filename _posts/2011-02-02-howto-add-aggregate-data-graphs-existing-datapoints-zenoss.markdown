---
layout: post
status: publish
published: true
title: HowTo add Aggregate Data Graphs from existing datapoints in Zenoss
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 346
wordpress_url: http://linuxdynasty.org/?p=346
date: !binary |-
  MjAxMS0wMi0wMiAyMzoxNjo0MiAtMDUwMA==
date_gmt: !binary |-
  MjAxMS0wMi0wMiAxODoxNjo0MiAtMDUwMA==
categories:
- Python
- Zenoss
tags:
- Python
- Zenoss
- Aggregate
comments: []
---
<p>Recently I had to aggregate the amount of 200, 400, 404, 500, 503,  and 504 HTTP 1.1 Codes from all of our Nginx and Ruby On Rails systems. So I decided to write a quick plugin for Zenoss that all you need to do is pass the devices or Device Class you want to aggregate the data from and the DataPoint name.</p>
<p>Also this makes it simple to use the Zenoss Thresholds and create Aggregate Reports based on the datapoints you use with out having to do some fancy python coding... :) Enjoy</p>
<p>&nbsp;</p>
<p>Example..</p>
<pre>python AllenZenossAggregate.py -h
Usage: AllenZenossAggregate.py -d "nginx-1" -d "nginx-2" -p "nginx_codes_count200"
OK Aggregate for devices  nginx-1 nginx-2 is 34|aggregate=34
     AllenZenossAggregate.py -o "/Server/Linux/Nginx" -p "nginx_codes_count200"
OK Aggregate for /Server/Linux/Nginx class is 22|aggregate=22
 Options:
  -h, --help            show this help message and exit
  -d DEVICE, --device=DEVICE
                        The device you want to grab the datapoints from.
  -o ORGANIZER, --organizer=ORGANIZER
                        The Class you want to get your list of devices from.
  -p DPOINTS, --dpoints=DPOINTS
                        Name of DataPoint nginx_codes_count200</pre>
<p>{filelink=1}</p>
<p>&nbsp;</p>
