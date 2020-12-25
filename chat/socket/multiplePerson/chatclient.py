# -*- encoding : utf-8 -*-
"""
@File       : chatclient.py
@Time       :2020/12/24 13:48
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import socket
import threading

global name


def recv(sock, addr):
    """
    一个UDP连接在接收消息前必须要让系统知道所占端口
    也就是需要send一次，否则win下会报错
    :param socket:
    :param addr:
    :return:
    """
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


def send(sock, addr):
    """
    发送数据的方法
    :param sock: 定义一个实例化socket对象
    :param addr: 传递的服务器IP和端口
    :return:
    """
    while True:
        string = input("")
        if string.lower() == 'exit':
            break
        message = "{}:{}".format(name, string).encode('utf-8')
        sock.sendto(message, addr)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ('127.0.0.1', 9999)
    tr = threading.Thread(target=recv, args=(s, server), daemon=True)
    ts = threading.Thread(target=send, args=(s, server))
    tr.start()
    ts.start()
    ts.join()
    s.close()


if __name__ == '__main__':
    print("-----------欢迎来到聊天室，退出时请输入'exit'(不区分大小写)-------")
    name = input('请输入你的名称:')
    print("--------------------{}--------------".format(name))
    main()
