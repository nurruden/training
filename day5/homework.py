#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import re

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

def calculator(*args):
    cc = calculator_mul(*args)
    dd = calculator_div(str(cc))
    ee = calculator_add(str(dd))
    ff = calculator_minus(str(ee))
    return ff
cal = "1 -2 * ((60 -30) + (-40.0/5) * (9-2*5/2 + 7 /3 * 99/3-2 +10*45/5)) - (4*3)"
num = re.split("\(([^()]+)\)",cal,1)
# print(num[1])
while True:
    origin = re.split("\(([^()]+)\)",cal,1)
    if len(origin) == 3:
        result1 = calculator(origin[1])
        print(result1)
        result = origin[0] + str(result1) + origin[2]
        print(result)
        cal = result
        print(cal)
    else:
        final = calculator(origin)
        print(final)
        break
