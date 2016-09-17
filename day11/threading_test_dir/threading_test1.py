#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
from time import ctime,sleep

def music():
    for i in range(2):
        print("I was listening to music. %s" %ctime())
        sleep(1)

def movie():
    for i in range(2):
        print("I was at the movies! %s" %ctime())
        sleep(5)

if __name__ == '__main__':
    music()
    movie()
    print("all over %s" %ctime())