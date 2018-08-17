###########线程的join与setdaemon##############


####与进程的方法都是类似的，其实是multiprocessing模仿threading的接口

# from threading import Thread
# import time
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     t=Thread(target=sayhi,args=('h',))
#     t.setDaemon(True)
#     t.start()
#     t.join()
#     print('主线程')
#     print(t.is_alive())



# Thread实例对象的方法
# # isAlive(): 返回线程是否活动的。
# # getName(): 返回线程名。
# # setName(): 设置线程名。
#
# threading模块提供的一些方法：
# # threading.currentThread(): 返回当前的线程变量。
# # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
from threading import Thread
import threading

def work():
    import time
    time.sleep(3)
    print(threading.current_thread().getName())


if __name__ == '__main__':
    #在主进程下开启线程
    t=Thread(target=work)
    t.start()

    print(threading.current_thread().getName())
    print(threading.current_thread()) #主线程
    print(threading.enumerate()) #连同主线程在内有两个运行的线程
    print(threading.active_count())
    print('主线程/主进程')
