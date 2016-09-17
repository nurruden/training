#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import threading

mylock = threading.RLock()
num = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num
        while True:
            mylock.acquire()
            print('\nThread(%s) locked, Number: %d' % (self.t_name, num))
            if num >= 4:
                mylock.release()
                print('\nThread(%s) released, Number: %d' % (self.t_name, num))
                break
            num += 1
            print('\nThread(%s) released, Number: %d' % (self.t_name, num))
            mylock.release()


def test():
    thread1 = myThread('A')
    thread2 = myThread('B')
    thread_list = [thread1,thread2]
    for t in thread_list:
        t.start()
    t.join()#主线程等待, join(2)最多等两秒


if __name__ == '__main__':
    test()