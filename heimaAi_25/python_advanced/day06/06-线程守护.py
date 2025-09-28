"""
细节:(执行逻辑和进程一致)
    主线程会等待所有子线程执行结束在结束
    守护主线程就是主线程退出子线程销毁不在执行
    格式:
        方式一:(推荐)
            threading.Thread(target=函数名,daemon=True)
        方式二:(废弃)
            线程对象.setDaemon(True)

"""
import threading,time

def work():
    for i in range(10):
        print(f"worker {i}")
        time.sleep(1)

if __name__ == "__main__":
    p1 = threading.Thread(target=work,daemon=True)
    p1.start()
    time.sleep(2)
    print("主进程执行结束")