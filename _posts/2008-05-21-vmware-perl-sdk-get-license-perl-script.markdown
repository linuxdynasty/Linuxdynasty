---
layout: post
status: publish
published: true
title: VMware Perl SDK get license perl script
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>I needed a script that would get all relevant license data from our
  VMWare ESX Server using the Perl SDK for VMWare. We needed to know what type of
  licenses we have with how many are being used and how many are available. I would
  like to thank my friend <strong>Chris Hahn</strong> for reminding me about Data::Dumper,
  because without that this would have taken me longer then it should have... ( I'm
  a Python Programmer )</p>\r\n<p>Update... I realized after working with the SDK
  for the past 2 months that I did not need Data:Dumper and the script has now been
  updated and it is shorter. </p>\r\n<p><span class=\"attention\"><font color=\"#000000\"><strong>This
  script assumes you have the</strong></font><font color=\"#000000\"><strong> </strong><strong>VMware
  Infrastructure (VI) Perl Toolkit Packages installed and your $HOME/.visdkrc set
  correctly. Without the above the script below will not work!!</strong></font></span><br
  />\r\n</p>\r\n<p>Example output of running this script.../</p>\r\n<p><strong>costUnit
  = cpuPackage<br />\r\nfeatureName = VMware DRS<br />\r\nfeatureDescription = count
  per CPU package<br />\r\ntotal = 100<br />\r\navailable = 90&nbsp;</strong></p>\r\n<br
  />"
wordpress_id: 176
wordpress_url: http://linuxdynasty.org/?p=176
date: !binary |-
  MjAwOC0wNS0yMSAyMjozNDozNCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0yMSAyMjozNDozNCAtMDQwMA==
categories: []
tags:
- VMware
- VMware Perl SDK get license perl script
comments: []
---
<p>I needed a script that would get all relevant license data from our VMWare ESX Server using the Perl SDK for VMWare. We needed to know what type of licenses we have with how many are being used and how many are available. I would like to thank my friend <strong>Chris Hahn</strong> for reminding me about Data::Dumper, because without that this would have taken me longer then it should have... ( I'm a Python Programmer )</p>
<p>Update... I realized after working with the SDK for the past 2 months that I did not need Data:Dumper and the script has now been updated and it is shorter. </p>
<p><span class="attention"><font color="#000000"><strong>This script assumes you have the</strong></font><font color="#000000"><strong> </strong><strong>VMware Infrastructure (VI) Perl Toolkit Packages installed and your $HOME/.visdkrc set correctly. Without the above the script below will not work!!</strong></font></span></p>
<p>Example output of running this script.../</p>
<p><strong>costUnit = cpuPackage<br />
featureName = VMware DRS<br />
featureDescription = count per CPU package<br />
total = 100<br />
available = 90&nbsp;</strong></p>
<p><a id="more"></a><a id="more-176"></a></p>
<p>#!/usr/bin/perl<br />
#</p>
<p><span>#</span>Purpose of this script is to get the Licenses we have from our VMWare ESX Server..<br />
#Type of License, How many used, How many available..<br />
<span><br />
#Copyright (C) 2008  Allen Sanabria</p>
<p>#This program is free software; you can redistribute it and/or modify<br />
#it under the terms of the GNU General Public License as published by<br />
#the Free Software Foundation; either version 2 of the License, or<br />
#(at your option) any later version.</p>
<p>#This program is distributed in the hope that it will be useful,<br />
#but WITHOUT ANY WARRANTY; without even the implied warranty of<br />
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the<br />
#GNU General Public License for more details.</p>
<p>#You should have received a copy of the GNU General Public License along<br />
#with this program; if not, write to the Free Software Foundation, Inc.,<br />
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.</span></p>
<p>#Example output<br />
#Cost per Unit:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cpuPackage<br />
#Feature Name:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ESX Server Standard<br />
#Feature Description:&nbsp;&nbsp;&nbsp; Grants: count per CPU package<br />
#Total Licenses:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 314<br />
#Total Available:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; 290</p>
<p>use strict;<br />
use warnings;<br />
use VMware::VIRuntime;<br />
Opts::parse();<br />
Opts::validate();<br />
Util::connect();</p>
<p>my $content&nbsp;&nbsp; = Vim::get_service_content();<br />
my $licMgr&nbsp;&nbsp;&nbsp; = Vim::get_view( mo_ref =&gt; $content-&gt;licenseManager );<br />
my $lic_usage = $licMgr-&gt;QueryLicenseSourceAvailability;</p>
<p>foreach my $line (@$lic_usage) {<br />
&nbsp;&nbsp;&nbsp; print &quot;Cost per Unit:tt&quot; . $line-&gt;feature-&gt;costUnit . &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp; print &quot;Feature Name:tt&quot; . $line-&gt;feature-&gt;featureName . &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp; print &quot;Feature Description:t&quot; . $line-&gt;feature-&gt;featureDescription . &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp; print &quot;Total Licenses:tt&quot; . $line-&gt;total . &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp; print &quot;Total Available:t&quot; . $line-&gt;available . &quot;nn&quot;;</p>
<p>}<br />
Vim::logout();</p>
