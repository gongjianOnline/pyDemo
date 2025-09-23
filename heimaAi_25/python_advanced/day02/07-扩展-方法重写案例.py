# 需求: 定义手机类,有打电话的功能,定义新式手机类,继承手机类,重写 打电话的行为

class Phone():
    def __init__(self):
        self.content = "手机"
    def call(self):
        print("打电话")

class Phone2(Phone):
    def __init__(self):
        self .content="新手机"


if __name__ == '__main__':
    phone2 = Phone2()
    phone2.call()

