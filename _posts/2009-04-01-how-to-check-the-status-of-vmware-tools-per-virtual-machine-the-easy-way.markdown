---
layout: post
status: publish
published: true
title: How to check the status of VMware Tools per virtual Machine the easy way.
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>The other day I was told to check and see if VMware Tools was installed
  on every Virtual Machine in our Cluster. I figured this was the perfect time for
  me to write another script to do this.</p>\r\n<p>Here are a list of things that
  I want to have in the script...</p>\r\n<ul>\r\n<li>List all Virtual Machines and
  the VMstatus and Version if installed</li>\r\n<li>Check for toolsOK</li>\r\n<li>Check
  for toolsNotInstalled</li>\r\n<li>Check for toolsNotRunning</li>\r\n<li>Check for
  toolsOld</li>\r\n<li>And last but not least, able to do this either on a per Virtual
  Machine or on the entire Cluster</li>\r\n</ul>\r\n<p>Well I was able to do all of
  the above in a nice Perl Script that I created. It can be downloaded here  <a href=\"View-details/VMware-Perl/36-vmTools-Status-Perl-Script.html\">vmToolsStatus.pl</a></p>\r\n<pre>{quickdown:36}<br
  />perl vmToolsStatus.pl <br />        help              : Hiding the command line
  arguments [--help]<br />        --toolsOld             : This will print out all
  the Virtual Machines with an Old version of vmTools and you need to upgrade<br />
  \       --toolsNotInstalled    : This will print out all the Virtual Machines with
  vmTools Not Installed<br />        --toolsNotRunning      : This will print out
  all the Virtual Machines with vmTools Not Running<br />        --toolsOk              :
  This will print out all Virtual Machines with vmTools running <br />        --all
  \            : This will print out all Virtual Machines with vmTools installed or
  not installed<br />        example           : Hiding the command line arguments
  --toolsOld <br />        example           : Hiding the command line arguments --toolsOk
  <br />        example           : Hiding the command line arguments --toolsNotInstalled
  <br />        example           : Hiding the command line arguments --toolsRunning
  <br />        example           : Hiding the command line arguments --all --vm_name
  \"vm_name\" <br />        example           : Hiding the command line arguments
  --all  </pre>\r\n<div><span class=\"attention\"> <strong>Remember!!! That in order
  to use this script you will need the Perl VI SDK installed on your linux box as
  well as $home/.visdkrc setup correctly</strong></span></div>\r\n<p>Here is an example
  .visdkrc...</p>\r\n<pre>VI_SERVER = Virtual Console Server<br />VI_USERNAME = login<br
  />VI_PASSWORD = passwd<br />VI_PROTOCOL = https <br />VI_PORTNUMBER = 443<br /></pre>\r\n<p> </p>\r\n<br
  />"
wordpress_id: 190
wordpress_url: http://linuxdynasty.org/?p=190
date: !binary |-
  MjAwOS0wNC0wMSAxNDozMzoyNCAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNC0wMSAxNDozMzoyNCAtMDQwMA==
categories: []
tags:
- VMware
- How to check the status of VMware Tools per virtual Machine the easy way.
comments: []
---
<p>The other day I was told to check and see if VMware Tools was installed on every Virtual Machine in our Cluster. I figured this was the perfect time for me to write another script to do this.</p>
<p>Here are a list of things that I want to have in the script...</p>
<ul>
<li>List all Virtual Machines and the VMstatus and Version if installed</li>
<li>Check for toolsOK</li>
<li>Check for toolsNotInstalled</li>
<li>Check for toolsNotRunning</li>
<li>Check for toolsOld</li>
<li>And last but not least, able to do this either on a per Virtual Machine or on the entire Cluster</li>
</ul>
<p>Well I was able to do all of the above in a nice Perl Script that I created. It can be downloaded here  <a href="View-details/VMware-Perl/36-vmTools-Status-Perl-Script.html">vmToolsStatus.pl</a></p>
<pre>{quickdown:36}<br />perl vmToolsStatus.pl <br />        help              : Hiding the command line arguments [--help]<br />        --toolsOld             : This will print out all the Virtual Machines with an Old version of vmTools and you need to upgrade<br />        --toolsNotInstalled    : This will print out all the Virtual Machines with vmTools Not Installed<br />        --toolsNotRunning      : This will print out all the Virtual Machines with vmTools Not Running<br />        --toolsOk              : This will print out all Virtual Machines with vmTools running <br />        --all             : This will print out all Virtual Machines with vmTools installed or not installed<br />        example           : Hiding the command line arguments --toolsOld <br />        example           : Hiding the command line arguments --toolsOk <br />        example           : Hiding the command line arguments --toolsNotInstalled <br />        example           : Hiding the command line arguments --toolsRunning <br />        example           : Hiding the command line arguments --all --vm_name "vm_name" <br />        example           : Hiding the command line arguments --all  </pre>
<div><span class="attention"> <strong>Remember!!! That in order to use this script you will need the Perl VI SDK installed on your linux box as well as $home/.visdkrc setup correctly</strong></span></div>
<p>Here is an example .visdkrc...</p>
<pre>VI_SERVER = Virtual Console Server<br />VI_USERNAME = login<br />VI_PASSWORD = passwd<br />VI_PROTOCOL = https <br />VI_PORTNUMBER = 443<br /></pre>
<p> </p>
<p><a id="more"></a><a id="more-190"></a></p>
<p> </p>
<p><strong>So if you want to list all of the Virtual Machines that are running an incompatible version of vmtools, you will run the script like so..</strong></p>
<pre>perl vmToolsStatus.pl --toolsOld<br />MNS<br />  Status toolsOld and Version 82663<br /><br />LDAP<br />  Status toolsOld and Version 82663<br /><br />RHEL 5.2<br />  Status toolsOld and Version 82663<br /><br />Ramona<br />  Status toolsOld and Version 82663<br /><br />Luminati<br />  Status toolsOld and Version 82663 <br /></pre>
<p><strong>Or if you want to list all Virtual Machines that do not have vmtools installed...</strong></p>
<pre>perl vmToolsStatus.pl --toolsNotInstalled<br />SLES<br />  StatustoolsNotInstalled<br /><br />X86_Model<br />  StatustoolsNotInstalled<br /><br />Mario<br />  StatustoolsNotInstalled<br /><br />ZCM<br />  StatustoolsNotInstalled<br /><br />Bot Hunter<br />  StatustoolsNotInstalled<br /><br /></pre>
<p><strong>Or you can do it on a per Virtual Machine basis...</strong></p>
<pre>perl vmToolsStatus.pl --toolsOk --vm_name "Mail"<br />Mail<br />  Status toolsOk and Version 110268 <br /></pre>
<p> </p>
