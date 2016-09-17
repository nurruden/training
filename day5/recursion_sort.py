#-*-coding:utf-8-*-
#/usr/bin/env python
# def f4(a1,a2):
#     if a1 > 10000:
#         return
#     print (a1)
#     a3 = a1 + a2
#     r = f4(a2,a3)
#
# f4(0,1)

def  f5(depth,a1,a2):
    # print(depth)
    if depth == 10:
        return a1
    a3 = a1 + a2
    r = f5(depth + 1,a2,a3)
    return r
ret  = f5(1,0,1)
print(ret)

# a=exec('print(2+3-4*5/2-7+8-79*7+34*2-25/5)')