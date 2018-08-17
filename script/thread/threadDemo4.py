########Python GIL(Global Interpreter Lock)###############


# 全局解释器锁。在Cpython解释器中，同一个进程下开启的多线程，同一时刻只能有一个线程执行，无法利用多核优势。
#
# 首先需要明确的一点是GIL并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念。就好比C++是一套语言（语法）标准，但是可以用不同的编译器来编译成可执行代码。有名的编译器例如GCC，INTEL C++，Visual C++等。Python也一样，同样一段代码可以通过CPython，PyPy，Psyco等不同的Python执行环境来执行。像其中的JPython就没有GIL。然而因为CPython是大部分环境下默认的Python执行环境。所以在很多人的概念里CPython就是Python，也就想当然的把GIL归结为Python语言的缺陷。所以这里要先明确一点：GIL并不是Python的特性，Python完全可以不依赖于GIL
#
# 补充：
# 1. cpu到底是用来做计算的，还是用来做I/O的？
# 1. 多cpu，意味着可以有多个核并行完成计算，所以多核提升的是计算性能
# 2. 每个cpu一旦遇到I/O阻塞，仍然需要等待，所以多核对I/O操作没什么用处
#
# 一个工人相当于cpu，此时计算相当于工人在干活，I/O阻塞相当于为工人干活提供所需原材料的过程，工人干活的过程中如果没有原材料了，则工人干活的过程需要停止，直到等待原材料的到来。
# 如果你的工厂干的大多数任务都要有准备原材料的过程（I/O密集型），那么你有再多的工人，意义也不大，还不如一个人，在等材料的过程中让工人去干别的活，
# 反过来讲，如果你的工厂原材料都齐全，那当然是工人越多，效率越高
# 结论：
# 　　对计算来说，cpu越多越好，但是对于I/O来说，再多的cpu也没用
#
# 我们有四个任务需要处理，处理方式肯定是要玩出并发的效果，解决方案可以是：
#
# 方案一：开启四个进程
# 方案二：一个进程下，开启四个线程
#
# 单核情况下，分析结果:
# 　　如果四个任务是计算密集型，没有多核来并行计算，方案一徒增了创建进程的开销，方案二胜
# 　　如果四个任务是I/O密集型，方案一创建进程的开销大，且进程的切换速度远不如线程，方案二胜
#
# 多核情况下，分析结果：
# 　　如果四个任务是计算密集型，多核意味着并行计算，在python中一个进程中同一时刻只有一个线程执行用不上多核，方案一胜
# 　　如果四个任务是I/O密集型，再多的核也解决不了I/O问题，方案二胜
#
# 结论：现在的计算机基本上都是多核，python对于计算密集型的任务开多线程的效率并不能带来多大性能上的提升，甚至不如串行(没有大量切换)，但是，对于IO密集型的任务效率还是有显著提升的。


#计算密集型
# from multiprocessing import Process
# import time
# def work():
#     res=0
#     for i in range(1000000):
#         res+=i
#
# if __name__ == '__main__':
#     t_l=[]
#     start_time=time.time()
#     # for i in range(300): #串行
#     #     work()
#
#     for i in range(30):
#         # t=Thread(target=work) #多线程49.64094281196594
#         t=Process(target=work) #多进程11.664679050445557
#         t_l.append(t)
#         t.start()
#
#     for i in t_l:
#         i.join()
#
#     stop_time=time.time()
#     print('run time is %s' %(stop_time-start_time))
#
#     print('主线程')





#I/O密集型
from threading import Thread
import time
import os
def work():
    time.sleep(2) #模拟I/O操作，可以打开一个文件来测试I/O,与sleep是一个效果
    print(os.getpid())

if __name__ == '__main__':
    t_l=[]
    start_time=time.time()
    for i in range(1000):
        t=Thread(target=work) #耗时大概为2秒
        # t=Process(target=work) #耗时大概为25秒,创建进程的开销远高于线程，而且对于I/O密集型，多cpu根本不管用
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()
    stop_time=time.time()
    print('run time is %s' %(stop_time-start_time))
