#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import socket
obj = socket.socket()
obj.connect(('127.0.0.1',8001,))
content = str(obj.recv(1024),encoding='utf-8')
print(content)
obj.close()