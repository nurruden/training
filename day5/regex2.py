#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import re
# origin = "hello allan angela,africa asdsa dsa19a sasx"
# r = re.split("a\w+",origin,1)       #1,最多分为两组
# print(r)
#
# g = re.split("(a\w+)",origin,2)
# #将分组放在返回值
# print(g)
#
# g1 = re.split("a(\w+)",origin,2)
# #将分组放在返回值
# print(g1)
#
# cal = "1 -2 * ((60 -30) + (-40.0/5) * (9-2*5/3 + 7 /3 * 99/4*2998 +10*46/14)) - (-4*3)"
# num = re.split("\(([^()]+)\)",cal,1)
# print(num)
# while True:
#     result = re.split("\(([^()]+)\)",cal,1)
#     if len(result) == 3:
#         pass
#     else:
#         pass

def calculator_mul(*args):
    while True:
        mul = re.split("(\d+\*\d+)",*args,1)
        if len(mul) != 3:
            return args
        result = eval(mul[1])
        new_args = mul[0] + str(result) + mul[2]
            # print(new_args)
        r = calculator_mul(new_args)
        return r
def calculator_div(*args):
    while True:
        mul = re.split("(\d+\/\d+)",*args,1)
        if len(mul) != 3:
            return args
        result = eval(mul[1])
        new_args = mul[0] + str(result) + mul[2]
            # print(new_args)
        r = calculator_div(new_args)
        return r

def calculator_add(*args):
    while True:
        mul = re.split("(\d+\+\d+)",*args,1)
        if len(mul) != 3:
            return args[0]
        result = eval(mul[1])
        new_args = mul[0] + str(result) + mul[2]
            # print(new_args)
        r = calculator_add(new_args)
        return r

def calculator_minus(*args):

    tmp = tuple(args)
    result = str(tmp[0]).replace(",","")
    # print(eval(eval(result)))
    return eval(eval((eval(result))))


cc = calculator_mul("2+3-4*5/2-7+8-79*7+34*2-25/5")
print(cc)
dd = calculator_div(str(cc))
print(dd)
ee = calculator_add(str(dd))
print(ee)
# ff = calculator_minus(ee)
# print(ee)
ff = calculator_minus(str(ee))
print(ff)


# ass = (("('5-10.0-15-621-5.0',)",))
# print(type(ass))
#
# print(str(ass[0]))
#
# abc = ass[0].replace(",","")
# print(eval(eval(abc)))
