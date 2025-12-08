"""
进程涉及到的参数如下:
    target  关联的是 当前进程要执行的函数
    name 设置当前进程的名字
    args 以元组的形式 给 当前进程关联的函数传参
    kwargs 以字典的形式 给当前进程关联的函数传参
细节:
    1. args 方式传参, 实参的个数和数据类型\顺序 必须和 进程关联的函数形参列表一致
    2. kwargs 方式传参, 实参的个数 和 数据类型 必须和 进程关联的函数的形参列表一致, 顺序无所谓
"""

# 案例: 使用多进程模拟小明一遍写num行代码 一边听 count首音乐功能实现
import multiprocessing
import time


def codeing(name, num):
    for i in range(num):
        print(f"{name} 正在写第 {i} 行代码")
        time.sleep(1)

def music(name,num):
    for i in range(num):
        print(f"{name} 正在听第 {i} 首歌")
        time.sleep(1)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=codeing,name="xiaoming",args=("xiaoming",10))
    p2 = multiprocessing.Process(target=music,name="xiaomi",kwargs={"name":"xiaomi","num":10})
    print(p1.name,p2.name)
    p1.start()
    p2.start()


