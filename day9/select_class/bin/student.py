#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import pickle
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib import models
from config import settings
# from lib.models import Course
# from lib.models import Admin
# from lib.models import Teacher
def register(user,pwd):
    obj = models.Student()
    obj.register(user,pwd)

def  select_course(student_obj):
    course_list = pickle.load(open(settings.COURSE_DB_DIR,'rb'))
    for num,item in enumerate(course_list):
        print(num,item.course_name,item.cost,item.teacher.name)
    while True:
        num = input("请选择课程(q退出):")
        if num == "q":
            break
        selected_course_obj = course_list[int(num)-1]
        if selected_course_obj not in student_obj.course_list:
            student_obj.course_list.append(selected_course_obj)
        else:
            print("您已经选了这门课")
    pickle.dump(student_obj,open(os.path.join(settings.STUDENT_DB_DIR,student_obj.username),'wb'))

def course_info(student_obj):
    for item in student_obj.course_list:
        print(item.course_name,item.teacher.name)

def login(user,pwd):
    if os.path.exists(os.path.join(settings.STUDENT_DB_DIR,user)):
       student_obj =  pickle.load(open(os.path.join(settings.STUDENT_DB_DIR,user),'rb'))
       if student_obj.login(user,pwd):
           while True:
               inp = input("1.选课\n2.上课\n3.查看课程信息\n>>>")
               if inp == "1":
                  select_course(student_obj)
               elif inp == "3":
                   course_info(student_obj)
               else:
                   break
       else:
           print("密码错误")
    else:
        print("不存在该用户")

def main():
    inp = input("1. 登录\n2. 注册\n>>>")
    user = input("学生用户名:")
    pwd = input("学生密码:")

    if inp == "1":
        login(user,pwd)
    elif inp == "2":
        register(user,pwd)


if __name__ == "__main__":
    main()

