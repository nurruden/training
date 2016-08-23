#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import threading
import time
def process(arg):
    time.sleep(1)
    print(arg)

for i in range(100):
    t = threading.Thread(target=process,args=(i,))
    t.start()
