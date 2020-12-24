# -*- encoding : utf-8 -*-
"""
@File       : chatserver.py
@Time       :2020/12/23 17:33
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import json
import socket
import time
from tkinter.scrolledtext import ScrolledText
import threading
import requests
import tkinter
from socket import *
from tkinter import *

global Text_Show


def AI_Talk(s):
    print(s)
    response = requests.post("http://www.tuling123.com/openapi/api", data={
        "key": "4105cb6db8c54f5db470b6c0ee42d24b",
        "info": s})
    response = response.json()
    answer = response['text']
    return answer
    # 线程二函数，用来进行对话


def Sever_Thread(sock, caddr):
    # Text_Show.insert('end', "客户端@" + str(caddr[1]) + "已连接!\n")
    while True:
        # 接收数据
        data = str(sock.recv(1024).decode('UTF-8'))
        data_dict = json.loads(data)
        name = data_dict.get("name")
        message = data_dict.get("message")
        if data_dict.get("message") == "quit":
            Text_Show.insert('end', "{}终止了对话\n".format(name))
            Text_Show.see(tkinter.END)
            break
        else:
            Text_Show.insert('end', "{}：{}\n".format(name, message))
            Text_Show.see(tkinter.END)
            # 发送数据
        time.sleep(0.2)
        data = AI_Talk(data)  #
        # data = '请输入发送至客户端的数据: 123123' #如果要手动输入的话就要设置好线程sleep时间不然还没有输入，就已经到其他线程了，就会发不出去。
        sock.sendall(bytes(data, 'UTF-8'))
    sock.close()  # 线程一函数，监听端口，一旦有客户端接入，开启线程二


def Sever_Accept(ss):
    while True:
        sock, caddr = ss.accept()
        Thread2 = threading.Thread(target=Sever_Thread, args=(sock, caddr))
        Thread2.daemon = True  # 线程守护
        Thread2.start()


# 服务器初始化
def Sever_Init():
    HOST = ''
    PORT = 4700
    ADDR = (HOST, PORT)
    ss = socket(AF_INET, SOCK_STREAM, 0)
    ss.bind(ADDR)
    ss.listen(20)  # 允许最大监听数
    Thread1 = threading.Thread(target=Sever_Accept, args=(ss,))
    Thread1.daemon = True  # 线程守护
    Thread1.start()


# 主函数
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("聊天小程序服务器端 ")
    frame1 = Frame(root)
    frame1.pack()
    IP_Show_Label = Label(frame1)
    IP_Show_Label.pack(side='left')
    frame2 = Frame(root)
    frame2.pack()
    Text_Show = ScrolledText(frame2, width=100, height=30)
    Text_Show.bind("<KeyPress>", lambda e: "break")
    Text_Show.pack(side="bottom", fill='both', expand=True)
    Sever_Init()
    root.mainloop()
