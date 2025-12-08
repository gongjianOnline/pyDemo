"""
property 关键字介绍
    概述: 是用来修饰 函数的 目的是 简化代码开发
    格式:
        1. property 充当 装饰器的用法
            @property  修饰的是 获取值的方法 即 get_xxx 方法
            @方法名.setter 修饰的是 设置值的方法 即 set_xxx 方法,这里的方法名指的是: @property 修饰的方法名
        2. property 充当 类变量
            类变量名 = property(获取值的方法，设置值的方法)
"""
# 需求： 定义学生类，有 1 个私有的属性 name ,对外提供公共的访问方式,让外界访问它
class Student:
    def __init__(self):
        self.__name = ""

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, name):
        self.__name = name

if __name__ == '__main__':

    s = Student()
    s.set_name = "11111"
    print(s.get_name)
