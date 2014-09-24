#!/usr/bin/env python
import re
import sys
import StringIO
import string
import lxml
from lxml import etree
import urllib2
from optparse import OptionParser

exitval = { 
          "OK" : 0,
          "WARNING" : 1,
          "CRITICAL" : 2,
          "UNKNOWN" : 3 
          }   

def get_queue_stats(queues):
    queue_stats = {}
    for queue in queues:
        status_table = queue.getchildren()
        queue_stats[status_table[1].text] = \
            {"consumers" : status_table[2].text,
             "memory" : re.sub(r'[A-Za-z]+', '', status_table[3].text),
             "count" : status_table[4].text,
             "msg_ready" : status_table[5].text,
             "msg_unack" : status_table[6].text,}
    return(queue_stats)

def get_connections(connections):
    running = 0
    con_stats = {}
    for connection in connections:
        status_table = connection.getchildren()
        if len(status_table) > 1:
            if re.search(r'\brunning\b', status_table[2].text):
                running += 1
                con_stats[re.sub(r'\:', '_', status_table[4].text)] = \
                   {"username" : status_table[1].text,
                    "vhost" : status_table[0].text,
                    "recv" : re.sub(r'[A-Za-z]+', '', status_table[5].text),
                    "send" : re.sub(r'[A-Za-z]+', '', status_table[6].text),
                    "pending" : re.sub(r'[A-Za-z]+', '', status_table[7].text)}
        else:
            break
    return(running, con_stats)

def get_core_stats(core):
    results_dict = {}
    for i in core:
        pair = i[0][0]
        if re.search(r'^node', pair.text):
            results_dict['node'] = pair.tail
        elif re.search(r'^pid', pair.text):
            results_dict['pid'] = pair.tail
        elif re.search(r'^bound to', pair.text):
            results_dict['bound_to'] = pair.tail
        elif re.search(r'^file descriptors', pair.text):
            match = re.search(r'^(\d+)\s+\/\s+(\d+)', pair.tail)
            used = match.group(1)
            avail = match.group(2)
            results_dict['file_descriptors'] = {'used' : used, 'avail' : avail}
        elif re.search(r'^erlang processes', pair.text):
            match = re.search(r'^(\d+)\s+\/\s+(\d+)', pair.tail)
            used = match.group(1)
            avail = match.group(2)
            results_dict['erlang_processes'] = {'used' : used, 'avail' : avail}
        elif re.search(r'^memory', pair.text):
            match = re.search(r'^(\b\d+\w+?\b)\s+\/\s+(\b\d+\w+\b)', pair.tail)
            used = match.group(1)
            avail = match.group(2)
            results_dict['memory'] = {'used' : used, 'avail' : avail}
        elif re.search(r'^ets memory', pair.text):
            results_dict['ets_memory'] = pair.tail
        elif re.search(r'^binary memory', pair.text):
            results_dict['binary_memory'] = pair.tail
    return(results_dict)

def output_zenoss_style(stats, connections, con_stats):
    core_stats = 'OK|connections=%s ' % (str(connections))
    for i, j in stats.items():
        if stats[i].__contains__('used') and stats[i].__contains__('avail'):
            used = re.sub('[A-Za-z]+$', '', stats[i]['used'])
            avail = re.sub('[A-Za-z]+$', '', stats[i]['avail'])
            core_stats += '%s_%s=%s %s_%s=%s ' % (i, 'used', used, i, 'avail', avail)
        elif not re.search(r'node|bound', i):
            core_stats += '%s=%s ' % (i, re.sub(r'[A-Za-z]', '', j))
    for i in con_stats.keys():
        core_stats += '%s_send=%s %s_recv=%s %s_pending=%s ' % (i, con_stats[i]['send'], i, con_stats[i]['recv'], i, con_stats[i]['pending'])
    for i in queue_stats.keys():
        core_stats += '%s_memory=%s %s_count=%s %s_msg_ready=%s %s_msg_unack=%s ' % (i, queue_stats[i]['memory'], 
                       i, queue_stats[i]['count'], i, queue_stats[i]['msg_ready'], i, queue_stats[i]['msg_unack'])
    return(core_stats)
    
if __name__ == "__main__":
    usage = 'python boo.py -u "http://rabbitmq1:55672" -a "zenoss-user zenossisinthehouse"'
    parser = OptionParser(usage)
    parser.add_option("-u", "--url", dest="url",
        help='This is the URL you will use to connect to RabbitMQ,\n \
             Example.. http://localhost/:55670')
    parser.add_option("-a", "--auth", dest="auth",
        help='This is the Login and Passwd you will use,\n \
             Example.. --auth=\'login passwd\'')
    (options, args) = parser.parse_args()

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = options.url
    options.auth = tuple(string.split(options.auth, sep=" "))
    login = options.auth[0]
    passwd = options.auth[1]
    password_mgr.add_password(None, top_level_url, login, passwd)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    fee = opener.open(top_level_url)
    html = re.sub("\[|\]|\'|\\\\n|\\\\|,",'',str(fee.readlines()))
    result = etree.HTML(html)
    body = result[1]
    core_stats = get_core_stats(body[1].getchildren())
    connections, con_stats = get_connections(body[4][1].getchildren())
    queue_stats = get_queue_stats(body[7][1].getchildren())
    zenoss_out = output_zenoss_style(core_stats, connections, con_stats)
    print zenoss_out
    sys.exit(0)
