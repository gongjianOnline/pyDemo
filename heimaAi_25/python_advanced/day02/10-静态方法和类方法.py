"""
类方法 和 静态方法详解:
    概述:
        类方法:
            1. 第一个参数必须是 当前类的对象 , 一般用 cls 当做变量名(即:class)
            2. 类方法必须通过 @classmethod 来修饰
            3. 类方法是属于 类的方法, 能被该类的所有对象共享
            4. 可以通过 类名,或者 对象名 的方式调用,推荐:前者
        静态方法:
            1. 静态方法没有参数的硬性要求
            2. 静态方法必须通过 @staticmethod 来修饰
            3. 静态方法内部的函数体中,访问不到任何类内的共享属性和函数
            4. 可以通过类名,或者 对象名 的方式调用,推荐:前者
"""

class MyClass:
    class_variable = 0
    def __init__(self):
        self.instance_variable = 1

    @classmethod
    def class_method(cls):
        print("class_method",cls.class_variable)

    @staticmethod
    def static_method():
        print("static_method")




if __name__ == '__main__':
    MyClass.static_method()
    obj = MyClass()
    obj.class_method()
    obj.static_method()