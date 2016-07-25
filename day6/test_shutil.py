#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import shutil
shutil.copyfileobj(open('ini','r'),open('new','w'))
shutil.copyfile('first.xml','first_copy.xml')
ret = shutil.make_archive("first_copu.xml",'gztar')