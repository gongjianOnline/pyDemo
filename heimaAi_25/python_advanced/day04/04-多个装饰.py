"""
多个装饰器装饰一个函数,细节如下: (洋葱圈模式/队列模式)
    1. 多个装饰器 装饰1个函数,装饰的顺序是 由内向外的
    2. 但是多个装饰器的执行顺序是,有上往下的
"""

# 需求: 发表评论只,需要 先登录用户.在进行验证码验证,在不改变原有函数基础上,对功能做增强
def check_login(call_back):
    def inner():
        print("登录")
        call_back()
    return inner

def check_code(call_back):
    def inner():
        print("验证")
        call_back()
    return inner

@check_login
@check_code
def commit():
    print("评论")

if __name__ == '__main__':
    commit()