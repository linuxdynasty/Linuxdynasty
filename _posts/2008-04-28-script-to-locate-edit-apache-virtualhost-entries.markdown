---
layout: post
status: publish
published: true
title: Script to locate, edit Apache VirtualHost entries
author:
  display_name: admin
  login: admin
  email: admin@linuxdynasty.org
  url: ''
author_login: admin
author_email: admin@linuxdynasty.org
excerpt: ! "<p><span style=\"font-family: courier new\">#!/usr/bin/perl<br />\r\n#
  Author: Christopher Hahn, 2006</span></p>\r\n<p><span style=\"font-family: courier
  new\">sub usage {<br />\r\n print STDERR &lt;&lt;EOT;<br />\r\nusage:<br />\r\n$0
  &lt;match&gt; [&lt;path&gt; [...]]</span></p>\r\n<p><span style=\"font-family: courier
  new\">Find and edit Apache virtual hosts matching &lt;match&gt;</span></p>\r\n<p><span
  style=\"font-family: courier new\">&lt;path&gt;  Path to an Apache conf to edit.<br
  />\r\n If a directory, equivalent to all files in &lt;path&gt;/<br />\r\n If omitted,
  &quot;./&quot; is assumed</span></p>\r\n<p><span style=\"font-family: courier new\">&lt;match&gt;
  is a PERL regular expression to match against ServerName or<br />\r\n ServerAlias
  for the virtual host entry you want to edit.</span></p>\r\n<p><span style=\"font-family:
  courier new\">If &lt;match&gt; is not found and &lt;path&gt; evaluates to a single
  file (extant or not)<br />\r\na template is provided to append a VirtualHost to
  the file.<br />\r\nEOT</span></p>\r\n<p><span style=\"font-family: courier new\">
  die &quot;n&quot;;<br />\r\n}</span></p>\r\n<br />"
wordpress_id: 86
wordpress_url: http://linuxdynasty.org/?p=86
date: !binary |-
  MjAwOC0wNC0yOCAxNzozMTowNiAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNC0yOCAxNzozMTowNiAtMDQwMA==
categories: []
tags:
- Perl HowTo's
- Script to locate
- edit Apache VirtualHost entries using Perl
comments: []
---
<p><span style="font-family: courier new">#!/usr/bin/perl<br />
# Author: Christopher Hahn, 2006</span></p>
<p><span style="font-family: courier new">sub usage {<br />
 print STDERR &lt;&lt;EOT;<br />
usage:<br />
$0 &lt;match&gt; [&lt;path&gt; [...]]</span></p>
<p><span style="font-family: courier new">Find and edit Apache virtual hosts matching &lt;match&gt;</span></p>
<p><span style="font-family: courier new">&lt;path&gt;  Path to an Apache conf to edit.<br />
 If a directory, equivalent to all files in &lt;path&gt;/<br />
 If omitted, &quot;./&quot; is assumed</span></p>
<p><span style="font-family: courier new">&lt;match&gt; is a PERL regular expression to match against ServerName or<br />
 ServerAlias for the virtual host entry you want to edit.</span></p>
<p><span style="font-family: courier new">If &lt;match&gt; is not found and &lt;path&gt; evaluates to a single file (extant or not)<br />
a template is provided to append a VirtualHost to the file.<br />
EOT</span></p>
<p><span style="font-family: courier new"> die &quot;n&quot;;<br />
}</span></p>
<p><a id="more"></a><a id="more-86"></a></p>
<p><span style="font-family: courier new">my $editor = $ENV{EDITOR} || $ENV{VISUAL} || '/bin/vi';<br />
my $re = shift;<br />
my @files = @ARGV;</span></p>
<p><span style="font-family: courier new">&amp;usage unless $re;</span></p>
<p><span style="font-family: courier new">my $rv = 0;<br />
my $rc = 0;</span></p>
<p><span style="font-family: courier new"># Put something in front so the script won't match itself. :)<br />
my $template = &quot;<br />
V&lt;VirtualHost *&gt;<br />
V ServerName $re<br />
V ServerAlias *.$re<br />
V # DocumentRoot /content/data/$re/htdocs/<br />
V # DocumentRoot /spln/data/<br />
V # Redirect / </span><a href="http://www.cbs.com/"><span style="font-family: courier new">http://</span></a><br />
<span style="font-family: courier new">V # RedirectMatch ^(.*) </span><a href="http://www.cbs.com/"><span style="font-family: courier new">http://</span></a><br />
<span style="font-family: courier new">V&lt;/VirtualHost&gt;</span><br />
<span style="font-family: courier new">&quot;;</span><br />
<span style="font-family: courier new">$template =~ s/^V//mg;</span></p>
<p><span style="font-family: courier new">$re = qr/.*?$re/;</span></p>
<p><span style="font-family: courier new">@files = ( '.' ) unless @files;<br />
@files = build_file_list(@files);</span></p>
<p><span style="font-family: courier new">my $edit_file = &quot;virt.$$&quot;;</span></p>
<p><span style="font-family: courier new">foreach $file (@files) {<br />
 # A single success is considered an overall success<br />
 $rc = virt($re, $file);<br />
 if($rc &lt; 1 &amp;&amp; $rv) { $rv = 0 }<br />
 else { $rv = $rc }<br />
}</span></p>
<p><span style="font-family: courier new">if($rv &gt; 0) {<br />
 print $rv;<br />
 die &quot;$!n&quot;;<br />
}</span></p>
<p>
<span style="font-family: courier new">unlink $edit_file;<br />
if( $rv == -1 &amp;&amp; $#files == 0 ) {<br />
 open EDITFILE, '&gt;&gt;', $edit_file;<br />
 print EDITFILE $template;<br />
 close EDITFILE;</span></p>
<p><span style="font-family: courier new"> open TARGFILE, '&gt;&gt;', $files[0];<br />
 print TARGFILE edit($edit_file);<br />
 close TARFILE;<br />
}</span></p>
<p><span style="font-family: courier new"></span></p>
<p><span style="font-family: courier new"></span></p>
<p><span style="font-family: courier new"># copy each matching virt to a temp file and run our editor (edit()) against it<br />
# then copy the virt back into place and rewrite the rest of the file<br />
sub virt {<br />
 my $re = shift;<br />
 my $file = shift;</span></p>
<p><span style="font-family: courier new"> my $invirt = -1; # position within the file when in a virt<br />
 my @virt_content = ();<br />
 my $match_flag = 0; # whether we are 'in' a matching virt<br />
 my $any_match = 0; # whether we have matched any virt<br />
 my $tmpfile = new_temp_file();</span></p>
<p><span style="font-family: courier new"> return $! unless open(IN, '+&lt;', $file);<br />
 return $! unless open(OUT, '+&gt;', $tmpfile);</span></p>
<p><span style="font-family: courier new"> while(&lt;IN&gt;) {<br />
 if($invirt &lt; 0) {<br />
 if(/^s*&lt;VirtualHost/) {<br />
 $invirt = tell IN;<br />
 $match_flag = 0;<br />
 @virt_content = (&quot;#!! You are editing $file. Leave this line here please.n&quot;, $_);<br />
 } else {<br />
 # Not part of a virt at all, so continue on our merry way...<br />
 print OUT $_;<br />
 }</span></p>
<p><span style="font-family: courier new"> } else {<br />
 # we're in a virt, so add the line<br />
 push @virt_content, $_;</span></p>
<p><span style="font-family: courier new"> # is it a match?<br />
 if(/^s*Server(?:Name|Alias) $re/) {<br />
 $any_match = $match_flag = 1;</span></p>
<p><span style="font-family: courier new"> } elsif(/^s*&lt;/VirtualHost/) {<br />
 # End of a virt -- to edit, or not to edit?<br />
 if( $match_flag ) {<br />
 unless(open EDIT, '&gt;', $edit_file) {<br />
 warn &quot;Write to $edit_file failed: $!n&quot;;<br />
 return $!;<br />
 }</span></p>
<p><span style="font-family: courier new"> print EDIT @virt_content;<br />
 close EDIT;</span></p>
<p><span style="font-family: courier new"> @virt_content = edit($edit_file);<br />
 }</span></p>
<p><span style="font-family: courier new"> shift @virt_content;<br />
 print OUT @virt_content;<br />
 $invirt = -1;<br />
 }<br />
 }<br />
 }</span></p>
<p><span style="font-family: courier new"> if($any_match) {<br />
 unlink $edit_file;<br />
 # Why not just move it a la rename()?<br />
 # Well think about it -- that's a new inode with a new ctime,<br />
 # possibly the wrong perms, and the old file might be open<br />
 # elsewhere, meaning a dangling file somewhere... et cetera.<br />
 seek OUT, 0, 0; # $tmpfile<br />
 seek IN, 0, 0; # $file</span></p>
<p><span style="font-family: courier new"> print IN $_ while &lt;OUT&gt;;</span></p>
<p><span style="font-family: courier new"> close IN;<br />
 unless(truncate $file, tell OUT) {<br />
 warn &quot;Truncating $file failed: $!n&quot;;<br />
 return $!;<br />
 }<br />
 close OUT;</span></p>
<p><span style="font-family: courier new"> } else {<br />
 close OUT;<br />
 close IN;<br />
 }</span></p>
<p><span style="font-family: courier new"> unlink $tmpfile;</span></p>
<p><span style="font-family: courier new"> return 0 if $any_match;<br />
 return -1;<br />
}</span></p>
<p><span style="font-family: courier new">sub build_file_list {<br />
 my @in_files = @_;<br />
 my @files = ();</span></p>
<p><span style="font-family: courier new"> foreach $file ( @in_files ) {<br />
 if( -d $file ) {<br />
 push @files, dirlist( $file );<br />
 } else {<br />
 push @files, $file;<br />
 }<br />
 }</span></p>
<p><span style="font-family: courier new"> return @files;<br />
}</span></p>
<p><span style="font-family: courier new">sub new_temp_file {<br />
 my $file = '/tmp/virt.';<br />
 my @c = split(//, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_');</span></p>
<p><span style="font-family: courier new"> do {<br />
 $file .= $c[ rand @c ];</span></p>
<p><span style="font-family: courier new"> } while(-e $file);</span></p>
<p><span style="font-family: courier new"> return $file;<br />
}</span></p>
<p><span style="font-family: courier new">sub dirlist {<br />
 my $dir = shift;<br />
 my @files = ();</span></p>
<p><span style="font-family: courier new"> die &quot;$dir: $!n&quot;<br />
 unless opendir DIR, $dir;</span></p>
<p><span style="font-family: courier new"> -f &quot;$dir/$_&quot; &amp;&amp; push @files, $_<br />
 while $_ = readdir DIR;</span></p>
<p><span style="font-family: courier new"> closedir DIR;</span></p>
<p><span style="font-family: courier new"> return @files;<br />
}</span></p>
<p>
<span style="font-family: courier new">sub edit {<br />
 my $file = shift;<br />
 my @contents = ();</span></p>
<p><span style="font-family: courier new"> system &quot;$editor $file&quot;;</span></p>
<p><span style="font-family: courier new"> die &quot;Failed reading $file after edit: $!n&quot;<br />
 unless open EDITFILE, $file;</span></p>
<p><span style="font-family: courier new"> @contents = &lt;EDITFILE&gt;;</span></p>
<p><span style="font-family: courier new"> close EDITFILE;</span></p>
<p><span style="font-family: courier new"> return @contents;<br />
}<br />
</span></p>
