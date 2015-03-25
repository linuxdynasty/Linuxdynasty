#!/usr/bin/env python

from argparse import ArgumentParser
from datetime import datetime
import re
from socket import gethostname
from subprocess import os, Popen, PIPE
import sys
from time import time

LOGTAIL = '/usr/local/bin/logtail'
TMPDIR = '/tmp'
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3
MESSAGE = {0: 'OK', 1: 'WARNING', 2: 'CRITICAL', 3: 'UNKNOWN'}

if not os.path.exists(LOGTAIL):
    print "Please install logtail"
    sys.exit(1)


def update_timestamp(fname, now):
    last_run_file = os.path.join(TMPDIR, fname + '_timestamp')
    try:
        file_handle = open(last_run_file, 'w')
        file_handle.write(str(now))
        file_handle.close()
    except Exception as e:
        print e
        sys.exit(CRITICAL)


def update_last_count(fname, count):
    last_count_file = os.path.join(TMPDIR, fname + '_count')
    try:
        file_handle = open(last_count_file, 'w')
        file_handle.write(str(count))
        file_handle.close()
    except Exception as e:
        print e
        sys.exit(CRITICAL)


def retrieve_last_count(fname):
    last_count_file = os.path.join(TMPDIR, fname + '_count')
    try:
        if os.path.exists(last_count_file):
            count = open(last_count_file, 'r').read()
        else:
            count = 0

        return count

    except Exception as e:
        print e
        sys.exit(CRITICAL)


def retrieve_timestamp(fname):
    last_run_file = os.path.join(TMPDIR, fname + '_timestamp')
    if os.path.exists(last_run_file):
        try:
            last_run_time = (
                datetime.fromtimestamp(
                    float(open(last_run_file, 'r').read())
                ).strftime('%m/%d/%Y %H:%M:%S')
            )
            return last_run_time
        except Exception as e:
            print e, ' foo'
            sys.exit(CRITICAL)
    else:
        return None


def alert(fname, now, count, warn, crit, lt=None, gt=None):
    file_name = fname.split('/')[-1]
    last_time = retrieve_timestamp(file_name)
    update_last_count(file_name, count)
    if not last_time:
        last_time = datetime.fromtimestamp(now).strftime('%m/%d/%Y %H:%M')

    update_timestamp(file_name, now)
    default_message = (
        '{0} line count {1} since last run {2} is'
        .format(fname, count, last_time)
    )
    if lt:
        if crit > warn:
            msg = (
                '{0}: Invalid threshold! Critical {1} is > Warning {2}'
                .format(MESSAGE[UNKNOWN], crit, warn)
            )
            return (UNKNOWN, msg)

        elif count < warn and count > crit:
            msg = (
                '{0}: {1} < than {2}'
                .format(MESSAGE[WARNING], default_message, warn)
            )
            return (WARNING, msg)

        elif count < warn and count < crit:
            msg = (
                '{0}: {1} < than {2}'
                .format(MESSAGE[CRITICAL], default_message, crit)
            )
            return (CRITICAL, msg)

        elif count > warn:
            msg = (
                '{0}: {1}'.format(MESSAGE[OK], default_message)
            )
            return (OK, msg)

    elif gt:
        if warn > crit:
            msg = (
                '{0}: Invalid threshold! Warning-{1} is > Critical-{2}'
                .format(MESSAGE[UNKNOWN], crit, warn)
            )
            return (UNKNOWN, msg)

        elif count > warn and count < crit:
            msg = (
                '{0}: {1} > than {2}'
                .format(MESSAGE[WARNING], default_message, warn)
            )
            return (WARNING, msg)

        elif count > warn and count > crit:
            msg = (
                '{0}: {1} > than {2}'
                .format(MESSAGE[CRITICAL], default_message, crit)
            )
            return (CRITICAL, msg)

        elif count < warn:
            msg = (
                '{0}: {1}'
                .format(MESSAGE[OK], default_message)
            )
            return (OK, msg)

    elif lt and gt or not lt and gt:
        msg = '{0}: Invalid args!'.format(MESSAGE[OK])
        return UNKNOWN


def print_stats(file_path, count, scheme, now):
    """Print out the stats in the graphite format, in which sensu can consume.
    Args:
        file_path (str): The full path of the file you are running this
            against.
        count (int): The line count.
            example = 200
        scheme (str): The base scheme to be used when sending the data to
            graphite.. default = hostname.file_name
        now (int|float): the unix timestamp of right now.

    Output:
    """
    file_path = re.sub(r'\/', '.', file_path)
    if isinstance(count, int):
        print '{0}{1}.count {2} {3}'.format(
            scheme.replace('.', '-'), file_path, count, now
        )

if __name__ == '__main__':
    usage = ''
    parser = ArgumentParser(usage)
    parser.add_argument(
        "--directory", dest="directory",
        help="The directory where the logs exist"
    )
    parser.add_argument(
        "--file", dest="file",
        help="name of the log"
    )
    parser.add_argument(
        "--scheme", dest="scheme",
        help="the metric naming scheme", default=gethostname()
    )
    parser.add_argument(
        "--warn", dest="warn", type=int,
        help="The value you would like to warn about"
    )
    parser.add_argument(
        "--crit", dest="crit", type=int,
        help="The value you would like to crit about"
    )
    parser.add_argument(
        '--lt', dest='lt', action='store_true', default=False,
        help='compare less than instead of greater than.'
    )
    parser.add_argument(
        '--gt', dest='gt', action='store_true', default=False,
        help='compare greater than instead of less than.'
    )
    parser.add_argument(
        '--nagios', dest='nagios', action='store_true', default=False,
        help='Create a Nagios alert.'
    )
    parser.add_argument(
        '--graphite', dest='graphite', action='store_true', default=False,
        help='Create a Graphite metric.'
    )
    parser.add_argument(
        '--use_last_count', dest='last_count', action='store_true',
        default=False, help="""Instead of calling logtail, use the
        /tmp/logfile_count file, that is generated when using the
        --nagios option."""
    )
    args = parser.parse_args()

    if args.directory and args.file:
        now = time()
        file_path = os.path.join(args.directory, args.file)
        if os.path.exists(file_path):
            tmp_file_path = os.path.join(TMPDIR, args.file)
            command = (
                Popen(
                    [
                        LOGTAIL, '-f', file_path, '-o', tmp_file_path
                    ], stdout=PIPE
                )
            )
            if args.nagios and not args.graphite:
                count = len(command.stdout.readlines())
                exit_code, msg = (
                    alert(
                        file_path, now, count, args.warn, args.crit,
                        args.lt, args.gt
                    )
                )
                print msg
                sys.exit(exit_code)

            elif not args.nagios and args.graphite:
                if args.last_count:
                    count = len(command.stdout.readlines())
                else:
                    count = retrieve_last_count(file_path)
                print_stats(file_path, count, args.scheme, now)
