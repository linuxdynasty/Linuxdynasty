---
layout: post
status: publish
published: true
title: HowTo List Virtual Machines using Python and CIM Part 1
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Good morning my fellow Admins, Engineers, Scripters, Programmers, etc.....
  YOU GET THE IDEA :). For the past week, I have been learning all about the CIM and
  WBEM API. Since I am working alot more then I have ever have with VMware. I am trying
  to automate as much as possible with out using Perl. Now please do not think I am
  hating on Perl, it is not that at all, it is just the fact that I love Python, thats
  all! That being said here is the 1st part in a 2 part series on Listing Virtual
  Machines using Pywbem in Python. I the 1st part I will show you how to list Virtual
  Machines and data related to those VMs. Example Below...\r\n\r\n<a href=\"howto-list-virtual-machines-using-python-and-cim-part-2.html\">Update,
  here is the link for part 2 of this article. </a>\r\n<pre>    python listVMsInfo.py
  -u \"http://esxhost\" -a \"login passwd\"\r\n\r\n    VM Name                  Linux
  DP1 Client     Operating System         Red Hat Enterprise Linux 5 (32-bit)    Host
  Name                dpclient.linuxdynasty    IP Address               192.168.101.124
  \   DataStore Used           [Esxlinuxvol2] Linux Data Protector Install Ser/Linux
  Data Protector Install Ser.vmx    Requested State          Not Applicable    Operational
  Status       Enabled    Enabled by Default       Enabled    Enabled State            Not
  Applicable</pre>\r\n"
wordpress_id: 185
wordpress_url: http://linuxdynasty.org/?p=185
date: !binary |-
  MjAwOS0wMy0yNCAxMzo1MjozNiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wMy0yNCAxMzo1MjozNiAtMDQwMA==
categories:
- Python
- VMware
tags:
- VMware
- HowTo List Virtual Machines using Python and CIM Part 1
comments: []
---
<p>Good morning my fellow Admins, Engineers, Scripters, Programmers, etc..... YOU GET THE IDEA :). For the past week, I have been learning all about the CIM and WBEM API. Since I am working alot more then I have ever have with VMware. I am trying to automate as much as possible with out using Perl. Now please do not think I am hating on Perl, it is not that at all, it is just the fact that I love Python, thats all! That being said here is the 1st part in a 2 part series on Listing Virtual Machines using Pywbem in Python. I the 1st part I will show you how to list Virtual Machines and data related to those VMs. Example Below...</p>
<p><a href="howto-list-virtual-machines-using-python-and-cim-part-2.html">Update, here is the link for part 2 of this article. </a></p>
<pre>    python listVMsInfo.py -u "http://esxhost" -a "login passwd"

    VM Name                  Linux DP1 Client     Operating System         Red Hat Enterprise Linux 5 (32-bit)    Host Name                dpclient.linuxdynasty    IP Address               192.168.101.124    DataStore Used           [Esxlinuxvol2] Linux Data Protector Install Ser/Linux Data Protector Install Ser.vmx    Requested State          Not Applicable    Operational Status       Enabled    Enabled by Default       Enabled    Enabled State            Not Applicable</pre>
<p><a id="more"></a><a id="more-185"></a></p>
<p>&nbsp;</p>
<p>As you see above you get quite a bit of info, that is if you have VMwareTools installed. If not you will get the below..</p>
<pre>    VM Name                  Linux DP2 Client    Operating System         Red Hat Enterprise Linux 5 (32-bit)    Host Name                None    IP Address               None    DataStore Used           [Esxtlinuxvol2] Linux Data Protector Client Ser/Linux Data Protector Install Ser.vmx    Requested State          Not Applicable    Operational Status       Enabled    Enabled by Default       Enabled    Enabled State            Not Applicable</pre>
<p>As you can see you are missing the Host Name and The IP Address. For the 2nd part of this HowTo, I will add a VM Name option, IP address option, OS option, and a hostname option. This will allow you to search for a particular Virtual Machine, instead of listing them All.</p>
<p>You can download the Script here<br />
{filelink=20}<br />
<a href="images/stories/screenshots/listvmsinfo.png" rel="shadowbox[0]"><img style="width: 229px; height: 238px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/listvmsinfo.png" alt="" align="left" /></a></p>
<p>Here to your left is a screenshot of part of the script.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
