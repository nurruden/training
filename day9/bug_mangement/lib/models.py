#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import time
import pickle
import os
import random
from config import settings

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

class Dev:
    def __init__(self):
        self.username = None
        self.password = None
        self.new_bug = []
        self.reopen_bug = []
        self.closed_bug = []
        self.resolved_bug = []

    def login(self,user,pwd):
        if self.username == user and self.password == pwd:
            return True
        else:
            return False
    def register(self,user,pwd):
        self.username = user
        self.password = pwd
        path = os.path.join(settings.DEV_DB_DIR,self.username )
        pickle.dump(self,open(path,'xb'))


class Tester:
    def __init__(self):
        self.username = None
        self.password = None
        self.new_bug = []
        self.reopen_bug = []
        self.closed_bug = []
        self.resolved_bug = []

    def login(self,user,pwd):
        if self.username == user and self.password == pwd:
            return True
        else:
            return False
    def register(self,user,pwd):
        self.username = user
        self.password = pwd
        path = os.path.join(settings.TESTER_DB_DIR,self.username )
        pickle.dump(self,open(path,'xb'))
class Bug:
    def __init__(self,bug_name,bug_des,bug_level,tester_obj,dev_obj,status,comment):
        self.name = bug_name
        self.bug_des = bug_des
        self.bug_level = bug_level
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_tester = tester_obj
        self.dev = dev_obj
        self.status = "new"
        self.comment = None
