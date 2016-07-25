#-*-coding:utf-8-*-
#/usr/bin/env python
import random


#65-90代表大写字母
#randomrange大于等于start,小于end

temp = ''
for i in range(6):
    num = random.randrange(0,4)
    if num == 3 or num ==1:
        rad2 = random.randrange(0,10)
        temp = temp + str(rad2)
    else:
        rad= random.randrange(65,91)
        c = chr(rad)
        temp = temp + c
print(temp)