# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import os
from module import Manager

class Student:
    menu = [
        ('查看班级', 'show_classes'),
        ('退出', 'exit')
    ]
    def __init__(self, name, **kwargs):
        self.name = name
        self.school = kwargs
        self.class_obj = kwargs  # 组合，对象组合到一个属性上
        self.score = 0

        self.Manager = Manager.Manager('alex')

    def show_classes(self):
        self.Manager.show_classes()

    def show_score(self):
        class_name = input("请输入所属的班级名称：")
        student_path = os.path.join(Manager.settings.STU_INFO, class_name)  # 拼接出.../student_info/python_s1的路径
        self.student_detail_obj = Manager.MyPickle(student_path)
        self.show('student_detail_obj')

    def exit(self):
        exit()