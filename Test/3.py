#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
'''
l1 =[11,22,33],l2 = [22,33,44],找到两个列表中相同元素的集合
'''
l1 = [11,22,33]
l2 = [22,33,44]
set1 = set(l1)
set2 = set(l2)
com = list(set1.intersection(set2))
print(com)