#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
# li = []
# inp = input("Please input:")
#
# # try:
# #     num = int(inp)
# #     print(num)
# # except Exception as e:   #e封装了所有异常信息
# #     print("Please inuput a int")
#
# li[inp]


#捕捉指定的error
# dic = ["wupeiqi", 'alex']
# try:
#     dic[10]
#
# except IndexError as e:
#     print("Index Error")
# except Exception as e:
#     print(e)


# #完整异常代码块
# try:
#     # 主代码块
#     pass
# except KeyError as e:
#     # 异常时，执行该块
#     pass
# else:
#     # 主代码块执行完，执行该块
#     pass
# finally:
#     # 无论异常与否，最终执行该块
#     pass


# try:
#     print("123")
#     raise Exception('error')
# except Exception as e:
#     print(e)

class Foo:
    def __init__(self,arg):
        self.xo = arg

    def __str__(self):
        return self.xo

obj = Foo("asw")
print(obj)