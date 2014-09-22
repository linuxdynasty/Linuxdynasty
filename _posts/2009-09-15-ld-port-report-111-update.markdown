---
layout: post
status: publish
published: true
title: LD Port Report 1.11 update
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 211
wordpress_url: http://linuxdynasty.org/?p=211
date: !binary |-
  MjAwOS0wOS0xNSAxMzo1ODoxNyAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wOS0xNSAxMzo1ODoxNyAtMDQwMA==
categories:
- Uncategorized
tags:
- Switch Port Report
- Fixed issue
- where the matching of the cdp neighbor was not matching correctly
- Port Report
- Port Mapper
- Port Mapper Tool
comments: []
---
<div>We are happy to announce the release of Port Report 1.11. In this release, we have fixed quite a few bugs that were in the previous release. Included in this release is the ability to follow EtherChannel aka PortChannel Ports using the Port Agreggation Protocol.<br />
Release notes are below.... If you want to see an example of the Port Report output and how to run it, please check this link</div>
<div>LD Port Report == {filelink=15}</div>
<div>..<a href="ld-port-report-project.html">http://www.linuxdynasty.org/ld-port-report-project.html</a></p>
</div>
<div>
<dl>
<dd>Revision 1.11 09/13/09</p>
<ul>
<li>More code clean up and another increase in speed.</li>
<li>Also port_report can now follow EtherChannel</li>
<li>Fixed issue, where the matching of the cdp neighbor was not matching correctly</li>
<li>Added better verbosity</li>
<li>Added Sanity Checking for cdp neighbors</li>
</ul>
<p>Revision 1.10 09/09/09</p>
<ul>
<li>Code Clean up and a slight increase in speed ( by a few seconds ) during the search by mac or ip</li>
</ul>
<p>Revision 1.9<br />
Code changes and Added CDP Support</p>
<ul>
<li>Detect CDP Neighbors during the scan for MAC Addresses or IP Addresses</li>
</ul>
<p>Revision 1.8<br />
Here is a quick update.....</p>
<ul>
<li>I just add dns reverse lookups to the output of this script.</li>
</ul>
<p>Revision 1.7<br />
Adds support to the following devices..</p>
<ol>
<li>Cisco
<ul>
<li>Catalyst 6509 w/ Supervisor 720 running IOS</li>
<li>Catalyst 3560</li>
<li>Catalyst 3550 (SMI)</li>
<li>Cisco CIGESM series Chassis Blades</li>
<li>Cisco Catalyst 2960</li>
</ul>
</li>
<li>Foundry
<ul>
<li>Foundry Server Iron</li>
</ul>
</li>
<li>Nortel
<ul>
<li>Nortel Passport 8600</li>
<li>Nortel 5520 Ethernet Routing Switch</li>
</ul>
</li>
<li>HP
<ul>
<li>HP Procurve 5406xl</li>
</ul>
</li>
</ol>
<p>&nbsp;</p>
<p>Revision 1.6<br />
New additions to this revision ....</p>
<ul>
<li>Support for HP Procurve Switches, ( Tested on the newer versions of HP )</li>
<li>combined switch_report.py in port_report.py.</li>
<li>Added --verbose flag</li>
</ul>
<p>Previous Releases....</p>
<ul>
<li>Search by MAC or IP or PORT</li>
</ul>
<p>&nbsp;</p>
<p>LD Port Reporter == {filelink=15}</p>
</dd>
</dl>
</div>
