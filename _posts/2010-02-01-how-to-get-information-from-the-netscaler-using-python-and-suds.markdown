---
layout: post
status: publish
published: true
title: How to get information from the Netscaler using Python and Suds.
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Recently I just started to use the Citrix Netscalers again ( Load Balancers
  ). Being the person that I am, I wanted a way to grab the information using the
  SOAP API.\r\nNow Citrix has a ton of documentation for Perl/C/C# and Java ( None
  for Python ). SOAP client support has not been the best for Python, in my opinion.\r\nI
  know you have <a href=\"http://pywebsvcs.sourceforge.net/\">soappy/ZSI</a>, which
  I have had issues with consuming Broken WSDL files ( Having to fix the Broken WSDL
  file manually, SUCKS!).\r\n\r\nJust 2 weeks ago, I encounterd <a href=\"https://fedorahosted.org/suds/\">SUDS</a>.
  This module is by far, the best SOAP client for Python.\r\nThere documentation is
  simple and straight to the point, with a bunch of nice samples to get you on your
  way.\r\n\r\n<span class=\"attention\">Install SUDS before proceeding further. You
  can get suds from here. <a href=\"https://fedorahosted.org/suds/\">https://fedorahosted.org/suds/</a></span>\r\nConnection
  to my netscaler was as simple as this...\r\n<pre>Python 2.4.3 (#1, Sep  3 2009,
  15:37:37)[GCC 4.1.2 20080704 (Red Hat 4.1.2-46)]</pre>\r\n<pre>on linux2Type \"help\",
  \"copyright\", \"credits\" or \"license\" for more information.\r\n&gt;&gt;&gt;
  from suds.client import Client\r\n&gt;&gt;&gt; url = \"http://nsip/api/NSConfig.wsdl\"\r\n&gt;&gt;&gt;
  from suds.xsd.doctor import *\r\n&gt;&gt;&gt; imp = Import('http://schemas.xmlsoap.org/soap/encoding/')\r\n&gt;&gt;&gt;
  imp.filter.add(\"urn:NSConfig\")\r\n&gt;&gt;&gt; d = ImportDoctor(imp)\r\n&gt;&gt;&gt;
  client = Client(url, doctor=d, location=\"http://nsip/soap/\")\r\n&gt;&gt;&gt; client.service.login(username=\"login\",
  password=\"pass\")(simpleResult){ rc = 0 message = \"Done\" }\r\n&gt;&gt;&gt;</pre>\r\n"
wordpress_id: 83
wordpress_url: http://linuxdynasty.org/?p=83
date: !binary |-
  MjAxMC0wMi0wMSAxMzoyMjoyMiAtMDUwMA==
date_gmt: !binary |-
  MjAxMC0wMi0wMSAxMzoyMjoyMiAtMDUwMA==
categories:
- Python
- Zenoss
- Netscaler
tags:
- Python HowTo's
- howto
- Netscaler
- Python
- Suds.
comments: []
---
<p>Recently I just started to use the Citrix Netscalers again ( Load Balancers ). Being the person that I am, I wanted a way to grab the information using the SOAP API.<br />
Now Citrix has a ton of documentation for Perl/C/C# and Java ( None for Python ). SOAP client support has not been the best for Python, in my opinion.<br />
I know you have <a href="http://pywebsvcs.sourceforge.net/">soappy/ZSI</a>, which I have had issues with consuming Broken WSDL files ( Having to fix the Broken WSDL file manually, SUCKS!).</p>
<p>Just 2 weeks ago, I encounterd <a href="https://fedorahosted.org/suds/">SUDS</a>. This module is by far, the best SOAP client for Python.<br />
There documentation is simple and straight to the point, with a bunch of nice samples to get you on your way.</p>
<p><span class="attention">Install SUDS before proceeding further. You can get suds from here. <a href="https://fedorahosted.org/suds/">https://fedorahosted.org/suds/</a></span><br />
Connection to my netscaler was as simple as this...</p>
<pre>Python 2.4.3 (#1, Sep  3 2009, 15:37:37)[GCC 4.1.2 20080704 (Red Hat 4.1.2-46)]</pre>
<pre>on linux2Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; from suds.client import Client
&gt;&gt;&gt; url = "http://nsip/api/NSConfig.wsdl"
&gt;&gt;&gt; from suds.xsd.doctor import *
&gt;&gt;&gt; imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
&gt;&gt;&gt; imp.filter.add("urn:NSConfig")
&gt;&gt;&gt; d = ImportDoctor(imp)
&gt;&gt;&gt; client = Client(url, doctor=d, location="http://nsip/soap/")
&gt;&gt;&gt; client.service.login(username="login", password="pass")(simpleResult){ rc = 0 message = "Done" }
&gt;&gt;&gt;</pre>
<p><a id="more"></a><a id="more-83"></a></p>
<p>As you can see above, I used the xsd doctor to import Soap encoding URL and added a filter for the Netscaler URN.<br />
If you do not import the SOAP encoding schema, this is the error you will receive..</p>
<p><span class="alert">suds.TypeNotFound: Type not found: '(Array, http://schemas.xmlsoap.org/soap/encoding/, )</span></p>
<p>Once you type the above, you can now run commands in the python shell. for instance...</p>
<ul>
<li>client.service.getlbvserver()</li>
<li>client.service.getservice()</li>
<li>client.service.getservicegroup()</li>
</ul>
<p>I am attaching a script that I have written, to get Load Balanced Virtual Servers and its Services and ServiceGroups.<br />
This script can also just list all the Virtual Servers, Services, or Service Groups. Examples below..<br />
queryns.py == {filelink=10}</p>
<p><small>python queryns.py -c "ZenossTest2_svc" -n "nsip" -u "login" -p "pass" Service Name Server Name Status IPAddress Port Protocol ZenossTest2_svc zenossTest OUT OF SERVICE 192.168.101.221 9090 HTTP python queryns.py -s foobar_test -n "nsip" -u "login" -p "pass" Virtual Server State IPAddress Port Protocol foobar_test UP 192.168.101.19 55555 HTTP ServiceGroup Name SG State Server Name Status IPAddress Port Protocol "Foo Bar" ENABLED billyboy UP 192.168.101.31 8080 HTTP "Foo Bar" ENABLED zenossTest UP 192.168.101.221 8080 HTTP Service Name Server Name Status IPAddress Port Protocol ZenossTest2_svc zenossTest OUT OF SERVICE 192.168.101.221 9090 HTTP ------------------------------------------------------------------------------------------------------------------------</small></p>
<p>All the options are here..</p>
<pre>python queryns.py -husage: queryns.py [options] arg --username=username --password=password --netscaler=netscalerip

options: -h, --help            
show this help message and exit 
-n NETSCALER, --netscaler=NETSCALER
                       Here you will put the netscaler IPAddress or the                       netscaler hostname-u USERNAME, --username=USERNAME
                       Your username -p PASSWORD, --password=PASSWORD                       Your password -l LIST, --list=LIST  
List all the names of the Virtual Servers, Services,
                       ServiceGroups. Example --list=lbvserver, --list=service, --list=servicegroup -s SERVER, ---vserver=SERVER
                       Virtual Server that you want to query. You can choose
                       a Virtual Server or you can pass all, so you get all
                       the Virtual Servers and its associated
                       ServiceGroups or Services. Example....
                       --vserver="foobar_test" or --vserver="all" 
-g SGROUP, --sgroup=SGROUP
                       ServiceGroup that you want the info from -c SERVICE, 
--service=SERVICE                       Service that you want the info from</pre>
