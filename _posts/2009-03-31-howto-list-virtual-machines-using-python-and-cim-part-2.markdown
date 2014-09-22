---
layout: post
status: publish
published: true
title: HowTo List Virtual Machines using Python and CIM Part 2
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 188
wordpress_url: http://linuxdynasty.org/?p=188
date: !binary |-
  MjAwOS0wMy0zMSAwMToyODoyOCAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wMy0zMSAwMToyODoyOCAtMDQwMA==
categories:
- Python
- CIM
tags:
- VMware
- HowTo List Virtual Machines using Python and CIM Part 2
comments: []
---
<p>Welcome to part 2 of the "<strong>HowTo List Virtual Machines using Python and CIM</strong>". In this part, I modified the original script so that you can pass the Virtual Machine name as well as run it with out the Virtual Machine name. In the <a href="howto-list-vms-using-python-and-cim-part-1.html">first part</a> of this HowTO I created the listVMsInfo.py script witch just listed all the Virtual Machines. So please enjoy the script and hopefully it will make your life just a bit easier.</p>
<pre>python listVMsInfo.py -u "http://esxhost" -a "login passwd" -n "testVM"
VM Name 		 testVM
Operating System 	 Suse Linux Enterprise Server 10 (32-bit)
Host Name 		 None
IP Address 		 None
DataStore Used 		 [Esxtestvol] testVM.vmxRequested
State 	 Not ApplicableOperational
Status 	 Enabled
Enabled by Default 	 Enabled
Enabled State 		 Not Applicable</pre>
<p>Download this script here!<br />
{filelink=20}</p>
