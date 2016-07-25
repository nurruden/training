#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import sys,os
# for i in sys.path:
#     print(i)
#
# print(os.name)
# print(os.system('ls -al'))
#
# print(os.path)
# import hashlib
# hash = hashlib.md5()
# hash.update(bytes('1123',encoding='utf-8'))
# print(hash.hexdigest())
#
#
# #加盐
# hash = hashlib.md5(bytes("asqedwadasadas",encoding = 'utf-8'))
# hash.update(bytes('1123',encoding='utf-8'))
# print(hash.hexdigest())

p1 = os.path.dirname(__file__)
p2 = "bin"
my_dir = os.path.join(p1,p2)
print(my_dir)
#将my_dir路径放入path中.
sys.path.append(my_dir)
import s3