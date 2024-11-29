from threading import Thread
import time

def task(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} complete")
    
if __name__ == "__main__":
    start_time = time.time()
    
    # Create threads
    threads = [Thread(target=task, args=(f"Thread-{i}",)) for i in range(3)]
    # Start threads
    for t in threads:
        t.start()
    # Wait for threads to complete
    for t in threads:
        t.join()
    
    end_time= time.time()
    
    print("All Thread done")
    print(f"Elapsed time: {end_time-start_time}")
    
    
    