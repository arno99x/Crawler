##########信号量Semahpore###########

# Semaphore管理一个内置的计数器，
# 每当调用acquire()时内置计数器-1；
# 调用release() 时内置计数器+1；
# 计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
#
# 实例：(同时只有5个线程可以获得semaphore,即可以限制最大连接数为5)：
import threading
import time

semaphore = threading.Semaphore(5)

def func():
    if semaphore.acquire():
        print (threading.currentThread().getName() + ' get semaphore')
        time.sleep(2)
        semaphore.release()

for i in range(20):
    t1 = threading.Thread(target=func)
    t1.start()
