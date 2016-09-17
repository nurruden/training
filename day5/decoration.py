#-*-coding:utf-8-*-
#/usr/bin/env python
def outer(func):
    def inner(*args,**kwargs):
        print("hello")
        r = func(*args,**kwargs)
        print("end")
        return r
#return 原函数的返回值
    return inner

def outer1(func):
    def inner(*args,**kwargs):
        print("hello1")
        r = func(*args,**kwargs)
        print("end1")
        return r
#return 原函数的返回值
    return inner
@outer1
@outer
def f1(a1,a2):
    print("F1")
    return a1 + a2
f1(1,2)

#1.执行outer函数,并且将其下面的函数名,当做参数
#2.将outer的返回值重新赋值给F1 = outer的返回值
#3新F1函数执行