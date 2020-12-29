# -*- encoding : utf-8 -*-
"""
@File       : factory.py
@Time       :2020/12/29 14:50
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from abc import abstractmethod


class product:

    def __init__(self, price, name):
        self.price = price
        self.name = name

    @abstractmethod
    def sell(self):
        print("这是父类")


class clothes(product):
    def __init__(self):
        super(product).__init__()

    def sell(self):
        print("这是{}卖出了{}元".format(self.name, self.price))

