from multiprocessing import Process,Pool
import os
from multiprocessing import pool
import time

def run_proc(name):
    print("第%s进程开始%s"%(name,os.getpid()))
    # while True:
    #     print("子进程启动%s"%os.getpid
    time.sleep(3)
    print("第%s进程结束%s"%(name,os.getpid()))
def run_proc1(name):
    print("第%s子子进程启动%s"%(name,os.getpid()))
    # while True:
    #     print("第二进程启动%s"%os.getpid())
    #     time.sleep(1)
    time.sleep(3)
    print("第%s子子进程结束%s"%(name,os.getpid()))

if __name__ =='__main__':
    # p = Process(target=run_proc)
    # p1 = Process(target=run_proc1)
    # p.start()
    # p1.start()
    # p.join()
    # while True:
    #     print('父进程启动%s'%os.getpid())
    #     time.sleep(1)
    #
    print("父进程开始")
    p = Pool(4)
    for i in range(1,7):
        if i%2 ==0:
            p.apply_async(run_proc,args=(i,))
        else:
            p.apply_async(run_proc1,args=(i,))
    p.close()
    p.join()
    print("父进程结束")