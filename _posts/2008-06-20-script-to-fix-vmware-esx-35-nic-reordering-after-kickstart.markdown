---
layout: post
status: publish
published: true
title: Script to fix VMWare ESX 3.5 NIC Reordering after kickstart
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Once we moved to VMWare ESX 3.+ we ran into a very annoying issue. The
  issue was that if you have multiple NICs from Multiple vendors, VMWare will reorder
  your NICs and cause havoc to you guys who use PXE boot/Kickstart. So I had to come
  with a work around that will alleviate this issue. I went ahead and created this
  script and I injected it in the post section of our kickstart profile and had it
  run after rebooting 3 times. Since After the third reboot the VMWare is done with
  its configuration, after the third reboot the script will run and then delete itself.
  Once all said and done your NICs will be in the proper order.\r\n\r\nSome of you
  might just use it as a once shot deal manually and some of you might use it as I
  did, but I did not realize how many f you are having the same issue as I did. Since
  I posted this script it has ad close to 3000 hits. So for those of you who have
  used it and appreciated the work I have done or for those of you who have modified
  it and added to it. Please leave some feed back weather in the form of comments
  or in the forums.\r\n\r\n"
wordpress_id: 179
wordpress_url: http://linuxdynasty.org/?p=179
date: !binary |-
  MjAwOC0wNi0yMCAwMjowNzo0MiAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNi0yMCAwMjowNzo0MiAtMDQwMA==
categories:
- Uncategorized
tags:
- VMware
- python VMware ESX 3.5 and 4.0 NIC Reordering script
comments:
- id: 4
  author: kklo
  author_email: kklo.malo@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMS0xMC0wNiAxNDo0NjowNiAtMDQwMA==
  date_gmt: !binary |-
    MjAxMS0xMC0wNiAwOTo0NjowNiAtMDQwMA==
  content: I'm unable to download your Script for vmnic reorder in esx 3.5. I've a
    similar issue on vSphere 4.0. Please check the link.
- id: 29
  author: dynasty
  author_email: asanabria@linuxdynasty.org
  author_url: ''
  date: !binary |-
    MjAxMS0xMi0wOSAyMjowMDo0NCAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0wOSAxNzowMDo0NCAtMDUwMA==
  content: I switched from Joomla to wordpress, I am working on getting the downloads
    section working again
- id: 32
  author: dynasty
  author_email: asanabria@linuxdynasty.org
  author_url: ''
  date: !binary |-
    MjAxMS0xMi0xMCAwMzo1ODoxNiAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0wOSAyMjo1ODoxNiAtMDUwMA==
  content: SCRIPT HAS BEEN UPLOADED
---
<p>Once we moved to VMWare ESX 3.+ we ran into a very annoying issue. The issue was that if you have multiple NICs from Multiple vendors, VMWare will reorder your NICs and cause havoc to you guys who use PXE boot/Kickstart. So I had to come with a work around that will alleviate this issue. I went ahead and created this script and I injected it in the post section of our kickstart profile and had it run after rebooting 3 times. Since After the third reboot the VMWare is done with its configuration, after the third reboot the script will run and then delete itself. Once all said and done your NICs will be in the proper order.</p>
<p>Some of you might just use it as a once shot deal manually and some of you might use it as I did, but I did not realize how many f you are having the same issue as I did. Since I posted this script it has ad close to 3000 hits. So for those of you who have used it and appreciated the work I have done or for those of you who have modified it and added to it. Please leave some feed back weather in the form of comments or in the forums.</p>
<p><a id="more"></a><a id="more-179"></a></p>
<p>Could you believe that VMWare says that a feature of there software will reorder your NICs after the kickstart???<br />
So if this was the order of our NICS<br />
03:02.0 Ethernet controller: Intel Corporation 82546EB Gigabit Ethernet Controller (Copper) (rev 01)<br />
03:02.1 Ethernet controller: Intel Corporation 82546EB Gigabit Ethernet Controller (Copper) (rev 01)<br />
eth0 == 03:02.0<br />
eth1 == 03:02.1<br />
When VMWare comes up it will reorder them so that vmnic0 will point to 03:02:01 when it should be 03:02:00 Now this only happens when you have a box with multiple nics from multiple vendors. This script will take care of it for you.</p>
<p>Here are some instructions on how to run this script and what you should do before and after you run this script on your ESX Server..</p>
<ol>
<li>run <span style="color: #0000ff;"><strong>esxcfg-nics -l</strong></span> (keep the ouput so you can compare it to the new ouput after the script has done its job)</li>
<li>copy this script in any directory you want... for instance  ( <span style="color: #ff0000;"><strong>/tmp/esx_nic_fix.py</strong></span> )</li>
<li>Reboot your ESX server and once it comes up ESXwill reboot again to apply the nic changes.</li>
<li>run <span style="color: #0000ff;"><strong>esxcfg-nics -l </strong></span>and compare the new output to the old output.... ( The order should be correct now ).</li>
<li>Leave me a comment on how my script helped you and digg this article. ( I would appreciate it ).</li>
</ol>
<p><span class="note">I have received numerous request on how to count reboots so that this script can run effectively right at the right moment. This is not an exact science and the number of reboots might have to be tweaked on a per environment basis, but here is what we use..</span></p>
<p>&nbsp;</p>
<pre>count=`last -x|grep "reboot" |wc -l`if [ $count -ge 3 ]; then   python /usr/local/bin/esx_nic_fix.py   chmod 644 /etc/rc.d/rc.local   reboot   exit 0fi</pre>
<p>esxnic_reordering.py<br />
{filelink=19}</p>
<p><a href="http://linuxdynasty.org/images/stories/Scripts/esx_fix_nix_python.png" rel="shadowbox[0]"><img style="width: 274px; height: 224px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/Scripts/esx_fix_nix_python.png" alt="" /></a></p>
