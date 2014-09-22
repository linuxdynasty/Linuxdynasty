---
layout: post
status: publish
published: true
title: Install/Configure GPG (GNU Privacy Guard)
author:
  display_name: tinkpen
  login: tinkpen
  email: tinkpen@sympatico.ca
  url: ''
author_login: tinkpen
author_email: tinkpen@sympatico.ca
excerpt: ! "<p><span>In this howto, we will show you how to Install/Configure GPG
  (GNU Privacy Guard)</span></p>\r\n<p><span>For CentOS:</span></p>\r\n<p><strong><span>Step
  1&nbsp; -Install</span></strong></p>\r\n<p><span>As root (<font color=\"#0000ff\"><strong>su
  -</strong></font>, then the root password):</span></p>\r\n<p><strong><span><font
  color=\"#0000ff\">yum install <font color=\"#ff0000\">gpg</font></font></span></strong></p>\r\n<p><span>(select
  y)</span></p>\r\n<p><span>It will then\r\ninstall</span><span style=\"font-size:
  12pt\" lang=\"EN-US\">\r\n<o:p></o:p></span></p>\r\n<p class=\"MsoNormal\">&nbsp;</p>\r\n<br
  />"
wordpress_id: 28
wordpress_url: http://linuxdynasty.org/?p=28
date: !binary |-
  MjAwOC0wNS0yNSAxODoxMzozNiAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0yNSAxODoxMzozNiAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- How to install GPG how to configure gpg
comments: []
---
<p><span>In this howto, we will show you how to Install/Configure GPG (GNU Privacy Guard)</span></p>
<p><span>For CentOS:</span></p>
<p><strong><span>Step 1&nbsp; -Install</span></strong></p>
<p><span>As root (<font color="#0000ff"><strong>su -</strong></font>, then the root password):</span></p>
<p><strong><span><font color="#0000ff">yum install <font color="#ff0000">gpg</font></font></span></strong></p>
<p><span>(select y)</span></p>
<p><span>It will then<br />
install</span><span style="font-size: 12pt" lang="EN-US"><br />
<o:p></o:p></span></p>
<p class="MsoNormal">&nbsp;</p>
<p><a id="more"></a><a id="more-28"></a></p>
<p class="MsoNormal"><strong><span style="font-size: 12pt" lang="EN-US"><br />
</span></strong></p>
<p><strong><span lang="EN-US"></span><span>Step 2 –Locate Program</span></strong></p>
<p><span>Locate GPG on your<br />
system:</span></p>
<p><font color="#0000ff"><strong><span>whereis <font color="#ff0000">gpg</font></span></strong></font></p>
<p><span>You should get<br />
back:</span></p>
<p><span>gpg: /usr/bin/gpg</span></p>
<p><strong><span>Step 3 –Change user rights</span></strong></p>
<p><span>So everyone can<br />
use it:</span></p>
<p><font color="#0000ff"><span><strong>chmod<br />
u+s <font color="#ff0000">/usr/bin/gpg</font></strong></span></font></p>
<p><strong><span>Step 4 –Create Files for GPG to Work</span></strong></p>
<p><font color="#0000ff"><strong><span>/usr/bin/gpg --gen-key [<font color="#ff0000">for root</font>]</span></strong></font></p>
<p><strong><span>Step 5 –Configuring<br />
Key</span></strong></p>
<p><span>Accept the defaults</span></p>
<p><strong><span>Step 6- Verify </span></strong></p>
<p><font color="#0000ff"><span><strong>gpg<br />
--list-secret-key</strong></span></font></p>
<p><strong><font color="#0000ff"><span>gpg<br />
--list-public-key</span></font></strong></p>
<p><font color="#0000ff"><strong><span>gpg<br />
--list-sig</span></strong></font></p>
<p><strong><span>Step 7 – Create Revocation Certificate</span></strong></p>
<p><strong><span><font color="#0000ff">gpg --output revoke.asc<br />
--gen-revoke</font> <font color="#ff0000"><a href="mailto:your_email_name@your_service_provider.com">your_email_name@your_service_provider.com</a></font><br />
[<font color="#ff0000">or ca, etc.</font>]</span></strong></p>
<p><strong><span>Step 8 –Export Your Public Key</span></strong></p>
<p><strong><span><font color="#0000ff">gpg<br />
--export --armor</font> &gt; <font color="#ff0000">yourname.asc</font></span></strong></p>
<p><strong><span>Step 9 – Import Someone Else’s Key</span></strong></p>
<p><span>Download key</span></p>
<p><strong><span><font color="#0000ff">gpg --import</font> <font color="#ff0000">arnoldSW.asc</font></span></strong></p>
<p><strong><span>Step 10 –Sign Downloaded Key</span></strong></p>
<p><font color="#0000ff"><strong><span>&nbsp;gpg –sign<font color="#ff0000">arnoldSW.asc</font></span></strong></font></p>
<p><span>&nbsp;</span></p>
<p><strong><span>Create a Signature File</span></strong></p>
<p><font color="#0000ff"><strong><span>Example ..<font color="#000000"> touch &lt;<font color="#ff0000">yourname</font>&gt;</font><br />
touch <font color="#000000"><font color="#ff0000">yourname</font></font></span></strong></font></p>
<p><strong><span><font color="#0000ff">gpg<br />
–clearsign</font> <font color="#ff0000">yourname</font></span></strong></p>
<p><span>&nbsp;</span></p>
<p><strong><span>Decrypt Files</span></strong></p>
<p><strong><span><font color="#0000ff">gpg –decrypt</font> <font color="#ff0000">yourfriendsfile.txt.gpg</font> &gt; <font color="#ff0000">yourfriendsfile.txt</font></span></strong></p>
<p><strong><span>Encrypt Files</span></strong></p>
<p><strong><span><font color="#0000ff">gpg --encrypt --r <font color="#ff0000">public</font></font><font color="#ff0000">_keyname_of_recipient</font><font color="#ff0000">yourfile.txt</font></span></strong></p>
<p><span>&nbsp;</span></p>
<p><span>&nbsp;</span></p>
