# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将系统目录添加到环境变量
sys.path.append(BASE_DIR)

from core import main


if __name__ == '__main__':

    # from bin.sys_init import sys_init
    # sys_init()

    main.main()