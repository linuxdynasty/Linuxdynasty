---
layout: post
status: publish
published: true
title: HowTo Customize Your Python Environment
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "<p>I've been programming in Python for about 2 years now and there are
  a few things I have learned along the way. One of the things I learned is..... How
  do I make my life easier???</p>\r\n<br />"
wordpress_id: 76
wordpress_url: http://linuxdynasty.org/?p=76
date: !binary |-
  MjAwOC0xMC0wOCAwMTozMDo1MiAtMDQwMA==
date_gmt: !binary |-
  MjAwOC0xMC0wOCAwMTozMDo1MiAtMDQwMA==
categories: []
tags:
- Python HowTo's
- HowTo Customize Your Python Environment
comments: []
---
<p>I've been programming in Python for about 2 years now and there are a few things I have learned along the way. One of the things I learned is..... How do I make my life easier???</p>
<p><a id="more"></a><a id="more-76"></a></p>
<p>One way is to customise your Python environment. This is quite easy to do! All you need to do is to create a pythonstartup file in your home directory.<br />
Example... /home/dynasty/.pythonstartup</p>
<pre>import readline<br />import rlcompleter<br />import os<br />import atexit<br />import os<br />readline.parse_and_bind('tab: complete')<br />histfile = os.path.join(os.environ['HOME'], '.pythonhistory')<br />try:<br />    readline.read_history_file(histfile)<br />except IOError:<br />    pass<br />atexit.register(readline.write_history_file, histfile)</pre>
<p>The above code will give you tab completion of your python modules. Which will save you so much time, here is an example...<br />
Also in your /home/dynasty/.bash_profile add this..<br />
PYTHONSTARTUP=$HOME/.pythonstartup<br />
export PYTHONSTARTUP</p>
<p>If you want these changes to take effect immediately, do this in your current shell..<br />
export PYTHONSTARTUP=$HOME/.pythonstartup<br />
Now run python...</p>
<pre><pre><br />&gt;&gt;&gt; sys.<br />Display all 224 possibilities? (y or n)<br />sys.__class__              sys.exit<br />sys.__delattr__            sys.exitfunc<br />sys.__dict__               sys.getcheckinterval<br />sys.__displayhook__        sys.getdefaultencoding<br />sys.__doc__                sys.getdlopenflags<br />sys.__egginsert            sys.getfilesystemencoding<br />sys.__excepthook__         sys.getrecursionlimit<br />sys.__getattribute__       sys.getrefcount<br />sys.__hash__               sys.hexversion<br />sys.__init__               sys.last_traceback<br />sys.__name__               sys.last_type<br />sys.__new__                sys.last_value<br />sys.__plen                 sys.maxint<br />sys.__reduce__             sys.maxunicode<br />sys.__reduce_ex__          sys.meta_path<br />sys.__repr__               sys.modules<br />sys.__setattr__            sys.path<br />sys.__stderr__             sys.path_hooks<br />sys.__stdin__              sys.path_importer_cache<br />sys.__stdout__             sys.platform<br />sys.__str__                sys.prefix<br />sys._current_frames        sys.ps1<br />sys._getframe              sys.ps2<br /></pre>
<p>Now that you have your Python environment ready we now need to get your VIM environment ready as well. For those of you who do not know what VIM is, it is an editor or should I say THE EDITOR. Now if you are running any distro of Linux you are sure to have VIM. For those of you who do not have VIM.... GETTTT ITTTT!!! :)</p>
<p>Once you know that you have vim, lets go ahead and create a vimrc&nbsp; file. For example /home/dynasty/.vimrc</p>
<pre><pre>set encoding=utf8<br />set paste<br />set expandtab<br />set textwidth=0<br />set tabstop=4<br />set softtabstop=4<br />set shiftwidth=4<br />set autoindent<br />set backspace=indent,eol,start<br />set incsearch<br />set ignorecase<br />set ruler<br />set wildmenu<br />set foldlevel=0<br />set clipboard+=unnamed<br />syntax on<br /></pre>
<pre>&nbsp;</pre>
<p>Now your vim environment is good and ready to go. If you need to know what each of those values mean all you need to do is run vim and <br />
type :help &lt;value_name&gt;</p>
