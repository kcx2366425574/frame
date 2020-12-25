# -*- encoding : utf-8 -*-
"""
@File       : click_hwnd.py
@Time       :2020/12/25 10:29
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import pyautogui
import win32gui
import win32con
import win32api
import time

wdname = '云上协同'  # 窗口名
handle = win32gui.FindWindow(0, wdname)  # 窗口句柄


def doClick(cx, cy):  # 点击坐标
    # long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
    # win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
    # win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起
    # 鼠标定位到(30,50)
    win32api.SetCursorPos([cx, cy])
    # 执行左单键击，若需要双击则延时几毫秒再点击一次即可
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # 右键单击
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


if handle == 0:
    print("没有获取到{}窗口".format(wdname))
    exit(0)
else:
    # 获取指定窗口所在位置的坐标
    left, top, right, bot = win32gui.GetWindowRect(handle)
    print(left, top, right, bot)
    time.sleep(5)
    doClick(left+30, top+250)


