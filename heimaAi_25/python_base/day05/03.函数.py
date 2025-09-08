"""
    python 函数概念：
    格式
    def 函数名(形参1,形参2):
        return
    关键词参数
        格式
            def fun(name,age,sex)
            fun(name="张三",age=18,sex="男")
    省略参数
        格式
            def fun(name,sex,age=18)
            fun("张三","男")
        细节
            省略参数必须放在形参的最后面
    不定长参数：
        *args  只能接收所有的 位置参数，封装到：元组中
        **kwargs 只能接收所有的 关键字参数，封装到：字典中
        格式
            def fun(*args):
                print(args)
            def fun(**kwargs):
                print(kwargs)
        细节
            关于实参,位置参数在前,关键字参数在后
            关于形参,如果两种 可变参数都有,则 *args在前, **kwargs在后
            关于形参,如果既有 缺省参数 又有不定长参数 则编写顺序为: *args,缺省参数,**kwargs
"""
# a = 66
# def fun1():
#     print(a)
#
# def fun2():
#     a = 100
#     print(a)
#
# fun1()
# fun2()
# fun1()


# def fun1(*args):
#     print(args)
#
# fun1("男")
#
# def fun2(**kwargs):
#     print(kwargs)
# fun2(name="男")

def get_sum(*args):
    print(*args)
    sum1 = 0
    for item in args:
        sum1+=item
    return sum1

print(get_sum(1,2,3))