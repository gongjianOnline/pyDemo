"""
背景：
    线程之间数据是共享的，进程之间的数据是隔离的
    如果多线程 并发 操作同一个数据 就有可能会引发安全问题，出现非法值
    可以用 线程同步（加锁）的思路来解决
    格式:
        互斥锁创建
        mutex = threading.Lock()
        上锁
        mutex.acquire()
        释放锁
        mutex.release()
    细节:
        用完之后一定要释放锁,否则可能会造成死锁的情况
"""

# 导包
import threading

mutex = threading.Lock()
# 定义全局变量
g_num = 0
# 定义 get_sum1() 函数,实现对 g_num 全局变量.累加1000次
def get_num1():
    global g_num
    mutex.acquire()
    for i in range(10000000):
        g_num += 1
    mutex.release()
    print(f"get_num1函数,累加后结果为: {g_num}")

def get_num2():
    mutex.acquire()
    global g_num
    for i in range(10000000):
        g_num += 1
    mutex.release()
    print(  f"get_num2,累加后结果为: {g_num}")


if __name__ == '__main__':
    t1 = threading.Thread(target=get_num1)
    t2 = threading.Thread(target=get_num2)
    # 启动线程
    t1.start()
    t2.start()


