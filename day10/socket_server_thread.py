#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall(bytes('Welcome to call 10086，please input 1xxx to customer service.',encoding='utf-8'))
        Flag = True
        while Flag:
            data_bytes = conn.recv(1024)
            data = str(data_bytes,encoding='utf-8')
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall(bytes('This communication will be recorded',encoding='utf-8'))
            else:
                conn.sendall(bytes('Please re-input.',encoding='utf-8'))


if __name__ == '__main__':
    #socket+select+多线程
    #IP端口,类名
    #Myserver==>RequestHandlerClass
    #obj = self.RequestHandlerClass
    #obj.handle()
    #ThreadingTCPServer.init =>TCPServer.init()
    #1.server对象
    #   self.server_address            ('127.0.0.1',8009)
    #   self.RequestHandlerClass       (MyServer)
    #   self.socket                     创建服务端socket对象
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    # 1.server对象的server_forever()
    server.serve_forever()

