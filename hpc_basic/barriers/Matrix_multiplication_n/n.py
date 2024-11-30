from threading import Thread, Barrier
import numpy as np

# Barrier to synchronize threads
num_threads = 4
barrier = Barrier(num_threads)

# Function for multiplying a segment of the matrix
def multiply_segment(start_row, end_row, A, B, result):
    print(f"Thread processing rows {start_row} to {end_row} started...")
    for i in range(start_row, end_row):
        for j in range(len(B[0])):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

    print(f"Thread processing rows {start_row} to {end_row} finished.")
    barrier.wait()  # Wait for all threads to complete their work

if __name__ == "__main__":
    # Example matrices
    n = 4
    A = np.random.randint(1, 10, (n, n))  # n*n random matrix
    B = np.random.randint(1, 10, (n, n))  # n*n random matrix

    # Result matrix
    result = np.zeros((n, n), dtype=int)

    # Print input matrices
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    # Define thread work division
    threads = []
    rows_per_thread = n // num_threads

    for i in range(num_threads):
        start_row = i * rows_per_thread
        end_row = (i + 1) * rows_per_thread if i != num_threads - 1 else n
        t = Thread(target=multiply_segment, args=(start_row, end_row, A, B, result))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Print result matrix
    print("\nResultant Matrix (A x B):")
    print(result)
