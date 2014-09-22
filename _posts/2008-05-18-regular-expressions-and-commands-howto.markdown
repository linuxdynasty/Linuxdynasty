---
layout: post
status: publish
published: true
title: Regular Expressions and Commands HowTo
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 17
wordpress_url: http://linuxdynasty.org/?p=17
date: !binary |-
  MjAwOC0wNS0xOCAyMTozMzoxNCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0xOCAyMTozMzoxNCAtMDQwMA==
categories: []
tags:
- Advance Linux HowTo's
- Regular Expressions and Commands HowTo Regex HowTo
comments: []
---
<p><span class="dropcap">T</span>here are a bunch of great regular expressions HowTo's out there..... Now you may be asking why am I creating another??? Well quite simple, I am creating this one because this is not really just a regular expression howto but more a regular expression HowTo with its everyday uses with linux/unix commands.&nbsp; So it will not cover perl/python/ruby/...etc programming languages regular expressions (That will be for another tutorial :) )</p>
<p>To start this off I will give you a basic introduction to regular expressions using the output <br />
of &quot;<font color="#0000ff"><strong>ls</strong></font>&quot; and piping it &quot;<font color="#0000ff"><strong>grep</strong></font>&quot; using the <strong>-<font color="#0000ff">oE</font></strong> options (The <font color="#0000ff"><strong>o</strong></font> stands for Exact match and the <font color="#0000ff"><strong>E</strong></font> stands for Extended Regular Expressions). Using &quot;(<font color="#ff0000"><strong>BRE</strong></font> and <strong><font color="#ff0000">ERE</font></strong>) <strong>B</strong>asic <strong>R</strong>egular <strong>E</strong>xpressions and <strong>P</strong>osix <strong>E</strong>xtended <strong>R</strong>egular <strong>E</strong>xpressions&quot;...</p>
<p><u><strong>THIS IS NOT A TUTORIAL BUT A HOWTO</strong><strong>!!</strong></u> So this means more examples and less explaining..</p>
<p>&nbsp;</p>
<table style="border-collapse: collapse" align="center" border="1" bordercolor="#000000" cellpadding="3" cellspacing="0" height="427" width="633">
<tbody>
<tr valign="top">
<th scope="col">
<p>Anchors</p>
</th>
<th scope="col">
<p>What it means&nbsp;</p>
</th>
<th scope="col">
<p>Example&nbsp;</p>
</th>
</tr>
<tr valign="top">
<td>
<p><strong><font color="#ff0000">^ </font></strong></p>
</td>
<td>
<p>Start of string</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls |grep -oE &quot;<font color="#ff0000">^</font>Cw+.jpg&quot;</strong></font><br />
Chunka.jpg<br />
Chunka1.jpg</p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>$</strong></font>&nbsp;</p>
</td>
<td>
<p>End of string&nbsp;</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls |grep -oE &quot;w+(.jpg<font color="#ff0000">$</font>)&quot;</strong></font><br />
Chunka.jpg<br />
Chunka1.jpg<br />
DSCF0732.jpg</p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>b</strong></font>&nbsp;</p>
</td>
<td>
<p>Word boundary&nbsp;</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls |grep -oE &quot;<font color="#ff0000">b</font>Chunka<font color="#ff0000">b</font>.jpg&quot;</strong></font><br />
Chunka.jpg </p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>&lt;</strong></font>&nbsp;</p>
</td>
<td>
<p>Start of word&nbsp;</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls |grep -oE &quot;<font color="#ff0000">&lt;</font>Chw+.jpg&quot;</strong></font><br />
Chunka.jpg<br />
Chunka1.jpg </p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>&gt;</strong></font>&nbsp;</p>
</td>
<td>
<p>End of word&nbsp;</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls Scripts/Python/ |grep -oE &quot;w+<font color="#ff0000">&gt;</font>.py&quot;</strong></font><br />
xen_mac_generate.py&nbsp;</p>
</td>
</tr>
</tbody>
</table>
<table style="border-collapse: collapse" align="center" border="1" bordercolor="#000000" cellpadding="3" cellspacing="0" height="222" width="355">
<tbody>
<tr valign="top">
<th scope="col">
<p>&nbsp;Character Classes&nbsp;</p>
</th>
<th scope="col"></p>
<p>What it means&nbsp;</p>
</th>
<th scope="col">
<p>Example&nbsp;</p>
</th>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>w</strong></font>&nbsp;</p>
</td>
<td>
<p>Word&nbsp;</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls | grep -oE &quot;<font color="#ff0000">w</font>&quot;</strong></font><br />
C<br />
C</p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>W&nbsp;</strong></font></p>
</td>
<td>
<p>Non word&nbsp;</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls |grep -oE &quot;<font color="#ff0000">W</font>&quot;</strong></font><br />
.<br />
. </p>
</td>
</tr>
</tbody>
</table>
<table style="border-collapse: collapse" align="center" border="1" bordercolor="#000000" cellpadding="3" cellspacing="0" height="618" width="630">
<tbody>
<tr valign="top">
<th scope="col">
<p>Quantifiers&nbsp;</p>
</th>
<th scope="col">
<p>what it means&nbsp;</p>
</th>
<th scope="col">
<p>example&nbsp;</p>
</th>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>*</strong></font>&nbsp;</p>
</td>
<td>
<p>zero or more times</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls | grep -oE &quot;w<font color="#ff0000">*</font>.jpg&quot;</strong></font><br />
Chunka.jpg<br />
Chunka1.jpg<br />
DSCF0732.jpg </p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>+</strong></font>&nbsp;</p>
</td>
<td>
<p>one or more times&nbsp;</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls | grep -oE &quot;w<font color="#ff0000">+</font>&quot;</strong></font><br />
Chunka<br />
Chunka1<br />
DSCF0732 </p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>?</strong></font>&nbsp;</p>
</td>
<td>matches either once or zero times </td>
<td>
<p><font color="#0000ff"><strong>ls | grep -oE &quot;Chunka1<font color="#ff0000">?</font>.jpg&quot;</strong></font><br />
Chunka.jpg<br />
Chunka1.jpg</p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>{2}</strong></font>&nbsp;</p>
</td>
<td>
<p>Exactly 2 times</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls | grep -oE &quot;(^C<font color="#ff0000">{2}</font>hw+.jpg)&quot;</strong></font><br />
CChunka.jpg </p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>{1,}</strong></font></p>
</td>
<td>
<p>1 or more times</p>
</td>
<td>
<p><font color="#0000ff"><strong>ls | grep -oE &quot;(^C<font color="#ff0000">{1,}</font>hw+.jpg)&quot;</strong></font><br />
CChunka.jpg<br />
CCChunka.jpg<br />
Chunka.jpg<br />
Chunka1.jpg<br />
Chunka11.jpg </p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>{1,2}&nbsp;</strong></font></p>
</td>
<td>
<p>1 through 2 times</p>
</td>
<td>
<p><strong><font color="#0000ff">ls | grep -oE &quot;(^C<font color="#ff0000">{1,2}</font>hw+.jpg)&quot;</font></strong><br />
CChunka.jpg<br />
Chunka.jpg<br />
Chunka1.jpg<br />
Chunka11.jpg </p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<table style="width: 100%; border-collapse: collapse" summary="" border="1" bordercolor="#000000" cellpadding="3" cellspacing="0">
<tbody>
<tr valign="top">
<th scope="col">
<p>Special Characters&nbsp;</p>
</th>
<th scope="col">
<p>What it means&nbsp;</p>
</th>
<th scope="col">
<p>Example&nbsp;</p>
</th>
</tr>
<tr valign="top">
<td>
<p><strong><font color="#ff0000">n</font></strong>&nbsp;</p>
</td>
<td>
<p>New line&nbsp;</p>
</td>
<td>
<p>&nbsp;</p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>r</strong></font>&nbsp;</p>
</td>
<td>
<p>Carriage return&nbsp;</p>
</td>
<td>
<p>&nbsp;</p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>t</strong></font></p>
</td>
<td>
<p>Tab&nbsp;</p>
</td>
<td>
<p>&nbsp;</p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>v</strong></font></p>
<p>
</td>
<td>
<p>Vertical tab&nbsp;</p>
</td>
<td>
<p>&nbsp;</p>
</td>
</tr>
<tr valign="top">
<td>
<p><font color="#ff0000"><strong>f</strong></font></p>
</td>
<td>
<p>Form feed&nbsp;</p>
</td>
<td>
<p>&nbsp;</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;</p>
<p></p>
