---
layout: post
status: publish
published: true
title: HowTo Send Splunk Alerts To Zenoss, And make them Look Like Splunk
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
excerpt: ! "We needed to integrate the Splunk Alerts into Zenoss, because even though
  Splunk can indeed send out alerts. Splunk does not have any clue about what an \"Escalation
  Process\" is. With Zenoss you can create an \"Escalation Process\".\r\n\r\nI have
  2 ways to send events to Zenoss from Splunk..\r\n<ol>\r\n\t<li>Write a Script that
  uses the snmptrap command.</li>\r\n\t<li>Write a Script that uses the Zenoss zensendevent
  command.</li>\r\n</ol>\r\nI decided to go with the Zenoss zensendevent command (
  Which is a python script with no external dependencies, which can be copied from
  the Zenoss Server at $ZENHOME/bin/zensendevent ).\r\n\r\nNow it's time to get the
  ball rolling..\r\n<ol>\r\n\t<li>On the Splunk Server I copied the zensendevent script
  from the Zenoss Server to Splunk on /opt/splunk/bin/scripts/zensendevent.</li>\r\n\t<li>I
  then created a shell script called Splunk2Zenoss.sh. ( This script takes the Saved
  Splunk Search and passes it over to Zenoss )This script will also be located in
  /opt/splunk/bin/scripts/Splunk2Zenoss.sh</li>\r\n\t<li>You will then need to modify
  the options in the script. (For instance the severity of the alert, the zenoss server,
  the event mapping, event key, login and passwd )</li>\r\n\t<li>I then created the
  saved search in Splunk and make sure to check the Trigger Shell Script option. (
  Make sure to put the script name in here )</li>\r\n</ol>\r\n"
wordpress_id: 197
wordpress_url: http://linuxdynasty.org/?p=197
date: !binary |-
  MjAxMC0wOC0wMyAxOTo0Mjo0MiAtMDQwMA==
date_gmt: !binary |-
  MjAxMC0wOC0wMyAxOTo0Mjo0MiAtMDQwMA==
categories:
- Zenoss
tags:
- Zenoss
- HowTo Send Splunk Alerts To Zenoss
- And make them Look Like Splunk
comments:
- id: 18
  author: bensbrowning
  author_email: benb@bensbrowning.com
  author_url: ''
  date: !binary |-
    MjAxMS0xMi0wMSAxNDowNTowMSAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0wMSAwOTowNTowMSAtMDUwMA==
  content: ! "Hi there,\r\n\r\nAny chance you could post your Splunk2Zenoss.sh? I\r\n\r\nThanks!"
- id: 30
  author: dynasty
  author_email: asanabria@linuxdynasty.org
  author_url: ''
  date: !binary |-
    MjAxMS0xMi0xMCAwMDozMzo1OSAtMDUwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0wOSAxOTozMzo1OSAtMDUwMA==
  content: It has been uploaded
---
<p>We needed to integrate the Splunk Alerts into Zenoss, because even though Splunk can indeed send out alerts. Splunk does not have any clue about what an "Escalation Process" is. With Zenoss you can create an "Escalation Process".</p>
<p>I have 2 ways to send events to Zenoss from Splunk..</p>
<ol>
<li>Write a Script that uses the snmptrap command.</li>
<li>Write a Script that uses the Zenoss zensendevent command.</li>
</ol>
<p>I decided to go with the Zenoss zensendevent command ( Which is a python script with no external dependencies, which can be copied from the Zenoss Server at $ZENHOME/bin/zensendevent ).</p>
<p>Now it's time to get the ball rolling..</p>
<ol>
<li>On the Splunk Server I copied the zensendevent script from the Zenoss Server to Splunk on /opt/splunk/bin/scripts/zensendevent.</li>
<li>I then created a shell script called Splunk2Zenoss.sh. ( This script takes the Saved Splunk Search and passes it over to Zenoss )This script will also be located in /opt/splunk/bin/scripts/Splunk2Zenoss.sh</li>
<li>You will then need to modify the options in the script. (For instance the severity of the alert, the zenoss server, the event mapping, event key, login and passwd )</li>
<li>I then created the saved search in Splunk and make sure to check the Trigger Shell Script option. ( Make sure to put the script name in here )</li>
</ol>
<p><a id="more"></a><a id="more-197"></a></p>
<p><a href="images/stories/Zenoss/SavedSearch.png" rel="shadowbox[0]"><img style="width: 200px; height: 200px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/Zenoss/SavedSearch.png" alt="" /></a><a href="images/stories/Zenoss/Splunk2Zenoss.png" rel="shadowbox[0]"><img style="width: 200px; height: 200px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/Zenoss/Splunk2Zenoss.png" alt="" /></a><a href="images/stories/Zenoss/Transform ScreenShot.png" rel="shadowbox[0]"><img style="width: 200px; height: 200px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/Zenoss/Transform ScreenShot.png" alt="" /></a></p>
<p>I did my best to mimic the Splunk Saved Search Alert that you get by email through Splunk, into Zenoss. As of right now any searches that you have saved, can now be sent to Zenoss by using zensendevent that comes with Zenoss.</p>
<p style="margin-top: 10px; margin-bottom: 15px;"><span class="attention">There are 2 caveats to this though....</span></p>
<ol>
<li>You will need to add to the following ( | fields - _raw ) to all your saved searches, with out the ().</li>
<li>modify zensendevent on line number 170,<br />
from..<br />
field, value = line.split('=')<br />
to..<br />
field, value = line.split('=',1)<br />
The reason for the change above, is because Splunk will send "=" signs in the message output, and zensendevent is splitting by "=". So to get rid if this issue, you set the maxsplit to 1.</li>
</ol>
<p>&nbsp;</p>
<p>Here are ScreenShot Examples of a Splunk Email and a Zenoss Email<br />
<a href="images/stories/Zenoss/ZenossSevereTest1.png" rel="shadowbox[0]"><img style="width: 200px; height: 200px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/Zenoss/ZenossSevereTest1.png" alt="" /></a><a href="images/stories/Zenoss/severeTest1_splunk.png" rel="shadowbox[0]"><img style="width: 200px; height: 200px;" src="http://linuxdynasty.org/wp-content/themes/twentyten/images/stories/Zenoss/severeTest1_splunk.png" alt="" /></a></p>
<p>Splunk2Zenoss.sh == {filelink=4}</p>
<p>SplunkTransfor.py == {filelink=5}</p>
