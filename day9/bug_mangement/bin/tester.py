#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import pickle
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib import models
from config import settings

def login(user,pwd):
    if os.path.exists(os.path.join(settings.TESTER_DB_DIR,user)):
       tester_obj =  pickle.load(open(os.path.join(settings.TESTER_DB_DIR,user),'rb'))

       dev_obj = None
       if tester_obj.login(user,pwd):
          print("登录成功")
          while True:
                sel = input("1.创建Bug(q退出)\n2.查看Bug\n")
                if str(sel).upper() == "Q":
                    break
                elif sel == "1":
                    new_bug(tester_obj,dev_obj)
                elif sel == "2":
                    bug_obj = pickle.load(open(settings.NEW_BUG_DB,'rb'))
                    bug_info(bug_obj)
                else:
                    break
       else:
           print("密码错误")
    else:
        print("不存在该用户")
def register(user,pwd):
    obj = models.Tester()
    obj.register(user,pwd)
def new_bug(tester_obj,dev_obj):
    new_bug_list = []
    bug_name = input("BUG名称(q退出):")
    bug_des = input("BUG描述:")
    bug_level = input("BUG级别:")
    status = "new"
    bug_comment = input("Bug 评论:")
    bug_obj = models.Bug(bug_name,bug_des,bug_level,tester_obj,dev_obj,status,bug_comment)
    new_bug_list.append(bug_obj)
    if os.path.exists(settings.NEW_BUG_DB):
        exist_list = pickle.load(open(settings.NEW_BUG_DB,'rb'))
        new_bug_list.extend(exist_list)

    pickle.dump(new_bug_list,open(settings.NEW_BUG_DB,'w+b'))
def bug_info(bug_obj):
    for i,item in enumerate(bug_obj):
        if item.dev == None:
            print(' Bug NO: %s\n'%(str(i+1)), 'Bug名称: %s\n'%(item.name),'Bug状态: %s\n'%(item.status),'Bug描述: %s\n'%(item.bug_des),'Bug级别: %s\n'%(item.bug_level),'Bug创建人: %s\n'%(item.create_tester.username),'Bug分配情况: 未分配\n')
def main():
    inp = input("1.Tester注册\n2.Tester登录\n>>>")
    user = input("用户名:")
    pwd = input("密码:")
    if inp == "2":
        login(user,pwd)
    elif inp == "1":
        register(user,pwd)

if __name__ == "__main__":
    main()
