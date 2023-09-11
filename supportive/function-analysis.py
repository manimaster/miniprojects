# function_timer.py

import time

def measure_time(func):
    """
    Measure the running time of a given function.

    Args:
        func: The function to be measured.

    Returns:
        The running time of the function in seconds.
    """
    start_time = time.time()
    func()  # Call the provided function
    end_time = time.time()
    running_time = end_time - start_time
    return running_time


# main_script.py

# from function_timer import measure_time

# Define the function you want to measure
def my_function():
    # Replace this with your actual function code
    total = 0
    for i in range(1, 1000001):
        total += i

# Measure the running time of the function
if __name__ == "__main__":
    running_time = measure_time(my_function)
    print(f"Function ran in {running_time:.4f} seconds")
