#-*-coding:utf-8-*-
#/usr/bin/env python
__aurthor__="Allan"

import time
print(time.time())  #时间戳
print(time.ctime())   #Sat Jun 11 11:24:30 2016
print(time.ctime(time.time()-86400)) #昨天的同一时间
time_obj = time.gmtime(time.time()-86400)
print(time_obj.tm_year,time_obj.tm_mon,time_obj.tm_mday)
print("%s-%s-%s" %(time_obj.tm_year,time_obj.tm_mon,time_obj.tm_mday))