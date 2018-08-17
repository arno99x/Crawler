############在一个进程下开启多个线程与在一个进程下开启多个子进程的区别##############

#####开启速度，主进程下开启线程速度较快。
# from threading import Thread
# from multiprocessing import Process
# import os
#
# def work():
#     print('hello')
#
# if __name__ == '__main__':
#     #在主进程下开启线程
#     t=Thread(target=work)
#     t.start()
#     print('主进程-->线程')
#     '''
#     打印结果:
#     hello
#     主进程-->线程
#     '''
#
#     #在主进程下开启子进程
#     t=Process(target=work)
#     t.start()
#     print('主进程-->子进程')
#     '''
#     打印结果:
#     主进程-->子进程
#     hello
#     '''


#####在主进程下开启多个线程,每个线程都跟主进程的pid一样，开多个进程,每个进程都有不同的pid

# from threading import Thread
# from multiprocessing import Process
# import os
#
# def work():
#     print('hello',os.getpid())
#
# if __name__ == '__main__':
#     #part1:在主进程下开启多个线程,每个线程都跟主进程的pid一样
#     t1=Thread(target=work)
#     t2=Thread(target=work)
#     t1.start()
#     t2.start()
#     print('主进程-->线程pid',os.getpid())
#
#     #part2:开多个进程,每个进程都有不同的pid
#     p1=Process(target=work)
#     p2=Process(target=work)
#     p1.start()
#     p2.start()
#     print('主进程-->子进程pid',os.getpid())


#####三个任务，一个接收用户输入，一个将用户输入的内容格式化成大写，一个将格式化后的结果存入文件
from threading import Thread
msg_l=[]
format_l=[]
def talk():
    while True:
        msg=input('>>: ').strip()
        if not msg:continue
        msg_l.append(msg)

def format_msg():
    while True:
        if msg_l:
            res=msg_l.pop()
            format_l.append(res.upper())

def save():
    while True:
        if format_l:
            with open('db.txt','a',encoding='utf-8') as f:
                res=format_l.pop()
                f.write('%s\n' %res)

if __name__ == '__main__':
    t1=Thread(target=talk)
    t2=Thread(target=format_msg)
    t3=Thread(target=save)
    t1.start()
    t2.start()
    t3.start()
