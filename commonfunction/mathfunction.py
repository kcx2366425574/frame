# -*- encoding : utf-8 -*-
"""
@File       : mathfunction.py
@Time       :2020/12/21 14:39
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
