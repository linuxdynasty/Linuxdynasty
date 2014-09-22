---
layout: post
status: publish
published: true
title: LDAP Client How To
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 14
wordpress_url: http://linuxdynasty.org/?p=14
date: !binary |-
  MjAwOC0wMi0xMCAyMzo1MDowNiAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAyMzo1MDowNiAtMDUwMA==
categories: []
tags:
- Advance Linux HowTo's
- LDAP Client How To on Linux Fedora ubuntu Gentoo
comments: []
---
<p><strong><span style="color: red"> In this tutorial we will show you how to authenticate to a already configured ldap server</span></strong></p>
<ol>
<li>This file <span style="color: blue">&quot;<strong>/etc/ldap.conf</strong>&quot;</span> is the 1st file that has to be modified as this is the file that tells the system which ldap server to authenticate too.
<pre><br />host yourdomain.com<br />base dc=yourdomain,dc=com<br />uri ldap://yourdomain.com/<br />ldap_version 3<br />rootbinddn cn=Manager,dc=yourdomain,dc=com<br />scope sub<br />timelimit 5<br />bind_timelimit 5<br />nss_reconnect_tries 2<br />pam_login_attribute uid<br />pam_member_attribute gid<br />pam_password md5<br />pam_password exop<br />nss_base_passwd		ou=People,dc=yourdomain,dc=com<br />nss_base_shadow		ou=People,dc=yourdomain,dc=com<br />  </pre>
</li>
<li>Now we have to add the passwd in this file <span style="color: blue">&quot;<strong>/etc/ldap.secret</strong>&quot;</span> so that we can authenticate to the ldap server
<pre>password</pre>
</li>
<li>Now we have to modify this file <span style="color: blue">&quot;<strong>/etc/nsswitch.conf</strong>&quot;</span>
<pre><br />passwd:         files ldap<br />group:          files ldap<br />hosts:          dns ldap<br />services:   ldap [NOTFOUND=return] files<br />networks:   ldap [NOTFOUND=return] files<br />protocols:  ldap [NOTFOUND=return] files<br />rpc:        ldap [NOTFOUND=return] files<br />ethers:     ldap [NOTFOUND=return] files<br />netmasks:   files<br />bootparams: files<br />publickey:  files<br />automount:  files<br />sendmailvars:   files<br />netgroup:   ldap [NOTFOUND=return] files<br />  </pre>
</li>
<li>Now it is time to modify the files in /etc/pam.d/ directory.<br />
First file to be modified is <span style="color: blue">&quot;<strong>/etc/pam.d/login</strong>&quot;</span></p>
<table border="0">
<tbody>
<tr>
<td width="100">auth</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">account</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">password</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">session</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
</tbody>
</table>
<pre><br />auth            requisite       pam_securetty.so<br />auth            requisite       pam_nologin.so<br />auth            sufficient      pam_ldap.so<br />auth            required        pam_unix.so use_first_pass<br />auth            required        pam_tally.so onerr=succeed file=/var/log/faillog<br />account         required        pam_access.so<br />account         required        pam_time.so<br />account         required        pam_unix.so<br />account         sufficient      pam_ldap.so <br />password        sufficient      pam_ldap.so<br />session         required        pam_mkhomedir.so skel=/etc/skel/ umask=0022<br />session         required        pam_unix.so<br />session         required        pam_env.so<br />session         required        pam_motd.so<br />session         required        pam_limits.so<br />session         optional        pam_mail.so dir=/var/spool/mail standard<br />session         sufficient      pam_ldap.so <br />session         optional        pam_lastlog.so<br />  </pre>
</li>
<li>Now we modify <span style="color: blue">&quot;<strong>/etc/pam.d/shadow</strong>&quot;</span><br />
<table border="0">
<tbody>
<tr>
<td width="100">auth</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">account</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">password</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">session</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
</tbody>
</table>
<pre><br />auth            sufficient      pam_rootok.so<br />auth            required        pam_unix.so<br />auth            sufficient      pam_ldap.so use_first_pass<br />account         required        pam_unix.so<br />account         sufficient      pam_ldap.so<br />session         required        pam_unix.so<br />session         sufficient      pam_ldap.so<br />password        sufficient      pam_ldap.so<br />password        required        pam_permit.so<br />  </pre>
</li>
<li>Now we modify <span style="color: blue">&quot;<strong>/etc/pam.d/passwd</strong>&quot;</span><br />
<table border="0">
<tbody>
<tr>
<td width="100">password</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
</tbody>
</table>
<pre><br />password        sufficient      pam_ldap.so <br />password        required        pam_unix.so shadow nullok<br />  </pre>
</li>
<li>Now we modify <span style="color: blue">&quot;<strong>/etc/pam.d/su</strong>&quot;</span><br />
<table border="0">
<tbody>
<tr>
<td width="100">auth</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">account</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">session</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
</tbody>
</table>
<pre><br />auth            sufficient      pam_ldap.so<br />auth            sufficient      pam_rootok.so<br />auth            required        pam_unix.so use_first_pass<br />account         sufficient      pam_ldap.so<br />account         required        pam_unix.so<br />session         sufficient      pam_ldap.so<br />session         required        pam_unix.so<br />  </pre>
</li>
<li>Now we modify <span style="color: blue">&quot;<strong>/etc/pam.d/sudo</strong>&quot;</span><br />
<table border="0">
<tbody>
<tr>
<td width="100">auth</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
</tbody>
</table>
<pre><br />auth            sufficient      pam_ldap.so<br />auth            required        pam_unix.so use_first_pass<br />auth            required        pam_nologin.so<br />  </pre>
</li>
<li>In this file <span style="color: blue">&quot;<strong>/etc/pam.d/sshd</strong>&quot;</span> you have to add 3 entries, one for auth, one for account, and one for session.<br />
<table border="0">
<tbody>
<tr>
<td width="100">auth</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">account</td>
<td width="100">sufficient</td>
<td width="300">pam_ldap.so</td>
</tr>
<tr>
<td width="100">password</td>
<td width="100">required</td>
<td width="300">pam_ldap.so</td>
</tr>
</tbody>
</table>
<pre><br />auth            required        pam_nologin.so<br />auth            sufficient      pam_ldap.so <br />auth            required        pam_env.so<br />auth            required        pam_unix.so use_first_pass<br />account         sufficient      pam_ldap.so<br />account         required        pam_unix.so<br />account         required        pam_time.so<br />password        required        pam_ldap.so <br />password        required        pam_unix.so<br />session         required        pam_mkhomedir.so skel=/etc/skel/ umask=0022<br />session         required        pam_unix_session.so<br />session         sufficient      pam_ldap.so <br />session         required        pam_limits.so<br />  </pre>
</li>
</ol>
