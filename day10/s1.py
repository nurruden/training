#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import socketserver

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):

        conn = self.request
        conn.sendall(bytes('Welcome',encoding='utf-8'))
        # self.request,self.client_address,self.server
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes,encoding='utf-8')
            if ret_str == 'q':
                break
            conn.sendall(bytes(ret_str+" cool",encoding='utf-8'))


if __name__ == '__main__':

    server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),Myserver)
    server.serve_forever()