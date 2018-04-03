# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


class Course:
    def __init__(self, course_name, course_period, course_price, school):
        self.course_name = course_name      # 课程名
        self.course_period = course_period  # 课程周期
        self.course_price = course_price    # 课程价格
        self.school = school                # 课程所属的学校

    def __repr__(self):    # 内置方法，改变对象的字符串显示
        return self.course_name
