---
layout: post
status: publish
published: true
title: HowTo Manage your networked devices using Python and Pexpect
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "This is my first release of ldNetDeviceManager.py. The ldNetManager.py
  tool gives you the ability to manage your network devices with out having to purchase
  a product like Cisco's LMS or go through the planning phase of deploying a product
  like func. Each of the tools I mentioned before, only have the ability to manage
  devices in their realm. Func supports Linux devices and Cisco LMS supports only
  Cisco devices.\r\n\r\nThis tool has one goal. And that is to update your devices
  with out deploying any software to your remote devices. All you need is either telnet
  or ssh access to your devices and Python2.4 or better with Pexpect installed. Once
  you have those 2 requirements fullfilled, then you are pretty much ready to go.\r\n\r\nYou
  will need Python 2.4 or better and Pexpect. ( has not been tested with Python 3+
  )\r\n\r\nYou can get Python from <a href=\"http://python.org\">http://python.org</a>
  and Pexpect ( I'm currently using Pexpect 2.3, which you can get from <a href=\"http://sourceforge.net/projects/pexpect/files/\">SourceForge</a>.\r\n\r\nNetwork
  Device Manager {filelink=14}\r\nFor support. please check the forums, <a href=\"forums/LD_Network_Device_Manager\">http://www.linuxdynasty.org/forums/LD_Network_Device_Manager</a>
  .\r\nHere are the release notes..\r\nRevision .21 10/01/2009\r\n<ul>\r\n\t<li>Can
  now save output to a file. using the --save option</li>\r\n</ul>\r\nRevision .20
  09/27/2009\r\n<ul>\r\n\t<li>Support for Cisco Devices and Linux Operating Systems</li>\r\n\t<li>Support
  for telnet and ssh or both</li>\r\n\t<li>Knows if you passed sudo, su, or enable</li>\r\n\t<li>Can
  pass either 1 device or multiple devices</li>\r\n\t<li>Can pass 1 command or multiple
  commands through a text file.</li>\r\n\t<li>Can pass 1 device or multiple devices
  through a text file.</li>\r\n\t<li>When running show commands on Cisco devices,
  the script will know to send a ( space bar ) to get more info</li>\r\n</ul>\r\n"
wordpress_id: 219
wordpress_url: http://linuxdynasty.org/?p=219
date: !binary |-
  MjAwOS0wOS0yNyAyMjo1NDo1NiAtMDQwMA==
date_gmt: !binary |-
  MjAwOS0wOS0yNyAyMjo1NDo1NiAtMDQwMA==
categories:
- Python
- LD Device Manager
tags:
- Linux
- LD Network manager
- Python
- Cisco
- Pexpect
- Python Pexepect
comments:
- id: 11
  author: frankcui24
  author_email: frankcui24@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMS0xMS0xNyAwMjoxMzozOCAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMS0xNiAyMToxMzozOCAtMDUwMA==
  content: can you make available the source code for doing this ? thanks
---
<p>This is my first release of ldNetDeviceManager.py. The ldNetManager.py tool gives you the ability to manage your network devices with out having to purchase a product like Cisco's LMS or go through the planning phase of deploying a product like func. Each of the tools I mentioned before, only have the ability to manage devices in their realm. Func supports Linux devices and Cisco LMS supports only Cisco devices.</p>
<p>This tool has one goal. And that is to update your devices with out deploying any software to your remote devices. All you need is either telnet or ssh access to your devices and Python2.4 or better with Pexpect installed. Once you have those 2 requirements fullfilled, then you are pretty much ready to go.</p>
<p>You will need Python 2.4 or better and Pexpect. ( has not been tested with Python 3+ )</p>
<p>You can get Python from <a href="http://python.org">http://python.org</a> and Pexpect ( I'm currently using Pexpect 2.3, which you can get from <a href="http://sourceforge.net/projects/pexpect/files/">SourceForge</a>.</p>
<p>Network Device Manager {filelink=14}<br />
For support. please check the forums, <a href="forums/LD_Network_Device_Manager">http://www.linuxdynasty.org/forums/LD_Network_Device_Manager</a> .<br />
Here are the release notes..<br />
Revision .21 10/01/2009</p>
<ul>
<li>Can now save output to a file. using the --save option</li>
</ul>
<p>Revision .20 09/27/2009</p>
<ul>
<li>Support for Cisco Devices and Linux Operating Systems</li>
<li>Support for telnet and ssh or both</li>
<li>Knows if you passed sudo, su, or enable</li>
<li>Can pass either 1 device or multiple devices</li>
<li>Can pass 1 command or multiple commands through a text file.</li>
<li>Can pass 1 device or multiple devices through a text file.</li>
<li>When running show commands on Cisco devices, the script will know to send a ( space bar ) to get more info</li>
</ul>
<p><a id="more"></a><a id="more-219"></a></p>
<p>Here is an example of running LdNetManager.py against 3 of my servers..<br />
In the examples below, you will notice I am not passing a password and I'm using the root account. The script will know if you have ssh keys installed on the remote servers.</p>
<pre>python ldNetDeviceManager.py --login="root" --dlist=gfs.txt --command="chkconfig --level 3 snmpd on" --term="ssh" --outfile list gfs.txt</pre>
<pre>connecting to 192.168.101.107
using ssh root@192.168.101.107
chkconfig --level 3 snmpd on
[root@gfs1 ~]
connecting to 192.168.101.111
using ssh root@192.168.101.111
chkconfig --level 3 snmpd on
[root@gfs2 ~]
connecting to 192.168.101.113
using ssh root@192.168.101.113
chkconfig --level 3 snmpd on
[root@gfs3 ~]
Total host that passed 3
192.168.101.107
192.168.101.111
192.168.101.113
Total host that failed 0
Total host that had either incorrect login or passwords 0
Total host that could not connect 0</pre>
<p>Another example, this example shows that snmpd is set to on ..</p>
<pre>python ldNetDeviceManager.py --login="root" --dlist=gfs.txt --command="chkconfig --list --level 3 |grep snmpd " --term="ssh" --outfile list gfs.txt
connecting to 192.168.101.107
using ssh root@192.168.101.107
chkconfig --list --level 3 |grep snmpd snmpd           0:off   1:off   2:off   3:on    4:off   5:off   6:off
[root@gfs1 ~]
connecting to 192.168.101.111
using ssh root@192.168.101.111
chkconfig --list --level 3 |grep snmpd snmpd           0:off   1:off   2:off   3:on    4:on    5:on    6:off
[root@gfs2 ~]
connecting to 192.168.101.113
using ssh root@192.168.101.113
chkconfig --list --level 3 |grep snmpd snmpd           0:off   1:off   2:off   3:on    4:on    5:on    6:off
[root@gfs3 ~]

Total host that passed 3
192.168.101.107
192.168.101.111
192.168.101.113

Total host that failed 0
Total host that had either incorrect login or passwords 0
Total host that could not connect 0</pre>
<p>Another example. This time logging into Cisco Devices and runnign a show cdp neighbor..</p>
<pre>python ldNetDeviceManager.py -l "localadmin" -p "pass" -D 1host.txt -c "show cdp neighbor" -t "both"  --tout=3 --outfile list 1host.txt
connecting to 192.168.101.6
using ssh localadmin@192.168.101.6

ssh key already in host file
Authenticatedbefore while loop 2
show cdp neighborCapability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port
ID2W_9thFl_South   Gig 0/24          143           T I      AIR-AP113 Fas 02W_4507R Gig 0/1
167          R S I     WS-C4507R Gig 5/14
L_904A_SW3&gt;
connecting to 192.168.101.7
using ssh localadmin@192.168.101.7

TIMED OUT, could not connect to 192.168.101.7

connecting to 192.168.101.8
using ssh localadmin@192.168.101.8

ssh key already in host file
Authenticatedbefore while loop 2
show cdp neighborCapability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
2W_4507R Gig 0/24          136          R S I     WS-C4507R Gig 4/22
L_805A_SW1&gt;
Total host that passed 2192.168.101.6

192.168.101.8

Total host that failed 0
Total host that had either incorrect login or passwords 0
Total host that could not connect 1192.168.101.7</pre>
<p>Here is the default output of ldNetDeviceManager.py</p>
<pre>python ldNetDeviceManager.py-l, --login         Your user name to the device. Example below..     -l 'admin', --login='admin'-p, --passwd        Your password to the device. Example below..      -p 'passwd', --passwd='pass'-e, --enable        Your enable or su or sudo password to the device. Example below..-e 'passwd', --enable='pass'-D, --dlist         List of devices you want to run this script against. Example below..-D '/home/test/switches.txt', --dlist='/home/test/switches.txt'-d, --device        The devices you want to run this script against. Example below..-d '192.168.101.1', --device='192.168.101.1'-C, --clist         List of commands that you want to run ithis script against. Example below..-C '/home/test/commands.txt', --clist='/home/test/commands.txt'-c, --command       The command that you want to run. Example below.. -c '/sbin/netstat -tln', --command='show vlan'-t, --term          What terminal you are going to use (ssh or telnet or both. Example below..-t 'ssh', --term='ssh'-o, --output        The default is to run all the commands with out outputting them, this will enable output-o, --output        -h, --help          The will display this help file                   &lt;

Examples Below..   python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -C './cmd.txt' -t ssh -e 'p@55wd' --output --tout=2
python ldNetDeviceManager.py --login=dynasty --passwd='passwd' --dlist='./switches' --clist='./cmd.txt' --term=both --enable='p@55wd' --output --tout=2
python ldNetDeviceManager.py --login=dynasty --passwd='passwd' --dlist='./switches' --command='service snmpd restart' --term=ssh --enable='p@55wd' --output --tout=2
python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -C './cmd.txt' -t ssh  -o --tout=2
If you have SSH Keys then you do not need to pass a password unless you have to get root access or sudo access. example below..
python ldNetDeviceManager.py -l dynasty -d 192.168.101.11 -C './cmd.txt' -t ssh  -o --tout=2
python ldNetDeviceManager.py -l dynasty -p 'passwd' -d 192.168.101.11 -c 'sudo service snmpd restart' --term=ssh  --output --tout=2</pre>
