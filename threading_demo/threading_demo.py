# -*- encoding : utf-8 -*-
"""
@File       : threading_demo.py
@Time       :2021/1/4 15:34
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import threading

account = 0
lock = threading.Lock()


def change_money(n):
    global account
    account += n
    account -= n


def run_thread(n):
    for i in range(10000):
        change_money(n)


def run_thread_withlock(n):
    for i in range(10000):
        lock.acquire()
        try:
            change_money(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread_withlock, args=(5, ))
t2 = threading.Thread(target=run_thread_withlock, args=(8, ))
t3 = threading.Thread(target=run_thread_withlock, args=(9, ))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print(account)
