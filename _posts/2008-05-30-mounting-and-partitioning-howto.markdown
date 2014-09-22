---
layout: post
status: publish
published: true
title: Mounting and Partitioning HowTo
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p><span class=\"dropcap\">I</span> see this question in forums all\r\nthe
  time.... How do I mount a file system? How do I create a new\r\npartition and a
  file system? How do I set it to mount automatically?\r\nhow do I set the permissions
  on the mount? Well I'm going to do my best\r\nhere and answer all the questions
  above.</p>\r\n<br />"
wordpress_id: 31
wordpress_url: http://linuxdynasty.org/?p=31
date: !binary |-
  MjAwOC0wNS0zMCAxMTozOTo1NCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0zMCAxMTozOTo1NCAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- How to mount a partition How to mount a device how to partition
comments: []
---
<p><span class="dropcap">I</span> see this question in forums all<br />
the time.... How do I mount a file system? How do I create a new<br />
partition and a file system? How do I set it to mount automatically?<br />
how do I set the permissions on the mount? Well I'm going to do my best<br />
here and answer all the questions above.</p>
<p><a id="more"></a><a id="more-31"></a></p>
<p><span class="attention">I'm doing this how to with the screen shots on <a target="_parent" href="/linux-mint-5-elyssa-install-screenshots.html" title="Linux Mint Screen Shots">Linux Mint</a> (based off of <strong>Ubuntu</strong>), which means I'm using <strong>sudo</strong> in front of all of my commands instead of being logged in as <strong>root</strong>, though you can be logged in as <strong>root</strong> as well </span></p>
<div class="important"><span class="important-title"><strong>Delete/Create a Partition and Create a File System</strong></span></p>
<p>I'm going to demonstrate how to delete and create a partition and create a file system using my trusty 4gig USB drive...<br />
If you have a USB drive, testing this will be a cinch :). <span class="alert">Make sure there is nothing on there that you want unless it is GONE!!!</span></p>
<p><span class="notice">You might have to delete the current file system first, if so please follow the directions below.</span> </p>
<div class="important"><span class="important-title"><strong>Delete The Partition</strong></span></p>
<ul>
<li>Insert your USB drive </li>
<li>Run <strong>&quot;<font color="#0000ff">fdisk -l</font>&quot;</strong> as the root user or &quot;<font color="#0000ff"><strong>sudo fdisk -l</strong></font>&quot; This command will print out your disks and its partitions</li>
<li>Now run &quot;<font color="#0000ff"><strong>fdisk</strong></font> <font color="#ff0000"><strong>/dev/sdb</strong></font>&quot; (This might be different for you, refer back to the output of &quot;<font color="#0000ff"><strong>fdisk -l</strong></font>&quot;)&nbsp;</li>
<li>Type&quot;<font color="#0000ff"><strong>p</strong></font>&quot; (This means print)</li>
<li>Now delete the partition by typing &quot;<font color="#0000ff"><strong>d</strong></font>&quot; (this means delete). If you only have 1 partition in there it will choose that one by default</li>
<li>Type &quot;<font color="#0000ff"><strong>p</strong></font>&quot; We are doing this is to verify that the partition is gone</li>
<li>
<p>Now finally type &quot;<font color="#0000ff"><strong>w</strong></font>&quot; This means to write the changes you just did<br />
Here is the screen shot of the steps above..<br />
<a href="images/stories/screenshots/fdisk_usb_del.jpg" rel="shadowbox[0]"><img alt="" style="width: 186px; height: 144px" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/fdisk_usb_del.jpg" /></a></p>
</li>
</ul>
</div>
<p></p>
<div class="important"><span class="important-title"><strong>Create The Partition</strong></span></p>
<ul>
<li>Now run &quot;<font color="#0000ff"><strong>fdisk</strong></font> <font color="#ff0000"><strong>/dev/sdb</strong></font>&quot; (This might be different for you, refer back to the output of &quot;<font color="#0000ff"><strong>fdisk -l</strong></font>&quot;) 
</li>
<li>Type&quot;<font color="#0000ff"><strong>p</strong></font>&quot; (This means print)</li>
<li>Now create the partition by typing &quot;<font color="#0000ff"><strong>n</strong></font>&quot; (This means create a new partition)</li>
<li>Type &quot;<font color="#0000ff"><strong>P</strong></font>&quot; (P for primary partition)</li>
<li>Type &quot;<font color="#0000ff"><strong>1</strong></font>&quot; for the first partition (You can only choose 1-4 for primary partitions after that it would have to be extended) </li>
<li>Now choose the default which is &quot;<font color="#0000ff"><strong>1</strong></font>&quot;. (You are choosing which cylinder to place the beginning of this partition at.)</li>
<li>Time to choose the size of your partition or use the default which is the entire size of the disk<br />
I chose to only use &quot;<font color="#0000ff"><strong>+1024M</strong></font>&quot; (which is 1G)</li>
<li>If you want you can type &quot;<font color="#0000ff"><strong>p</strong></font>&quot; To print your partition table and see if the partition was created.</li>
<li>Finally type &quot;<font color="#0000ff"><strong>w</strong></font>&quot; (This will commit your changes)</li>
<li>Below is the screen shot of the whole process..<br />
<a href="images/stories/screenshots/fdisk_usb_fs.jpg" rel="shadowbox[0]"><img alt="" style="width: 186px; height: 144px" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/fdisk_usb_fs.jpg" /></a>
</li>
</ul>
</div>
<p>&nbsp;</p>
<div class="important"><span class="important-title"><strong><strong>Create The File System</strong></strong></span></p>
<p>Now it is time to choose the type of file system you want to create. I chose to use &quot;ext3&quot; file system. (Which is the default on most distributions of late)</p>
<ul>
<li>To create the ext3 file system you will have to run this command...<br />
<strong>Example</strong> &quot;<strong><font color="#0000ff">mkfs -t</font> <font color="#ff0000">ext3 /dev/sdb1</font></strong>&quot;<br />
<strong>Syntax</strong> &quot;<strong><font color="#0000ff">mkfs -t</font> &lt;<font color="#ff0000">File System Type</font>&gt; &lt;<font color="#ff0000">Target Partition</font>&gt;</strong>&quot;<br />
Here is the screen shot below..<br />
<a href="images/stories/screenshots/mkfs.jpg" rel="shadowbox[0]"><img alt="" style="width: 186px; height: 144px" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/mkfs.jpg" /></a></li>
</ul>
</div>
</div>
<p>&nbsp;</p>
<div class="important"><span class="important-title"><strong><strong>Mounting a File System</strong></strong></span></p>
<p>Here I will show you how to mount an NTFS File System.</p>
<ul>
<li>Run <strong>&quot;<font color="#0000ff">fdisk -l</font>&quot;</strong> as the root user or &quot;<font color="#0000ff"><strong>sudo fdisk -l</strong></font>&quot;<br />
Here is a screen shot of the output<br />
<a href="images/stories/screenshots/fdisk.jpg" rel="shadowbox[0]"><img alt="" style="width: 186px; height: 144px" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/fdisk.jpg" /></a></li>
<li>From<br />
that screen shot you can tell that my NTFS file system is /dev/sda2.<br />
Now I want to mount it. First thing you need to do is create a<br />
directory where you want to mount your NTFS file system at. <br />
<strong>Example</strong> &quot;<strong><font color="#0000ff">mkdir</font> <font color="#ff0000">/mnt/share</font></strong>&quot;<br />
<strong>Syntax</strong> &quot;<strong><font color="#0000ff">mkdir</font> &lt;<font color="#ff0000">Target Directory</font>&gt;</strong>&quot;
</li>
<li>Now it is time to mount the file system.<br />
<strong>Example</strong> &quot;<strong><font color="#0000ff">mount -t <font color="#ff0000">ntfs</font></font> <font color="#ff0000">/dev/sda2</font> <font color="#ff0000">/mnt/share</font></strong>&quot; <strong><br />
Syntax</strong> &quot;<strong><font color="#0000ff">mount -t</font> &lt;<font color="#ff0000">File System Type</font>&gt; &lt;<font color="#ff0000">File System</font>&gt; &lt;<font color="#ff0000">Target Directory</font>&gt;</strong>&quot;<br />
<span class="attention">This command will mount /dev/sda2 to /mnt/share as Read and Write by default.</span><br />
 just for sanity purposes,<br />
verify that you can write to that directory... <br />
<strong>Example</strong> &quot;<font color="#0000ff"><strong>touch</strong></font> <font color="#ff0000"><strong>/mnt/share/test</strong></font>&quot;<br />
<strong>Syntax</strong> &quot;<font color="#0000ff"><strong>touch</strong></font> &lt;<font color="#ff0000"><strong>create empty file at current or target directory</strong></font>&gt;&quot;
</li>
<li>Now when you run a &quot;<font color="#0000ff"><strong>df -h</strong></font>&quot;&nbsp; or &quot;<font color="#0000ff"><strong>mount</strong></font>&quot; and now you should see your mount at the bottom of the output of either command.
<p>here is a screen shot of the output of both commands.<br />
<a href="images/stories/screenshots/df_mount.jpg" rel="shadowbox[0]"><img alt="" style="width: 186px; height: 144px" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/df_mount.jpg" /></a></li>
<li>Now what if you want to mount that NTFS Volume as Read Only??<br />
First thing you need to do is unmount the volume. You can do this by running this command.<br />
<strong>Example</strong> &quot;<strong><font color="#0000ff">umount</font> <font color="#ff0000">/mnt/share</font></strong>&quot;<br />
<strong>Syntax</strong> &quot;<font color="#0000ff"><strong>umount</strong></font> <strong>&lt;<font color="#ff0000">Directory where file system is mounted</font>&gt;</strong><br />
As you can see the &quot;<font color="#0000ff"><strong>umount</strong></font>&quot; command is to unmount a file system. <br />
<span class="notice">There are quite a few good options to use with umount that we will discuss later.</span>&nbsp;</li>
<li>Now mount the file system using this command..<br />
<strong>Example</strong> &quot;<strong><font color="#0000ff">mount -t</font> <font color="#ff0000">ntfs</font> <font color="#0000ff">-o</font> <font color="#ff0000">ro /dev/sda2 /mnt/share</font></strong>&quot;<br />
<strong>Syntax</strong> &quot;<strong><font color="#0000ff">mount -t</font> &lt;<font color="#ff0000">File System Type</font>&gt; <font color="#0000ff">-o</font> &lt;<font color="#ff0000">Permissions</font>&gt; &lt;<font color="#ff0000">file system</font>&gt; &lt;<font color="#ff0000">Target Directory</font>&gt;</strong></li>
</ul>
</div>
<p>&nbsp;</p>
<div class="important"><span class="important-title"><strong>Add Mount to Automatically Mount After Every Reboot</strong></span></p>
<p>In the steps above I showed you how to delete/create a partition, how to create a filesystem, and how to mount/unmount the file system. Now I will show you how to make your system automaticall mount your file system every time. We can do this 2 ways, either using an editor (vi) or by appending the output to /etc/fstab. I will show you how to append ( I do not feel like teaching <font color="#0000ff"><strong>VI</strong></font> right now ;).</p>
<ul>
<li>Lets show you how to append the output to &quot;/etc/fstab&quot;.<br />
<span class="attention">I tried using <strong>sudo</strong> in front of echo but it did not work so I had to use the root account for the following..</span><br />
The Example below will automatically mount /dev/sda2 to /mnt/share using the ntfs file system and mounting as &quot;<strong>ro</strong>&quot; Read Only. <br />
You could also use the &quot;<strong>rw</strong>&quot; which is Read Write<br />
Example <strong><font color="#0000ff">echo</font> &quot;<font color="#ff0000">/dev/sda2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /mnt/share &nbsp;&nbsp; ntfs&nbsp;&nbsp;&nbsp; ro&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2</font>&quot; &gt;&gt;<font color="#ff0000"> /etc/fstab</font></strong><br />
Syntax <font color="#0000ff"><strong>echo</strong></font> &quot;<strong>&lt;<font color="#ff0000">file system</font>&gt; &lt;<font color="#ff0000">mount point</font>&gt;&nbsp;&nbsp; &lt;<font color="#ff0000">type</font>&gt;&nbsp; &lt;<font color="#ff0000">options</font>&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;<font color="#ff0000">dump</font>&gt;&nbsp; &lt;<font color="#ff0000">pass</font>&gt;</strong>&quot; &gt;&gt; &lt;<font color="#ff0000"><strong>File To Append To</strong></font>&gt;<br />
Here is the screen shot below..<br />
<a href="images/stories/screenshots/fstab.jpg" rel="shadowbox[0]"><img alt="" style="width: 186px; height: 144px" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/fstab.jpg" /></a>
</li>
</ul>
</div>
