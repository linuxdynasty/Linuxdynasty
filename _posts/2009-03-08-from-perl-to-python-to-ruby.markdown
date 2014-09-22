---
layout: post
status: publish
published: true
title: From Perl To Python To Ruby..
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
wordpress_id: 115
wordpress_url: http://linuxdynasty.org/?p=115
date: !binary |-
  MjAwOS0wMy0wOCAyMzowODozMSAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wMy0wOCAyMzowODozMSAtMDQwMA==
categories: []
tags:
- Dynastys Blog
- From Perl To Python To Ruby..
comments: []
---
<p>Well, I want to start this off, by saying that I am not leaving Python or Perl behind for Ruby, but that is the order in which I learned these 3 languages.&nbsp; I learned Perl first and I used it strictly for about 3 years, then I learned Python and I have been using Python mainly since then and Perl when needed. Now since I am playing with Puppet, I figured I should go ahead and learn Ruby as well.</p>
<p>So far I am pretty impressed with Ruby as it reminds me of Python and Perl put together. Everything in Ruby is a Object just like it is in Python. Also you do not require a semicolon at the end of every line in Ruby like you do in Perl. You do not require a $ for a Scalar variable or a @ for an array or a % for a hash in Ruby, which you do require in Perl but not in Python. There are a lot more similarities then that, and I will post some of the commands that are similar and ones that are a bit different. Now this will not be a complete list of differences but enough so that you get the idea. </p>
<pre>python	print &quot;hello world&quot; 			#This will print hello world but with a New Line at the End<br />ruby		puts &quot;hello world&quot;  			#This will print hello world but with a New Line at the End<br />perl		print &quot;hello worldn&quot;;			#This will print hello world but with a New Line at the End<br /><br />python	x = 8 					#x is equal to 8 which is an integer<br />ruby		x = 8					#x is equal to 8 which is an integer<br />perl		$x = 8;					#x is equal to 8 which is an integer<br /><br />python	type(x)					#x is what type.... Integer, String, Class... etc<br />ruby		x.class					#x is of what class.... FixNum, String, Class.. etc<br /><br />python	x, y, z = 1, 2, 3			#multiple assignments on one line<br />ruby		x, y, z = 1, 2, 3   			#multiple assignments on one line<br />perl		($x, $y, $z) = (1, 2, 3);   		#multiple assignments on one line<br /><br />python	se = &quot;foil&quot;				#Assign a string to se<br />ruby		se = &quot;foil&quot;				#Assign a string to se<br />perl		$se = &quot;foil&quot;				#Assign a string to se<br /><br />python	se[0:4]					#Access a slice of a string<br />ruby		se[0..4]				#Access a slice of a string <br /></pre>
