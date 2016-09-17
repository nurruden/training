#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import configparser

con = configparser.ConfigParser()
con.read("ini",encoding='utf-8')

resutl = con.sections()
print(resutl)            #['kaixin', 'wangyong']

ret = con.options("kaixin")
print(ret)

sections = con.has_section("kaixin")
print(sections)