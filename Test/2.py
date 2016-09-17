#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
# print(ord("a"))
# print(ord("z"))
# print(ord("A"))
# print(ord("Z"))

'''
检查一个字符串内有多少大写字符,小写字符,多少数字
如果是数字item.isdigit()会返回True
'''

def check_type(string_string):
    num = 0
    Capital = 0
    Lower = 0

    for item in string_string:
        if item.isdigit():
            num += 1
        elif ord(item) in range(97,123):
            Lower += 1
        elif ord(item) in range(65,91):
            Capital += 1
        else:
            continue
    return num,Capital,Lower
ret = check_type("sasQ12z ()ZAa")
print(ret)

