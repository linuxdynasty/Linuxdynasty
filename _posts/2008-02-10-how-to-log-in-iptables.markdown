---
layout: post
status: publish
published: true
title: How to log in IPTABLES
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 59
wordpress_url: http://linuxdynasty.org/?p=59
date: !binary |-
  MjAwOC0wMi0xMCAyMzo0NTo0NyAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAyMzo0NTo0NyAtMDUwMA==
categories: []
tags:
- Linux Networking HowTo's
- How to setup logging in IPTABLES on linux fedora ubuntu gentoo iptables logging
comments: []
---
<p><span style="color: red"><strong>Welcome again to LinuxDynasty.org. In this quick how to, we are going to show you how to get iptables to log when it drops packets</strong>.</span></p>
<ol>
<li>
<ul><strong>In the previous tutorial <a href="SSH_Blocking+-+How_to_block_ssh_attacks_using_iptables">SSH BLOCKING HOW TO</a> we showed you how to drop those pesky ssh attacks, well int his tutorial we are going to show you how to log those attacks. If you have not read the previous tutorial, then please read it now as I am not going to reexplain the options I used for blocking ssh attacks</strong></p>
<li>Before we get into the iptables rules, lets make sure that what we are doing is going to log. First lets open up &quot;<strong><span style="color: blue">/etc/syslog.conf</span></strong>&quot; and add this entry
<pre><br />kern.*                          /var/log/firewall.log<br />  </pre>
</li>
<li>Now restart your syslog daemon.. &quot;<strong><span style="color: blue">/etc/init.d/syslog restart</span></strong>&quot; (This is ofcourse assuming you are using Fedora or any other redhat base linux) </li>
<li><strong><span style="color: blue">iptables -A INPUT -i eth0 -p tcp -m tcp --dport 22 -m state --state NEW -m recent --set --name ssh_attempt --rsource -j LOG --log-prefix &quot;SSH connection attempt: &quot;</span></strong> </li>
<li>As you can see this &quot;<span style="color: blue"><strong>-j LOG --log-prefix &quot;SSH connection attempt</strong>: &quot;</span>&quot;  was appended to our previous <a href="SSH_Blocking+-+How_to_block_ssh_attacks_using_iptables">SSH BLOCKING HOW TO</a>. This is essentially logging all ssh attempts.</li>
<li>&quot;<strong><span style="color: blue">-j LOG</span></strong>&quot; This means to jump to the LOG chain in iptables. </li>
<li>&quot;<span style="color: blue"><strong>--log-prefix &quot;SSH connection attempt</strong>: &quot;</span>&quot; This is labeling the log with SSH connection attempt: &quot;.</li>
</ul>
</li>
<li>
<ul><strong>That was basic logging, now we will get into some more options in logging.</strong></p>
<li>Now lets say you want your logging to be more verbose. In iptables we can fix that by adding this entry in the rule.. <strong><span style="color: blue">--log-level 7</span></strong>. This is the highest level of logging (DEBUG LEVEL). </li>
<li>Now what if you logs are getting saturated by the second and overwhelming your processor? Well we can add limits also. Here is an example <strong><span style="color: blue">-m limit --limit 2/second --limit-burst 5</span></strong>. This will limit the logging to 2 entries per second and a max of 5 packets per second. </li>
</ul>
</li>
<li>
<ul><strong>So if we put it all together it would look like this..</strong></p>
<li><strong><span style="color: blue">iptables -A INPUT -i eth0 -p tcp -m tcp --dport 22 -m state --state NEW -m recent --set --name ssh_attempt --rsource -j LOG --log-level 7 -m limit --limit 2/second --limit-burst 5 --log-prefix &quot;SSH connection attempt: &quot;</span></strong></li>
</ul>
</li>
</ol>
<p><strong>There are a few more options that we can discuss on logging. If anybody wants to see them just leave a comment. If you liked the tutorial also please leave a comment. I will be adding a ULOG howto in the next day or so, which is my preferred way to log in iptables.</strong></p>
