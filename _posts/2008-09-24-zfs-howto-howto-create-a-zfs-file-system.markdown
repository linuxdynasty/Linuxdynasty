---
layout: post
status: publish
published: true
title: ZFS HowTO, HowTo Create a ZFS File System
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p><span class=\"dropcap\">H</span>ere is another HowTo, but this time
  its on ZFS. The ZFS file system is a revolutionary new file system that was developed
  by SUN. I have to say ZFS is awesome and very easy to administer, I've been pissed
  off lately with things that I can not do on OpenSolaris/SolarisExpress or things
  that take way to much time to do on Solaris. One thing that has been extremely easy
  to implement and administer has been ZFS. </p>\r\n<br />"
wordpress_id: 204
wordpress_url: http://linuxdynasty.org/?p=204
date: !binary |-
  MjAwOC0wOS0yNCAxMzo1ODo1NCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wOS0yNCAxMzo1ODo1NCAtMDQwMA==
categories: []
tags:
- Advance OpenSolaris HowTo's
- ZFS HowTO
- HowTo Create a ZFS File System
comments: []
---
<p><span class="dropcap">H</span>ere is another HowTo, but this time its on ZFS. The ZFS file system is a revolutionary new file system that was developed by SUN. I have to say ZFS is awesome and very easy to administer, I've been pissed off lately with things that I can not do on OpenSolaris/SolarisExpress or things that take way to much time to do on Solaris. One thing that has been extremely easy to implement and administer has been ZFS. </p>
<p><a id="more"></a><a id="more-204"></a></p>
<p>Here I will explain the many benefits of ZFS below..</p>
<ul>
<li>ZFS is a transactional file system, which means that the file system state is always consistent on disk.</li>
<li>All data and meta data is checksummed using a user-selectable algorithm.&nbsp;</li>
<li>No silent data corruption ever: ZFS self healing features automatically repairs corrupt data</li>
<li>ZFS supports storage pools with varying levels of data redundancy, including mirroring and a variation on RAID-5</li>
<li>The ZFS file system itself is 128-bit, allowing for 256 quadrillion zettabytes of storage</li>
<li>ZFS supports SnapShots</li>
<li>ACL Support</li>
<li>many more......</li>
</ul>
<p>&nbsp;You will need Solaris Express nv80 or newer or OpenSolaris 2008.05</p>
<p>&nbsp;</p>
<ol>
<li><font color="#0000cc"><strong>df -h</strong></font>&nbsp;&nbsp;&nbsp; { See what devices are being used }
<pre><span>-bash-3.2# df -h</span><br /><p><span>Filesystem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; size&nbsp;&nbsp; used&nbsp; avail capacity&nbsp; Mounted on</span></p><span>/dev/dsk/c0d0s0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7.6G&nbsp;&nbsp; 5.4G&nbsp;&nbsp; 2.1G&nbsp;&nbsp;&nbsp; 72%&nbsp;&nbsp;&nbsp; /</span><span><br />/devices&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /devices</span><span><br />/dev&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /dev</span><span><br />ctfs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /system/contract</span><span><br />proc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /proc</span><span><br />mnttab&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /etc/mnttab</span><span><br />swap&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.0G&nbsp;&nbsp; 996K&nbsp;&nbsp; 1.0G&nbsp;&nbsp;&nbsp;&nbsp; 1%&nbsp;&nbsp;&nbsp; /etc/svc/volatile</span><span><br />objfs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /system/object</span><span><br />sharefs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /etc/dfs/sharetab</span><span><br />/usr/lib/libc/libc_hwcap3.so.1</span><span><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7.6G&nbsp;&nbsp; 5.4G&nbsp;&nbsp; 2.1G&nbsp;&nbsp;&nbsp; 72%&nbsp;&nbsp;&nbsp; /lib/libc.so.</span><span><br />fd&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /dev/fd</span><span><br />swap&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.0G&nbsp;&nbsp;&nbsp; 48K&nbsp;&nbsp; 1.0G&nbsp;&nbsp;&nbsp;&nbsp; 1%&nbsp;&nbsp;&nbsp; /tmp</span><span><br />swap&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.0G&nbsp;&nbsp;&nbsp; 44K&nbsp;&nbsp; 1.0G&nbsp;&nbsp;&nbsp;&nbsp; 1%&nbsp;&nbsp;&nbsp; /var/run</span><span><br />/dev/dsk/c0d0s7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7.6G&nbsp;&nbsp;&nbsp; 37M&nbsp;&nbsp; 7.5G&nbsp;&nbsp;&nbsp;&nbsp; 1%&nbsp;&nbsp;&nbsp; /export/home</span><br /><br /></pre>
</li>
<li><font color="#0000cc"><strong>format</strong></font>&nbsp;&nbsp; ( See what disks are available to us }
<pre>-bash-3.2# format<br /><p>Searching for disks...done</p>AVAILABLE DISK SELECTIONS<br />       0. c0d0 &lt;DEFAULT cyl 2085 alt 2 hd 255 sec 63&gt;<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /pci@0,0/pci-ide@1,1/ide@0/cmdk@0,0<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. c0d1 &lt;DEFAULT cyl 1021 alt 2 hd 128 sec 32&gt;<br />          /pci@0,0/pci-ide@1,1/ide@0/cmdk@1,0<br />       2. c1d1 &lt;DEFAULT cyl 1021 alt 2 hd 128 sec 32&gt;<br />          /pci@0,0/pci-ide@1,1/ide@1/cmdk@1,0<br /> Specify disk (enter its number):</pre>
</li>
<li>As you can see we have 2 disks ( c0d1and c1d1 ) available to use. So now we can create our zpool.<br />
<font color="#ff0000"><strong><font color="#0000cc">zpool create</font> linuxdynasty c0d1 c1d1</strong></font></p>
<pre>-bash-3.2# zpool create linuxdynasty c0d1 c1d2</pre>
</li>
<li><span>Lets check the status of our newly create pool</span><font color="#0000cc"><strong>.<br />
zpool status</strong></font></p>
<pre>-bash-3.2# zpool status<br /><p>pool: linuxdynasty</p>state: ONLINE<br />scrub: none requested<br />config:<br /><p>NAME&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STATE&nbsp;&nbsp;&nbsp;&nbsp; READ WRITE CKSUM</p>linuxdynasty&nbsp; ONLINE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp; 0<br />c0d1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ONLINE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp; 0<br />c1d1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ONLINE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp; 0<br /><br />errors: No known data errors</pre>
</li>
<li><span>We know we only have one pool but if you wanted to see the status of all of your zpools this is how you do it.</span><font color="#0000cc"><strong><br />
zpool list</strong></font></p>
<pre>-bash-3.2# zpool list<br /><p>NAME&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SIZE&nbsp;&nbsp; USED&nbsp; AVAIL&nbsp;&nbsp;&nbsp; CAP&nbsp; HEALTH&nbsp; ALTROOT</p>linuxdynasty&nbsp; 3.97G&nbsp;&nbsp; 220K&nbsp; 3.97G&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp; ONLINE&nbsp; -</pre>
</li>
<li><font color="#ff0000"><strong><font color="#0000cc">zfs create</font> linuxdynasty/opt</strong></font>&nbsp;&nbsp; { Here we created the /linuxdynasty/opt file system, as you will see ZFS will automatically mount it for you as well }
<pre>-bash-3.2# zfs create linuxdynasty/opt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br /></pre>
</li>
<li>Now I want to make my /opt directory into a ZFS managed filesystem. In order to do this I will have to move the contents of /opt into /linuxdynasty/opt.
<pre>-bash-3.2# mv /opt /linuxdynasty/opt</pre>
</li>
<li>Remove the origianl /opt dir
<pre>-bash-3.2# rm -rf /opt</pre>
</li>
<li>Now we need to tell ZFS to change where the /linuxdynasty/opt points to in the file system.
<pre>-bash-3.2# zfs set mountpoint=/opt linuxdynasty/opt</pre>
</li>
<li>What if you do not want the /opt file system to grow out of control?? Well ZFS also can handle that by setting a quota on the file system as well
<pre><p>-bash-3.2# zfs set quota=1G linuxdynasty/opt <br /></p></pre>
</li>
<li>Now you can run a <font color="#0000ff"><strong>df -h</strong></font>,and as you can see all the mounting is done for you.. Now when you reboot the box all of your ZFS mounts will mount up automatically with out you having to modify<font color="#ff0000"><strong> /etc/vfstab</strong></font> since ZFS takes care of this for you.
<pre>bash-3.2$ df -h<br /><br />Filesystem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; size&nbsp;&nbsp; used&nbsp; avail capacity&nbsp; Mounted on<br />/dev/dsk/c0d0s0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7.6G&nbsp;&nbsp; 4.9G&nbsp;&nbsp; 2.6G&nbsp;&nbsp;&nbsp; 66%&nbsp;&nbsp;&nbsp; /<br />/devices&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /devices<br />/dev&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /dev<br />ctfs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /system/contract<br />proc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /proc<br />mnttab&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /etc/mnttab<br />swap&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 986M&nbsp;&nbsp; 1.0M&nbsp;&nbsp; 985M&nbsp;&nbsp;&nbsp;&nbsp; 1%&nbsp;&nbsp;&nbsp; /etc/svc/volatile<br />objfs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /system/object<br />sharefs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /etc/dfs/sharetab<br />/usr/lib/libc/libc_hwcap3.so.1<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7.6G&nbsp;&nbsp; 4.9G&nbsp;&nbsp; 2.6G&nbsp;&nbsp;&nbsp; 66%&nbsp;&nbsp;&nbsp; /lib/libc.so.1<br />fd&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0K&nbsp;&nbsp;&nbsp;&nbsp; 0%&nbsp;&nbsp;&nbsp; /dev/fd<br />swap&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 985M&nbsp;&nbsp;&nbsp; 48K&nbsp;&nbsp; 985M&nbsp;&nbsp;&nbsp;&nbsp; 1%&nbsp;&nbsp;&nbsp; /tmp<br />swap&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 985M&nbsp;&nbsp;&nbsp; 44K&nbsp;&nbsp; 985M&nbsp;&nbsp;&nbsp;&nbsp; 1%&nbsp;&nbsp;&nbsp; /var/run<br />/dev/dsk/c0d0s7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7.6G&nbsp;&nbsp;&nbsp; 54M&nbsp;&nbsp; 7.5G&nbsp;&nbsp;&nbsp;&nbsp; 1%&nbsp;&nbsp;&nbsp; /export/home<br />linuxdynasty&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3.9G&nbsp;&nbsp;&nbsp; 20K&nbsp;&nbsp; 3.4G&nbsp;&nbsp;&nbsp;&nbsp; 1%&nbsp;&nbsp;&nbsp; /linuxdynasty<br />linuxdynasty/opt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.0G&nbsp;&nbsp; 543M&nbsp;&nbsp; 481M&nbsp;&nbsp;&nbsp; 53%&nbsp;&nbsp;&nbsp; /opt<br /><br /></pre>
</li>
</ol>
<p>Now there is alot more that ZFS can do so If you want to see more please let me know and I will be more then happy to create more tutorials based on ZFS. </p>
