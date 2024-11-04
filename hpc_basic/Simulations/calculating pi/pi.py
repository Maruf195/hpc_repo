import random
from time import time
from multiprocessing import Process,Array
from threading import Thread

'''

n=10000000
i=0
start_time =time()
for _ in range(n):
    x= random.uniform(-1,1)
    y= random.uniform(-1,1)
    r= x**2 + y**2
    # print(f'x:{x}, y:{y}, r: {r} ')
    if (x**2+y**2) <=1:
        i+=1
pi = 4 * i/n
end_time = time()
print('pi: %10.5f, i:%10d, n: %10d '%(pi,i,n))
print('The elapsed time not using any processing:%.5f' %(end_time-start_time))


'''

'''

##############################################################################################
#                           Use  Process                                                       #
##############################################################################################





# Function to estimate pi in a separate process
def estimate_pi_part(num_points, result, index):
    inside = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)  # Generate random x coordinate
        y = random.uniform(-1, 1)  # Generate random y coordinate
        
        if x**2 + y**2 <= 1:  # Check if the point is inside the circle
            inside += 1
    result[index] = inside  # Store the count of points inside the circle in the shared array

if __name__ == '__main__':
    n = 10000000  # Total number of points
    num_processes = 4  # Number of processes
    points_per_process = n // num_processes  # Points per process

    # Shared array to hold results from each process
    result = Array('i', num_processes)
    

    processes = []
    
    start_time = time()

    # Start each process
    for i in range(num_processes):
        p = Process(target=estimate_pi_part, args=(points_per_process, result, i))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()
    
    # Sum all the inside counts from all processes
    total_inside = sum(result)

    # Calculate the value of pi
    pi = 4 * total_inside / n
    
    end_time = time()
    
    print('pi: %10.5f, inside count:%10d, total points:%10d' % (pi, total_inside, n))
    print('The elapsed time using process: %.5f seconds' % (end_time - start_time))




'''

##############################################################################################
#                           Use Thread                                                       #
##############################################################################################





# Function to estimate pi in a separate thread
def estimate_pi_part(num_points, inside_count):
    local_inside = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)  # Generate random x coordinate
        y = random.uniform(-1, 1)  # Generate random y coordinate
        if x**2 + y**2 <= 1:  # Check if the point is inside the circle
            local_inside += 1
    return local_inside  # Return the count of points inside the circle for this thread

if __name__ == '__main__':
    n = 10000000  # Total number of points
    num_threads = 4  # Number of threads
    points_per_thread = n // num_threads  # Points per thread

    threads = []
    results = []  # List to hold results from each thread
    
    start_time = time()

    # Start each thread
    for _ in range(num_threads):
        t = Thread(target=lambda: results.append(estimate_pi_part(points_per_thread, results)))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()
    
    # Sum all the inside counts from all threads
    total_inside = sum(results)

    # Calculate the value of pi
    pi = 4 * total_inside / n
    
    end_time = time()
    
    print('pi: %10.5f, inside count:%10d, total points:%10d' % (pi, total_inside, n))
    print('The elapsed time using thread: %.5f seconds' % (end_time - start_time))

