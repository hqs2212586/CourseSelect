# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import os
import sys
import logging

# 父级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将系统目录添加到环境变量
sys.path.append(BASE_DIR)

# DB目录及文件
DB_PATH = os.path.join(BASE_DIR, 'db')

USER_INFO = os.path.join(DB_PATH, 'user_info')
SCHOOL_INFO = os.path.join(DB_PATH, 'school_info')
STU_INFO = os.path.join(DB_PATH, 'student_info')

teacher_obj = os.path.join(DB_PATH, 'teacher_obj')
course_obj = os.path.join(DB_PATH, 'course_obj')
classes_obj = os.path.join(DB_PATH, 'classes_obj')

# 日志级别：DEBUG,INFO,WARNING,ERROR,CRITICAL
LOG_LEVEL = logging.INFO

LOG_TYPES = {
    'access': 'access.log',   # 操作日志
    'transaction': 'transactions.log'   # 交易日志（购买课程）
}

LOG_PATH = os.path.join(BASE_DIR, 'log')

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
