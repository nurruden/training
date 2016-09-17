#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import pickle
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib import models
from config import settings
def create_course(admin_obj):
    teacher_list = pickle.load(open(settings.TEACHER_DB_DIR,'rb'))
    for num,item in enumerate(teacher_list,1):
        print(num,item.name,item.age,item.create_time,item.create_admin.username)
    course_list=[]
    while True:

        name = input('请输入课程名称(q退出):')
        if name == 'q':
            break
        cost = input('请输入课时费:')
        num = input('请选择老师:')
        obj = models.Course(name,cost,teacher_list[int(num)-1],admin_obj)
        course_list.append(obj)
    if os.path.exists("course_list"):
        exist_list = pickle.load(settings.COURSE_DB_DIR,'rb')
        course_list.append(exist_list)
    pickle.dump(course_list,open(settings.COURSE_DB_DIR,'wb'))

def create_teacher(admin_obj):
    teacher_list = []
    while True:
        name = input("请输入老师姓名:(q for quit)")
        if name == "q":
            break
        age = input("请输入老师年龄:")

        teacher_obj = models.Teacher(name,age,admin_obj)
        teacher_list.append(teacher_obj)
    if os.path.exists(settings.TEACHER_DB_DIR):
        exist_list = pickle.load(open(settings.TEACHER_DB_DIR,'rb'))
        teacher_list.extend(exist_list)
    pickle.dump(teacher_list,open(settings.TEACHER_DB_DIR,'w+b'))


def login(user,pwd):
    if os.path.exists(os.path.join(settings.BASE_ADMIN_DIR,user)):
        admin_obj = pickle.load(open(os.path.join(settings.BASE_ADMIN_DIR,user),'rb'))
        if admin_obj.login(user,pwd):
            print("登录成功")
            while True:
                sel = input("1.创建老师\n2.创建课程\n")
                if sel == "1":
                    create_teacher(admin_obj)
                elif sel == "2":
                    create_course(admin_obj)
                else:
                    break
        else:
            return 1
    else:
        return 0

def register(user,pwd):
    admin_obj = models.Admin()
    admin_obj.register(user,pwd)

def  main():
    inp = input("1.管理员登录:\n2.管理员注册:\n>>>")
    user = input('请输入用户名:')
    pwd = input('请输入密码:')

    if inp == '1':
        ret = login(user,pwd)
        if ret == 1:
            print("密码错误")
        elif ret == 0:
            print("用户不存在")
    elif inp =='2':
        register(user,pwd)

if __name__ == "__main__":
    main()
# print(os.path.dirname(os.path.dirname(__file__)))