#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import socket
import select
sk1 = socket.socket()
sk1.bind(('127.0.0.1',8001, ))
sk1.listen()

sk2 = socket.socket()
sk2.bind(('127.0.0.1',8002, ))
sk2.listen(5)

sk3 = socket.socket()
sk3.bind(('127.0.0.1',8003, ))
sk3.listen(5)

inputs = [sk1]

while True:
    #[sk1,sk2],select内部sk1,sk2两个对象,一旦某个句柄发生变化
    #如果有人连sk1,r_list = [sk1]
    #1代表等1秒
    #谁发生变化,放在第一个参数里,谁发生错误了,放在第三个参数里,第二个参数传了什么,原封不动的交给w_list
    r_list,w_list,e_list = select.select(inputs,[],inputs,1)
    print('正在监听的socket对象%d' %len(inputs))
    print(r_list)
    for sk_or_conn in r_list:
        #每一个连接对象
        if sk_or_conn == sk1:
            #表示有新用户连接
            conn,address = sk_or_conn.accept()
            inputs.append(conn)
        else:
            #老用户发消息
            try:
                data_byte = sk_or_conn.recv(1024)

            except Exception as e:
                print(e)
                inputs.remove(sk_or_conn)
            else:
                data_str = str(data_byte, encoding='utf-8')
                sk_or_conn.sendall(bytes(data_str + ' good', encoding='utf-8'))