#!/usr/bin/python3

import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      # time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
    seqnce = 0
    while seqnce <2000000:
        _thread.start_new_thread( print_time, (seqnce, 2, ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass