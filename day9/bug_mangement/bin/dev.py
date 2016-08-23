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
    if os.path.exists(os.path.join(settings.DEV_DB_DIR,user)):
       dev_obj =  pickle.load(open(os.path.join(settings.DEV_DB_DIR,user),'rb'))
       bug_obj = pickle.load(open(settings.NEW_BUG_DB,'rb'))
       assign_bug_obj = pickle.load(open(settings.ASSIGN_BUG_DB,'rb'))
       if dev_obj.login(user,pwd):
          print("登录成功")
          print("下列为未分配的bug:")
          check_new_bug(bug_obj)
          print("下列为已分配的bug:")
          check_assign_bug(assign_bug_obj)
       else:
           print("密码错误")
    else:
        print("不存在该用户")
def register(user,pwd):
    obj = models.Dev()
    obj.register(user,pwd)

def check_new_bug(bug_obj):
    for num,new_bug_item in enumerate(bug_obj):
        print(' Bug NO: %s\n'%(str(num+1)),'Bug名称: %s\n'%(new_bug_item.name),'Bug分配给: %s\n'%(new_bug_item.dev),'Bug描述: %s\n'%(new_bug_item.bug_des),'Bug级别: %s\n'%(new_bug_item.bug_level),'Bug分配情况: %s\n'%(new_bug_item.status),'Bug评论: %s\n'%(new_bug_item.comment))
def check_assign_bug(assign_bug_obj):
    for i,item in enumerate(assign_bug_obj):
        print(' Bug NO: %s\n'%(str(i+1)),'Bug名称: %s\n'%(item.name),'Bug分配给: %s\n'%(item.dev),'Bug描述: %s\n'%(item.bug_des),'Bug级别: %s\n'%(item.bug_level),'Bug分配情况: %s\n'%(item.status),'Bug创建人: %s\n'%(item.create_tester.username),'Bug评论: %s\n'%(item.comment))



def main():
    inp = input("1.Dev注册\n2.Dev登录\n>>>")
    user = input("用户名:")
    pwd = input("密码:")
    if inp == "2":
        login(user,pwd)
    elif inp == "1":
        register(user,pwd)

if __name__ == "__main__":
    main()

# assign = pickle.load(open(settings.ASSIGN_BUG_DB,'rb'))
# print(assign)
