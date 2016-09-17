#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
from multiprocessing import Process, Array
from multiprocessing import Process, Manager
# temp = Array('i', [11, 22, 33, 44])
# #i数组类型
#
# def Foo(i):
#     temp[i] = 100 + i
#     for item in temp:
#         print(i, '----->', item)
#
#
# for i in range(2):
#     p = Process(target=Foo, args=(i,))
#     p.start()
# 'c': ctypes.c_char,  'u': ctypes.c_wchar,
#     'b': ctypes.c_byte,  'B': ctypes.c_ubyte,
#     'h': ctypes.c_short, 'H': ctypes.c_ushort,
#     'i': ctypes.c_int,   'I': ctypes.c_uint,
#     'l': ctypes.c_long,  'L': ctypes.c_ulong,
#     'f': ctypes.c_float, 'd': ctypes.c_double
#
# 类型对应表

###########################################################################################################################




def Foo(i,dic):
    dic[i] = 100 + i
    print(dic.values())
    # for k,v in dic.items():
    #     print(k,v)
    #     print(len(dic))
    # 普通dic
    print(len(dic))
if __name__ == '__main__':
    manage = Manager()
    dic = manage.dict()
    for i in range(2):
        p = Process(target=Foo, args=(i,dic,))
        p.start()
        p.join()
# dic={0:100,1:101}
# Foo(2,dic)
# 普通dic