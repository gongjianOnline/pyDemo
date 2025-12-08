"""
装饰器介绍:
    概述
        装饰器 =  闭包函数 即装饰器是闭包函数的一种写法
    目的作用:
        在不改变原有函数的基础上,对原有函数功能做 增强
    前提条件:
        1. 有嵌套
        2. 有引用
        3. 有返回
        4. 有额外功能
    装饰器的用法:
        写法1: 传统写法
            变量名 = 装饰器名(要被装饰的原函数名)
            变量名() # 执行的就是 装饰后的 原函数
        写法2: 语法糖
            在定义原函数的时候,加上@装饰器名即可,之后就正常调用 改原函数即可
"""

def check_login(call_back):
    def inner():
        print("登录中,,,登录完成")
        call_back()
    return inner

@check_login
def commit():
    print("评论成功")



if __name__ == "__main__":
    # checkLogin(commit)

    # 方式一
    # check_login(commit)()
    # 方式二
    commit()