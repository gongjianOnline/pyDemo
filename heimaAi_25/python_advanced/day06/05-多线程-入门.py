"""
多线程实现步骤(步骤和参数和进程一致)
    1. 导包
        import threading
    2. 创建线程对象,关键函数
        t1 = threading.Thread(target=目标函数)
    3. 开启线程
        t1.start()
    参数说明：
        target： 目标函数
        name：线程名称
        args：元组参数
        kwargs：map参数
"""

# 需求: 使用多线程模拟-遍写代码,一边投影云月

import threading
def codeing():
    for i in range(10):
        print("正在写代码")

def music():
    for i in range(10):
        print("正在听音乐")

if __name__ == '__main__':
    p1 = threading.Thread(target=codeing)
    p2 = threading.Thread(target=music)
    p1.start()
    p2.start()