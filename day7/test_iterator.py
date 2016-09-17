#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

# def xrange():
#     print(11)
#     yield 1
#
#     print(22)
#     yield 2
#
# r = xrange()
# ret = r.__next__()
# print(ret)
#
# ret = r.__next__()
# print(ret)


def xrange(n):
    print('start')
    start = 0
    while True:
        if start > n:
            return
        yield start
        start += 1
obj = xrange(5)
n1 = obj.__next__()
n2 = obj.__next__()
n3 = obj.__next__()
n4 = obj.__next__()
n5 = obj.__next__()
n6 = obj.__next__()


print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)

a = iter([1,2,3,4,6,8])
print(a.__next__())
print(a.__next__())

for i in xrange(10):
    print(i)
