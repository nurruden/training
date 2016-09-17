#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import socket
def handle_request(client):
    buf = client.recv(1024)
    client.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n","utf8"))
    f = open('abc','r')
    data = f.read()
    f.close
    # client.sendall(bytes("<h1 style='color:green'>Hello, World</h1>","utf8"))
    client.sendall(bytes(data, "utf8"))
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8082))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':

    main()