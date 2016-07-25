#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
class oldboy:
    def __init__(self,bk):
        self.backend = bk
    def fetch(self):
        print(self.backend)

    def add_record(self,record):
        print(self.backend,record)

    def del_record(self):
        print(self.backend)

obj1 = oldboy("www.eee.org")

obj1.fetch()


obj2 = oldboy("test.eee.org")

obj2.fetch()