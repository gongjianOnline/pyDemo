"""
    封装解释:
        封装就是隐藏对象的 属性 和 实现细节 , 进对外提供公共的访问方式

    隐藏:
        私有化 __变量/方法名
    公共访问:
        通过提供的对外访问内部成员的接口(方式) 例如 get__xx(),set__xx()
"""

#  故事六: 小明把技术传给徒弟的同时,不想把自己的私房钱继承给徒弟,请用所学,模拟该知识

class Parent:
    def __init__(self):
        self.skill  = "大招"
        self.__money = "2000"

    def getMoney(self):
        return self.__money
    def setMoney(self, money):
        self.__money = money

class Child(Parent):
    def getSkill(self):
        print(Parent().skill)
    def getMoney(self):
        print(super().getMoney())

if __name__ == '__main__':
    c = Child()
    c.getSkill()
    c.setMoney(100)
    c.getMoney()
