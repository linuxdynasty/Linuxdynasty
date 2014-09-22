---
layout: post
status: publish
published: true
title: HowTo Increase GFS2 Performance in a Cluster
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "In the last HowTo, I showed you how to setup GFS2 file system with Red
  Hat Clustering. I will now show you how to optimize the performance of your GFS2
  mounts. The gfs_controld daemon manages the mounting, unmounting, and the recovery
  of the GFS2 mounts. gfs_controld also manages the posix lock.\r\n\r\nBy default 
  the plock_rate_limit option is set to 100. This will allow a maximum of 100 locks
  per second, which will decrease your GFS2 performance. See below...\r\n\r\n<strong> &lt;dlm
  plock_ownership=\"0\" plock_rate_limit=\"100\"/&gt;\r\n&lt;gfs_controld plock_rate_limit=\"100\"/&gt;</strong>\r\n\r\nYou
  can test the performance of you cluster by downloading the program <strong><a title=\"\"
  href=\"http://wiki.samba.org/index.php/Ping_pong\">ping_pong.c.</a></strong> This
  program was very helpful to me in debugging the poor performance in my GFS2 cluster.\r\nThe
  instructions on how to compile the program and run it is on the site http://wiki.samba.org/index.php/Ping_pong.When
  I initially ran ping_pong, I only got a max of 97 plocks per second. After removing
  the rate limit I was able to get about 3000 Plocks per second.\r\n\r\n"
wordpress_id: 216
wordpress_url: http://linuxdynasty.org/?p=216
date: !binary |-
  MjAwOS0wOC0xNCAxNzowNToxNSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wOC0xNCAxNzowNToxNSAtMDQwMA==
categories:
- Clustering
tags:
- RedHat Clustering
- HowTo Increase GFS2 Performance in a Cluster
comments: []
---
<p>In the last HowTo, I showed you how to setup GFS2 file system with Red Hat Clustering. I will now show you how to optimize the performance of your GFS2 mounts. The gfs_controld daemon manages the mounting, unmounting, and the recovery of the GFS2 mounts. gfs_controld also manages the posix lock.</p>
<p>By default  the plock_rate_limit option is set to 100. This will allow a maximum of 100 locks per second, which will decrease your GFS2 performance. See below...</p>
<p><strong> &lt;dlm plock_ownership="0" plock_rate_limit="100"/&gt;<br />
&lt;gfs_controld plock_rate_limit="100"/&gt;</strong></p>
<p>You can test the performance of you cluster by downloading the program <strong><a title="" href="http://wiki.samba.org/index.php/Ping_pong">ping_pong.c.</a></strong> This program was very helpful to me in debugging the poor performance in my GFS2 cluster.<br />
The instructions on how to compile the program and run it is on the site http://wiki.samba.org/index.php/Ping_pong.When I initially ran ping_pong, I only got a max of 97 plocks per second. After removing the rate limit I was able to get about 3000 Plocks per second.</p>
<p><a id="more"></a><a id="more-216"></a></p>
<p>You should change the plock_rate_limit to 0 and the dlm plock_ownership to 1. See below..</p>
<p><strong> &lt;dlm plock_ownership="1" plock_rate_limit="0"/&gt;<br />
&lt;gfs_controld plock_rate_limit="0"/&gt;</strong></p>
<p>FYI.. The settings above are set in <strong>/etc/cluster/cluster.conf</strong>   Example below...<br />
<strong>    &lt;cman/&gt;<br />
&lt;dlm plock_ownership="1" plock_rate_limit="0"/&gt;<br />
&lt;gfs_controld plock_rate_limit="0"/&gt;</strong><br />
<strong>&lt;/cluster&gt;</strong></p>
<p>My settings were added to the end of cluster.conf.<br />
<span class="attention">After adding the above settings, please reboot all the nodes for the settings to take affect. </span></p>
<p>The above will increase locking operations at the cost of an increase in network utilization. You also can increase the performance of your GFS2 mount by mounting it with these options ( <strong>noatime</strong> and <strong>nodiratime</strong> )... Example below..</p>
<p><strong>mount -o noatime,nodiratime, /dev/mapper/mytest_gfs2-MyGFS2test /GFS/</strong></p>
<p>Another way to tune GFS2 directly, is by decreasing how often GFS2 demotes its locks.  Demote_secs is the number of seconds that gfsd will wake up and demote locks and flush data to disk. The default is set to 300 seconds which is equal to 5 minutes. I currently have mine to demote every 20 seconds, and believe you me... I saw a big performance increase.</p>
<p><strong>gfs2_tool settune /GFS demote_secs 20</strong></p>
<p>I chose 20 seconds, but it does not mean that is what you need to chose. You can play with those numbers and see how performance either increases or decreases. The option needs to be set every time the file system is mounted. So you might want to add this option in rc.local or in the gfs2 startup script at the end.</p>
<p><strong> echo "gfs2_tool settune /GFS demote_secs 20" &gt;&gt; /etc/rc.local</strong></p>
<p>When all was said and done I was able to get over 3000 plocks per sec after the optimization was done and my file level operations drastically increased in performance. I Hope the above helps you the way it helped me.</p>
<p><span class="attention">Very Important.... Make sure that updatedb does not run on your GFS2 mounts.. This will kill your GFS2 mount!!!! </span></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
