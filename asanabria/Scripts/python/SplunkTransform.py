#!/usr/bin/env python
"""I built this script, because I needed to integrate Splunk Alerts into Zenoss.
   I did my best to mimic the Splunk Saved Search Alert that you get by email through Splunk, into Zenoss.
   As of right now any searches that you have saved, can now be sent to Zenoss by using zensendevent that comes with Zenoss.
   There are 2 caveats to this though....
   1- You will need to add to all your saved search | fields - _raw
   2- modify zensendevent on line number 170, 
   from.. 
   field, value = line.split('=')
   to..
   field, value = line.split('=',1)

   The reason for this change, is because Splunk will send "=" signs in the message output, and zensendevent is splitting by "=".
   So to get rid if this issue, you set the maxsplit to 1.

"""
import re
import string

__author__ = "Allen Sanabria"
__copyright__ = "Copyright 2010, LinuxDynasty"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer = "Allen Sanabria"
__email__ = "asanabria@linuxdynasty.org"
__status__ = "Production"

#Here I'm setting The Common Splunk Saved search Email OutPut
evt.summary = evt.SAVED_SEARCH
new_message = "Saved search results. <br><br>"
new_message += "Name: %s<br>" % (evt.SAVED_SEARCH)
new_message += "Query Terms: %s<br>" % (evt.SEARCH_STRING)
new_message += "Link To Results: <a href=%s>%s</a><br>" % ( evt.SPLUNK_LINK, evt.SPLUNK_LINK )
new_message += "Alert was triggered because of: %s<br><br>" % ( evt.TRIGGERED )

csv_header_orig = evt.CSV_HEADER.split(",")
header_length = len(csv_header_orig)
header_range = range(header_length)
body_length = len(evt.CSV_BODY.split(","))
line_length = body_length / header_length

#I do not want any of the columns that begin with __, as they do not have any relevant information  ( From what I can tell from my saved searches )
csv_header = []
for i in range(len(csv_header_orig)):
    if not re.search(r"^\"?_{1,}", csv_header_orig[i]):
        csv_header.append([csv_header_orig[i], i])

#Creating the table and its headers
new_message += "<table border=1>"
new_message += "<tr>"
for header in csv_header:
    new_message += "<th>%s</th>" % (header[0])
new_message += "</tr>"

#parse the message body and put it into pretty columns :)
list_of_events = evt.CSV_BODY.split(",")
for i in range(line_length):
    events = list_of_events[header_range[0]:header_range[-1]]
    for i in range(len(events)):
        events[i] = re.sub("\"|\s{1,}", "", events[i])
    new_message += "<tr valign=top>"
    for index in csv_header:
        index_number = index[1]
        new_message += "<td><pre>%s</pre></td>" % (events[int(index_number)])
    new_message += "</tr>"
    list_of_events.__delslice__(header_range[0],header_range[-1])
new_message += "</table>"
evt.message = new_message
