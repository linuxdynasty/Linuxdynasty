#!/usr/bin/env python
import os, sys, re, string
from optparse import OptionParser


def generateSNMP(bstats):
    for keys in bstats.keys():
        for skeys in bstats[keys].keys():
            print "exec %s%s /usr/local/bin/getBindStats.py -t \'%s\' -s \'%s\'" % (re.sub(r'\s+', '',keys),re.sub(r'\s+|>|<|\/','-',skeys),keys, skeys)

def poutput(bstats, gtype, bstat):
    print  bstats[gtype][bstat]

def getRequestType(stats, index):
    while not re.search(r'^\+{2}\s+(\w.*)\s+\+{2}', stats[index]):
        index = index - 1
    rtype = re.search(r'^\+{2}\s+(\w.*)\s+\+{2}', stats[index]).group(1)
    return rtype

def main():
    try:
        fstats = open('/var/cache/bind/named.stats', 'r').readlines()
    except IOError, e:
        print e
        sys.exit(1)
    allStats = {}
    for i in range(len(fstats)):
        fstats[i] = re.sub(r'\s{2,}|\]|\]|\'|\\n|\n', '', fstats[i])
    index = 0
    for i in fstats:
        stype = getRequestType(fstats, index)
        j = re.search(r'(^\d+)\s+(\w+.*)', i)
        if j:
            try:
                allStats[stype][j.group(2)] = int(j.group(1))
            except:
                allStats[stype] = {j.group(2) : int(j.group(1))}
            #print stype, j.group(2)
        index +=1
    if options.print_stat:
        poutput(allStats, options.gtype, options.print_stat)
    elif options.generate:
        generateSNMP(allStats)
    os.system('/usr/sbin/rndc stats')
    sys.exit(0)

if __name__ == '__main__':
    usage = "usage: %prog arg --grouptype=\'Incoming Requests\' --printstat=\'A\'"
    parser = OptionParser(usage)
    parser.add_option("-t", "--grouptype", dest="gtype",
                     help="Cache DB RRsets,Incoming Queries,Incoming Requests,Name Server Statistics,Outgoing Queries,Resolver Statistics,Socket I/O Statistics,Zone Maintenance Statistics ")
    parser.add_option("-s", "--printstat", dest="print_stat",
                     help="Acceptable Values are these:::TXT,PTR,SPF,queries caused recursion,A,IPv4 NS address fetch failed,mismatch responses received,TCP/IPv4 connections established,queries with RTT 100-500ms,query timeouts,query retries,NSEC,IPv4 responses received,requests with EDNS(0) received,TCP/IPv4 sockets closed,IPv4 IXFR requested,SRV,NOTIFY,queries with RTT 10-100ms,TCP/IPv4 connections accepted,lame delegations received,FORMERR received,RRSIG,queries with RTT > 1600ms,UDP/IPv4 recv errors,NS,IPv4 notifies sent,queries with RTT 800-1600ms,SERVFAIL received,IPv4 AXFR requested,auth queries rejected,ANY,IPv4 requests received,queries with RTT < 10ms,IPv4 notifies received,IPv4 queries sent,queries resulted in referral answer,NXDOMAIN,other errors received,QUERY,truncated responses received,MX,TCP requests received,")
    parser.add_option("-g", "--gensnmp", action="store_true",
                     dest="generate",default=False,
                     help="This will generate in STDOUT the SNMP info you need in snmpd.conf")
    (options, args) = parser.parse_args()

    main()
