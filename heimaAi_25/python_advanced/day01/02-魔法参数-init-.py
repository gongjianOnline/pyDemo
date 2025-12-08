"""
魔法方法注释
    概述:
        在 python 中,有一类方法是用来 对 python 类的功能做 加强()扩展的,且这一来方法都无需手动调用
        在满足特定情况的场景下,会被自动调用,他们就称为: 魔法函数
    格式:
        __魔法方法名__()  注意,这里是两个下划线
    常用的魔法方法:
        __init__() 用于初始化对象的属性值的,在创建对象的时候,会被:自动调用
        __str__() 用于快速打印对象的各个属性值,在输出语句打印对象的时候会自动调用
        __del__() 当删除对象的时候,或者 main 函数执行完毕后,会自动调用

"""

# class Car:
#     def __init__(self):
#         self.color= "黑色"
#         self.number = 3
#
# if __name__ == '__main__':
#     c1 = Car()
#     print(c1.color)
#     print(c1.number)

# init 传参
class Car:
    def __init__(self,color,number):
        self.color = color
        self.number = number
    def __str__(self):
        return f"{self.color} {self.number}"
    def __del__(self):
        print(f"{self}被释放了")
if __name__ == '__main__':
    car = Car('red',10)
    print(car.color)
    print(car.number)
    print(car)



