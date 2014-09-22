---
layout: post
status: publish
published: true
title: HowTo setup GFS2 with Clustering
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "In my last project at work, I had to replace NFS with GFS2 and Clustering.
  So in this tutorial I will show you how to create a Red Hat or CentOS cluster with
  GFS2. I will also show you how to optimize GFS2 performance in the next HowTo, because
  you will quickly notice some loss of performance until you do a little optimization
  first.I will 1st show you how do build a Cluster with GFS2 on the Command Line and
  in the next tutorial I will show you how to do the same thing using Conga.\r\n\r\nIn
  this tutorial I am using 3 CentOS Virtual Machines running CentOS 5.3 in VMware
  ESX 3.5. For the GFS2 File System I am using a vmdk built with the thick option,
  that is shared among all the Virtual Machines. You also can use iscsi or fiber...
  This option is up to you.\r\n\r\n<span class=\"attention\">Always make sure your
  iptables (If you know the port's and protocols for clustering, then add it to iptables
  ) and selinux is OFF. If not you will run into issues.</span>\r\n\r\nThe 3 machines
  I am using are called\r\n<ul>\r\n\t<li>gfs1 == 192.168.101.100</li>\r\n\t<li>gfs2
  == 192.168.101.101</li>\r\n\t<li>gfs3 == 192.168.101.103</li>\r\n</ul>\r\n"
wordpress_id: 215
wordpress_url: http://linuxdynasty.org/?p=215
date: !binary |-
  MjAwOS0wOC0xNCAxNjo0ODo0OSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wOC0xNCAxNjo0ODo0OSAtMDQwMA==
categories:
- Clustering
tags:
- RedHat Clustering
- HowTo setup GFS2 with Clustering
- GFS2 Clustering
comments:
- id: 34
  author: Bubbagump
  author_email: cburke@innova-partners.com
  author_url: ''
  date: !binary |-
    MjAxMi0wMS0yMCAwMjo1Nzo1MiAtMDUwMA==
  date_gmt: !binary |-
    MjAxMi0wMS0xOSAyMTo1Nzo1MiAtMDUwMA==
  content: What confuses me in all of the online cook books is that can you use GFS2
    without clustering? As in, can I create a shared LUN, format it as GFS2, mount
    it on 3 hosts, and have it work? Or must the nodes be aware of each other somehow
    outside of the shared storage? I don't care about shared IPs or the like, I just
    need a replacement for NFS as I have a load balancer in front of my web servers
    that will determine if a host is dead and react accordingly.
- id: 35
  author: dynasty
  author_email: asanabria@linuxdynasty.org
  author_url: ''
  date: !binary |-
    MjAxMi0wMS0yMCAxOTo1MToyNiAtMDUwMA==
  date_gmt: !binary |-
    MjAxMi0wMS0yMCAxNDo1MToyNiAtMDUwMA==
  content: Since I no longer actually work with GFS, I could not really give you an
    answer. From the time I worked with it, I do not think it is a viable solution
    as a replacement for nfs. Then again that was almost 2 years ago.. I'm sure much
    has probably changed since than.
---
<p>In my last project at work, I had to replace NFS with GFS2 and Clustering. So in this tutorial I will show you how to create a Red Hat or CentOS cluster with GFS2. I will also show you how to optimize GFS2 performance in the next HowTo, because you will quickly notice some loss of performance until you do a little optimization first.I will 1st show you how do build a Cluster with GFS2 on the Command Line and in the next tutorial I will show you how to do the same thing using Conga.</p>
<p>In this tutorial I am using 3 CentOS Virtual Machines running CentOS 5.3 in VMware ESX 3.5. For the GFS2 File System I am using a vmdk built with the thick option, that is shared among all the Virtual Machines. You also can use iscsi or fiber... This option is up to you.</p>
<p><span class="attention">Always make sure your iptables (If you know the port's and protocols for clustering, then add it to iptables ) and selinux is OFF. If not you will run into issues.</span></p>
<p>The 3 machines I am using are called</p>
<ul>
<li>gfs1 == 192.168.101.100</li>
<li>gfs2 == 192.168.101.101</li>
<li>gfs3 == 192.168.101.103</li>
</ul>
<p><a id="more"></a><a id="more-215"></a></p>
<p>Since I'm using VMware ESX for the 3 machines above I will also be using vmware for fencing. The info is below for my test setup</p>
<ul>
<li>ESX Host Name == esxtest<br />
ESX IP Address == 192.168.101.50</li>
<li>ESX user login info below<br />
login == esxuser<br />
password == esxpass</li>
<li>ESX admin login info below<br />
login == root<br />
password == esxpass</li>
</ul>
<p>&nbsp;</p>
<p>The 1st command you need to know for creating and modifying your cluster is the '<strong>ccs_tool</strong>' command.</p>
<p>Below I will show you the necessary steps to create a cluster and then the GFS2 filesystem</p>
<ol>
<li>First step is to install the necessary RPM's..<br />
<strong>yum -y install modcluster rgmanager gfs2 gfs2-utils lvm2-cluster cman</strong></li>
<li>Second step is to create a cluster on gfs1<br />
<strong>ccs_tool create GFStestCluster</strong></li>
<li>Now that the cluster is created, we will now need to add the fencing devices.<br />
( For simplicity you can just use fence_manual for each host.. <strong>ccs_tool addfence -C gfs1_ipmi fence_manual</strong> )<br />
But if you are using VMware ESX like I am you should use fence_vmware like so...<br />
<strong>ccs_tool addfence -C gfs1_vmware fence_vmware ipaddr=esxtest login=esxuser passwd=esxpass vmlogin=root vmpasswd=esxpass port="/vmfs/volumes/49086551-c64fd83c-0401-001e0bcd6848/eagle1/gfs1.vmx"</strong><br />
<strong>ccs_tool addfence -C gfs2_vmware fence_vmware ipaddr=esxtest login=esxuser passwd=esxpass vmlogin=root vmpasswd=esxpass port="vmfs/volumes/49086551-c64fd83c-0401-001e0bcd6848/gfs2/gfs2.vmx"</strong><br />
<strong>ccs_tool addfence -C gfs3_vmware fence_vmware ipaddr=esxtest login=esxuser passwd=esxpass vmlogin=root vmpasswd=esxpass port="/vmfs/volumes/49086551-c64fd83c-0401-001e0bcd6848/gfs3/gfs3.vmx"</strong></li>
<li>Now that we added the Fencing devices, it is time to add the nodes..<br />
<strong>ccs_tool addnode -C gfs1 -n 1 -v 1 -f gfs1_vmware<br />
ccs_tool addnode -C gfs2 -n 2 -v 1 -f gfs2_vmware<br />
ccs_tool addnode -C gfs3 -n 3 -v 1 -f gfs3_vmware</strong></li>
<li>Now we need to copy this configuration over to the other 2 nodes from gfs1 or we can run the exact same commands above on the other 2 nodes..<br />
<strong>scp /etc/cluster/cluster.conf root@gfs2:/etc/cluster/cluster.conf<br />
scp /etc/cluster/cluster.conf root@gfs3:/etc/cluster/cluster.conf</strong></li>
<li>You can verify the config on all 3 nodes by running the following commands below..<br />
<strong>ccs_tool lsnode<br />
ccs_tool lsfence</strong></li>
<li>You are ready to proceed with starting up the following daemons on all the nodes in the cluster, once you either copied over the configs or re ran the same commands above on the other 2 nodes<br />
<strong>/etc/init.d/cman start<br />
/etc/init.d/rgmanager start</strong></li>
<li>You can now check the status of your cluster by running the commands below...<strong><br />
clustat<br />
cman_tool status</strong></li>
<li>If you want to test the vmware fencing you can do so by doing the following..<strong> ( </strong>run the command below on the 1st node and use the 2nd node as the node to be fenced<strong> )<br />
fence_vmware -a esxtest -l esxuser -p esxpass -L root -P esxpass -n "/vmfs/volumes/49086551-c64fd83c-0401-001e0bcd6848/gfs2/gfs2.vmx" -v<br />
</strong></li>
<li>Before we start to create the LVM2 volumes and Proceed to GFS2, we will need to enable clustering in LVM2.<br />
<strong>lvmconf --enable-cluster</strong></li>
<li>Now it is time to create the LVM2 Volumes...<br />
<strong>pvcreate MyTestGFS /dev/sdb<br />
vgcreate -c y mytest_gfs2 /dev/sdb<br />
lvcreate -n MyGFS2test -L 5G mytest_gfs2<br />
/etc/init.d/clvmd start</strong></li>
<li>You should now also start <strong>clvmd</strong> on the other 2 nodes..<strong><br />
</strong></li>
<li>Once the above has been completed, you will now need to create the GFS2 file system.. Example below..<br />
mkfs -t &lt;filesystem&gt; -p &lt;locking mechanism&gt; -t &lt;ClusterName&gt;:&lt;PhysicalVolumeName&gt; -j &lt;JournalsNeeded == amount of nodes in cluster&gt; &lt;location of filesystem&gt;<br />
<strong>mkfs -t gfs2 -p lock_dlm -t MyCluster:MyTestGFS -j 4 /dev/mapper/mytest_gfs2-MyGFS2test</strong></li>
<li>All we need to do on the 3 nodes, is to mount the GFS2 file system.<br />
<strong>mount /dev/mapper/mytest_gfs2-MyGFS2test /mnt/<br />
</strong></li>
<li>Once you mounted your GFS2 file system You can the following commands..<strong><br />
gfs2_tool list<br />
gfs2_tool df </strong></li>
</ol>
<p>Now it is time to wrap it up with some final commands...</p>
<ol>
<li>Now that we have a fully functional cluster and a mountable GFS2 file system, we need to make sure all the necessary daemons start up with the cluster..<br />
<strong>chkconfig --level 345 rgmanager on<br />
chkconfig --level 345 clvmd on<br />
chkconfig --level 345 cman on<br />
chkconfig --level 345 gfs2 on</strong></li>
<li>If you want the GFS2 file system to be mounted at startup you can add this to /etc/fstab..<br />
<strong>echo "/dev/mapper/mytest_gfs2-MyGFS2test /GFS gfs2 defaults,noatime,nodiratime 0 0" &gt;&gt; /etc/fstab</strong></li>
</ol>
<p>In the next up coming tutorials I will show you how to do the same as above but with the Red Hat Conga gui and I will also show you how to optimize your GFS2 Cluster setup.</p>
