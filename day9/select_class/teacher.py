#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import pickle
import os
class teacher:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.__asset = 0

    def gain(self,cost):

        self.__asset += cost

    def decrease(self,cost):

        self.__asset -= cost


class course:

    def __init__(self,name,course_cost,course_time,teacher):
        self.name = name
        self.course_cost = course_cost
        self.course_time = course_time

def admin_login():
    print("Welcome to admin system,Please Select:\n")
    init_select = input("1.Register\n"
          "2.Login\n")
    try:
        assert init_select != "1" or "2"
    except Exception as e:
        print("illeagal input, please re-input")


    if init_select == "2":
        username = input("Username:")
        password = input("Password:")
        data = {username:password}
        with open('data.pkl','rb') as r:
            info = pickle.load(r,encoding='utf-8')
            # print(data,type(data))
            # print(info,type(info))
            if data == info:
                print("Welcome to administration system")
                # show_teacher_course()
            else:
                print("Wrong info, please re-intput username and password")

def create_teacher():
    teacher_list = []
    while True:
        name = input("Please input teacher's name:(q for quit)")
        if name == "q":
            break
        age = input("Please input teacher's age:")
        gender = input("Please input teacher's gender:")
        teacher_obj = teacher(name,age,gender)
        teacher_list.append(teacher_obj)
    if os.path.exists("teacher_list"):
        exist_list = pickle.load(open('teacher_list','rb'))
        teacher_list.extend(exist_list)
    pickle.dump(teacher_list,open('teacher_list','w+b'))

def create_course():
    course_list = []
    teacher_list = pickle.load(open('teacher_list','rb'))
    for num,item in enumerate(teacher_list,1):
        print(num,item.name,item.age,item.gender)
    while True:
        name = input("Please input course name::(q for quit)")
        if name == "q":
            break
        cost = input("Please input course cost:")
        time = input("Please input course time:")
        num = input("Please select teacher's number:")
        course_obj = course(name,cost,time,teacher_list[int(num)-1])
        course_list.append(course_obj)
    if os.path.exists("course_list"):
        exist_list = pickle.load(open('course_list','rb'))
        course_list.extend(exist_list)
    pickle.dump(course_list,open('course_list','w+b'))

def show_teacher_course():
    homedir = os.getcwd()
    filename = homedir + '/teacher_list'
    if os.path.exists(filename):
        with open("teacher_list",'rb') as f:
            info = pickle.load(f,encoding='utf-8')
            print(info)
    else:
        print("bucunzai")



