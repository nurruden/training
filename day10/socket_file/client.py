#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import socket
import os
obj = socket.socket()
obj.connect(('127.0.0.1',9999,))
#最多接收1024字节

result = obj.recv(1024)

ret_str = str(result,encoding='utf-8')

print(ret_str)
size = os.stat('f.jpg').st_size
obj.sendall(bytes(str(size),encoding='utf-8'))
obj.recv(1024)

with open('f.jpg','rb') as f:
    for line in f:
        obj.sendall(line)

obj.close()