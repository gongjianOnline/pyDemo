"""
细节:
    1. 进程之间数据是相互隔离的 不能共享
    2. 子进程相当于父进程的副本,即 把父进程的内容拷贝一遍单独执行,注意 main外资源
    3. 默认情况下 主进程会等待子进程结束后再结束
"""

# 案例: 在不同进程中修改列表 my_list[] 并新增元素,设置在个进程中观察列表的变化
import time
import multiprocessing

my_list = []
def write_data():
    for i in range(10):
        my_list.append(i)
        print(f'add:{i}')
    print(f"写入结果:{my_list}")

def read_data():
    time.sleep(1)
    print(f'读取结果:{my_list}')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)

    p1.start()
    p2.start()