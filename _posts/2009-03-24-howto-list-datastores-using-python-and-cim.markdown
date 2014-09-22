---
layout: post
status: publish
published: true
title: HowTo List DataStores using Python and CIM
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p><span>Here I created another Python script using Pywbem to get the
  Storage Pools from ESX. <br /> In this script you can get the disk utilisation statistics
  from each datastore or from a particular datastore. <br /> <span class=\"attention\">Script
  Updated to include the .VMX files that belong to each DataStore..</span></span></p>\r\n<p><span><br
  /> <span style=\"font-family: monospace\"> example below...<br /> python VMdataStorePool.py
  -u \"http://esxhost\" -a \"login passwd\"<br /> Available DataStores on http://esxhost<br
  /> <br /> DataStore Name                   Esxtestvol2<br /> Total Disk Space                
  499G<br /> Remaining Disk Space             189G<br /> Used Disk Space                 
  310G<br /> Percentage Used                  62%<br /> VMX files that belong to this
  DataStore::<br /> [Esxtestvol2] Win2003test3/Win2003test3.vmx<br /> [Esxtestvol2]
  netwaretest/netwaretest.vmx<br /> [Esxtestvol2] RHEL 4 NFS test/RHEL 4 NFS test.vmx<br
  /> [Esxtestvol2] RHEL 5 NFS test/RHEL 5 NFS test.vmx<br /> [Esxtestvol2] RHEL 3
  NFS test/RHEL 3 NFS test.vmx<br /> [Esxtestvol2] vicfg/vicfg.vmx<br /> <br /> DataStore
  Name                   ISO<br /> Total Disk Space                 49G<br /> Remaining
  Disk Space             38G<br /> Used Disk Space                  11G<br /> Percentage
  Used                  22%<br /> VMX files that belong to this DataStore::<br />
  None Exist<br /> <br /><br /> python VMdataStorePool.py -u \"http://esxhost\" -a
  \"login passwd\" --dstore=\"KodakVol1\"<br /> Available DataStores on http://esxhost<br
  /> <br /> DataStore Name                   KodakVol1<br /> Total Disk Space                
  499G<br /> Remaining Disk Space             379G<br /> Used Disk Space                 
  120G<br /> Percentage Used                  24%<br /> VMX files that belong to this
  DataStore::<br /> [KodakVol1] Kojak/Kojak.vmx<br /> [KodakVol1] Sakai/Sakai.vmx<br
  /> [KodakVol1] bbtest2.vmx<br /> [KodakVol1] bbtest.vmx<br /> <br /> -u, --url      
  This is the URL you will use to connect to the ESX server, \"http://esxhost\"<br
  /> -a, --auth      This is the Login and Passwd you will use, \"login passwd\"<br
  /> -d, --dstore    This is the DataStore aka VMFS to check, \"Esxtestvol2\"</span></span></p>\r\n<p> </p>\r\n<div>\r\n<br
  />"
wordpress_id: 186
wordpress_url: http://linuxdynasty.org/?p=186
date: !binary |-
  MjAwOS0wMy0yNCAyMDowOTowNyAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wMy0yNCAyMDowOTowNyAtMDQwMA==
categories: []
tags:
- VMware
- HowTo List DataStores and its VMX files using Python and CIM
comments: []
---
<p><span>Here I created another Python script using Pywbem to get the Storage Pools from ESX. <br /> In this script you can get the disk utilisation statistics from each datastore or from a particular datastore. <br /> <span class="attention">Script Updated to include the .VMX files that belong to each DataStore..</span></span></p>
<p><span><br /> <span style="font-family: monospace"> example below...<br /> python VMdataStorePool.py -u "http://esxhost" -a "login passwd"<br /> Available DataStores on http://esxhost</p>
<p> DataStore Name                   Esxtestvol2<br /> Total Disk Space                 499G<br /> Remaining Disk Space             189G<br /> Used Disk Space                  310G<br /> Percentage Used                  62%<br /> VMX files that belong to this DataStore::<br /> [Esxtestvol2] Win2003test3/Win2003test3.vmx<br /> [Esxtestvol2] netwaretest/netwaretest.vmx<br /> [Esxtestvol2] RHEL 4 NFS test/RHEL 4 NFS test.vmx<br /> [Esxtestvol2] RHEL 5 NFS test/RHEL 5 NFS test.vmx<br /> [Esxtestvol2] RHEL 3 NFS test/RHEL 3 NFS test.vmx<br /> [Esxtestvol2] vicfg/vicfg.vmx</p>
<p> DataStore Name                   ISO<br /> Total Disk Space                 49G<br /> Remaining Disk Space             38G<br /> Used Disk Space                  11G<br /> Percentage Used                  22%<br /> VMX files that belong to this DataStore::<br /> None Exist</p>
<p> python VMdataStorePool.py -u "http://esxhost" -a "login passwd" --dstore="KodakVol1"<br /> Available DataStores on http://esxhost</p>
<p> DataStore Name                   KodakVol1<br /> Total Disk Space                 499G<br /> Remaining Disk Space             379G<br /> Used Disk Space                  120G<br /> Percentage Used                  24%<br /> VMX files that belong to this DataStore::<br /> [KodakVol1] Kojak/Kojak.vmx<br /> [KodakVol1] Sakai/Sakai.vmx<br /> [KodakVol1] bbtest2.vmx<br /> [KodakVol1] bbtest.vmx</p>
<p> -u, --url       This is the URL you will use to connect to the ESX server, "http://esxhost"<br /> -a, --auth      This is the Login and Passwd you will use, "login passwd"<br /> -d, --dstore    This is the DataStore aka VMFS to check, "Esxtestvol2"</span></span></p>
<p> </p>
<div>
<br /><a id="more"></a><a id="more-186"></a><br />
<span>I'm thinking of combining this script with the previous one I created <a href="howto-list-vms-using-python-and-cim-part-1.html" title=" HowTo List Virtual Machines using Python and CIM Part 1">here</a> ... Let me know what you guys think....</span></div>
<p>You can download this script here {quickdown:33}<br /> <a href="View-details/VMware/33-VMstoragePool.py.html" title="title">VMstoragePool.py </a></p>
<p><a href="images/stories/screenshots/vmstoragepool.png" rel="shadowbox[0]"><img alt="alt" style="width: 229px; height: 238px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/vmstoragepool.png" align="left" /></a></p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
