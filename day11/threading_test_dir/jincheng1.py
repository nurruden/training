#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
from multiprocessing import Process
from threading import Thread
import time
li = []
def foo(i):
    time.sleep(1)
    li.append(i)
    print('say hi',li)
# if __name__ == "__main__":
#     for i in range(10):
#         p = Process(target=foo,args=(i,))
#         p.start()

if __name__ == "__main__":
    for i in range(10):
        p = Thread(target=foo,args=(i,))
        p.start()