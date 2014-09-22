---
layout: post
status: publish
published: true
title: Synergy How To
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 22
wordpress_url: http://linuxdynasty.org/?p=22
date: !binary |-
  MjAwOC0wMi0xMCAyMjozNDo1MyAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAyMjozNDo1MyAtMDUwMA==
categories: []
tags:
- Beginner Linux HowTo's
- Synergy How To Synergy Tutorial
comments: []
---
<p><span style="color: red"><strong> You really got to love synergy, since it is the only App I know of that can share a mouse and keyboard across multiple boxes/Operating systems<br />
 </strong></span></p>
<p> <strong>FYI, this tutorial assumes that you know basic linux/windows and how to download the software/install<br />
 </strong></p>
<ol>
<li>
<ul>
In this quick but really easy tutorial, we will show you how to setup synergy for 2 boxes side by side. One box is Windows, The other box is linux. The Windows box will be the one that is controlling the mouse.</p>
<li>You need at minimum 2 section statements, one for the <strong>screens</strong> section and the other for the <strong>links</strong> section
 </li>
<li>In the <strong>screens</strong> section you will put the hostname of the boxes that will be involved in synergy.(if you do not have the hostname in DNS, then input the hostname in (/etc/hosts for linux and C:WINDOWSsystem32driversetchost in windows)
 </li>
<li>Now that you have the hostnames in now it is time to configure the <strong>links</strong> section. In this section all you have to do is put in the hostnames of the box and what direction to the next box they are in... example.. chewy is left of chewbaca and chewbaca is right of chewy. </li>
<li>Create this file if it does not exist..<br />
 <span style="color: blue">/etc/synergy.conf</span></p>
<pre><br />section: screens<br />  chewy:<br />  chewbaca:<br /><br />end<br /><br />section: links<br />  <br />  chewy:<br />    left = chewbaca<br /><br />  chewbaca:<br />    right = chewy<br /><br />end<br />  </pre>
</li>
<li>Now, I personally boot into multiuser mode, so I will describe the steps associated with that. 1st edit your $HOME/.xinitrc.. Mine looks like this
<pre><br />exec gnome-session &amp;<br />synergyc -f chewy<br />  </pre>
<p>&nbsp;</p>
</li>
<li>Now you can substitute gnome-session with startkde or what ever window manager you prefer.
 </li>
<li>The line <span style="color: blue">&quot;synergyc -f chewy&quot;</span>, this is where the connection to the box that is in charge of the mouse and keyboard.
 </li>
<li>Now you can run startx and it will try to connect to the synergy server in charge of the mouse and keyboard. Now we are off to the windows section. </li>
</ul>
</li>
<li>
<ul>
Now there are 3 simple steps in Windows.</p>
<li>Run synergy, click the &quot;Share this computer and mouse(server) button </li>
<li>Click configure, then add the screens to there appropriate positions like you did in linux. </li>
<li>now after you applied the settings click on start of the main synergy window </li>
</ul>
<p><strong>Example... WINDOWS STYLE</strong></li>
</ol>
<p><img alt="" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/synergy1.jpg" border="0" /><br />
<img alt="" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/screenshots/synergy2.jpg" border="0" height="348" width="511" /></p>
