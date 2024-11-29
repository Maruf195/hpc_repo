from multiprocessing import Barrier, Process
import time

# Barrier for 3 processes
barrier = Barrier(3)

def task(name):
    print(f"{name} is starting...")
    time.sleep(2)  # Simulate work
    print(f"{name} reached the barrier.")
    barrier.wait()  # Wait for all processes to reach the barrier
    print(f"{name} is continuing after the barrier.")

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    # Create processes
    processes = [Process(target=task, args=(f"Process-{i}",)) for i in range(3)]

    # Start processes
    for p in processes:
        p.start()

    # Wait for processes to complete
    for p in processes:
        p.join()

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    print("All processes have passed the barrier.")
    print(f"Total elapsed time: {elapsed_time:.2f} seconds")
