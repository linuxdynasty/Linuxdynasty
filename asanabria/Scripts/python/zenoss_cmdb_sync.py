#!/bin/env python
##############################################################
#Created by Allen Sanabria aka LinuxDynasty aka PrNino69
#This is my attempt to essentially translate my perl zenoss
#syncing script to python, wish me LUCK...
#Started July 19
#Almost done July 20th
#Finally completed, July 24th
##############################################################

import sys, os, re, getopt, string, MySQLdb
from xmlrpclib import Fault
from xmlrpclib import ServerProxy
from urllib import urlopen


script = os.path.basename(sys.argv[0])
user = "test"
passwd = 'test'
util = '@test'
base = "http://%s:%s%s:8080" % (user,passwd,util)
searchDevUrl = base+'/zport/dmd/Devices/searchDevices?queryString='
groupsUrl = base+'/zport/dmd/Groups/getOrganizerNames'
systemsUrl = '/getSystemNamesString'

mydb =  'CMDB'
db_user = 'test'
db_passwd = 'test'
host_db = 'test'

try:
  Con = MySQLdb.connect(host=host_db, port=3306, user=db_user, passwd=db_passwd, db=mydb)
except Exception, e:
  print e
else:
  Cursor = Con.cursor(  )


def main():
  cmdb_query()

def cmdb_query():
  sql = "SELECT host_name FROM host_info"
  Cursor.execute(sql)
  Results = Cursor.fetchall(  )
  cmdb_update(Results)

def cmdb_update(Results):
  for host in Results:
    device = cluster = rack = "NULL"
    device = re.sub("\s+|\(|\)|\,", "", host[0])
    url = http(host[0])
    if re.search("^http", url):
      cluster = http(url+systemsUrl)
    rack_valid = re.search("^cc", device)
    valid = re.search("http", url)
    if rack_valid:
      octet = re.search("\-([0-9]{0,3})", device).group(1)
      rack = "Rack_"+octet
    if valid:
      print device
      print cluster
      print rack
      cmdb_up = "UPDATE host_info SET cluster_name = '%s', rack_info = '%s' WHERE (host_name = '%s')" \
      % ( cluster, rack, device )
      Cursor.execute(cmdb_up)
  Con.close(  )
        
def http(url):
  group_match= re.search("Groups", url)
  system_match= re.search("System", url)
  if group_match:
    gmatch = urlopen(groupsUrl).read()
    print gmatch
    group_sub = re.sub("\'|\s+|\[|\]", "",gmatch)
    group_list = group_sub.split(",")
    return group_list
  if system_match:
    smatch = urlopen(url).read()
    system_sub = re.sub("\/|\'|\s+|\[|\]", "",smatch)
    if re.search("\w+", system_sub):
      return system_sub
    else:
      return "NULL"
  else:
    device_url = urlopen(searchDevUrl+url).geturl()
    match_url = re.search("query", device_url)
    if match_url:
      return "none"
    else:
      return device_url


if __name__ == "__main__":
   main()
