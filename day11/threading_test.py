#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import threading
import time
def f0():
    pass
def f1(a1,a2):
    time.sleep(5)
    a3 = int(a1)+int(a2)
    print(str(a1)+" + " + str(a2) + " = " + str(a3))
    f0()
for i in range(3):
    t = threading.Thread(target=f1,args=(i,2,))
    # t.setDaemon(True)  #主线程执行完是否等待子线程,true等待
    t.start()
# t = threading.Thread(target=f1,args=(2,3,))
# t.setDaemon(True)
# t.start()
# t = threading.Thread(target=f1,args=(3,4,))
# t.setDaemon(True)
# t.start()