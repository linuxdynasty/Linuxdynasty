#!/usr/bin/env python



import os
import sys
import re
import MySQLdb
from optparse import OptionParser
#libs
import Globals
import Acquisition
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from transaction import commit

mydb = 'puppet'
db_user = 'ls_mon_user'
db_passwd = 'GetM*niTor$ing10N3'
host_db = 'stats0-db.livestream.com'

current_groups = dmd.Groups.getOrganizerNames()
current_groups.pop(0)
print current_groups
