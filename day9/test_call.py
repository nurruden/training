#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

class Foo:
    '''
    This is explanation
    '''
    def __init__(self):
        print("init")
        self.name = "allan"

    def __call__(self,*args,**kwargs):
        print("call")
        return 1

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)
#
# r = Foo() #__init__
# r()
# r['asd']  #__getitem__
# r['21'] = 123   #__setitem__
# r[1:3]    #__getitem__
# del r['21']     #__delitem__
# print(r)
# r = Foo()() #__call__
# print(r)


obj = Foo()
print(obj.__dict__)
print(Foo.__dict__)
print(Foo.__doc__)