---
layout: post
status: publish
published: true
title: How to remove the last character of every filename in a directory
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<pre>#!/usr/bin/env python<br />#Created by LinuxDynasty<br />import os,
  re, sys<br /><br />os.chdir(sys.argv[1])<br />ls = os.listdir('./')<br />for file_o
  in ls:<br />  file_n = re.sub(&quot;w.&quot;, &quot;.&quot;, file_o)<br />  os.rename(file_o,
  file_n)<br /><br />print os.listdir(&quot;./&quot;)<br /></pre>\r\n<br />"
wordpress_id: 71
wordpress_url: http://linuxdynasty.org/?p=71
date: !binary |-
  MjAwOC0wNC0yOSAwMzozMDo0MSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNC0yOSAwMzozMDo0MSAtMDQwMA==
categories: []
tags:
- Python HowTo's
- How to remove the last character of every filename in a directory using Python
comments: []
---
<pre>#!/usr/bin/env python<br />#Created by LinuxDynasty<br />import os, re, sys<br /><br />os.chdir(sys.argv[1])<br />ls = os.listdir('./')<br />for file_o in ls:<br />  file_n = re.sub(&quot;w.&quot;, &quot;.&quot;, file_o)<br />  os.rename(file_o, file_n)<br /><br />print os.listdir(&quot;./&quot;)<br /></pre>
<p><a id="more"></a><a id="more-71"></a></p>
<p><strong>To run this script you will do this.</strong></p>
<p><strong>python &lt;script&gt; &lt;&quot;directory&quot;&gt;</strong></p>
<p><strong>python rename1.py &quot;/home/dynasty/test&quot;</strong></p>
