# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import sys
from conf import settings
from module.Manager import Manager
from module.Student import Student
from module.Teacher import Teacher


def login():
    """
    登录函数，应该读取user_info文件中的信息，对用户名和密码进行查验
    登录成功之后，查看这个人的身份，来确定进入哪一个视图
    :return:
    """
    usr = input('username: ')
    pwd = input('password: ')
    with open(settings.USER_INFO) as f:
        for line in f:
            username, passwd, role = line.strip().split('|')
            if username == usr and passwd == pwd:
                print('\033[1;32m登录成功！\033[0m')
                return {'username': usr, 'role': role}
        else:
            print('\033[1;31m登录失败！\033[0m')


def main():
    """
    打印欢迎信息
    login：得到返回值：用户的姓名和身份
    打印用户身份对应的功能菜单
    用户想要调用任何方法都应该通过角色的对象去调用，跳转到对应对象的方法里
    :return:
    """
    print("\033[1:42m欢迎登录选课系统\033[0m".center(50, '-'))
    ret = login()  # ret = {'username':'eva', 'role':'Manager'}
    if ret:
        role_class = getattr(sys.modules[__name__], ret['role'])  # 根据userinfo文件当中最后一项内容反射对应的角色类
        obj = role_class(ret['username'])
        TAG = True
        while TAG == True:   # 可以实现多次操作
            for i, j in enumerate(role_class.menu, 1):
                print(i, j[0])  # j[0]：menu中元组的第一个元素
            ret = int(input('请输入对应操作的序列号：'))  # 避免数字不合法
            if ret <= 12:
                getattr(obj, role_class.menu[ret-1][1])()  # 得到数字对应的方法名
            elif ret == 13:
                TAG = False
                getattr(obj, role_class.menu[ret - 1][1])()
            else:
                print("你输入的内容有误！")
