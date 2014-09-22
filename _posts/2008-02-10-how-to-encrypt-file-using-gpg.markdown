---
layout: post
status: publish
published: true
title: How to Encrypt file using GPG
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 10
wordpress_url: http://linuxdynasty.org/?p=10
date: !binary |-
  MjAwOC0wMi0xMCAwNToyMzozNSAtMDUwMA==
date_gmt: !binary |-
  MjAwOC0wMi0xMCAwNToyMzozNSAtMDUwMA==
categories: []
tags:
- Advance Linux HowTo's
- How to Encrypt file using GPG on Linux Fedora Ubuntu Gentoo CentOS
comments: []
---
<p><strong><span style="color: red">Have you ever wanted to keep a certain file from nosy Sys Admins??? Well in this quick HOWTO I will show you how using GPG.</span></strong></p>
<p> <strong>Section-1 &quot;BASIC ENCRYPTION&quot;</strong></p>
<ol>
<li>
<ul>
With <strong><span style="color: blue">GPG</span></strong> you can encrypt and decrypt files with a password. <strong><span style="color: blue">GPG</span></strong> is an encryption and signing tool for Linux/UNIX like operating system such as OpenBSD/Solaris/Fedora.</p>
<li>In this first example I will show you the basics on how to encrypt a file. But before we do that lets create a file called <strong><span style="color: blue">encrypt_example</span>.<br />
<span style="color: blue">echo &quot;I'm  Encrypted&quot;&quot; &gt;encrypt_example</span></strong>. </li>
<li>To encrypt single file, use the <strong><span style="color: blue">GPG</span></strong> command as follows:<br />
<strong><span style="color: blue">gpg -c encrypt_example</span></strong>. This will create a encrypt_example.gpg file. </li>
<li>The <strong><span style="color: blue">-c</span></strong> option will Encrypt with symmetric cipher </li>
<li>You can now delete the original file if you like or send it to your home pc or whatever your heart desires :p.</li>
</ul>
<p><strong>Caution if you ever forget your passphrase, you cannot recover the data as it uses a very strong encryption.</strong></p>
<p> <strong>Section-2 &quot;Advanced Encryption&quot;</strong></p>
</li>
<li>
<ul>
In Section-1 you saw how to create a basic encryption for a file, now we will see how to do it with a few other options.</p>
<li>The first step is to make sure you generate a gpg key. You can do so by doing this:<br />
<strong><span style="color: blue">gpg --gen-key</span></strong>. This will generate your public and private keys and sign them for you. </li>
<li>When you run that command, you will have a few questions you will need to answer.
<pre>asanabria@ubuntu-dynasty:~$ gpg --gen-key<br />gpg (GnuPG) 1.4.6; Copyright (C) 2006 Free Software Foundation, Inc.<br />This program comes with ABSOLUTELY NO WARRANTY.<br />This is free software, and you are welcome to redistribute it<br />under certain conditions. See the file COPYING for details.<br /><br />Please select what kind of key you want:<br />   (1) DSA and Elgamal (default)<br />   (2) DSA (sign only)<br />   (5) RSA (sign only)<br />Your selection? 1<br />DSA keypair will have 1024 bits.<br />ELG-E keys may be between 1024 and 4096 bits long.<br />What keysize do you want? (2048) <br />Requested keysize is 2048 bits<br />Please specify how long the key should be valid.<br />         0 = key does not expire<br />        = key expires in n days<br />      w = key expires in n weeks<br />      m = key expires in n months<br />      y = key expires in n years<br />Key is valid for? (0) <br />Key does not expire at all<br />Is this correct? (y/N) Y<br /><br />You need a user ID to identify your key; the software constructs the user ID<br />from the Real Name, Comment and Email Address in this form:<br />    &quot;Heinrich Heine (Der Dichter) &quot;<br /><br />Real name: example<br />Email address: <a href="mailto:example@linuxdynasty.org">example@linuxdynasty.org</a><br />Comment: example<br />You selected this USER-ID:<br />    &quot;example (example) &quot;<br /><br />Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O<br />You need a Passphrase to protect your secret key.<br /> </pre>
</li>
<li>Now that you have your keys, we can get into the new options. Lets encrypt encrypt_example with this:<br />
<strong><span style="color: blue">gpg -sec encrypt_example</span>.</strong> </li>
<li>The <strong><span style="color: blue">-s</span></strong> option means to sign the file with your key, the <span style="color: blue">-e</span> option is to encrypt the file with a password, the <span style="color: blue">-c</span> option means to encrypt with a symmetric cipher using a passphrase.</li>
</ul>
<pre>asanabria@ubuntu-dynasty:~$ gpg -sce encrypt_example<br />                   <br />You need a passphrase to unlock the secret key for<br />user: &quot;example (example) &quot;<br />1024-bit DSA key, ID 846FA1E8, created 2007-08-31<br /><br />You did not specify a user ID. (you may use &quot;-r&quot;)<br /><br />Current recipients:<br /><br />Enter the user ID.  End with an empty line: example<br /><br />Current recipients:<br />2048g/0DFEBEF0 2007-08-31 &quot;example (example) &quot;<br /><br />Enter the user ID.  End with an empty line:<br /> </pre>
<p> <strong>Section-3 &quot;Decryption&quot;</strong></p>
<p> <strong>Quick Gotcha</strong>If you encrypt using the -s (The signature Option) you will have to use the password you created when you generate the public and private keys and not the password you used with the -c option (Unless they are both the same password).</p>
</li>
<li>
<ul>
Now if you want to decrypt file, you will have to use the <strong><span style="color: blue">-d</span></strong> option</p>
<li>Example <strong><span style="color: blue">gpg -d encrypt_example.gpg</span></strong>.
<pre>asanabria@ubuntu-dynasty:~$gpg -d encrypt_example.gpg <br />gpg: CAST5 encrypted data<br />gpg: encrypted with 1 passphrase<br />I&quot;m Encrypted!!!<br />  </pre>
</li>
<li>Now if you want to decrypt the file and send it to a new file name instead of standard output.<br />
You can do this <strong><span style="color: blue">gpg -o decrypt_example -d encrypt_example.gpg</span>. </strong></p>
<pre>asanabria@ubuntu-dynasty:~$ gpg -o decrypt_example -d encrypt_example.gpg <br />gpg: CAST5 encrypted data<br />gpg: encrypted with 1 passphrase<br />gpg: WARNING: message was not integrity protected<br />  </pre>
<pre>asanabria@ubuntu-dynasty:~$ cat decrypt_example <br />I'm Encrypted!!<br />  </pre>
</li>
</ul>
</li>
</ol>
<p><strong>Remember if file extension is .asc, it is a ASCII encrypted file and if file extension is .gpg, it is a binary encrypted file.</strong></p>
