#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import settings
from lib import models
import pickle


def register(user,pwd):
    admin_obj = models.Admin()
    admin_obj.register(user,pwd)
def login(user,pwd):
    if os.path.exists(os.path.join(settings.BASE_ADMIN_DIR,user)):
        admin_obj = pickle.load(open(os.path.join(settings.BASE_ADMIN_DIR,user),'rb'))
        bug_obj = pickle.load(open(settings.NEW_BUG_DB,'rb'))
        if admin_obj.login(user,pwd):
            print("登录成功")
            print("下列是未分配的bug:")
            check_new_bug(bug_obj)
            while True:
                inp = input("是否现在分配bug给DEV?(Y/N)(Q退出)")
                if str(inp).upper() == "Y":
                    assign_bug_to_dev(bug_obj)
                elif str(inp).upper() == "N":
                    pass
                else:
                    if str(inp).upper() == "Q":
                        break
        else:
            return 1
    else:
        return 0

def check_new_bug(bug_obj):
    for num,new_bug_item in enumerate(bug_obj):
        if new_bug_item.dev == None:
            print(str(num+1),'Bug名称: %s\n'%(new_bug_item.name),' Bug描述: %s\n'%(new_bug_item.bug_des),' Bug级别: %s\n'%(new_bug_item.bug_level),' Bug创建人: %s\n'%(new_bug_item.create_tester.username),' Bug分配状况:未分配')

def assign_bug_to_dev(bug_obj_spec):
    bug_obj_spec = pickle.load(open(settings.NEW_BUG_DB,'rb'))
    for num,new_bug_item in enumerate(bug_obj_spec):
        if new_bug_item.dev == None:
            print(str(num+1),'Bug名称: %s\n'%(new_bug_item.name),' Bug描述: %s\n'%(new_bug_item.bug_des),' Bug级别: %s\n'%(new_bug_item.bug_level),' Bug创建人: %s\n'%(new_bug_item.create_tester.username),' Bug分配状况:未分配')
    bug_num = input("请选择bug NO:")
    assign_bug = bug_obj_spec[int(bug_num)-1]
    del bug_obj_spec[int(bug_num)-1]
    pickle.dump(bug_obj_spec,open(settings.NEW_BUG_DB,'wb'))
    assign_bug_list=[]
    list = os.listdir(settings.DEV_DB_DIR)
    for i,item in enumerate(list):
        print(str(int(i)+1),item)
    dev_num = int(input("请从上面的Dev列表中选择Dev:"))
    dev_obj = pickle.load(open(os.path.join(settings.DEV_DB_DIR,list[dev_num-1]),'rb'))
    assign_bug.dev = dev_obj.username
    assign_bug.status = "assigned"
    assign_bug_list.append(assign_bug)
    if os.path.exists(settings.ASSIGN_BUG_DB):
        exist_list = pickle.load(open(settings.ASSIGN_BUG_DB,'rb'))
        assign_bug_list.extend(exist_list)
    pickle.dump(assign_bug_list,open(settings.ASSIGN_BUG_DB,'w+b'))


def main():
    inp = input("1.管理员登录\n2.管理员注册\n>>>")
    username = input("用户名:")
    password = input("密码:")
    if inp == "1":
        ret =  login(username,password)
        if ret == 1:
            print("密码错误")
        elif ret == 0:
            print("用户名不存在")
    elif inp == "2":
        register(username,password)

if __name__ == "__main__":
    main()
