from threading import Thread
import time

def task(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} complete")
    
if __name__ == "__main__":
    start_time = time.time()
    p1= Thread(target = task, args = ("thread",)) # 2 second delay
    p2 = Thread(target = task, args = ("thread",)) # 3 second delay
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    end_time= time.time()
    
    print("All Thread done")
    print(f"Elapsed time: {end_time-start_time}")
    
    
    