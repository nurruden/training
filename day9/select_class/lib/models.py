#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import time
import pickle
import os
import random
from config import settings
class Teacher:
    def __init__(self,name,age,admin):
        self.name = name
        self.age = age
        self.__asset = 0
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin

    def gain(self,cost):

        self.__asset += cost

    def decrease(self,cost):

        self.__asset -= cost
class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def login(self,user,pwd):

        if self.username == user and self.password == pwd:
            return True
        else:
            return False

    def register(self,user,pwd):
        self.username = user
        self.password = pwd

        path = os.path.join(settings.BASE_ADMIN_DIR,self.username)
        pickle.dump(self,open(path,'xb'))

class Course:

    def __init__(self,course_name,cost,teacher_obj,admin):
        self.course_name = course_name
        self.cost = cost
        self.teacher = teacher_obj
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin

    def have_lesson(self):
        self.teacher.gain(self.cost)
        content = random.randrange(10,100)

class Student:
    def __init__(self):
        self.username = None
        self.password = None
        self.course_list = []
        self.study_dict = {}

    def select_course(self,course_obj):
        self.course_list.append(course_obj)

    def study(self,course_obj):
        class_result = course_obj.have_lesson()
        if class_result in self.study_dict.keys():
            self.study_dict[course_obj].append(class_result)
        else:
            self.study_dict[course_obj] = [class_result,]

    def login(self,user,pwd):
        if self.username == user and self.password == pwd:
            return True
        else:
            return False
    def register(self,user,pwd):
        self.username = user
        self.password = pwd
        path = os.path.join(settings.STUDENT_DB_DIR,self.username )
        pickle.dump(self,open(path,'xb'))
