###CourseSelect（选课系统）
系统允许三类用户（学生、老师、管理员）登录选课平台。
学生可以在选课系统选择学校、课程、交学费。
老师可以在选课系统查看可管理的班级、查看班级内学生、修改学生成绩。
管理员可以创建老师、创建班级、创建课程
###程序运行方法
运行程序必须使用Python3.X版本解释器
下载程序包后，直接运行.../CourseSelect/bin/start.py
###程序结构
.
|____core  
| |______init__.py  
| |____utils.py  
| |____MyPickle.py  
| |____main.py  
|____bin  
| |____sys_init.py  
| |____startup.py  
| |______init__.py  
|____module  
| |____School.py  
| |____Teacher.py  
| |____Course.py  
| |______init__.py  
| |____Student.py  
| |____Classes.py  
| |____Manager.py  
|____README.md  
|____db  
| |____course_obj  
| |____student_info  
| | |____python_s1  
| |______init__.py  
| |____teacher_obj  
| |____school_info  
| |____classes_obj  
| |____user_info  
|____log  
| |______init__.py  
|____UML.png  
|____题目需求  
|____conf  
| |______init__.py  
| |____settings.py  
