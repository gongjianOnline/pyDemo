"""
多任务介绍:
    概述:
        多任务指的是 多任务的执行方式 按照执行方式不同 分为: 并行和并发
    面试题: 并行和并发的区别
        并发: 多个任务同时请求执行,但是同一瞬间,CPU只能执行 1个任务,于是安排他们交替执行,开起来好像是同时执行的 其实不是
            CPU 在做着高效的切换
        并行: 多个任务同时执行,前提,需要多核CPU

    进程和线程的介绍
        进程： 指的是 可执行程序文件 如 .exe 1个 exe = 1个进程
        线程： 指的是 进程的执行路径，执行的单元
        便于理解：
            车 = 进程 多辆车 = 多进程
            车道 = 线程 单车道 = 单线程
    进程介绍：
        进程指的是（Process） ，他是由 CPU 分配资源的最小单位， 例如 CPU给微信多少等
        多进程的基本工作方式： 1个exe = 1个进程, 程序运行起来形成主进程,在主进程上创建子进程
    多进程实现步骤
        导包
        import multiprocessing
        创建进程对象,关联:要执行的任务
        p1 = multiprocessing.Process()
        开启进程
        p1.start()
"""
# 案例: 使用多进程模拟一边写代码一边听音乐
import time
import multiprocessing

def codeing():
    for i in range(10):
        print(f"写代码...{i}")
        time.sleep(1)

def music():
    for i in range(10):
        print(f"听音乐。。。{i}")
        time.sleep(1)

if __name__ == '__main__':
    # codeing()
    # music()

    p1 = multiprocessing.Process(target=music)
    p2 = multiprocessing.Process(target=codeing)
    p1.start()
    p2.start()