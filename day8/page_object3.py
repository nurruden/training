#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
class Animals:
    def chi(self):
        print(self.name + " chi")

    def he(self):
        print(self.name + " he")

class Dog(Animals):
    def __init__(self,name):
        self.name = name

    def jiao(self):
        print(self.name + " wang")
alex = Dog("lijie")
alex.chi()
alex.jiao()