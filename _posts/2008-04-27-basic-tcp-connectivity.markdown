---
layout: post
status: publish
published: true
title: Basic TCP Connectivity
author:
  display_name: tinkpen
  login: tinkpen
  email: tinkpen@sympatico.ca
  url: ''
author_login: tinkpen
author_email: tinkpen@sympatico.ca
wordpress_id: 88
wordpress_url: http://linuxdynasty.org/?p=88
date: !binary |-
  MjAwOC0wNC0yNyAxNTowNzoxNiAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNC0yNyAxNTowNzoxNiAtMDQwMA==
categories: []
tags:
- Introduction to Networking
- Basic TCP Connectivity TCP HowTo TCP Tutorial
comments: []
---
<p class="MsoNormal"><strong><span style="font-size: 14pt">TCP</span></strong></p>
<p class="MsoNormal"><strong>Create a connection</strong></p>
<p class="MsoNormal">It uses a three-way handshake</p>
<ol style="margin-top: 0cm" start="1" type="1">
<li class="MsoNormal">The<br />
     client [a machine/device requesting a service/connection] sends a SYN flag<br />
     &amp; the server port number of the service it wants to communicate (i.e.<br />
     Port 80 for http/web services) <br />
 The packet also includes the client’s Initial Sequence Number (ISN)</li>
<li class="MsoNormal">Server<br />
     – Resplies with it’s own SYN flag &amp; ISN to the client’s TCP port<br />
 An ACK flag is included in the packet in reply to the client’s SYN flag</li>
<li class="MsoNormal">Client<br />
     replies with an ACK flag that acknowledges the server’s SYN Flag<br />
<o:p></o:p></li>
</ol>
<p class="MsoNormal"><strong><br />
<o:p> </o:p></strong></p>
<p class="MsoNormal"><strong>Terminate a<br />
connection</strong></p>
<p class="MsoNormal">After all data is sent or session no longer needs the<br />
session is terminated. This can be done either by client or server. Here is an<br />
example of what is called an <strong>active<br />
close</strong></p>
<ol style="margin-top: 0cm" start="1" type="1">
<li class="MsoNormal">The<br />
     application (i.e. Web browser –Firefore) on the client sends a <strong>close</strong> command to the application<br />
     (i.e. Web Server – Apache)<span> </span>on the<br />
     server</li>
<li class="MsoNormal">Server<br />
     sends a FIN flag to client</li>
<li class="MsoNormal">Client<br />
     sends an ACK flag to acknowledge the FIN flag</li>
<li class="MsoNormal">Client<br />
     sends a FIN flag to server</li>
<li class="MsoNormal">Server<br />
     replies with ACK flag –acknowledging the termination of the TCP connection</li>
</ol>
<p class="MsoNormal">
<o:p> </o:p></p>
<p class="MsoNormal">
<o:p> </o:p></p>
<p class="MsoNormal"><strong>Flags used in TCP<br />
Connections?</strong></p>
<p class="MsoNormal">SYN<span> </span><span> </span>Synchronized sequence number<br />
FIN<span> </span><span> </span>Sender FINished sending data –end connection<br />
RST<span> </span><span> </span>Reset Connection<br />
PSH<span> </span>Push the data<br />
ACK<span> </span>Acknowledgment<br />
URG<span> </span>Urgent</p>
<p class="MsoNormal">
