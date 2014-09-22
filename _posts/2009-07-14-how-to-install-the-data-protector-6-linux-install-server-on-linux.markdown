---
layout: post
status: publish
published: true
title: How To install the Data Protector 6.+ Linux Install Server on Linux
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 214
wordpress_url: http://linuxdynasty.org/?p=214
date: !binary |-
  MjAwOS0wNy0xNCAxMjoxODo0NSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wNy0xNCAxMjoxODo0NSAtMDQwMA==
categories: []
tags:
- Data Protector HowTo's
- How To install the Data Protector 6.+ Linux Install Server on Linux
- Data Protector 6.+ Linux Install Server on Linux
comments: []
---
<p>Now for those of you who are like me and really do not like reading<br />
long winded PDF Installation guides. Here is the SHORT on how to get<br />
Data Protector Installation server installed on RedHat/CentOS/Suse Linux System.</p>
<p user="true" style="display: none" mce_style="display:none">&nbsp;</p>
<ol>
<li>Download the 2 Data Protector Linux Installer ISO Images from HP's WebSite.</li>
<li>Mount both images on the server you are installing this on<br />
Example... ( <strong>mount -o loop -t iso9660 /root/B6960-10011.iso /mnt1/</strong> )<br />
Example... ( <strong>mount -o loop -t iso9660 /root/B6960-10012.iso /mnt2/</strong> )</li>
<li>Now copy over the contents of DP_DEPOT and LOCAL_INSTALL to a local mount of disc1<br />
Example... ( <strong>mkdir /root/DPINSTALL</strong> )<br />
Example... ( <strong>cp -rf /mnt1/DP_DEPOT /root/DPINSTALL</strong>/</li>
<li>Now copy over the contents of DP_DEPOT from disc2 into /root/DPINSTALL/DP_DEPOT/<br />
Example... ( <strong>cp -rf /mnt2/DP_DEPOT/* DP_DEPOT/</strong> )&nbsp;&nbsp; You will be overiding 2 rpm's, but that is alright</li>
<li>Change over to the DPINSTALL directory and install the RPM's<br />
Example... ( <strong>cd /root/DPINSTALL</strong> )<br />
Example... ( <strong>rpm -ivh *.rpm</strong> )</li>
<li>Almost done..... :)</li>
<li>I'm<br />
assuming you will install clients using SSH Keys. And this is how I<br />
will be showing you on how to get this to work. You can copy over the<br />
example omnirc file and use that one..<br />
Example... ( <strong>cp /opt/omni/.omnirc.TMPL&nbsp; /opt/omni/.omnirc</strong> )</li>
<li>Now you will need to enable the ssh keys option.<br />
Example.... ( open up /opt/omni/.omnirc using your favorite editor ) and modify this line....<br />
<strong>#&nbsp; OB2_SSH_ENABLED=0|1</strong><br />
and change it to....<br />
<strong>OB2_SSH_ENABLED=1</strong></li>
<li>We now need to generate a SSH KEY<br />
Example... ( <strong>ssh-keygen -t rsa -b 2048</strong> )</li>
<li>Once the key is generated ( assuming with&nbsp; out a password ) you now need to copy that key over to the clients that you want Data Protector installed on.<br />
Example... ( <strong>scp /root/.ssh/id_rsa.pub client:/root/.ssh/authorized_keys</strong> ) This is assuming that you have a /root/.ssh/ directory on your clients. If not you will have to create one.
</li>
</ol>
<p user="true" style="display: none" mce_style="display:none">&nbsp;</p>
<p>You are now ready to import the installtion server into your Data<br />
Protector Cell Manager... <span class="attention">VERY IMPORTANT &quot;&quot;&quot;&quot; DNS or your HOST entries<br />
for your Installation Server/Cell Manager/ and all your Clients has to<br />
be correct &quot;&quot;&quot;&quot;</span></p>
<p>&nbsp;</p>
