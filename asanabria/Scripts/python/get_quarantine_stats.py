#!/usr/bin/env python

import sys
import re
import string

from subprocess import os
from datetime import date
from optparse import OptionParser
import MySQLdb

mydb =  'MONITOR'
db_user = 'zenoss'
db_passwd = 'iwanttomonitor'
host_db = '74.217.230.87'
Con = MySQLdb.connect(host=host_db, port=3306, user=db_user, passwd=db_passwd, db=mydb)
Cursor = Con.cursor(  )

directory = '/usr/mbs'
ls = os.listdir(directory)
today = date.today()
yesterday = date(today.year, today.month, today.day - 1)
QUOTAS = ('userlimiter', 'xfirelimiter', 'expiredclips', 'storagecleanup')
quotas = {}
bytes_deleted = []
file_count = 0
base_count = 0
insert_into = ["date", "files_userlimiter","size_userlimiter","files_xfirelimiter", \
              "size_xfirelimiter", "files_storagecleanup", "size_storagecleanup"]
for i in QUOTAS:
      quotas[i] = {'files_deleted': file_count,
                  'bytes_deleted': base_count}
line_number = 0
#print quotas

if __name__ == '__main__':
    usage =''
    parser = OptionParser(usage)
    parser.add_option("-d", "--date", dest="date",
                     help = "The date of the logs you want to parse, default is yesterday")
    (options, args) = parser.parse_args()

    mdate = re.compile(r'(\d{4})-?\/?(\d{2})-?\/?(\d{2})')
    if options.date:
        try:
            year = int(mdate.search(options.date).group(1))
            month = int(mdate.search(options.date).group(2))
            day = int(mdate.search(options.date).group(3))
            options.date = date(year, month, day)
        except:
            print 'input date in right format.. 2011-12-04 or 2011/12/04'
            sys.exit(1)
    else:
        options.date = yesterday
    logfiles = []
    for i in ls:
        atime = date.fromtimestamp(os.stat(os.path.join(directory, i)).st_atime)
        mtime = date.fromtimestamp(os.stat(os.path.join(directory, i)).st_mtime)
        if mtime == options.date and re.search("INFO",i) or atime == options.date and re.search("INFO",i):
            logfiles.append(os.path.join(directory, i))
    logdate = re.compile(r'^\[(\d{4})-(\d{2})-(\d{2})')
    moving = re.compile(r'.*Dst\:\s+\/[A-Za-z0-9-_]+\/[A-Za-z0-9-_]+\/quarantine\/(\w+)')
    bdeleted = re.compile(r'.*bytes\s+deleted\:\s+([0-9]+)')

    for files in logfiles:
        logfile = open(files, 'r')
        for line in logfile:
            line_number +=1
            try:
                year = int(logdate.search(line).group(1))
                month = int(logdate.search(line).group(2))
                day = int(logdate.search(line).group(3))
                match = date(year, month, day)
            except Exception as e:
               continue
            if date(year, month, day) == options.date:
                if moving.search(line):
                    file_count +=1
                    quotas[moving.search(line).group(1)]['files_deleted'] = file_count
                elif bdeleted.search(line) and int(bdeleted.search(line).group(1)) != 0:
                    bytes_deleted.append(bdeleted.search(line).group(1))
                else:
                    next
    for key, value in quotas.items():
        print "%s %s files deleted = %s" % (options.date, key, value['files_deleted'])
    for i in bytes_deleted:
        base_count = base_count + int(i)
    if base_count > 0:
        quotas['userlimiter']['bytes_deleted'] = base_count
        print 'userlimiter total bytes deleted %s' % ( str(base_count) )

    insertint = "INSERT INTO storageapi_files_deleted(%s,%s,%s,%s,%s,%s,%s) \
                 VALUES('%s','%s','%s','%s','%s','%s','%s')" \
                 % (insert_into[0],insert_into[1],insert_into[2],insert_into[3],insert_into[4], \
                 insert_into[5],insert_into[6],\
                 options.date, quotas['userlimiter']['files_deleted'], quotas['userlimiter']['bytes_deleted'], \
                 quotas['xfirelimiter']['files_deleted'], quotas['xfirelimiter']['bytes_deleted'], \
                 quotas['storagecleanup']['files_deleted'], quotas['storagecleanup']['bytes_deleted'])
    print insertint
    Cursor.execute(insertint)
    Con.commit()
