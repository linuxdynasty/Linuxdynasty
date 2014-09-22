---
layout: post
status: publish
published: true
title: HowTo setup a Quorum Disk
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Today's tutorial will be on the infamous Quorum disk.  When I first setup
  my <a title=\"\" href=\"http://www.linuxdynasty.org/howto-setup-gfs2-with-clustering.html\">GFS2
  shared Cluster of 3 nodes</a>, I was quite impressed with the fact that 3 nodes
  were sharing the same file system.  Now that everything was up and running, I wanted
  to see what would happen if I brought down, 2 out of the 3 nodes in the cluster.
  I turned off 1st node and all was well, I was still able to access my GFS2 mount
  on the other 2 nodes. Then I decided to reboot the 2nd node, and guess what happened????
  QUORUM DISSOLVED!!! Now on my final node the GFS2 file system was still mounted
  but I could not touch a file or run a ls on the mount... It just hung there!!\r\n\r\nWell
  I knew this was not going to be acceptable.... Since if I still have 1 node available,
  the node should still be able to use the GFS2 mount. So I did some research about
  this quorum disk and what it can do for me. Let me tell you, this was exactly what
  I was looking for. 1st let me start out my explaining what a quorum is ( relating
  to clustering ). A quorum is the minimal number of votes that is needed in a cluster,
  usually the majority. So if you have 3 nodes in a cluster, that means you have a
  total of 3 votes in the cluster and you will need a minimum of 2 votes to remain
  in a quorate state. Which means you can lose 1 node in the cluster and the other
  nodes are still functional. But if you lose 2 nodes, your quorum will be dissolved.
  Which means even though your GFS2 file system is still mounted on your final node,
  it will not be accessible to you.\r\n\r\nThe quorum disk will help this particular
  situation... You ask how???? Well here it is...  Qdisk needs at a minimum of a 10MB
  disk partition shared across the cluster.\r\nQdiskd runs on each node in the cluster,
  periodically checking its\r\nown health and then placing its state information into
  its assigned\r\nportion of the shared disk. On each node qdiskd then looks at the
  state of\r\nthe other nodes in the cluster as posted in their area of the qdisk\r\npartition.
  When all the nodes that are running qdiskd are in a healthy state, the quorum of
  the cluster is increased by the value of the shared Quorum Disk.\r\n\r\n<span class=\"attention\">The
  Value of the Quorum Disk should be n-1 ( Number of nodes - 1 ). In this case the
  Value should be 2 ( 3 -1 ).</span>\r\n\r\n"
wordpress_id: 217
wordpress_url: http://linuxdynasty.org/?p=217
date: !binary |-
  MjAwOS0wOC0yNCAwMToyNToyMiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wOC0yNCAwMToyNToyMiAtMDQwMA==
categories:
- Clustering
tags:
- RedHat Clustering
- HowTo setup a Quorum Disk
comments: []
---
<p>Today's tutorial will be on the infamous Quorum disk.  When I first setup my <a title="" href="http://www.linuxdynasty.org/howto-setup-gfs2-with-clustering.html">GFS2 shared Cluster of 3 nodes</a>, I was quite impressed with the fact that 3 nodes were sharing the same file system.  Now that everything was up and running, I wanted to see what would happen if I brought down, 2 out of the 3 nodes in the cluster. I turned off 1st node and all was well, I was still able to access my GFS2 mount on the other 2 nodes. Then I decided to reboot the 2nd node, and guess what happened???? QUORUM DISSOLVED!!! Now on my final node the GFS2 file system was still mounted but I could not touch a file or run a ls on the mount... It just hung there!!</p>
<p>Well I knew this was not going to be acceptable.... Since if I still have 1 node available, the node should still be able to use the GFS2 mount. So I did some research about this quorum disk and what it can do for me. Let me tell you, this was exactly what I was looking for. 1st let me start out my explaining what a quorum is ( relating to clustering ). A quorum is the minimal number of votes that is needed in a cluster, usually the majority. So if you have 3 nodes in a cluster, that means you have a total of 3 votes in the cluster and you will need a minimum of 2 votes to remain in a quorate state. Which means you can lose 1 node in the cluster and the other nodes are still functional. But if you lose 2 nodes, your quorum will be dissolved. Which means even though your GFS2 file system is still mounted on your final node, it will not be accessible to you.</p>
<p>The quorum disk will help this particular situation... You ask how???? Well here it is...  Qdisk needs at a minimum of a 10MB disk partition shared across the cluster.<br />
Qdiskd runs on each node in the cluster, periodically checking its<br />
own health and then placing its state information into its assigned<br />
portion of the shared disk. On each node qdiskd then looks at the state of<br />
the other nodes in the cluster as posted in their area of the qdisk<br />
partition. When all the nodes that are running qdiskd are in a healthy state, the quorum of the cluster is increased by the value of the shared Quorum Disk.</p>
<p><span class="attention">The Value of the Quorum Disk should be n-1 ( Number of nodes - 1 ). In this case the Value should be 2 ( 3 -1 ).</span></p>
<p><a id="more"></a><a id="more-217"></a></p>
<p>If on a particular node, qdisk is unable to access its shared disk<br />
area after several attempts. The qdiskd running on another node in<br />
the cluster will request that the node which has issues communicating, to be fenced. Now that you have the basic understanding of what Qdisk is, I will now show you how to set it up.</p>
<ol>
<li>You will need a shared volume like ( iscsi, Fiber, VMware Shared Disk, etc.. )  that can be accessed by all nodes in the cluster. In this tutorial I am using a shared vmdk, and on all my nodes that is /dev/sdc. I will be using the 1st partition on /dev/sdc
<pre>fdisk -l /dev/sdc

Disk /dev/sdc: 5368 MB, 5368709120 bytes255 heads, 63 sectors/track, 652 cylindersUnits = cylinders of 10065 * 512 = 8225280 bytes

   Device Boot      Start         End      Blocks   Id  System/dev/sdc1               1           2       16033+  83  Linux/dev/sdc2               3         652     5221125   83  Linux</pre>
<p>&nbsp;</li>
<li>Once the volumes are accessible from all the nodes, you will now need to create the Quorum Disk.example below...
<pre>mkqdisk -c /dev/sdc1 -l testQdisk

mkqdisk v0.6.0Writing new quorum disk label 'testQdisk' to /dev/sdc1.WARNING: About to destroy all data on /dev/sdc1; proceed [N/y] ? yWarning: Initializing previously initialized partitionInitializing status block for node 1...Initializing status block for node 2...Initializing status block for node 3...Initializing status block for node 4...Initializing status block for node 5...Initializing status block for node 6...Initializing status block for node 7...Initializing status block for node 8...Initializing status block for node 9...Initializing status block for node 10...Initializing status block for node 11...Initializing status block for node 12...Initializing status block for node 13...Initializing status block for node 14...Initializing status block for node 15...Initializing status block for node 16...</pre>
</li>
<li>Now we need to verify that the quorum disk has been initialized correctly. You should run the blow command on all 3 nodes, so that you have a piece of mind.... Example below..
<pre>mkqdisk -L

mkqdisk v0.6.0/dev/disk/by-path/pci-0000:00:11.0-scsi-0:0:1:0-part1:/dev/sdc1:        Magic:                eb7a62c2        Label:                testQdisk        Created:              Mon Aug 24 10:20:25 2009        Host:                 gfs1        Kernel Sector Size:   512        Recorded Sector Size: 512</pre>
</li>
<li>We now need to add the qdisk information into /etc/cluster/cluster.conf after the  &lt;/clusternodes&gt; but before we do that, lets make a backup of cluster.conf... .example below
<pre>cp /etc/cluster/cluster.conf /etc/cluster.conf.orig</pre>
<p>Now we edit cluster.conf</p>
<pre>        &lt;/clusternodes&gt;        &lt;quorumd interval="3" tko="23" votes="2" label="testQdisk"&gt;        &lt;/quorumd&gt;</pre>
</li>
<li>Once you added the above info into cluster.conf, you should also increase the version number by 1. Example below..
<pre>&lt;cluster config_version="31" name="MyCluster"&gt;</pre>
</li>
<li>Now to verify that your config is correct, run ccs_tool update /etc/cluster/cluster.conf. If you get no errors from ccs_tool, you are now able to proceed to the next step.</li>
<li>You will then copy the new /etc/cluster/cluster.conf to the other 2 nodes in the cluster.
<pre>scp /etc/cluster/cluster.conf gfs2:/etc/clusterscp /etc/cluster/cluster.conf gfs3:/etc/cluster</pre>
</li>
<li>Now restart the CMAN daemon on all 3 nodes like so "service cman restart". Now wait a minutes or so and run clustat on all 3 nodes, you will notice that a quorum disk entry should popup on the bottom of the list like so..
<pre>clustatCluster Status for MyCluster @ Mon Aug 24 10:40:47 2009Member Status: Quorate

 Member Name                                                     ID   Status ------ ----                                                     ---- ------ gfs1                                                            1 Online, Local gfs2                                                            2 Online gfs3                                                            3 Online /dev/disk/by-path/pci-0000:00:11.0-scsi-0:0:1:0-part1           0 Offline, Quorum Disk</pre>
<p>Or you can taill -f /var/log/messages</p>
<p><small>Aug 24 10:39:32 gfs3 qdiskd[14488]: &lt;info&gt; Quorum Partition: /dev/disk/by-path/pci-0000:00:11.0-scsi-0:0:3:0-part1 Label: testQdisk Aug 24 10:39:32 gfs3 qdiskd[14489]: &lt;info&gt; Quorum Daemon Initializing Aug 24 10:40:47 gfs3 qdiskd[14489]: &lt;info&gt; Initial score 1/1 Aug 24 10:40:47 gfs3 qdiskd[14489]: &lt;info&gt; Initialization complete Aug 24 10:40:47 gfs3 openais[2561]: [CMAN ] quorum device registered Aug 24 10:40:47 gfs3 qdiskd[14489]: &lt;notice&gt; Score sufficient for master operation (1/1; required=1); upgrading </small>&nbsp;</li>
<li>We are pretty much done now. All we need to do now is verify that our total votes went from 3 to 5 and our expected votes went from 2 to 3..
<pre>cman_tool status

Version: 6.1.0Config Version: 32Cluster Name: MyClusterCluster Id: 46516Cluster Member: YesCluster Generation: 384Membership state: Cluster-MemberNodes: 3Expected votes: 3Quorum device votes: 2Total votes: 5Quorum: 3  Active subsystems: 10Flags: Dirty Ports Bound: 0 11 177  Node name: gfs1Node ID: 1Multicast addresses: 239.192.181.106 Node addresses: 192.168.101.100</pre>
</li>
</ol>
<p>Well that was not that bad.... Was it??? If all went well you can now have the GFS2 shared file system mounted on either 1 or 3 nodes and it will still be accessible by your cluster. Also your cluster will still be quorate, even if you are down to 1 node in that cluster.</p>
