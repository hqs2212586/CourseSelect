# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from module import Manager


class Teacher:
    menu = [
        ('查看自己的班级', 'show_classes'),
        ('查看新成绩/查看班级详情', 'show_classes_member'),
        ('修改成绩', 'change_score'),
        ('退出', 'exit')
    ]

    def __init__(self, name):
        self.name = name    # 名字
        self.class_list = []

        self.Manager = Manager.Manager('admin')

    def show_classes(self):
        self.Manager.show_classes()

    def show_classes_member(self):
        self.Manager.show_class_stu()

    def change_score(self):  # 修改的是../student_info/python_s1
        self.Manager.change_score()


    def exit(self):
        exit()