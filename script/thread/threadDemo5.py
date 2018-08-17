###########同步锁################
# import time
# import threading
#
# def addNum():
#     global num #在每个线程中都获取这个全局变量
#     #num-=1
#
#     temp=num
#     time.sleep(0.1)
#     num =temp-1  # 对此公共变量进行-1操作
#
# num = 100  #设定一个共享变量
#
# thread_list = []
#
# for i in range(100):
#     t = threading.Thread(target=addNum)
#     t.start()
#     thread_list.append(t)
#
# for t in thread_list: #等待所有线程执行完毕
#     t.join()
#
# print('Result: ', num)



#####锁通常被用来实现对共享资源的同步访问。为每一个共享资源创建一个Lock对象，当你需要访问该资源时，调用acquire方法来获取锁对象（如果其它线程已经获得了该锁，则当前线程需等待其被释放），待资源访问完后，再调用release方法释放锁：
# import threading
#
# R=threading.Lock()
#
# R.acquire()
# '''
# 对公共数据的操作
# '''
# R.release()

# 补充：
# GIL VS Lock
# Python已经有一个GIL来保证同一时间只能有一个线程来执行了，为什么这里还需要lock?
# 然后，我们可以得出结论：保护不同的数据就应该加不同的锁。
# 最后，问题就很明朗了，GIL 与Lock是两把锁，保护的数据不一样，前者是解释器级别的（当然保护的就是解释器级别的数据，比如垃圾回收的数据），后者是保护用户自己开发的应用程序的数据，很明显GIL不负责这件事，只能用户自定义加锁处理，即Lock


