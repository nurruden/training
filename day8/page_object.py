#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

# class oldboy:
#     def fetch(self,backend):
#         print(backend,self)
#
#     def add_record(self,backend,record):
#         pass
#
#     def del_record(self,backend):
#         pass
#
# obj1 = oldboy()
#
# print(obj1)
# obj1.fetch("bb")
# <__main__.oldboy object at 0x101379c88>
# bb <__main__.oldboy object at 0x101379c88>




class oldboy:

    def fetch(self):
        print(self.backend)

    def add_record(self,record):
        print(self.backend,record)

    def del_record(self):
        print(self.backend)

obj1 = oldboy()
obj1.backend = "www.eee.org"
obj1.fetch()
obj1.add_record("sasdqwd")

obj2 = oldboy()
obj2.backend = "www.3232.org"
obj2.fetch()