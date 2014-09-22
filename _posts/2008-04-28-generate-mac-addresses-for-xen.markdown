---
layout: post
status: publish
published: true
title: Generate MAC addresses for XEN using shell
author:
  display_name: admin
  login: admin
  email: admin@linuxdynasty.org
  url: ''
author_login: admin
author_email: admin@linuxdynasty.org
wordpress_id: 90
wordpress_url: http://linuxdynasty.org/?p=90
date: !binary |-
  MjAwOC0wNC0yOCAxNjowOToyMiAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0wNC0yOCAxNjowOToyMiAtMDQwMA==
categories: []
tags:
- Shell HowTo's
- shell random unique XEN MAC addresses
comments: []
---
<p><span style="font-family: courier new;">#!/bin/bash<br /># Generate unique valid XEN MAC addresses in shell, 'cause it's faster ;)<br /># Xen MAC's begin with 00:16:3e</span></p>
<p><span style="font-family: courier new;">declare -i num="${1:-0}"<br />until [[ $num -gt 0 ]]; do<br /> read -p "How many MAC's do you want to generate? " num<br />done</span></p>
<p><span style="font-family: courier new;">declare -a macs=( )</span></p>
<p><span style="font-family: courier new;">while [[ $num -gt 0 ]]; do<br /> mac=$(printf '%02x:%02x:%02x' $((RANDOM % 256)) $((RANDOM % 256)) $((RANDOM % 256)))</span></p>
<p><span style="font-family: courier new;"> for i in "${macs[@]}"; do<br /> [[ $mac = $i ]] &amp;&amp; continue 2<br /> done</span></p>
<p><span style="font-family: courier new;"> macs[${#macs[*]}]=$mac<br /> echo 00:16:3e:$mac<br /> num=$((num-1))<br />done</span></p>
