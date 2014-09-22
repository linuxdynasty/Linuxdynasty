---
layout: post
status: publish
published: true
title: Using rsync to move files around
author:
  display_name: admin
  login: admin
  email: admin@linuxdynasty.org
  url: ''
author_login: admin
author_email: admin@linuxdynasty.org
wordpress_id: 26
wordpress_url: http://linuxdynasty.org/?p=26
date: !binary |-
  MjAwOC0wNS0yNCAxMDo1NTowOCAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNS0yNCAxMDo1NTowOCAtMDQwMA==
categories: []
tags:
- Beginner Linux HowTo's
- howto use rsync How to use rsync
comments: []
---
<p>You can use <strong>rsync</strong> to transfer files from either one directory to another or from one server to another. When copying over large directory structures, <strong>rsync</strong> is usually better than using <strong>cp -av</strong>. The <strong>cp</strong> command copies files and directories blindly, while <strong>rsync</strong> compares the two directories and only copies the differences. This saves time, hard drive load, system load, and if copying across a network, bandwidth. It is very useful when backing up a hard drive or an entire server. The command to use is:</p>
<p># <strong>rsync -avH --delete --exclude=/junk --exclude=/otherjunk /home /backup/ </strong></p>
<p><strong><font color="#0000ff">rsync</font> -avH --delete --exclude=&lt;<font color="#ff0000">file/directory to exclude</font>&gt; &lt;<font color="#ff0000">source files/directories</font>&gt; &lt;<font color="#ff0000">destination directory</font>&gt;</strong></p>
<p>The &quot;<strong>a</strong>&quot; flag will preserve important settings such as permissions, ownership, symbolic links, etc., as well as recursively copy the entire directory tree. The &quot;<strong>v</strong>&quot; flag is optional, and will list each file as it is copied and will give a summary of how much data was transferred. The &quot;<strong>H</strong>&quot; flag preserves hard links (a standard linux installation is often full of these). If you are absolutely sure that you don't have any hard links in the data you are copying, then you can omit it, but adding it won't hurt. The &quot;<strong>--delete</strong>&quot; flag means &quot;delete anything in the destination directory that doesn't exist in the source directory&quot;. This is useful if you are backing up a hard drive and you want to make sure that files that you removed from the main drive are removed from the backup drive as well. The &quot;<strong>--exclude</strong>&quot; flag allows you to skip over certain directories that you don't want copied over to the destination directory. You can have multiple &quot;<strong>exclude</strong>&quot; flags.</p>
<p>If you want to copy your data to another server, then you can use &quot;<strong>rsync://&lt;<font color="#ff0000">hostname</font>&gt;/&lt;<font color="#ff0000">path</font>&gt;</strong>&quot; as either the source or destination. The &quot;hostname&quot; is the IP or full hostname of the remote server, and &quot;path&quot; is the exported path that is set up in the rsync configuration on the remote server. </p>
<p><strong># rsync -avH --delete --exclude=/junk --exclude=/otherjunk /home rsync://backup.server/backup_path</strong></p>
<p><strong><font color="#0000ff">rsync</font> -avH --delete --exclude=&lt;</strong><strong><font color="#ff0000">file/directory to exclude</font></strong><strong><font color="#ff0000"></font>&gt; &lt;</strong><strong><font color="#ff0000">source files/directories</font></strong><strong><font color="#ff0000"></font>&gt; &lt;</strong><strong>rsync://<font color="#ff0000">hostname</font>/<font color="#ff0000">path</font>&gt;</strong></p>
<p><strong><font color="#0000ff">rsync</font> -avH --delete --exclude=&lt;</strong><strong><font color="#ff0000">file/directory to exclude</font></strong><strong>&gt; </strong><strong>&lt;</strong><strong>rsync://<font color="#ff0000">hostname</font>/<font color="#ff0000">path</font>&gt; </strong><strong>&lt;<font color="#ff0000">destination directory</font>&gt;</strong></p>
<p><strong>&nbsp;</strong></p>
