from threading import Thread,Condition
import time

# create condition veriable
condition = Condition()

# download thread activites

def download_file():
    print("File downloading...")
    time.sleep(3)  # 3 second delay for downloading file
    print("File downloaded!")
    
    with condition:
        condition.notify()  # notify after file is downloded


def process_file():
    with condition:
        condition.wait()  # wait untill file is downloded
    print("Processing file...")

# Main Thread
def main():
    download_thread = Thread(target=download_file)
    process_thread =  Thread(target=process_file)
    
    download_thread.start() 
    process_thread.start() 
    
    download_thread.join()
    process_thread.join()
    
    print("All tasks are complete.")


if __name__ == "__main__":
    main()
