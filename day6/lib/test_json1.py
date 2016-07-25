#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import urllib3
import json
import urllib.request as request
import requests


#
# s = '{"name":"Allan","age":15}'
# #loads将字符串转换为基本数据类型
# result = json.loads(s)
# print(result)
# print(type(result))
# #dumps将基本数据类型转换为字符串
# result1 = json.dumps(result)
# print(result1)
# print(type(result1))
# a =  request.urlopen("http://www.weather.com.cn/adat/sk/101050101.html")
# re1 = a.read().decode('utf-8')
# print(re1)
dic = {"k1":123,"k2":456}
#dump先把字典转换为字符串,然后写入文件
re2 = json.dump(dic,open('db','w'))
print(re2)

#load打开文件,转换为字典
re3 = json.load(open('db','r'))
print(re3)