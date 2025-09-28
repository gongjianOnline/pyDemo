"""
生成器介绍:
    概述:
        生成器就是用来生成数据的,用一个 生成1个 这样可以节省大量的内存空间
    大白话解释:
        生成器的推导式写法,类似于列表\集合\字典推导式,只不过换成小括号而已
    实现方式:
        推导式写法
        yield 关键字
    如何从生成器中获取到数据
        next() 函数
        便利生成器
    细节:
        只要 def 函数中看到了 yield 关键字,就是生成器
        yield 关键字作用:临时存储所有的数据,并放到生成器中,函数调用时会返回一个生成器对象
"""

def get_generator():
    for i in range(1,6):
        yield i

if __name__ == '__main__':
    list = get_generator()
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))


