---
layout: post
status: publish
published: true
title: How to list Virtual Machines in VMware using the Perl SDK API
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>In this Quick HowTo, I will show you how to list all the Virtual Machines
  on VMware ESX 3.+ server using the Perl SDK API for VMware. </p>\r\n<p><span class=\"attention\"><font
  color=\"#000000\"><strong>This script assumes you have the</strong></font><font
  color=\"#000000\"><strong> </strong><strong>VMware\r\nInfrastructure (VI) Perl Toolkit
  Packages installed and your\r\n$HOME/.visdkrc set correctly. Without the above the
  script below will\r\nnot work!!</strong></font></span><br />\r\n</p>\r\n<br />"
wordpress_id: 177
wordpress_url: http://linuxdynasty.org/?p=177
date: !binary |-
  MjAwOC0wNi0wNSAwMDo0MTozNCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNi0wNSAwMDo0MTozNCAtMDQwMA==
categories: []
tags:
- VMware
- How to list Virtual Machines in VMware using the Perl SDK API
comments: []
---
<p>In this Quick HowTo, I will show you how to list all the Virtual Machines on VMware ESX 3.+ server using the Perl SDK API for VMware. </p>
<p><span class="attention"><font color="#000000"><strong>This script assumes you have the</strong></font><font color="#000000"><strong> </strong><strong>VMware<br />
Infrastructure (VI) Perl Toolkit Packages installed and your<br />
$HOME/.visdkrc set correctly. Without the above the script below will<br />
not work!!</strong></font></span></p>
<p><a id="more"></a><a id="more-177"></a></p>
<p>
#!/usr/bin/perl</p>
<p><span>#This script will create a snapshot and list them for you<br />
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
<p></p>
<p>
use strict;<br />
use warnings;<br />
use VMware::VIRuntime;<br />
Opts::parse();<br />
Opts::validate();<br />
Util::connect();<br />
use Data::Dumper;</p>
<p>
# Obtain all inventory objects of the specified type<br />
my $e_vm = Vim::find_entity_views(view_type =&gt; 'VirtualMachine');<br />
foreach $views (sort(@$e_vm)) {<br />
&nbsp;&nbsp;&nbsp; $vm_name = $views-&gt;name;<br />
&nbsp;&nbsp;&nbsp; print $vm_name, &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp; }<br />
}<br />
Util::disconnect();</p>
