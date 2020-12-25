# -*- encoding : utf-8 -*-
"""
@File       : getWindow.py
@Time       :2020/12/25 9:39
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : 获取所有的句柄
"""
import win32gui


hwnd_title = {}


def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd) and
        win32gui.IsWindowEnabled(hwnd) and
            win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)


def print_hwnd():
    for h, t in hwnd_title.items():
        if t:
            print(h, t)
            if t == 'Notepad++ update':
                left, top, right, bottom = win32gui.GetWindowRect(h)
                print(left, top, right, bottom)


# parent为父窗口句柄id
def get_child_windows(parent):
    """
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     """
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    return hwndChildList


def getTitle_class(hwnd):
    # 获取标题
    title = win32gui.GetWindowText(hwnd)

    # 获取类名
    clsname = win32gui.GetClassName(hwnd)

    return title, clsname


# 根据句柄将窗口放在最前
def set_front(hwnd):
    win32gui.SetForegroundWindow(hwnd)


print_hwnd()
