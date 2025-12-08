"""
 单继承:类只能继承自另外的1个类,从中继承过来 属性和行为
 故事1: 一个摊煎饼的老师傅,在煎饼果子界摸爬滚打多年，研发了一套精湛的摊煎技术,要报这套技术传授给他的唯一最得意的弟子
"""

class Master(object):
    def __init__(self):
        self.kongfu = "古法技术"
    def make_cake(self):
        print("摊煎饼")

class Prenice(Master):
    pass

if __name__ == "__main__":
    p = Prenice()
    p.make_cake()
    print(p.kongfu)