---
layout: post
status: publish
published: true
title: HowTo List Virtual Machines By OStype and by hostname on VMware ESX
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>In my last post I asked a <a href=\"http://www.linuxdynasty.org/vote-from-users.html\"
  title=\"\">vote </a>from the users if they would like to see my last <a href=\"http://www.linuxdynasty.org/how-to-list-virtual-machines-and-all-its-properties-in-vmware.html\"
  title=\"\">script </a>but with added command line features. So here it is...<br
  />\r\nYou can pass these options... <strong>{--linux&nbsp;&nbsp; |&nbsp; --</strong><strong>windesk&nbsp;&nbsp;
  | --</strong><strong>winserv&nbsp;&nbsp; | --</strong><strong>xml&nbsp;&nbsp;&nbsp;&nbsp;
  |&nbsp;&nbsp; --</strong><strong>hostname}</strong></p>\r\n<p>So for example to
  run this script you will type &quot;<strong><font color=\"#0000ff\">perl VMlist.pl
  --linux --xml</font>&quot; </strong>This will list all of your Virtual Machines
  that are Linux in XML format. or here is the same command with out the <font color=\"#0000ff\"><strong>--xml</strong></font>
  option... &quot;<font color=\"#0000ff\"><strong>perl VMlist.pl --linux</strong></font>&quot;<strong>
  <br />\r\n</strong></p>\r\n<p><strong>&nbsp;</strong><br />\r\n<span class=\"attention\"><font
  color=\"#000000\"><strong>This script assumes you have the</strong></font><font
  color=\"#000000\"><strong> </strong><strong>VMware\r\nInfrastructure (VI) Perl Toolkit
  Packages installed and your\r\n$HOME/.visdkrc set correctly. Without the above the
  script below will\r\nnot work!!</strong></font></span><br />\r\n&nbsp;</p>\r\n<br
  />"
wordpress_id: 172
wordpress_url: http://linuxdynasty.org/?p=172
date: !binary |-
  MjAwOC0wNi0xMCAyMDoyMjo1OSAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNi0xMCAyMDoyMjo1OSAtMDQwMA==
categories: []
tags:
- Perl
- HowTo List Virtual Machines By OStype and by hostname on VMware ESX
comments: []
---
<p>In my last post I asked a <a href="http://www.linuxdynasty.org/vote-from-users.html" title="">vote </a>from the users if they would like to see my last <a href="http://www.linuxdynasty.org/how-to-list-virtual-machines-and-all-its-properties-in-vmware.html" title="">script </a>but with added command line features. So here it is...<br />
You can pass these options... <strong>{--linux&nbsp;&nbsp; |&nbsp; --</strong><strong>windesk&nbsp;&nbsp; | --</strong><strong>winserv&nbsp;&nbsp; | --</strong><strong>xml&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp; --</strong><strong>hostname}</strong></p>
<p>So for example to run this script you will type &quot;<strong><font color="#0000ff">perl VMlist.pl --linux --xml</font>&quot; </strong>This will list all of your Virtual Machines that are Linux in XML format. or here is the same command with out the <font color="#0000ff"><strong>--xml</strong></font> option... &quot;<font color="#0000ff"><strong>perl VMlist.pl --linux</strong></font>&quot;<strong> <br />
</strong></p>
<p><strong>&nbsp;</strong><br />
<span class="attention"><font color="#000000"><strong>This script assumes you have the</strong></font><font color="#000000"><strong> </strong><strong>VMware<br />
Infrastructure (VI) Perl Toolkit Packages installed and your<br />
$HOME/.visdkrc set correctly. Without the above the script below will<br />
not work!!</strong></font></span><br />
&nbsp;</p>
<p><a id="more"></a><a id="more-172"></a></p>
<p>&nbsp;</p>
<p>#!/usr/bin/perl<br />
#Create by Allen Sanabria AKA LinuxDynasty <br />
use strict;<br />
use warnings;<br />
use VMware::VIRuntime;<br />
use XML::Writer;<br />
my $writer = new XML::Writer(DATA_MODE =&gt; 1, DATA_INDENT =&gt;1);<br />
use Data::Dumper;<br />
use Getopt::Long;<br />
our ($linux, $windesk, $winserv, $hostname, $xml);<br />
GetOptions('linux'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; =&gt; $linux,<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'windesk'&nbsp;&nbsp;&nbsp; =&gt; $windesk,<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'winserv'&nbsp;&nbsp;&nbsp; =&gt; $winserv,<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'hostname=s' =&gt; $hostname,<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'xml'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; =&gt; $xml);<br />
Opts::parse();<br />
Opts::validate();<br />
Util::connect();</p>
<p>
# Obtain all inventory objects of the specified type<br />
my $e_vm = Vim::find_entity_views(view_type =&gt; 'VirtualMachine');</p>
<p>&nbsp; foreach my $views (sort(@$e_vm)) {<br />
&nbsp;&nbsp;&nbsp; if(Dumper($views-&gt;guest) =~/(linuxGuest)/ and $linux){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;letsGo($views-&gt;name, $views-&gt;guest)<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; <br />
&nbsp;&nbsp;&nbsp; if(Dumper($views-&gt;guest) =~/(^Microsofts+Windowss+Server.*)/ and $winserv){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;letsGo($views-&gt;name, $views-&gt;guest)<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; <br />
&nbsp;&nbsp;&nbsp; if(Dumper($views-&gt;guest) =~/(^Microsofts+Windowss+XP.*)/ and $windesk){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;letsGo($views-&gt;name, $views-&gt;guest)<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; <br />
&nbsp;&nbsp;&nbsp; if($hostname){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($hostname =~/$views-&gt;hostName/){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;letsGo($views-&gt;name, $views-&gt;guest)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; unless($hostname or $windesk or $winserv or $linux){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;letsGo($views-&gt;name, $views-&gt;guest)<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $hostname = &quot;&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
}<br />
sub letsGo{<br />
&nbsp;&nbsp;&nbsp; my $vm_name = shift @_;<br />
&nbsp;&nbsp;&nbsp; my $guest = shift @_;<br />
&nbsp;&nbsp;&nbsp; my @gval = qw /guestFullName guestId guestFamily guestState <br />
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; numCPU memoryMB ipAddress toolsVersion toolsStatus/;<br />
&nbsp;&nbsp;&nbsp; my @netval = qw /deviceConfigId network macAddress connected/;<br />
&nbsp;&nbsp;&nbsp; my @diskval = qw /diskPath capacity freeSpace/;<br />
&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;startTag($vm_name);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;startTag(&quot;host_config&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;startTag(&quot;name&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;characters($vm_name);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;endTag(&quot;name&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;#################################################n&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;tt$vm_namen&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;--------------------host_config-------------------n&quot;;<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; foreach my $value(@gval) {<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (Dumper($guest) !~ /$value/){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;NA($value);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; if(Dumper($guest-&gt;$value) =~/val/){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;AV($value, $guest-&gt;$value-&gt;val);<br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;AV($value, $guest-&gt;$value);<br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;endTag(&quot;host_config&quot;);<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; else{ <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; if ($guest-&gt;net){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;startTag(&quot;network_info&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;--------------network_info-----------------n&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (Dumper($guest) =~/net/){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; my $vm_nic = $guest-&gt;net;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; foreach my $nic(@$vm_nic){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; foreach my $nval(@netval){<br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;AV($nval, $nic-&gt;$nval);<br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;endTag(&quot;network_info&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;startTag(&quot;network_info&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;----------------network_info------------------n&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;NA(&quot;deviceConfigId&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;NA(&quot;network&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;NA(&quot;macAddress&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;NA(&quot;connected&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;endTag(&quot;network_info&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; if ($guest-&gt;disk){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;startTag(&quot;disk_info&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;-----------------disk_info-------------------n&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (Dumper($guest) =~/disk/){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; my $vm_disk = $guest-&gt;disk;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; foreach my $disk(@$vm_disk){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; foreach my $dval(@diskval){<br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;AV($dval, $disk-&gt;$dval);<br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;endTag(&quot;disk_info&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;startTag(&quot;disk_info&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;--------------disk_info--------------------n&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;NA(&quot;diskPath&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;NA(&quot;capacity&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp;NA(&quot;freeSpace&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;endTag(&quot;disk_info&quot;);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;n&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;endTag($vm_name);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;end();<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;#############################################nn&quot;;<br />
&nbsp;&nbsp;&nbsp; }<br />
}<br />
sub AV{<br />
&nbsp;&nbsp;&nbsp; my $meth = shift @_;<br />
&nbsp;&nbsp;&nbsp; my $val = shift @_;<br />
&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;startTag($meth);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;characters($val);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;endTag($meth);<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($meth =~ /guestId|numCPU|network/){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;$methttt $valn&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;$methtt $valn&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; }<br />
}<br />
sub NA{<br />
&nbsp;&nbsp;&nbsp; my $meth = shift @_;<br />
&nbsp;&nbsp;&nbsp; my $val = &quot;Not Available&quot;;<br />
&nbsp;&nbsp;&nbsp; if($xml){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;startTag($meth);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;characters($val);<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $writer-&gt;endTag($meth);<br />
&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if($meth =~ /guestId|numCPU|network/){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;$methttt $valn&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print &quot;$methtt $valn&quot;;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />
&nbsp;&nbsp;&nbsp; }<br />
}<br />
Util::disconnect();<br />
&nbsp;</p>
