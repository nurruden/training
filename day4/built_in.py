# -*-coding:utf-8-*-
# /usr/bin/env python
# i = abs(123)
# print i
# j = abs(-123)
# print j
# #all,需要传一个可迭代的东西,里面所有的值是真,返回真
# r1 = all([True,True])
# r2 = all([True,True,False])
# print r1,r2
#
# #any,有一个真则为真
# m = any ([True,False])
# print m

# ascii,对象的类中找__repr__,获取返回值,python3.5有效,2.7没有
# class Foo:
#     def __repr__(self):
#         return hello
#
# obj = Foo()
# l = ascii(obj)
# print(l)

# bin()二进制
# oct()八进制
# int()十进制
# hex()十六进制
# print bin(10)
# print oct(9)
# print hex(20)
#
# #
# a = chr(66)
# print a
# z = ord('B')
# print z
# callable是否可以执行
# f1 = 123
# r = callable(f1)
# print r

# dir() 看函数提供什么功能
# li = []
# print dir(li)

# divmod
# r = divmod(10,3)
# print r
# eval可以执行一个字符串形式的表达式
# a = "1 + 3"
# ret = eval("1 + 3")
# print ret
# ret1 = eval("a + 60",{"a":90})
# print ret1
#
# exec("for i in range(10):print i")
#filter获取符合条件的,循环可迭代的对象,获取每一个参数,函数(参数)
# def f1(x):
#     if x > 22:
#         return True
#     else:
#         return False
# ret = filter(f1,[11,22,33])
# print ret
#map,让所有的数都统一做操作

# def f2(x):
#     return x + 100
# ret2 = map(f2,[1,2,3,4,5])
# print ret2
#iter创建可以被迭代的东西
# obj = iter([1,2,3,4,55])
# print obj
# r1 = next(obj)
# print r1
# r2 = next(obj)
# print r2

# li = [11,22,33,44,55,66,77,88,101,11,101.5]
# print max(li)
# print min(li)

# i = pow(2,10)
# print i

l1 = [1,2,3,4]
l2 = ["q","w","e","r"]
z = zip(l1,l2)
print(z)