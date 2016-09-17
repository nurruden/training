#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func,ctime()))
        sleep(4)

def move(func):
    for i in range(2):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=('爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=('阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    print("All start %s" %ctime())
    for t in threads:
        t.setDaemon(True) #设置为true,主线程执行完后,不再等待子线程执行
        t.start()
    t.join()
    #我们只对上面的程序加了个join()方法，用于等待线程终止。join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    print("all over %s" %ctime())