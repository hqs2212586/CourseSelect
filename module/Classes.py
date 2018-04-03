# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


class Classes:
    """班级类"""
    def __init__(self,school_name, name, course, class_time, student_path):
        self.school_name = school_name  # 学校
        self.name = name   # 班级
        self.course = course  # 课程  python/go/linux
        self.class_time = class_time
        self.student_path = student_path  # 班级路径, ../student_info/python_s9
        self.teacher = None  # 一班一个老师
        self.student = []
