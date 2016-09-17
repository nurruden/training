#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9999,))
sk.listen(5)

while True:
    conn,access = sk.accept()
    conn.sendall(bytes("Welcome",encoding='utf-8'))
    file_size = str(conn.recv(1024),encoding='utf-8')
    conn.sendall(bytes("Received",encoding='utf-8'))

    total_size = int(file_size)
    has_recv = 0
    f = open('new.jpg','wb')
    while True:
        if total_size ==has_recv:
            break
        data = conn.recv(1024)
        f.write(data)
        has_recv += len(data)

    f.close()