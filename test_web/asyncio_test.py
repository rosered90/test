# _*_ coding:utf-8 _*_
from threading import Thread
import threading
from multiprocessing import Process
import os

def work():
    import time
    time.sleep(10)
    print(threading.current_thread().getName())
    print('子线程结束')


if __name__ == '__main__':
    #在主进程下开启线程
    t=Thread(target=work)
    t.start()

    print(threading.current_thread().getName())
    print(threading.current_thread()) #主线程
    print(threading.enumerate()) #连同主线程在内有两个运行的线程
    print(threading.active_count())
    print('主线程/主进程')
