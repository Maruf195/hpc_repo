from multiprocessing import Process
import time

def task(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} complete")
    
if __name__ == "__main__":
    start_time = time.time()
    p1= Process(target = task, args = ("process1",))
    p2 = Process(target = task, args = ("process2",))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    end_time= time.time()
    
    print("All process done")
    print(f"Elapsed time: {end_time-start_time}")
    
    
    