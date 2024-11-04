import time
from threading import Thread


def do_work():
    print("Starting work")
    
    
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work")
    print(i)


start_time = time.time()
for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()
end_time = time.time()

print("Elapsed time: ", end_time-start_time)

    
