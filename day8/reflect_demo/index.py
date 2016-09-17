#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

from lib import account
# url = input('Please input url:')
# if str(url).endswith("login"):
#     r = account.login()
#     print(r)
# elif str(url).endswith("logout"):
#     r = account.logout()
#     print(r)
# else:
#     print("404")

# url = input("Please input url:")
# inp = str(url).split('/')[-1]
# if hasattr(account,inp):
#     target_func = getattr(account,inp)
#     r = target_func()
#     print(r)
# else:
#     print("404")

url = input("Please input url:")
target_module,target_func = str(url).split('/')
m = __import__("lib." +target_module,fromlist=True)


if hasattr(m,target_func):
    target_func = getattr(m,target_func)
    r = target_func()
    print(r)
else:
    print('404')