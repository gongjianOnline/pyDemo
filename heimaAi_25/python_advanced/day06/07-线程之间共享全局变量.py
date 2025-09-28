"""
多线程-线程间共享数据
"""
import threading
# 案例：定义个列表类型的全局变量，创建两个子线程分别执行向全局变量添加数据的任务和想全局变量读取的任务，查看线程之间是否共享全局变量数据

import time

my_list = []
def write_data():
    for item in range(10):
        my_list.append(item)
        time.sleep(0.5)

def read_data():
    print(my_list)

if __name__ == "__main__":
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)
    t1.start()

    time.sleep(3)
    t2.start()




