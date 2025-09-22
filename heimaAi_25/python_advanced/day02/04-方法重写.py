"""
方法重写 解释: (同 JS 原型链)
    概述:
        子类中出现和父亲一模一样的 属性 或者 行为(函数)时,称为:方法重写
    应用场景:
        当子类需要从父类沿袭一些功能,但是功能主体又有子集独有需求的时候,就可以考虑使用方法重写了
    
"""

class Father(object):
    def __init__(self):
        self.gender = "男"
    def walk(self):
        print("抽烟喝酒烫头")

class Son(Father):
    def __init__(self):
        self.gender = "劳资蜀道山"

if __name__ == "__main__":
    s = Son()
    print(s.gender)
    s.walk()