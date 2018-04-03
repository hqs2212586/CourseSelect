# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


def sys_init():
    """初始化学校和课程"""
    from module.Course import Course
    from module.School import School
    from core.MyPickle import MyPickle
    from conf import settings
    school_pickle = MyPickle(settings.SCHOOL_INFO)
    python = Course('python', '6 month', 19800, '北京校区')
    linux = Course('linux', '5 month', 12800, '北京校区')
    go = Course('go', '4 month', 9800, '上海校区')

    beijing = School('北京校区', [linux, python])
    shanghai = School('上海校区', [go])
    school_pickle.dump(beijing)
    school_pickle.dump(shanghai)

    course_pickle = MyPickle(settings.course_obj)
    course_pickle.dump(python)
    course_pickle.dump(linux)
    course_pickle.dump(go)