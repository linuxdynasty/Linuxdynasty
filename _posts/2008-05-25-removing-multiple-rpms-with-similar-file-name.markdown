---
layout: post
status: publish
published: true
title: ! "Removing Multiple RPM\x03s with Similar File Name"
author:
  display_name: tinkpen
  login: tinkpen
  email: tinkpen@sympatico.ca
  url: ''
author_login: tinkpen
author_email: tinkpen@sympatico.ca
wordpress_id: 29
wordpress_url: http://linuxdynasty.org/?p=29
date: !binary |-
  MjAwOC0wNS0yNSAyMDoyMjowNyAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0yNSAyMDoyMjowNyAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- How to remove multiple RPMs with similar names
comments: []
---
<p><span>Removing<br />
Multiple RPM's with Similar File Names</span></p>
<p><span>Use<br />
the rpm’s command <strong>-e</strong> (for remove) with the <strong>--allmatches</strong> option</span></p>
<p><strong><span><font color="#0000ff"><font color="#000000">&quot;rpm</font></font><font color="#000000"><br />
–e&nbsp; --allmatches</font> </span></strong><strong><span>&lt;<font color="#ff0000">package-to-be-removed</font>&gt;&quot;</span></strong></p>
<p><span>i.e.:</span></p>
<p><strong><span><font color="#0000ff"><font color="#000000">&quot;rpm</font></font><font color="#ff0000"><font color="#000000"> </font><font color="#000000">-e --allmatches</font> kernel-2.4.25-8tr<font color="#000000">&quot;</font></font></span></strong></p>
<p><span>&nbsp;</span></p>
<p><span>The <strong>--allmatches</strong><br />
allows you to match all rpms with a given expression..</span></p>
<p><span>&nbsp;</span></p>
