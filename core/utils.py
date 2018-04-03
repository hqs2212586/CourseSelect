# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


def print_warning(msg):
    # print("\033[33;1m%s\033[0m" % msg)
    print("\033[33;1mWarning:\033[0m%s" % msg)  # 黄色


def print_error(msg):
    print("\033[31;1mError:\033[0m%s" % msg)   # 红色
