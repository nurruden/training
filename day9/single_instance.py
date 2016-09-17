#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import random
class ConnectionPool:

    __instance = None

    def __init__(self):
        self.ip = '1.1.1.1'
        self.port = 3306
        self.pwd = "121212"
        self.username = "admin"
        self.conn_list = [1,2,3,4,5,6,7,8,9,10]
    @staticmethod
    def get__instance():
        if ConnectionPool.__instance:
            return ConnectionPool.__instance
        else:
            ConnectionPool.__instance = ConnectionPool()
            return ConnectionPool.__instance

    def get_connection(self):

       r = random.randrange(1,11)
       return r


# pool = ConnectionPool()
for i in range(10):
    pool = ConnectionPool.get__instance()
    print("Get data from connection pool")
    conn = pool.get_connection()
    print("What I get is: ",conn)

# obj1 = ConnectionPool.get__instance()
# print(obj1)
#
# obj2 = ConnectionPool.get__instance()
# print(obj2)
#
# obj3 = ConnectionPool.get__instance()
# print(obj3)
#