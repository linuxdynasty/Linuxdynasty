---
layout: post
status: publish
published: true
title: HowTo Remaster a LiveCD or LiveDVD using SLAX
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>The other day I had to come up with a way to transfer a Solaris Express
  nv97 DVD 3G image to remote locations while not using the network. The reason for
  this is, I needed to perform a LiveUpgrade on over 700 boxes and each being at a
  different locations. So I said to myself I guess I can put this image on a custom
  LiveDVD... But then I said to myself, which Linux LiveCD/DVD distro will I use????
  It has to be small enough so that I can fit the Solaris Express nv97 image as well
  as the LiveCD Image. </p>\r\n<br />"
wordpress_id: 19
wordpress_url: http://linuxdynasty.org/?p=19
date: !binary |-
  MjAwOC0wOS0xNiAxOToyMDozNyAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wOS0xNiAxOToyMDozNyAtMDQwMA==
categories: []
tags:
- Advance Linux HowTo's
- HowTo Remaster a LiveCD or LiveDVD using SLAX
comments: []
---
<p>The other day I had to come up with a way to transfer a Solaris Express nv97 DVD 3G image to remote locations while not using the network. The reason for this is, I needed to perform a LiveUpgrade on over 700 boxes and each being at a different locations. So I said to myself I guess I can put this image on a custom LiveDVD... But then I said to myself, which Linux LiveCD/DVD distro will I use???? It has to be small enough so that I can fit the Solaris Express nv97 image as well as the LiveCD Image. </p>
<p><a id="more"></a><a id="more-19"></a></p>
<p>I thought to first use Knoppix or Puppet Linux or even DSL Linux.. But after going through there documentation I was like ok, this is getting confusing!!! I decided to try first Knoppix and let me tell you during the compression phase it failed every time. Then I was on my way to try Puppy Linux, but right before I did that I ran into SLAX Linux. And I am so glad that I did! The instructions were straight to the pointand not to metnion easy to read.</p>
<p>So in this HowTo I will show you how to remaster your own LiveCD/DVD image using SLAX and some of the cool things that you can do with SLAX. All comments are appreciated and if you found this HowTo helpful then please digg and leave a comment. Thank You.</p>
<p>&nbsp;</p>
<p>I would suggest that you have either VirtualBox or VMware installed so you can do all your testing on VirtualMachines.</p>
<p>Requirements for me for this project were....</p>
<ul>
<li>Solaris Express nv97 DVD Image must fit on LiveDVD</li>
<li>sshd needs to be started with a valid root password</li>
<li>The Image needs to be shared via NFS</li>
</ul>
<p>&nbsp;&nbsp;<br />
&nbsp;</p>
<p>This HowTo makes some assumptions...</p>
<ul>
<li>You have used Linux before and understand how to use a terminal</li>
<li>You have used either VirtualBox or VMware Workstation&nbsp;</li>
<li>Create a VirtualDisk of at least 10G for this example... Now normally this all really depends on how many extra packages you want and files you want to addto the live Image that you are creating.
</li>
</ul>
<p>The first thing that you need to do is to download SLAX from this link&nbsp;<a href="http://www.slax.org/get_slax.php" title="">SLAX</a>. Now using either <a href="http://www.virtualbox.org/wiki/Downloads" title="Download VirtualBox">VirtualBox</a> or <a href="http://www.vmware.com/products/ws/" title="Download Free Trial of Vmware">Vmware</a>, boot into SLAX using the ISO image you downloaded. Once you are logged into the system you will follow the steps below...</p>
<ol>
<li><font color="#0000ff"><strong>fdisk -l</strong></font>&nbsp;&nbsp;&nbsp; { The reason for this command is that you want to see what available disk you have to use for this LiveDVD }
</li>
<li><strong><font color="#0000ff">fdisk</font> <font color="#ff0000">/dev/sda</font></strong>&nbsp; { This command you will use to create the partition you want to use }
</li>
<li><strong><font color="#0000ff">mkfs.ext3</font> <font color="#ff0000">/dev/sda1</font></strong> { This command will create the ext3 filesystem on /dev/sda1 }
</li>
<li><font color="#0000ff"><strong>fdisk -l&nbsp;</strong></font>&nbsp; { This command will show you the available partition that you just created above }
</li>
<li><strong><font color="#0000ff">mkdir</font> <font color="#ff0000">/mnt/NewSlax</font></strong>&nbsp;&nbsp; { here you will create the directorywhere you will mount the newly created filesystem }
</li>
<li><strong><font color="#0000ff">mount</font> <font color="#ff0000">/dev/sda1 /mnt/NewSlax/</font></strong>&nbsp; { Here you will mount the newly created filesystem on /mnt/NewSlax }
</li>
<li><font color="#0000ff"><strong>df -h</strong></font>&nbsp; { Here you will see the newly mounted drive and where it is mounted }
</li>
<li><font color="#0000ff"><strong>cp -rfpa</strong></font> <font color="#ff0000"><strong>/mnt/live/mnt/hdc/* /mnt/NewSlax/</strong></font>&nbsp; { This is where you will copy the entire SLAX Live env to the newly mounted partition }</li>
<li>Time to download the 3G Solaris Express nv97 image from <a href="http://opensolaris.org/os/downloads/sol_ex_dvd_1/" title="Solaris Express ">here</a>. Please make sure you save it into the IMAGES directory that you will create as so... <strong><font color="#0000ff">mkdir</font> <font color="#ff0000">/mnt/NewSlax/slax/IMAGES</font></strong>&nbsp; { This will take a while so spawn a new shell and contnue the following steps }</li>
<li><font color="#0000ff"><strong>cd</strong></font> <font color="#ff0000"><strong>/mnt/NewSlax/slax/modules/</strong></font>&nbsp; { Here you will change into the Live environment and change into the modules directory }
</li>
<li><font color="#0000ff"><strong>wget</strong></font> <strong><font color="#ff0000">http://www.slax.org/modules/618/dl/sshd-activate.lzm</font></strong>&nbsp; { Here we will download the sshd activate lzm compressed module, all this module contains is a sshd startup script so that sshd will start up by default as sshd comes with SLAX } </li>
<li><font color="#0000ff"><strong>cd</strong></font> <font color="#ff0000"><strong>~</strong></font>&nbsp; { We now change back into our home directory which is /root/ }</li>
<li><strong><font color="#0000ff">wget</font> <font color="#ff0000">http://carroll.cac.psu.edu/pub/linux/distributions/slackware/slackware-12.1/slackware/n/nfs-utils-1.1.2-i486-1.tgz</font></strong><br />
{ SLAX does not come with NFS support so we have to add it by downloading the slackware package of nfs-utils }
</li>
<li><strong><font color="#0000ff">wget</font> <font color="#ff0000">http://carroll.cac.psu.edu/pub/linux/distributions/slackware/slackware-12.1/slackware/n/portmap-6.0-i486-1.tgz</font></strong><br />
{ In order to install nfs-utils we will also need portmap for nfs to work }
</li>
<li><strong><font color="#0000ff">tgz2lzm</font> <font color="#ff0000">nfs-utils-1.1.2-i486-1.tgz</font> <font color="#ff0000">nfs-utils-1.1.2-i486-1.lzm</font></strong>&nbsp; { Time to convert the SLACKWARE tgz packaged nfs-utils using the custom built slax tool for converting slackware to lzm compressed modules for SLAX }
</li>
<li><strong><font color="#0000ff">tgz2lzm</font></strong> <font color="#ff0000"><strong>portmap-6.0-i486-1.tgz portmap-6.0-i486-1.lzm</strong></font> { repeating the same process above }
</li>
<li><strong><font color="#0000ff">mv</font> <font color="#ff0000">*.lzm /mnt/NewSlax/slax/modules/</font></strong>&nbsp; {Now we need to move the newly created LZM modules to the new live module directory in&nbsp; /mnt/NewSlax/slax/modules/ }
</li>
<li>Now it is time for us to create our own custom compressed module aka custom startup script. First thing to do is to create the directory structure of where you are going to place the files under the root aka '<strong>/</strong>' directory. </li>
<li><strong><font color="#0000ff">mkdir -p</font> <font color="#ff0000">MySampleRcScript/etc/rc.d/init.d</font></strong></li>
<li><strong><font color="#0000ff">mkdir -p</font> <font color="#ff0000">MySampleRcScript/etc/rc.d/rc3.d</font></strong></li>
<li><font color="#0000ff"><strong>cd</strong></font> <font color="#ff0000"><strong>MySampleRcScript/etc/rc.d/init.d/</strong></font></li>
<li><strong><font color="#0000ff">vi</font></strong> <font color="#ff0000"><strong>rc.mySampleRc</strong></font> { Here we need to create our startup script, in this startup script we will change the root password to test and the rest you can read off of the screenshot :) }<br />
<a href="http://www.linuxdynasty.org/images/stories/distros/slax/rc.png" rel="shadowbox[0]"><img alt="" style="width: 289px; height: 223px" src="http://www.linuxdynasty.org/images/stories/distros/slax/rc.png" /></a></li>
<li><font color="#0000ff"><strong>cd</strong></font> <font color="#ff0000"><strong>../rc3.d/</strong></font></li>
<li><font color="#0000ff"><strong>ln -s</strong></font> <font color="#ff0000"><strong>../init.d/rc.mySampleRc SmySampleRc</strong><font color="#000000">&nbsp; { Here we will symlink the original script to the default run level rc3.d directory and make sure to append a capital S in front of the startup script so that when sysv runs it will catch that script and start up properly. }<br />
</font></font></li>
<li><font color="#0000ff"><strong>ln -s</strong></font> <font color="#ff0000"><strong>../init.d/rc.mySampleRc KmySampleRc </strong><font color="#000000">{ Same as above except to stop the script during the shutdown process. }</font><br />
</font></li>
<li><font color="#0000ff"><strong>cd ~ </strong><font color="#000000">{ We now will change back into the root directory so that we can prepare for the final stage of the module creation }</font><br />
</font></li>
<li><font color="#0000ff"><strong>dir2lzm</strong></font> <font color="#ff0000"><strong>MySampleRcScript MySampleModule.lzm&nbsp; </strong><font color="#000000">{ Final stage of the module creation.... the dir2lzm will take that directory structure and convert it into the lzm compressed module }</font><br />
</font></li>
<li><font color="#0000ff"><strong>cp</strong></font> <font color="#ff0000"><strong>MySampleModule.lzm /mnt/NewSlax/slax/modules/</strong></font> { Now we will copy the newly created module into the new live environment module directory }</li>
<li><strong><font color="#0000ff">cd</font> <font color="#ff0000">/mnt/NewSlax/slax/</font></strong>&nbsp; { we ar almost done, we will now change into the new live environment root directory and prepare for the final step }
</li>
<li><strong><font color="#0000ff">./make_iso.sh</font>&nbsp; <font color="#ff0000">/mnt/NewSlax/NewSlax.iso</font></strong> { At last the final step and all you need to do is run a simple script called make_iso.sh}</li>
<li><font color="#0000ff"><strong>ls -ltrh<font color="#ff0000"> ../</font></strong></font> { The image should be a little above 3Gigs which is good considering you have a 3Gig iso image and a liveDVD environment under one dvd. }</li>
</ol>
<p>&nbsp;</p>
<p><a href="http://www.linuxdynasty.org/images/stories/distros/slax/initial_boot.png" rel="shadowbox[0]"><img alt="" style="width: 289px; height: 223px" src="http://www.linuxdynasty.org/images/stories/distros/slax/initial_boot.png" /></a><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step1.png" rel="shadowbox[0]"><img alt="" style="width: 274px; height: 224px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step1.png" /></a><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step3.png" rel="shadowbox[0]"><img alt="" style="width: 297px; height: 224px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step3.png" /></a></p>
<p><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step4.png" rel="shadowbox[0]"><img alt="" style="width: 289px; height: 223px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step4.png" /></a><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step5.png" rel="shadowbox[0]"><img alt="" style="width: 274px; height: 224px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step5.png" /></a><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step6.png" rel="shadowbox[0]"><img alt="" style="width: 297px; height: 224px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step6.png" /></a></p>
<p><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step7.png" rel="shadowbox[0]"><img alt="" style="width: 289px; height: 223px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step7.png" /></a><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step8.png" rel="shadowbox[0]"><img alt="" style="width: 274px; height: 224px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step8.png" /></a><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step9.png" rel="shadowbox[0]"><img alt="" style="width: 297px; height: 224px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step9.png" /></a></p>
<p><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step10.png" rel="shadowbox[0]"><img alt="" style="width: 289px; height: 223px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step10.png" /></a><a href="http://www.linuxdynasty.org/images/stories/distros/slax/step11.png" rel="shadowbox[0]"><img alt="" style="width: 274px; height: 224px" src="http://www.linuxdynasty.org/images/stories/distros/slax/step11.png" /></a></p>
