"""
    python 继承
    格式:
        class 子类名(父类名):
            pass
    例如:
        calss A(B):
            pass
    叫法
        类A : 子类,派生类,扩展来
        类B : 父类,基类,超类
    好处:
        提高代码的复用性
    细节:
        所有的类都直接或者间接继承自 Object 类,它是所有类的父类,基类
"""
# 案例 : 定义父类 Father 类,属性:性别=男,行为:散步,定义子类Son,继承父类,创建对象,并调用

class Father(object):
    def __init__(self):
        self.gender = "男"
    def walk(self):
        print("抽烟喝酒烫头")

class Son(Father):
    pass

if __name__ == "__main__":
    s = Son()
    print(s.gender)
    s.walk()