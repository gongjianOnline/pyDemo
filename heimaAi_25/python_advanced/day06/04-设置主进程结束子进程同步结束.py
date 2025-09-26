"""
案例: 演示 主进程执行完毕后, 子进程会被同步关闭

当 主进程结束的时候 如果想让 子进程同步结束,方式如下:
    方式一: 设置子进程为 守护进程（推荐）
        格式:
            子进程名.daemon = True
        特点:
            当非守护进程关闭的时候,他的守护进程也会被同步关闭
    方式二: "强制"销毁子进程
        格式: 进程变量.terminate()
        可能会出现问题,子进程会变成"僵尸进程",即资源不会被释放,而是交给 init 进程来维护管理,在合适的时机释放资源
            子进程 => main进程 (main进程关闭后,内部的正在执行的子进程会变成僵尸进程,僵尸进程会交给 main 管理)
            僵尸进程 => init进程
"""
import multiprocessing
import time


# 需求: 创建 1 个子进程,执行完大概需要 2 秒. 而主进程执行需要1秒,实现该需求,观察结果

def work():
    for i in range(100):
        print(f"work {i} ...")
        time.sleep(1)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=work)
    # 方式1：设置子进程为守护进程，当非守护进程（main）结束的时候，守护进程会同步结束
    # p1.daemon = True
    p1.start()
    time.sleep(2)
    # 方式2：销毁子进程
    p1.terminate()

