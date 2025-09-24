#无参数有返回值
"""
def check_log(call_back):
    def inner():
        print("登录中")
        call_back()
        return print("登录成功")
    return inner

@check_log
def commit():
    print("评论")


if __name__ == '__main__':
    commit()
"""

# 有参数有返回值
"""
def check_log(call_back):
    def inner(a,b):
        print("登录中")
        call_back(a,b)
        return print("登录成功")
    return inner

@check_log
def commit(a,b):
    print("评论",a+b)

if __name__ == '__main__':
    commit(1,2)
"""

#可变参数
"""
def check_log(call_back):
    def inner(*arg,**kwargs):
        print("登录中")
        call_back(*arg,**kwargs)
        return print("登录成功")
    return inner

@check_log
def commit(*arg,**kwargs):
    print("评论",arg,kwargs)
    arg_sum = 0
    kwargs_sum = 0
    for item in arg:
        arg_sum += item
    for item in kwargs:
        kwargs_sum += kwargs[item]

    print(arg_sum, kwargs_sum)
if __name__ == '__main__':
    commit(1,2,3,a=1,b=2,c=3)
"""



