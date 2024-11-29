from threading import Thread
import threading


# here I create a conditon variable
condition = threading.Condition()



#Functiion for the first thread

def thread_one():
    print("Thread one started")
    
    # Simulate some work
    condition.acquire() # Acquire the lock
    print("Thread one completed")
    condition.notify() # Notify the second thread
    condition.release() # Release the lock
    
    
# funcition for the second thread  
def thread_two():
    
    condition.acquire()
    print("Thread two waiting for Thread thread one to complete...")
    condition.wait() # wait for the thread one's signal
    print("Thread two started after thread one completed")
    condition.release()
    

# Main function to start threads

def main():
    t1 = Thread(target=thread_one)
    t2 = Thread(target=thread_two)
    
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("All tasks completed.")
    
if __name__ == "__main__":
    main()    


