"""
    闭包:
        概念及原理和JS一直
    区别:
        nonlocal 关键字介绍
            它是1个关键字,可以实现 让内部函数 去修改 外边函数的变量值
    回顾:
        global 声明变量为全局变量
        nonlocal 声明变量可以被内部函数修改

"""
def fn_outer():
    a = 100
    def fn_inner():
        nonlocal a # 闭包关键字
        a = a + 1
        print(a)
    return fn_inner

if __name__ == "__main__":
    fn = fn_outer()
    fn()
    fn()