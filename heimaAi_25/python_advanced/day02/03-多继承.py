"""
多继承
    格式
        class P1:
        class P2:
        class C1 (P1,P2):
    细节:
        如果一类继承了多个类出现重复的方法和属性,优先继承第一个父类的同名属性和方法,(父类的私有成员除外)
"""


class Master(object):
    def __init__(self):
        self.kongfu = "古法技术"
    def make_cake(self):
        print("摊煎饼")

class Heima(object):
    def __init__(self):
        self.kongfu = "IThiema"
    def make_cake(self):
        print("摊煎饼")

class Prenice(Master,Heima):
    pass

if __name__ == "__main__":
    p = Prenice()
    p.make_cake()
    print(p.kongfu)