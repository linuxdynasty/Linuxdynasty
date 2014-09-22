---
layout: post
status: publish
published: true
title: HowTo monitor RedHat Cluster using snmp and python
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "Now that I am done with the implementation of RHE Cluster with GFS2, I
  now need to setup monitoring. As you all know, monitoring is a vital part of any
  environment. Even though we have a cluster of nodes setup, we still need to be aware
  of what is happening. Currently here are 2 very important tools, for checking the
  cluster status.\r\n\r\n<span style=\"color: #0000ff;\"><strong>clustat</strong>
  </span> ( which is installed by the rgmanager rpm ) The clustat command will give
  you a quick status about all the nodes in the cluster and of the services running.\r\n<span
  style=\"color: #0000ff;\"><strong>cman_tool</strong></span> ( which is installed
  by the cman rpm ) The cman_tool command is for managing a node in the cluster (
  leaving, joining, votes, and status ).\r\n\r\nHere is an example of <span style=\"color:
  #0000ff;\"><strong>clustat</strong></span>...\r\n<pre><code>clustat Cluster Status
  for MyCluster @ Sat Aug 29 18:37:27 2009Member Status: Quorate Member Name ID Status
  ------ ---- ---- ------ gfs1 1 Online, Local, rgmanager gfs2 2 Online, rgmanager
  gfs3 3 Online, rgmanager /dev/disk/by-path/pci-0000:00:11.0-scsi-0:0:1:0-part1 0
  Online, Quorum Disk Service Name Owner (Last) State ------- ---- ----- ------ -----
  service:CIM gfs1 started service:Pirahna (gfs2) disabled</code></pre>\r\n&nbsp;\r\n\r\n"
wordpress_id: 218
wordpress_url: http://linuxdynasty.org/?p=218
date: !binary |-
  MjAwOS0wOC0yOCAxNTowNTo1MSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wOC0yOCAxNTowNTo1MSAtMDQwMA==
categories:
- Clustering
tags:
- RedHat Clustering
- HowTo monitor RedHat Cluster using snmp and python
comments: []
---
<p>Now that I am done with the implementation of RHE Cluster with GFS2, I now need to setup monitoring. As you all know, monitoring is a vital part of any environment. Even though we have a cluster of nodes setup, we still need to be aware of what is happening. Currently here are 2 very important tools, for checking the cluster status.</p>
<p><span style="color: #0000ff;"><strong>clustat</strong> </span> ( which is installed by the rgmanager rpm ) The clustat command will give you a quick status about all the nodes in the cluster and of the services running.<br />
<span style="color: #0000ff;"><strong>cman_tool</strong></span> ( which is installed by the cman rpm ) The cman_tool command is for managing a node in the cluster ( leaving, joining, votes, and status ).</p>
<p>Here is an example of <span style="color: #0000ff;"><strong>clustat</strong></span>...</p>
<pre><code>clustat Cluster Status for MyCluster @ Sat Aug 29 18:37:27 2009Member Status: Quorate Member Name ID Status ------ ---- ---- ------ gfs1 1 Online, Local, rgmanager gfs2 2 Online, rgmanager gfs3 3 Online, rgmanager /dev/disk/by-path/pci-0000:00:11.0-scsi-0:0:1:0-part1 0 Online, Quorum Disk Service Name Owner (Last) State ------- ---- ----- ------ ----- service:CIM gfs1 started service:Pirahna (gfs2) disabled</code></pre>
<p>&nbsp;</p>
<p><a id="more"></a><a id="more-218"></a></p>
<p>Here is an example of the <span style="color: #0000ff;"><strong>cman_tool</strong></span> command...</p>
<pre>cman_tool statusVersion: 6.1.0Config Version: 39Cluster Name: MyClusterCluster Id: 46516Cluster Member: YesCluster Generation: 392Membership state: Cluster-MemberNodes: 3Expected votes: 5Quorum device votes: 2Total votes: 5Quorum: 3  Active subsystems: 10Flags: Dirty Ports Bound: 0 11 177  Node name: gfs1Node ID: 1Multicast addresses: 239.192.181.106 Node addresses: 192.168.101.100</pre>
<p>As you noticed above, the information you get from both commands are extremely useful. The issue is that if you want the information from <span style="color: #0000ff;"><strong>clustat</strong></span> or <span style="color: #0000ff;"><strong>cman_tool</strong></span>, you will have to run those commands on a node that is part of the cluster. The reason this is an issue to me, is because I do not want to be burdened with sshing into one of the nodes anytime I want to know the status of the cluster. I want to be able to get that info directly from my desktop or from my monitoring system. After some research I discovered that there is a package called cluster-snmp that is part fo the yum "Clustering" Group.</p>
<p>This was exactly what I was looking for! A way to monitor or check the status of my cluster with out ssh. The next step is to configure cluster-snmp so that we can use it..<br />
<span class="note">NOTE... please do the following commands on all the nodes in your cluster...</span></p>
<ol>
<li>yum install cluster-snmp</li>
<li>vi /etc/snmp/snmpd.conf<br />
If your nodes are 32bit, add this into the file</p>
<pre class="jive-pre"><code class="jive-code">dlmod RedHatCluster /usr/lib/cluster-snmp/libClusterMonitorSnmp.soview systemview included REDHAT-CLUSTER-MIB:RedHatCluster</code></pre>
<p>Or if your nodes are 64bit, add this into the file</p>
<pre class="jive-pre"><code class="jive-code">dlmod RedHatCluster /usr/lib64/cluster-snmp/libClusterMonitorSnmp.soview systemview included REDHAT-CLUSTER-MIB:RedHatCluster</code></pre>
</li>
<li>restart snmpd ( service snmpd restart )</li>
<li>Now do a snmpwalk... Example below..
<pre>snmpwalk -v2c -c public  localhost REDHAT-CLUSTER-MIB::RedHatCluster</pre>
<pre>REDHAT-CLUSTER-MIB::rhcMIBVersion.0 = INTEGER: 1REDHAT-CLUSTER-MIB::rhcClusterName.0 = STRING: "MyCluster"REDHAT-CLUSTER-MIB::rhcClusterStatusCode.0 = INTEGER: 4REDHAT-CLUSTER-MIB::rhcClusterStatusDesc.0 = STRING: "Some services not running"REDHAT-CLUSTER-MIB::rhcClusterVotesNeededForQuorum.0 = INTEGER: 3REDHAT-CLUSTER-MIB::rhcClusterVotes.0 = INTEGER: 5REDHAT-CLUSTER-MIB::rhcClusterQuorate.0 = INTEGER: 1REDHAT-CLUSTER-MIB::rhcClusterNodesNum.0 = INTEGER: 3REDHAT-CLUSTER-MIB::rhcClusterNodesNames.0 = STRING: "gfs1, gfs2, gfs3"REDHAT-CLUSTER-MIB::rhcClusterAvailNodesNum.0 = INTEGER: 3REDHAT-CLUSTER-MIB::rhcClusterAvailNodesNames.0 = STRING: "gfs1, gfs2, gfs3"REDHAT-CLUSTER-MIB::rhcClusterUnavailNodesNum.0 = INTEGER: 0REDHAT-CLUSTER-MIB::rhcClusterUnavailNodesNames.0 = ""REDHAT-CLUSTER-MIB::rhcClusterServicesNum.0 = INTEGER: 2REDHAT-CLUSTER-MIB::rhcClusterServicesNames.0 = STRING: "Pirahna, CIM"REDHAT-CLUSTER-MIB::rhcClusterRunningServicesNum.0 = INTEGER: 1REDHAT-CLUSTER-MIB::rhcClusterRunningServicesNames.0 = STRING: "CIM"REDHAT-CLUSTER-MIB::rhcClusterStoppedServicesNum.0 = INTEGER: 1REDHAT-CLUSTER-MIB::rhcClusterStoppedServicesNames.0 = STRING: "Pirahna"REDHAT-CLUSTER-MIB::rhcClusterFailedServicesNum.0 = INTEGER: 0REDHAT-CLUSTER-MIB::rhcClusterFailedServicesNames.0 = ""REDHAT-CLUSTER-MIB::rhcNodeName."gfs1" = STRING: "gfs1"REDHAT-CLUSTER-MIB::rhcNodeName."gfs2" = STRING: "gfs2"REDHAT-CLUSTER-MIB::rhcNodeName."gfs3" = STRING: "gfs3"REDHAT-CLUSTER-MIB::rhcNodeStatusCode."gfs1" = INTEGER: 0REDHAT-CLUSTER-MIB::rhcNodeStatusCode."gfs2" = INTEGER: 0REDHAT-CLUSTER-MIB::rhcNodeStatusCode."gfs3" = INTEGER: 0REDHAT-CLUSTER-MIB::rhcNodeStatusDesc."gfs1" = STRING: "Participating in cluster"REDHAT-CLUSTER-MIB::rhcNodeStatusDesc."gfs2" = STRING: "Participating in cluster"REDHAT-CLUSTER-MIB::rhcNodeStatusDesc."gfs3" = STRING: "Participating in cluster"REDHAT-CLUSTER-MIB::rhcNodeRunningServicesNum."gfs1" = INTEGER: 1REDHAT-CLUSTER-MIB::rhcNodeRunningServicesNum."gfs2" = INTEGER: 0REDHAT-CLUSTER-MIB::rhcNodeRunningServicesNum."gfs3" = INTEGER: 0REDHAT-CLUSTER-MIB::rhcNodeRunningServicesNames."gfs1" = STRING: "CIM"REDHAT-CLUSTER-MIB::rhcNodeRunningServicesNames."gfs2" = ""REDHAT-CLUSTER-MIB::rhcNodeRunningServicesNames."gfs3" = ""REDHAT-CLUSTER-MIB::rhcServiceName."CIM" = STRING: "CIM"REDHAT-CLUSTER-MIB::rhcServiceName."Pirahna" = STRING: "Pirahna"REDHAT-CLUSTER-MIB::rhcServiceStatusCode."CIM" = INTEGER: 0REDHAT-CLUSTER-MIB::rhcServiceStatusCode."Pirahna" = INTEGER: 1REDHAT-CLUSTER-MIB::rhcServiceStatusDesc."CIM" = STRING: "running"REDHAT-CLUSTER-MIB::rhcServiceStatusDesc."Pirahna" = STRING: "stopped"REDHAT-CLUSTER-MIB::rhcServiceStartMode."CIM" = STRING: "automatic"REDHAT-CLUSTER-MIB::rhcServiceStartMode."Pirahna" = STRING: "automatic"REDHAT-CLUSTER-MIB::rhcServiceRunningOnNode."CIM" = STRING: "gfs1"</pre>
</li>
</ol>
<p>As you can see you get a wealth of information from SNMP, though it is not all the information you need, but it has about 90% of what is important... So I decided to massage the data I get from snmp and create my own <a href="View-details/LinuxDynasty/45-clustat_snmp.py.html"><span style="color: #0000ff;"><strong>clustat_snmp.py</strong></span></a> command and my own <span style="color: #0000ff;"><strong><a href="View-details/Clustering-Tools/46-rh_cluster_check.py.html">rhe_cluster_check.py</a> </strong></span>. One command is to behave some what like the clustat utility and the other command is to check the status of your cluster through snmp, for monitoring systems like Nagios and Zenoss.</p>
<p>clustat_snmp.py =={filelink=17}<br />
Here is an example of the output you will get from<a href="View-details/LinuxDynasty/45-clustat_snmp.py.html"><span style="color: #0000ff;"><strong> clustat_snmp.py</strong></span>..</a></p>
<p><small>clustat_snmp.py -d gfs1 -c publicCluster Status for MyCluster @ Fri Aug 28 11:59:40 2009Member Status: QuorateTotal Nodes: 3Total Votes: 5Votes Needed For Quorum: 3</small><small> Member Name Status ------ ---- ------ gfs1 Participating in cluster gfs2 Participating in cluster gfs3 Participating in cluster Service Name Owner State Start Up Mode ------- ---- ----- ----- ------------- Pirahna stopped automatic CIM gfs1 running automatic</small></p>
<p>As you can see above, you get some of what the <span style="color: #0000ff;"><strong>clustat</strong></span> command gives you and some of what the <span style="color: #0000ff;"><strong>cman_tool status</strong></span> command gives you. But you get it all in one command through Python and Snmp. For both Python scripts you will need the two python modules. which are pysnmp and pyasn1.<br />
To make your life easier you should do the following...</p>
<ol>
<li>install <a title="title" href="http://pypi.python.org/pypi/setuptools">python-setuptools<br />
</a></li>
<li>then run easy_install pysnmp</li>
<li>and easy_install pyasn1</li>
<li>or you can download the 2 modules manually.<br />
<a title="title" href="http://voxel.dl.sourceforge.net/sourceforge/pysnmp/pysnmp-4.1.10a.tar.gz">pysnmp</a> and <a title="title" href="http://voxel.dl.sourceforge.net/sourceforge/pyasn1/pyasn1-0.0.8a.tar.gz">pyasn1</a></li>
<li>then unzip the 2 files and in each directory run <strong>python setup.py install</strong></li>
</ol>
<p>I am using the following revisions from the python cheese shop pysnmp 4.1.7a and pyasn1 0.0.6</p>
<p>The next command is the Nagios/Zenoss compatible <span style="color: #0000ff;"><strong>rh_cluster_check.py.</strong></span>..<br />
{filelink=18}<br />
Here is an example of the output you will get from rh_cluster_check.py..</p>
<pre>     python rh_cluster_check.py -d gfs1 -c public -t node -n gfs3      OK, gfs3 is Participating in cluster</pre>
<pre>      python rh_cluster_check.py -d gfs1 -c public -t service -s CIM      OK, CIM is running on gfs1</pre>
<pre>      python rh_cluster_check.py -d gfs2 -c public -t cluster      WARNING, MyCluster is Quorate and Some services not running

      python rh_cluster_check.py -d gfs1 -c public -t service -s Pirahna      CRITICAL, Pirahna is stopped</pre>
<p>The above command will allow you to check your cluster information by the means of pysnmp. You can check on the status of a particular node, the status of the cluster, and the status of a service.</p>
<p>&nbsp;</p>
