#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEV_DB_DIR = os.path.join(BASE_DIR,"db","dev")
NEW_BUG_DB = os.path.join(BASE_DIR,"db","bug","new")
ASSIGN_BUG_DB = os.path.join(BASE_DIR,"db","bug","assign")
REOPEN_BUG_DB= os.path.join(BASE_DIR,"db","bug","reopen")
RESOLVED_BUG_DB = os.path.join(BASE_DIR,"db","bug","resolved")
CLOSED_BUG_DB = os.path.join(BASE_DIR,"db","bug","closed")
TESTER_DB_DIR = os.path.join(BASE_DIR,"db","tester")
BASE_ADMIN_DIR = os.path.join(BASE_DIR,"db","admin")
