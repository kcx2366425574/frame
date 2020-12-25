# -*- encoding : utf-8 -*-
"""
@File       : client_demo.py
@Time       :2020/12/24 18:49
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import socket

client = socket.socket()
client.connect(('127.0.0.1', 9999))

while True:
    msg = input(">>>").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8"))
    # 这里是字节1k
    data = client.recv(1024)
    print("recv:>", data.decode())

client.close()
