---
layout: post
status: publish
published: true
title: How to recover root password
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 11
wordpress_url: http://linuxdynasty.org/?p=11
date: !binary |-
  MjAwOC0wMi0xMCAwNToyODozNSAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAwNToyODozNSAtMDUwMA==
categories: []
tags:
- Advance Linux HowTo's
- How to recover root password on Linux using Grub Fedora ubuntu Gentoo
comments: []
---
<p><strong><span style="color: red">Have you forgotten the root password on your box and said @#$%%^. Well do not fear, Linux Dynasty is here to save the day.</span></strong></p>
<ol>
<li>
<ul><strong>Booting into single user mode from GRUB</strong>.</p>
<li>First, reboot your system. </li>
<li>Second, When GRUB comes up type e (got to be quick). </li>
<li>Third, now select entry that begins with kernel and hit enter. </li>
<li>Fourth, at the end of the kernel entry type either <strong><span style="color: blue">s</span></strong> or <strong><span style="color: blue">single</span></strong>, now hit enter. </li>
<li>Fifth, type <strong><span style="color: blue">b</span></strong>, the box will boot up and now you can type in the cmd prompt <span style="color: blue"><strong>passwd</strong> <strong>root</strong></span>. This will reset the password to whatever you like. </li>
<li>If this does not bring you to a root prompt, then try this. </li>
<li>Then try appending <strong><span style="color: blue">single init=/bin/bash</span></strong> </li>
</ul>
<p> <strong><span style="color: red">Be happy, now you have root access again. or maybe for the first time... ;)<br />
 </span></strong></p>
</li>
<li>
<ul><strong>Booting into single-user mode from LILO</strong></p>
<li>First, reboot your system. </li>
<li>Second, When LILO comes up, type in <strong><span style="color: blue">linux s</span></strong>. Hit enter. </li>
<li>Box will boot into single user mode, which brings you to a root prompt. If this does not happen to you, and ask you for the root password, you will have to do the following. </li>
<li>Try this <strong><span style="color: blue">linux init=/bin/bash</span></strong> </li>
</ul>
</li>
</ol>
