# -*- encoding : utf-8 -*-
"""
@File       : serversocket_demo.py
@Time       :2020/12/24 17:42
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import socketserver


class MyHandle(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote {}".format(self.client_address[0], str(self.data)))
        self.request.sendall(self.data.upper())


if __name__ == '__main__':
    addr = ('127.0.0.1', 9999)
    server = socketserver.ThreadingTCPServer(addr, MyHandle)
    server.serve_forever()
