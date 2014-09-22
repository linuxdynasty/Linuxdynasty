---
layout: post
status: publish
published: true
title: LD Network Device Manager update .21
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Here is another quick update for today. This time it is for ldNetDeviceManager.py.\r\nRevision
  .21 10/01/2009\r\n<ul>\r\n\t<li>Can now save output to a file. using the --save
  option</li>\r\n</ul>\r\n{quickdown:49}\r\n\r\n"
wordpress_id: 220
wordpress_url: http://linuxdynasty.org/?p=220
date: !binary |-
  MjAwOS0xMC0wMSAxMzoyODo1NiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0xMC0wMSAxMzoyODo1NiAtMDQwMA==
categories:
- Python
- LD Device Manager
tags:
- LD Network manager
- Python
- Pexpect
- LD Network Device Manager
comments: []
---
<p>Here is another quick update for today. This time it is for ldNetDeviceManager.py.<br />
Revision .21 10/01/2009</p>
<ul>
<li>Can now save output to a file. using the --save option</li>
</ul>
<p>{quickdown:49}</p>
<p><a id="more"></a><a id="more-220"></a></p>
<p>Here are some examples below...</p>
<pre>python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -C './cmd.txt' -t ssh -e 'p@55wd' --output --tout=2python ldNetDeviceManager.py --login=dynasty --passwd='passwd' --dlist='./switches' --clist='./cmd.txt' --term=both --enable='p@55wd' --output --tout=2python ldNetDeviceManager.py --login=dynasty --passwd='passwd' --dlist='./switches' --command='service snmpd restart' --term=ssh --enable='p@55wd' --output --tout=20, --savepython ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -C './cmd.txt' -t ssh  -o --tout=2

If you have SSH Keys then you do not need to pass a password unless you have to get root access or sudo access. example below..</pre>
<pre>python ldNetDeviceManager.py -l dynasty -d 192.168.101.11 -C './cmd.txt' -t ssh  -o --tout=2python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -c 'sudo service snmpd restart' --term=ssh  --output --tout=2python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -c 'sudo service snmpd restart' --output --save</pre>
<p>&nbsp;</p>
