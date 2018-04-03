# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import os
import pickle


class MyPickle:
    def __init__(self, filepath):
        self.filepath = filepath   # 记录一个变量在内存中

    def dump(self, obj):        # 存
        with open(self.filepath, 'ab') as f:
            pickle.dump(obj, f)

    def loaditer(self):         # 读
        with open(self.filepath, 'rb') as f:
            # for obj in pickle.load(f):
            #     yield obj
            while True:
                try:
                    obj = pickle.load(f)  # load一个对象操作一次
                    yield obj
                except:
                    break

    def edit(self, obj):        # 修改已经pickle的文件
        f2 = MyPickle(self.filepath + '.bak')
        for item in self.loaditer():
            if item.name == obj.name:
                f2.dump(obj)
            else:
                f2.dump(item)
        os.remove(self.filepath)
        os.rename(self.filepath + '.bak', self.filepath)