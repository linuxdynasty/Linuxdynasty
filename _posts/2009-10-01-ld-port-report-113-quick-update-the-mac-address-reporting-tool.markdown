---
layout: post
status: publish
published: true
title: LD Port Report 1.13 quick update. The Mac Address Reporting Tool
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 213
wordpress_url: http://linuxdynasty.org/?p=213
date: !binary |-
  MjAwOS0xMC0wMSAxMzoxMjoxNSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0xMC0wMSAxMzoxMjoxNSAtMDQwMA==
categories:
- Port Report Projects
tags:
- Switch Port Report
- Python
- Port Report
- Mac Address Reporting Tool
- Port Reporting Tool
comments: []
---
<p>Quick update today! User Christianha, pointed out to me that the port_report tool was not matching any MAC address he passed. The reason for this is because he was passing the MAC address in uppercase. As per his suggestion, I fixed line 348 so that before it returns the mac, it willl make the MAC lower case. Then I just realized something.... I reverted line 348 back to way it was and changed line 676 instead..</p>
<p>It was if nmac == cmac:<br />
Now it is  re.search(nmac, cmac, re.IGNORECASE):</p>
<p>I felt this was the safer option..</p>
<p>Thank you Christianha for pointing the issues out..</p>
<p>LD Port Report == {filelink=15}</p>
