import os
import sys
import re
import string
from imaplib import *
from time import sleep, ctime
from threading import RLock
from threading import Lock
import Queue
import threading

WORKERS = 100
count = []
folders = re.compile("\"(\w+.*)\"")
class Worker(threading.Thread):
    def __init__(self, queue):
        self.__queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            host, cred = self.__queue.get()
            if host is None:
                print "breaking"
                break
            server = IMAP4(host)
            #print host + " started ", len(count)
            try:
                aboo = server.login(cred[0], cred[1])
                print server.state
                #if server.state() == 'AUTH':
                count.append(1)
                a, b = server.list()
                #server.select()
            except:
                print "Next"
                break
            if aboo:
                for c in string.split(b[0]):
                    if server.state == 'AUTH':
                        server.select()
                    #if server.state == 'SELECTED':
                    elif server.state == 'SELECTED':
                        ok, text = server.fetch('1*', '(RFC822)' )
                        #count.append(1)
                        print "booh yah", len(count)#, text
                        server.close()
                    else:
                        print server.state(), "Why am I here"
      
        server.logout()
        self.__queue.task_done()
#connections = 5000
#connections = 2000
queue = Queue.Queue(100)
connections = 100

threads = []
started_time = ctime()
for i in range(WORKERS):
    Worker(queue).start() # start a worker

for conn in range(connections):
    #print "push", ("149.31.111.104", ("testusr1", "testusr1"))
    queue.put(("149.31.58.164", ("sanabria", "Ch3wR@ng069")))
    #queue.put(("149.31.111.104", ("testusr1", "testusr1")))

for i in range(WORKERS):
    queue.put(None) # add end-of-queue markers

queue.join()

#print "STARTING HERE", ctime()
#for conn in xrange(connections):
#    after = threading.Thread(target=cmdb_exec, args=("149.31.111.104", ("testusr1", "testusr1")))
#    threads.append(after)
#for i in xrange(connections):
#    m = i%100
#    if m == 0:
#       print "sleeping 2 seconds"
#       sleep(2)
#    else:
#       threads[i].start()
    #sleep(.5)
    

#for i in xrange(connections):
#    threads[i].join()
ended_time = ctime()
print "ENDING HERE", ctime()
print started_time + " and " + ended_time


