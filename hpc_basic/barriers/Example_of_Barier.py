from threading import Barrier, Thread
import time

# Barrier for 3 threads
barrier = Barrier(3)

def task(name):
    print(f"{name} is starting...")
    time.sleep(2)  # Simulating some work
    print(f"{name} reached the barrier.")
    barrier.wait()  # Wait for all threads to reach the barrier
    print(f"{name} is continuing after the barrier.")

if __name__ == "__main__":
    # Create threads
    threads = [Thread(target=task, args=(f"Thread-{i}",)) for i in range(3)]

    # Start threads
    for t in threads:
        t.start()

    # Wait for threads to complete
    for t in threads:
        t.join()

    print("All threads have passed the barrier.")
