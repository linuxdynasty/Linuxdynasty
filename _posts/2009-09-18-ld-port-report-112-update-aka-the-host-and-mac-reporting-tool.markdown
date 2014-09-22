---
layout: post
status: publish
published: true
title: LD Port Report 1.12 update aka the Host and MAC Reporting tool
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<div>\r\n<div>We are happy to announce the release of Port Report 1.12.
  In this release, we can now follow CDP Neighbors while using the <strong>--report</strong>
  or <strong>-r</strong> options. Before when you used the <strong>--report</strong>
  option, the script will report on just that one switch. Now if you pass the <strong>--follow</strong>
  or <strong>-f </strong>option with the <strong>--report</strong> or <strong>-r</strong>
  option, port_report will follow the CDP neighbors and create multiple CSV files.\r\nRelease
  notes are below.... If you want to see an example of the Port Report output and
  how to run it, please check this link</div>\r\n<div>LD Port Report == {filelink=15}\r\n..<a
  href=\"ld-port-report-project.html\">http://www.linuxdynasty.org/ld-port-report-project.html</a>\r\n\r\n</div>\r\n<div><dl><dd>Revision
  1.12 09/18/09\r\n<ul>\r\n\t<li>The report option of the script can now follow cdp
  neighbors using the <strong>--follow</strong> option or <strong>-f</strong>.\r\nWhen
  you run the command below it will create ONE CSV file per cdp neighbor it scanned.\r\nI
  was able to scan from my core Switch down to the last neighbor in the line ( 44
  Neighbors in just under 20 minutes. )\r\nWhich equaled to a little over 4K Mac Addresses\r\nFor
  instance...port_report.py -d 192.168.101.1 -c public -r -f</li>\r\n</ul>\r\n"
wordpress_id: 212
wordpress_url: http://linuxdynasty.org/?p=212
date: !binary |-
  MjAwOS0wOS0xOCAxMToyNDoyNyAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wOS0xOCAxMToyNDoyNyAtMDQwMA==
categories:
- Uncategorized
tags:
- Switch Port Report
- Port Report
- Port Mapper
- Port Mapper Tool
- Switch Reporter
- Host Report
- MAC Report
- Port Mapping Tool
comments: []
---
<div>
<div>We are happy to announce the release of Port Report 1.12. In this release, we can now follow CDP Neighbors while using the <strong>--report</strong> or <strong>-r</strong> options. Before when you used the <strong>--report</strong> option, the script will report on just that one switch. Now if you pass the <strong>--follow</strong> or <strong>-f </strong>option with the <strong>--report</strong> or <strong>-r</strong> option, port_report will follow the CDP neighbors and create multiple CSV files.<br />
Release notes are below.... If you want to see an example of the Port Report output and how to run it, please check this link</div>
<div>LD Port Report == {filelink=15}<br />
..<a href="ld-port-report-project.html">http://www.linuxdynasty.org/ld-port-report-project.html</a></p>
</div>
<div>
<dl>
<dd>Revision 1.12 09/18/09</p>
<ul>
<li>The report option of the script can now follow cdp neighbors using the <strong>--follow</strong> option or <strong>-f</strong>.<br />
When you run the command below it will create ONE CSV file per cdp neighbor it scanned.<br />
I was able to scan from my core Switch down to the last neighbor in the line ( 44 Neighbors in just under 20 minutes. )<br />
Which equaled to a little over 4K Mac Addresses<br />
For instance...port_report.py -d 192.168.101.1 -c public -r -f</li>
</ul>
<p><a id="more"></a><a id="more-212"></a></p>
<p>Revision 1.11 09/13/09</p>
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
</dd>
</dl>
</div>
</div>
