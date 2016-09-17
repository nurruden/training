#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
'''
 在100-300区间内,取既可以被3整除,又可以被7整除的数
'''
result = []
for i in range(100,301):
    if i % 3 == 0 and i % 7 ==0:
        result.append(i)
print(result)
