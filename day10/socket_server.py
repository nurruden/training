#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9999, ))
sk.listen(5)    #等等队列最多5个
#接收客户端请求
# print('before')
#conn,表示连接,address表示客户端地址

while True:
    conn,address = sk.accept()   #accept阻塞
    #setblocking,是否阻塞
    conn.sendall(bytes('Welcome',encoding='utf-8'))
    #sendall一次不能发完,就进行循环,继续发送,直至发送完
    while True:
        ret_bytes = conn.recv(1024)
        ret_str = str(ret_bytes,encoding='utf-8')
        if ret_str == 'q':
            break
        conn.sendall(bytes(ret_str+" cool",encoding='utf-8'))
    print(address,conn)
# print('after')
