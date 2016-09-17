#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
# import test_reflect
# r = test_reflect.f1()
# print(r)

# inp = input("Input Module:")
# dd = __import__(inp)
# r1 = dd.f1()
# print(r1)

# inp = input("Input Module:")
# dd = __import__(inp)
# inp_func = input('Input function:')
# f = getattr(dd,inp_func)
# r = f()
# print(r)
f = 'lib.test.com'
a = __import__(f,fromlist=True)
dd = a.f10()
print(dd)