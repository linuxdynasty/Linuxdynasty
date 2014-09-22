---
layout: post
status: publish
published: true
title: You don't know Python
author:
  display_name: admin
  login: admin
  email: admin@linuxdynasty.org
  url: ''
author_login: admin
author_email: admin@linuxdynasty.org
excerpt: ! "<p>Not long ago I was mutually baited into an argument with one of our
  developers, in which he challenged me on why I had chosen Python for my most recent
  project. His claim that I didn't &quot;know Python&quot; he backed up with a few
  questions:</p>\r\n<ol>\r\n<li>What is Python's method resolution order?</li>\r\n<li>How
  does it bind variables on its stack?</li>\r\n<li>Does Python implement closures,
  and if so, how?</li></ol>\r\n<p>Now, I'll be the first to admit that I don't &quot;know
  Python&quot;. I can express my logic in the Pythonic vernacular, but there's much
  about it that I don't yet know about or understand. In much the same way as a person
  unfamiliar with English will use the imperative mood where the subjunctive is called
  for, it still works, but it's not done in the clearest and most accurate way.<br
  />\r\n<br />I jokingly retorted that I didn't even know those things about Perl,
  not because it's true but to make a point. I know Perl (and I know the answers in
  Python, too). But I don't need to know its MRO, how it &quot;binds variables on
  its stack&quot;, or how to write a closure in it, in order to write good Perl code.</p>\r\n<blockquote>&quot;Fools
  ignore complexity. Pragmatists suffer it. Some can avoid it. Geniuses remove it.&quot;
  -- Alan J. Perlis, &quot;Epigrams in Programming&quot;, 1982.<br />\r\n</blockquote>\r\n<p>\r\n<p>Do
  you really have to know everything about X in order to &quot;know X&quot;? Do I
  need to know Python's opcodes and when they're invoked? Do I need to know Perl's
  SV, HV, and other such structs and the hints maintained therein? Really, half the
  point of using these interpretted languages is so that you <em>don't</em> need to
  know their guts.</p></p>\r\n<br />"
wordpress_id: 208
wordpress_url: http://linuxdynasty.org/?p=208
date: !binary |-
  MjAwOS0wMy0xNyAxNzowMjozNCAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wMy0xNyAxNzowMjozNCAtMDQwMA==
categories: []
tags:
- Chahns Blog
- You don't know Python
comments: []
---
<p>Not long ago I was mutually baited into an argument with one of our developers, in which he challenged me on why I had chosen Python for my most recent project. His claim that I didn't &quot;know Python&quot; he backed up with a few questions:</p>
<ol>
<li>What is Python's method resolution order?</li>
<li>How does it bind variables on its stack?</li>
<li>Does Python implement closures, and if so, how?</li>
</ol>
<p>Now, I'll be the first to admit that I don't &quot;know Python&quot;. I can express my logic in the Pythonic vernacular, but there's much about it that I don't yet know about or understand. In much the same way as a person unfamiliar with English will use the imperative mood where the subjunctive is called for, it still works, but it's not done in the clearest and most accurate way.</p>
<p>I jokingly retorted that I didn't even know those things about Perl, not because it's true but to make a point. I know Perl (and I know the answers in Python, too). But I don't need to know its MRO, how it &quot;binds variables on its stack&quot;, or how to write a closure in it, in order to write good Perl code.</p>
<blockquote><p>&quot;Fools ignore complexity. Pragmatists suffer it. Some can avoid it. Geniuses remove it.&quot; -- Alan J. Perlis, &quot;Epigrams in Programming&quot;, 1982.
</p></blockquote>
<p><p>Do you really have to know everything about X in order to &quot;know X&quot;? Do I need to know Python's opcodes and when they're invoked? Do I need to know Perl's SV, HV, and other such structs and the hints maintained therein? Really, half the point of using these interpretted languages is so that you <em>don't</em> need to know their guts.</p></p>
<p><a id="more"></a><a id="more-208"></a></p>
<p><p>So at what point do we say that someone &quot;knows a language&quot;? Is it when the person can write something in it that actually works?</p></p>
<blockquote><p><code>print &quot;I know Perl and Python and PHP.&quot;;</code></p></blockquote>
<p>Or is it really just a matter of being able to write the most easily used (i.e. imported, subclassed) and maintained code? Well, that kind of code usually costs more in terms of conciseness and efficiency.</p>
<p>Is it when someone can effectively employ esoteric parts of the language, like Python's metaclasses, Perl's formats and indirect objects, or English's subjunctive mood? Some might argue that esoteric language features ought <em>not</em> to be used because they reduce semantic transparency, making the expressions more difficult to maintain.</p>
<p>Perhaps &quot;knowing a language&quot; means being aware of those esoteric features, knowing how they work when you encounter them, and knowing what to not do. (On split infinitives, cf. Brown, 1851; Jespersen, 1905; Fowler, 1926; Curme, 1931; and many more.) At first reading, that seems like a good fit to me, but think about it: you couldn't say you knew the language until you were familiar and comfortable with <em>every language feature available.</em></p>
<p>One of my former co-workers is notorious for writing terrible code. It works, yes, but consider: a Python script that provided singleton classes automatically instantiated which, upon instantiation, directly interacted with global collections which were in turn indexed by global functions that might or might not end up accessing methods of one (and no more than one) of those objects. And that's just the beginning. Or consider his project in which he invoked metaclasses like a crackhead invokes his pipe: as a solution to every problem he didn't want to deal with the right way.</p>
<p>This person knew Python's features. What he didn't know was how to write good Python. The code he wrote is unmaintainable, inextensible, single-use garbage.</p>
<p>There are plenty of examples I could bring up in Perl, Python, and even Bash, but the point is made: knowing a language doesn't mean using its every feature or knowing everything about it. It means being able to understand its less cryptic expressions without assistance; to discover and subsequently understand the meanings in its crypts; and to express oneself according to its grammar in a way that is clear, concise, correct, natural, and appropriate.</p>
<blockquote><p>&quot;Don't have good ideas if you aren't willing to be responsible for them.&quot; -- Alan J. Perlis, &quot;Epigrams in Programming&quot;, 1982.
</p></blockquote>
