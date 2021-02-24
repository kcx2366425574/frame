# -*- encoding : utf-8 -*-
"""
@File       : seek_and_hide.py
@Time       :2021/2/23 10:59
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import threading

lock = threading.Lock()


def seek(cond, name):
    cond.acquire()
    print("{}:我已经把眼睛蒙好了".format(name))
    cond.wait()
    print("{}:好的，我来找你了".format(name))
    cond.notify()
    cond.release()


def hide(cond, name):
    cond.acquire()
    print("{}:已经藏好了，来找我吧！".format(name))
    cond.notify()
    cond.wait()
    print("{}:居然被你找到了".format(name))
    cond.release()


if __name__ == '__main__':
    cond = threading.Condition()
    t1 = threading.Thread(target=seek, args=(cond, "seeker"))
    t2 = threading.Thread(target=hide, args=(cond, "hider"))

    t1.start()
    t2.start()

