
#############开启线程的两种方式（同Process）####################

###方法1

# from threading import Thread
# import time
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     t1=Thread(target=sayhi,args=('hh',))
#     t1.start()
#
#     t2=Thread(target=sayhi,args=('dd',))
#     t2.start()
#     print('主线程')


###方法2
from threading import Thread
import time
class Sayhi(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)


if __name__ == '__main__':
    t = Sayhi('hh')
    t.start()
    print('主线程')
