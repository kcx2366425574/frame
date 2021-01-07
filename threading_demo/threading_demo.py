# -*- encoding : utf-8 -*-
"""
@File       : threading_demo.py
@Time       :2021/1/4 15:34
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import threading


class threading_demo:

    def __init__(self, account):
        self._cond = threading.Condition
        self.account = account
