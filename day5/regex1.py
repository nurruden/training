#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import re
# r = re.findall("\d+\w\d+","a2b3c4d5")
# print(r)
# q = re.findall("(\d+)(\w*)(\d+)","a2b3c4d5")
# print(q)

origin = "hello, allan,angela,afric,as,df,a19w,alan"
g = re.findall("a(\w+)",origin)
n = re.search("(a)(\w+)",origin)
k = re.findall("(a)(\w+)",origin)
print(n.group())
print(n.groups())
print(k)
# print(g)

m = re.findall("(a)(\w+(a))(n)",origin)
print(m)

o = re.findall('(\dasd)+','1asd2asdp3asd98ka')
print(o)