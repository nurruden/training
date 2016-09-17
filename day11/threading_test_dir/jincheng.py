#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import multiprocessing
import time
def f1(a1):
    time.sleep(2)
    print(a1)

if __name__ == "__main__":
    t = multiprocessing.Process(target=f1,args=(11,))
    # t.daemon = True
    #主进程终止,子进程终止
    t.start()
    t.join()
    t2 = multiprocessing.Process(target=f1, args=(22,))
    # t2.daemon = True
    t2.start()
    t2.join()
    print("End")