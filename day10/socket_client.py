#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import socket
obj = socket.socket()
obj.connect(('127.0.0.1',9999,))
#最多接收1024字节
print("waiting")
result = obj.recv(1024)
print("Get feedback from server!")
ret_str = str(result,encoding='utf-8')
print(ret_str)
while True:
    inp = input("Please input the detail: ")
    if inp =='q':

        obj.sendall(bytes(inp,encoding='utf-8'))
        break
    else:
        obj.sendall(bytes(inp,encoding='utf-8'))
        ret = str(obj.recv(1024),encoding='utf-8')
        print(ret)
obj.close()

# obj.sendall(bytes(inp,encoding='utf-8'))