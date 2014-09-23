---
layout: post
status: publish
published: true
title: Two years of silence
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 852
wordpress_url: http://linuxdynasty.org/?p=852
date: !binary |-
  MjAxNC0wNi0xNCAxMToxMToyMiAtMDQwMA==
date_gmt: !binary |-
  MjAxNC0wNi0xNCAwNjoxMToyMiAtMDQwMA==
categories:
- Blog
tags: [vFense]
comments: []
---
I have been so focused on vFense, that I have been negligent of this blog.
vFense has come a long way from it's inception a little over 20 months ago.
We are still in the Beta, but we are continuously making improvements.
As of right now, I'm currently the only active developer working on the next
major release 0.8.0, which is a complete server rewrite. Examples of what is comming...

* All functions, methods, and classes will be fully documented.
* Vulnerability correlation for the following operating systems...
    * RedHat and clones
    * Ubuntu and clones
    * Windows
    * CVE/NVD
* Moved to using [APScheduler v3.1.0](https://linuxdynasty@bitbucket.org/linuxdynasty/apscheduler.git) for managing scheduled jobs
* Logging of all administrative tasks into RethinkDB.
* Remote command line tool for making API calls to vFense (Think of chef's knife command)
* Token based authentication for the agents
* Separated WEB authentication from Agent authentication.
