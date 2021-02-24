# -*- encoding : utf-8 -*-
"""
@File       : sina.py
@Time       :2021/1/12 17:11
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("www.sina.com", 80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
print(data)
s.close()
