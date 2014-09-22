---
layout: post
status: publish
published: true
title: VMware ESX SDK SnapShot Perl Script Part 3
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>This is the 3rd and I think final revision of this script. I added
  the --list function, which before had to be combined with the --vm_name function.
  The main reason for creating this script was so that there can be an easy way to
  manage snapshots, especially automating the deletion, creation, reverting, and listing
  of snapshots. If you find this script or any of my scripts useful, please let me
  know. </p>\r\n<p>&nbsp;</p>\r\n<pre>perl vm_snapshot.pl --list<br />Platinum<br
  />  name:         test1<br />  description:  <br />  state:        poweredOff<br
  />  vm type:      VirtualMachine<br />  time created: 2009-03-17T10:26:34.605171-04:00<br
  /><br />Gold <br />  name:         test2<br />  description:  <br />  state:        poweredOff<br
  />  vm type:      VirtualMachine<br />  time created: 2009-03-17T13:32:05Z<br /><br
  />Silver<br />  name:         test3<br />  description:  <br />  state:        poweredOff<br
  />  vm type:      VirtualMachine<br />  time created: 2009-03-17T13:32:22Z&nbsp;
  <br /></pre>\r\n<p><span class=\"attention\"> <strong>Remember!!! That in order
  to use this script you will need the Perl VI SDK installed on your linux box as
  well as $home/.visdkrc setup correctly</strong></span></p>\r\n<p>Here is an example
  .visdkrc...</p>\r\n<pre>VI_SERVER = Virtual Console Server<br />VI_USERNAME = login<br
  />VI_PASSWORD = passwd<br />VI_PROTOCOL = https <br />VI_PORTNUMBER = 443<br /></pre>\r\n<br
  />"
wordpress_id: 189
wordpress_url: http://linuxdynasty.org/?p=189
date: !binary |-
  MjAwOS0wMy0zMSAxOTo1MToyNiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wMy0zMSAxOTo1MToyNiAtMDQwMA==
categories: []
tags:
- VMware
- VMware ESX SDK SnapShot Perl Script Part 3
comments: []
---
<p>This is the 3rd and I think final revision of this script. I added the --list function, which before had to be combined with the --vm_name function. The main reason for creating this script was so that there can be an easy way to manage snapshots, especially automating the deletion, creation, reverting, and listing of snapshots. If you find this script or any of my scripts useful, please let me know. </p>
<p>&nbsp;</p>
<pre>perl vm_snapshot.pl --list<br />Platinum<br />  name:         test1<br />  description:  <br />  state:        poweredOff<br />  vm type:      VirtualMachine<br />  time created: 2009-03-17T10:26:34.605171-04:00<br /><br />Gold <br />  name:         test2<br />  description:  <br />  state:        poweredOff<br />  vm type:      VirtualMachine<br />  time created: 2009-03-17T13:32:05Z<br /><br />Silver<br />  name:         test3<br />  description:  <br />  state:        poweredOff<br />  vm type:      VirtualMachine<br />  time created: 2009-03-17T13:32:22Z&nbsp; <br /></pre>
<p><span class="attention"> <strong>Remember!!! That in order to use this script you will need the Perl VI SDK installed on your linux box as well as $home/.visdkrc setup correctly</strong></span></p>
<p>Here is an example .visdkrc...</p>
<pre>VI_SERVER = Virtual Console Server<br />VI_USERNAME = login<br />VI_PASSWORD = passwd<br />VI_PROTOCOL = https <br />VI_PORTNUMBER = 443<br /></pre>
<p><a id="more"></a><a id="more-189"></a></p>
<p>
You can still run this script with the Virtual Machine Name as well...</p>
<pre>perl vm_snapshot.pl --list --vm_name &quot;Platinum&quot;<br />  name:         test1<br />  description:  test snap<br />  state:        poweredOff<br />  vm type:      VirtualMachine<br />  time created: 2009-03-18T16:21:45.447627-04:00<br />&nbsp;</pre>
<p>You can also remove snapshots too...</p>
<pre><pre>perl vm_snapshot.pl --vm_name &quot;Platinum&quot; --delete --sn_name &quot;test1&quot;<br />Snapshot 'test1' removed for VM Development Server of Platinum </pre>
<p>You can also revert and do a powerOn as well.</p>
<pre>perl vm_snapshot.pl --vm_name &quot;Platinum&quot; --revert --sn_name &quot;new_snap&quot; --vm_on<br /><br />Operation :: Revert To Snapshot new_snap For Virtual Machine Platinum completed <br /><br /> Virtual machine 'Platinum' has been started <br /></pre>
<p>Also you can create snapshots as well...</p>
<pre>perl vm_snapshot.pl --vm_name &quot;Platinum&quot; --create --descr &quot;nice&quot; --sn_name &quot;new_snap&quot;<br />Snapshot 'new_snap' completed for VM The Platinum</pre>
<p></p>
<p><a href="http://www.linuxdynasty.org/View-details/VMware-Perl/35-VMware-ESX-SDK-SnapShot-Perl-Script-Part-3.html" title="">You can download the script here</a></p>
