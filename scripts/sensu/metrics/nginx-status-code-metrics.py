#!/usr/bin/env python

import sys
import re
from subprocess import os, Popen, PIPE
from optparse import OptionParser
from socket import gethostname
from time import time

LOGTAIL = '/usr/sbin/logtail'
TMPDIR = '/tmp'

json_status_code = re.compile(r'"status": "([0-9]{3})"')
txt_status_code = re.compile(r'HTTP\/1.[0-9]\"\s+([0-9]{3})\s+')

if not os.path.exists(LOGTAIL):
    print "Please install logtail"
    sys.exit(1)

def parse_log(tmpfile, file_type):
    """Parse each line and retrieve the status code..
    Args:
        tmpfile (list): List of entries in the log
        file_type (str): txt or json

    Example:
        txt:
            "GET /test/foo HTTP/1.0" 200 76288 "-" "Ruby"
        json:
            {
                "@timestamp": "2014-09-26T08:45:35-04:00",
                "@fields": {
                "remote_addr": "127.0.0.1",
                "remote_user": "-",
                "body_bytes_sent": "4823",
                "request_time": "0.127",
                "status": "200",
                "request": "POST /rubyamf_gateway/ HTTP/1.0",
                "request_method": "POST",
                "http_referrer": "https://foo.bar.net/test/test",
                "http_user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36"
            }
        }
    """
    stats = {}
    if file_type == 'json':
        code_search = json_status_code
    else:
        code_search = txt_status_code


    for i in tmpfile:
        code = code_search.search(i)
        if code:
            status_code = int(code.group(1))
            if stats.has_key(status_code):
                stats[status_code] += 1
            else:
                stats[status_code] = 1
    return stats

def print_stats(stats, scheme, now):
    """Print out the stats in the graphite format, in which sensu can consume.
    Args:
        stats (dict): Dictionary of the http status codes and its count.
            example {200: 20, 500: 10}
        scheme (str): The base scheme to be used when sending the data to graphite..
            default hostname.nginx
        now (int|float): the unix timestamp of right now.
    """
    if isinstance(stats, dict) and len(stats) > 0:
        for key, val in stats.items():
            print '{0}.codes.{1} {2} {3}'.format(scheme, key, val, now)

if __name__ == '__main__':
    usage =''
    parser = OptionParser(usage)
    parser.add_option("-d", "--directory", dest="directory",
                     help="The directory where the access logs exist")
    parser.add_option("-f", "--file", dest="file",
                     help="name of the access log")
    parser.add_option("-t", "--file_format", dest="file_format",
                     help="json or txt", default="txt")
    parser.add_option("-s", "--scheme", dest="scheme",
                     help="the metric naming scheme", default=gethostname())
    (options, args) = parser.parse_args()

    if options.directory and options.file:
        now = time()
        file_path = os.path.join(options.directory, options.file)
        if os.path.exists(file_path):
            tmp_file_path = os.path.join(TMPDIR, options.file)
            command = (
                Popen(
                    [
                        LOGTAIL, '-f', file_path, '-o', tmp_file_path
                    ], stdout=PIPE
                )
            )
            tmp_file = command.stdout.readlines()
            stats = parse_log(tmp_file, options.file_format)
            print_stats(stats, options.scheme, now)
