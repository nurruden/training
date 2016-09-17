#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import socket


ip_port = ('127.0.0.1',8009)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data = sk.recv(1024)
    print('receive:',data)
    inp = input('please input:')
    sk.sendall(bytes(inp,encoding='utf-8'))
    if inp == 'exit':
        break

sk.close()
