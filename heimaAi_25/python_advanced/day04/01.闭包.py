

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