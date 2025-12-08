"""
获取进程编号
细节:
    1. 1个进程拥有一个唯一的 进程id 当该进程被关闭的时候 进程 id 会同步释放,即:进程id是可以重复使用的
    2. 知道了进程id 就可以锁定到唯一的进程 方便我们管理和维护,以及梳理 子进程 和 父进程之间的关系
    3. 获取当前进程的id 有两种方式
        方式1: os 模块的 getpid() 函数
        方式2: multiprocessing.current_process().pid 模块的 pid 属性
    4. 获取当前进程的父id , 方式如下
        os 模块的 getppid() 函数
"""

# 案例: 使用多进程模拟小明一遍写num行代码 一边听 count首音乐功能实现
import multiprocessing
import time
import os


def codeing(name, num):
    print("codeing的pid",os.getpid(),"父进程",os.getppid())
    for i in range(num):
        print(f"{name} 正在写第 {i} 行代码")
        time.sleep(1)

def music(name,num):
    print("music的pid", multiprocessing.current_process().pid,"父进程",os.getppid())
    for i in range(num):
        print(f"{name} 正在听第 {i} 首歌")
        time.sleep(1)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=codeing,name="xiaoming",args=("xiaoming",10))
    p2 = multiprocessing.Process(target=music,name="xiaomi",kwargs={"name":"xiaomi","num":10})
    print(p1.name,p2.name)
    p1.start()
    p2.start()


