from argparse import ArgumentParser
from datetime import datetime
from json import dumps, loads
import os
from re import search, sub
import sys
from socket import gethostname
from subprocess import Popen, PIPE
from time import time

GLUSTER = '/usr/sbin/gluster'
TMPDIR = '/tmp/'
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3
MESSAGE = {
    0: 'OK',
    1: 'WARNING',
    2: 'CRITICAL',
    3: 'UNKNOWN'
}

usage = 'foo'
parser = ArgumentParser(usage)
parser.add_argument("--out_of_sync", dest="out_of_sync", action='store_true',
                    default=False,
                    help="Check how many files are out of sync."
                    )
parser.add_argument("--only_this_brick", dest="only_this_brick",
                    action='store_true', default=False,
                    help="Only check for values on this brick"
                    )
parser.add_argument("--volume_name", dest="volume_name",
                    help="The name of the gluster volume."
                    )
parser.add_argument("--scheme", dest="scheme",
                    help="the metric naming scheme", default=gethostname()
                    )
parser.add_argument("--warn", dest="warn", type=int,
                    help="The value you would like to warn about"
                    )
parser.add_argument("--crit", dest="crit", type=int,
                    help="The value you would like to crit about"
                    )
parser.add_argument('--nagios', dest='nagios', action='store_true',
                    default=False, help='Create a Nagios alert.'
                    )
parser.add_argument('--graphite', dest='graphite', action='store_true',
                    default=False, help='Create a Graphite metric.'
                    )
parser.add_argument('--use_last_count', dest='use_last_count',
                    action='store_true', default=False,
                    help="""Instead of calling logtail, use the
                            /tmp/logfile_count file, that is
                            generated when using the --nagios option.
                         """
                    )
args = parser.parse_args()


def update_timestamp(fname, now):
    last_run_file = os.path.join(TMPDIR, fname + '_timestamp')
    try:
        file_handle = open(last_run_file, 'w')
        file_handle.write(str(now))
        file_handle.close()
    except Exception as e:
        print e
        sys.exit(CRITICAL)


def update_count(fname, data):
    last_count_file = os.path.join(TMPDIR, fname + '_count')
    try:
        file_handle = open(last_count_file, 'w')
        file_handle.write(dumps(data, indent=4))
        file_handle.close()
    except Exception as e:
        print e
        sys.exit(CRITICAL)


def retrieve_last_count(fname):
    last_count_file = os.path.join(TMPDIR, fname + '_count')
    try:
        if os.path.exists(last_count_file):
            data = loads(open(last_count_file, 'r').read())
        else:
            data = []

        return data

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


def print_stats(brick_name, count, scheme, now):
    """Print out the stats in the graphite format, in which sensu can consume.
    Args:
        brick_name (str): The name of the brick.
        count (int): The number of files that are out of sync
            example = 200
        scheme (str): The base scheme to be used when sending the data to
            graphite.. default = hostname.file_name
        now (int|float): the unix timestamp of right now.

    Output:
    """
    brick_name = sub(r'\/|\:', '.', brick_name)
    if isinstance(count, int):
        print '{0}.{1}count {2} {3}'.format(
            scheme.replace('.', '-'), brick_name.replace('..', '.'), count, now
        )


def alert_on_out_of_sync(output):
    bricks = ""
    severities = []
    for key, val, in output.items():
        hostname = val['brick_name'].split(':')[0]
        if val['out_of_sync_count'] < args.warn:
            msg = (
                '{0}:Files are in sync on {1} == {2} and is less than {3}!'
                .format(
                    MESSAGE[OK], val['brick_name'],
                    val['out_of_sync_count'], args.warn
                )
            )
            if args.only_this_brick:
                if search(hostname, gethostname()):
                    severities.append(OK)
                    bricks = bricks + msg + "\n"
                    break
            else:
                severities.append(OK)
                bricks = bricks + msg + "\n"

        elif (val['out_of_sync_count'] >= args.warn and
                val['out_of_sync_count'] < args.crit):
            msg = (
                '{0}:Files out of sync on {1} == {2} and is greater than {3}!'
                .format(
                    MESSAGE[WARNING], val['brick_name'],
                    val['out_of_sync_count'], args.warn
                )
            )
            if args.only_this_brick:
                if search(hostname, gethostname()):
                    severities.append(WARNING)
                    bricks = bricks + msg + "\n"
                    break
            else:
                severities.append(WARNING)
                bricks = bricks + msg + "\n"

        elif val['out_of_sync_count'] > args.crit:
            msg = (
                '{0}: Files out of sync == {1} and is greater than {2}!'
                .format(MESSAGE[WARNING], val['out_of_sync_count'], args.warn)
            )
            if args.only_this_brick:
                if search(hostname, gethostname()):
                    severities.append(CRITICAL)
                    bricks = bricks + msg + "\n"
                    break
            else:
                severities.append(CRITICAL)
                bricks = bricks + msg + "\n"

    severities.sort()
    return(severities[-1], bricks.rstrip())


def parse_out_of_sync(output, now):
    bricks = {}
    brick_name = ''
    for line in output:
        if search('Brick', line):
            brick_name = line.split()[-1]
            bricks[brick_name] = {'brick_name': brick_name}
            bricks[brick_name]['last_run_time'] = now
        if search('Number of entries', line):
            if brick_name:
                bricks[brick_name]['out_of_sync_count'] = int(line.split()[-1])

    update_count('out_of_sync', bricks)
    return bricks


def out_of_sync(now):
    command_options = [
        GLUSTER, 'volume', 'heal', '{0}'.format(args.volume_name), 'info'
    ]
    if args.use_last_count:
        bricks = retrieve_last_count('out_of_sync')
        if not bricks:
            bricks = parse_out_of_sync(
                Popen(command_options, stdout=PIPE).stdout.readlines(), now
            )
    else:
        bricks = parse_out_of_sync(
            Popen(command_options, stdout=PIPE).stdout.readlines(), now
        )

    if args.graphite and not args.nagios:
        for brick, val in bricks.items():
            hostname = brick.split(':')[0]
            if args.only_this_brick:
                if search(hostname, gethostname()):
                    print_stats(
                        val['brick_name'], val['out_of_sync_count'],
                        args.scheme, now
                    )
            else:
                print_stats(
                    val['brick_name'], val['out_of_sync_count'], args.scheme,
                    now
                )
    elif args.nagios and args.warn and args.crit and not args.graphite:
        if args.warn > args.crit:
            msg = (
                '{0}: Invalid threshold. Warn {1} can not be > Crit {2}'
                .format(MESSAGE[WARNING], args.warn, args.crit)
            )
            print msg
            sys.exit(UNKNOWN)
        else:
            status_code, msg, = alert_on_out_of_sync(bricks)
            print msg
            sys.exit(status_code)

if __name__ == '__main__':
    now = time()
    if args.out_of_sync and args.volume_name:
        out_of_sync(now)
