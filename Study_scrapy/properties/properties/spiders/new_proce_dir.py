import os,time
from multiprocessing import Pool
from multiprocessing import Process
# kaishi = time.time()
# os.chdir('D:\proc\dira')
# dir_list = os.listdir()
# for i in dir_list:
#     os.remove(i)
# jieshu = time.time()
# shijian = jieshu-kaishi
# print("将文件删除%0.2f"%shijian)

def jincheng():
    while True:
        os.chdir('D:\proc\dira')
        dir_list = os.listdir()
        if len(dir_list)==0:
            break
        else:
            os.remove(dir_list[0])
if __name__ == '__main__':
    kaishi = time.time()
    # p = Pool(4)
    # for i in range(4):
    #     p.apply_async(jincheng)
    # p.close()
    p = Process(target=jincheng)
    p.start()
    p.join()
    jieshu = time.time()
    shijian = jieshu - kaishi
    print("总共用时%0.4f"%shijian)