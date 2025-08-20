print("1111");

# num = int(input("input"));
# if num < 10 :
#     print("啥玩意")
# elif num < 11 :
#     print("啥玩意2")
# else:
#     print("啥玩意3")

#
# items = [1,2,3,4,5,6,7]
# print(items[0:3])

# t1 = (35, 12, 98)
# print(t1[::3])   # ('骆昊', 43)
# print(t1 <= (35, 12, 90))

# def testFun (num) :
#     return num
#
# print(testFun(1))

class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


t = Triangle(3, 4, 5)
print(f'是不是三角形: {t.is_valid(1,3,3)}')
print(f'周长: {t.perimeter}')
print(f'面积: {t.area}')