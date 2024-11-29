from multiprocessing import Process
import time

def task(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} complete")
    
if __name__ == "__main__":
    start_time = time.time()
    # Create Process
    p = [Process(target=task, args=(f"Process-{i}",)) for i in range(3)]
    # Start Process
    for t in p:
        t.start()
    # Wait for process to complete
    for t in p:
        t.join()
        
    end_time = time.time()
    print("All process done")
    print(f"Elapsed time: {end_time-start_time}")
    
    
    