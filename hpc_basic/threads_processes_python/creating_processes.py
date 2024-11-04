import multiprocessing
import time
from multiprocessing import Process


def do_work():
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work")
    print(i)


if __name__ == '__main__':
    
    multiprocessing.set_start_method('spawn')
    start_time = time.time()
    for _ in range(5):
        p = Process(target=do_work, args=())
        p.start()
    end_time = time.time()
    
    print("Elapsed time: ",end_time-start_time)
