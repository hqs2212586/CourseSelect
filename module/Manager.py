# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import os
import time
from conf import settings
from core.MyPickle import MyPickle
from module.Teacher import Teacher
from module.Classes import Classes
from module.Student import Student
from module.Course import Course


class Manager:
    menu = [
        ('创建老师账号', 'create_teacher'), ('查看老师账号', 'show_teacher'),
        ('创建学生账号', 'create_student'), ('查看学校', 'show_school'),
        ('创建课程', 'create_course'), ('查看课程', 'show_course'),
        ('创建班级', 'create_classes'), ('查看班级', 'show_classes'),
        ('查看班级详细信息', 'show_class_stu'),
        ('给班级指定老师', 'bound_class'), ('退出', 'exit')
    ]

    def __init__(self, name):
        self.name = name    # 管理员用户名
        self.teacher_pickle_obj = MyPickle(settings.teacher_obj)  # 拿到对象
        self.course_pickle_obj = MyPickle(settings.course_obj)
        self.school_pickle_obj = MyPickle(settings.SCHOOL_INFO)
        self.class_pickle_obj = MyPickle(settings.classes_obj)

    @staticmethod
    def user_info_handle(content):
        with open(settings.USER_INFO, 'a') as f:
            f.write('\n%s' % content)

    def show(self, pickle_obj):
        pickle_obj = getattr(self, pickle_obj)
        load_g = pickle_obj.loaditer()  # 生成器对象
        for random_obj in load_g:   # 来的什么对象打印什么对象
            for i in random_obj.__dict__:
                print(i, random_obj.__dict__[i])  # 打印key和value
            print(''.center(50,'-'))

    def show_course(self):
        # 打开course文件
        # 将文件中的学科对象读取展示 pickle一次次load/down
        self.show('course_pickle_obj')

    def show_school(self):
        self.show('school_pickle_obj')

    def show_classes(self):
        self.show('class_pickle_obj')

    def show_teacher(self):
        self.show('teacher_pickle_obj')

    def show_class_stu(self):
        self.show_classes()
        class_name = input("请输入要查看的班级名称：")
        student_path = os.path.join(settings.STU_INFO, class_name)  # 拼接出.../student_info/python_s1的路径
        self.student_detail_obj = MyPickle(student_path)
        self.show('student_detail_obj')

    def create_teacher(self):
        # 将讲师的信息写入userinfo文件
        # 输入讲师所在学校  # 三个信息：用户名、身份、学校
        # 实例化一个讲师的对象，存储在讲师对应的文件内
        teacher_name = input("输入新讲师姓名：")
        teacher_passwd = input('输入新讲师密码：')
        teacher_salary = input("输入新讲师工资：")
        self.show_school()  # 显示所有的学校
        school = input("学校：")
        content = '%s|%s|Teacher' % (teacher_name, teacher_passwd)
        Manager.user_info_handle(content)   # 添加进user_info文件
        teacher = Teacher(teacher_name)  # 实例化
        self.teacher_pickle_obj.dump(teacher)   # MyPickle里方法保存信息
        print('老师创建成功！')

    def create_course(self):
        """

        :return:
        """
        course_name = input('新课程名称: ')
        course_price = input('新课程价格：')
        course_period = input('新课程周期：')
        course_school = input("新课程校区：")
        # 创建一个课程对象，dump进course文件
        new_course = Course(course_name, course_period, course_price, course_school)
        self.course_pickle_obj.dump(new_course)
        print('课程创建成功！')

    def create_classes(self):
        # 绑定一个学科对象，要先调用查看学科(showCourse)方法获取学科对象，用户选择学科，再将对象绑定到班级
        # 创建一个属于这个班级的文件用于存储学生信息，将文件的路径存储到班级对象中
        # 创建一个班级对象（名称 学校 学科对象 讲师空列表 学生信息所在文件的路径），dump进classes文件
        print('in create_classes function')
        class_name = input("请输入班级名称：")
        self.show_school()   # 查看学校信息
        school_name = input("请输入学校名称：")
        self.show_course()   # 查看课程信息
        course = input("请输入课程名称：")
        student_path = os.path.join(settings.STU_INFO, class_name)  # 拼接出.../student_info/python_s1的路径
        open(student_path, 'w').close()  # 创建对应班级的文件
        class_time = time.strftime('%Y-%m-%d')
        class_obj = Classes(school_name, class_name, course, class_time, student_path)  # 班级对象
        self.class_pickle_obj.dump(class_obj)

    def create_student(self):
        # 将学生信息写入userinfo文件中
        # 创建一个学生对象(姓名 讲师空列表)
        # 必须要有班级才能创建学生
        print('in create_student function')
        student_name = input("请输入学生姓名：")
        student_pwd = input("请输入学生密码：")
        self.show_school()
        student_school = input("请输入学生所在的学校：")
        self.show_classes()
        student_class = input("请输入学生所在的班级：")
        class_g = self.class_pickle_obj.loaditer()  # 班级生成器
        for class_obj in class_g:       # 班级对象
            if class_obj.name == student_class:     # 符合条件是有效班级
                content = '%s|%s|Student' % (student_name, student_pwd)
                Manager.user_info_handle(content)       # 添加进user_info文件
                """学生对象信息存入../student_info/python_s1班级文件中"""
                stu_obj = Student(student_name, student_school, class_obj)  # 实例化学生对象
                MyPickle(class_obj.student_path).dump(stu_obj)  # 实例化学生的路径,学生信息存入../student_info/python_s1
                print('学生创建成功!')
                """给class_obj中对应班级添加学生姓名"""
                class_obj.student.append(student_name)
                self.class_pickle_obj.edit(class_obj)
                print("班级中添加学生成功")
                break
        else:
            print('您输入的内容有误，创建学生失败！')

    def change_score(self):
        print('in change_student_score function')
        self.show_classes()
        class_name = input("请输入要修改学生所在班级：")
        student_name = input("请输入要修改学生姓名：")
        student_score = input("请输入学生新成绩：")
        student_path = os.path.join(settings.STU_INFO, class_name)
        self.student_detail_obj = MyPickle(student_path)
        self.show('student_detail_obj')
        class_g = self.student_detail_obj.loaditer()
        for student_obj in class_g:
            if student_obj.name == student_name:
                student_obj.score = student_score
                self.student_detail_obj.edit(student_obj)

    def bound_class(self):   # 为班级去指定老师
        # 管理员选择为老师还是学生指定班级
        # 如果是为老师绑定班级：
        # 找到指定的老师和对应的班级（都是通过show方法查看之后选择）
        # 给讲师对象的班级属性的列表中加入一个新的项 ，值为班级的对象
        # 给班级对象中的讲师属性列表加入一个新的项，值为讲师的对象
        # 如果为学生绑定班级
        # 找到指定的学生和对应的班级（都是通过show方法查看之后选择）
        # 给学生创建新的班级属性，将属性的值设置为班级对象
        # 将学生对象的信息 根据班级对象中存储的学生信息存储路径 dump入对应文件
        print('in boundClass function')
        self.show_classes()
        class_name = input('请输入要绑定的班级：')
        self.show_teacher()
        teacher_name = input('请输入要指定的老师：')
        """老师对象class属性添加班级名"""
        teach_g = self.teacher_pickle_obj.loaditer()
        for teacher_obj in teach_g:
            if teacher_obj.name == teacher_name:
                teacher_obj.class_list.append(class_name)
                self.teacher_pickle_obj.edit(teacher_obj)
                print('老师信息绑定班级成功')
        """class_obj里的老师信息修改为老师姓名"""
        class_g = self.class_pickle_obj.loaditer()
        for class_obj in class_g:
            if class_obj.name == class_name:
                class_obj.teacher = teacher_name
                self.class_pickle_obj.edit(class_obj)
                print("班级信息已添加老师")
                return

    def exit(self):
        exit()

# 首先以管理员的身份登录
# 登录后就应该实例化一个对应身份的对象 manage_obj = Manager(name)
