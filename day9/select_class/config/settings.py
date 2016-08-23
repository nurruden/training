#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEACHER_DB_DIR = os.path.join(BASE_DIR,"db","teacher_list")
COURSE_DB_DIR = os.path.join(BASE_DIR,"db","course_list")
STUDENT_DB_DIR = os.path.join(BASE_DIR,"db","student")
BASE_ADMIN_DIR = os.path.join(BASE_DIR,"db","admin")