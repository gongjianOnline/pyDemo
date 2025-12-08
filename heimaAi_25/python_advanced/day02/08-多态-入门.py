"""
多态介绍:
    概述
        多态指的是同一个事务在不同场景下表现出的不同形态,状态
        python 中的多态指的是,同一个函数,传入不同的对象,会实现不同的结果
    多态的前提条件
        1. 要有继承关系
        2. 要有方法重写
        3. 要有父类引用指向子类对象
    好处
        提高代码的可维护性, 实现 1 个函数 多种效果
    应用场景:
        父类型充当函数形参的类型,这样可以接受其任意子类的对象,实现:传入什么(子类)对象,就调用其对应的功能
"""

# 案例 动物类案例
class Animal:
    def __init__(self):
        self.skill = ""
    def speak(self):
        print("叫")

class Dog(Animal):
    def __init__(self):
        self.skill=""
    def speak(self):
        print("王")

class Cat(Animal):
    def __init__(self):
        self.skill=""
    def speak(self):
        print("秒 ")


def make_noise(an:Animal):
    an.speak()



if __name__ == '__main__':
    d = Dog()
    c = Cat()
    make_noise(d)
