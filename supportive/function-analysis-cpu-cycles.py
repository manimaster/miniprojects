# cpu_cycle_counter.py

import psutil

def measure_cpu_cycles(func, *args, **kwargs):
    """
    Measure the CPU cycles used by a given function.

    Args:
        func: The function to be measured.
        args: Positional arguments to pass to the function.
        kwargs: Keyword arguments to pass to the function.

    Returns:
        The approximate CPU cycles used by the function.
    """
    start_cpu_cycles = psutil.cpu_times().user
    func(*args, **kwargs)  # Call the provided function
    end_cpu_cycles = psutil.cpu_times().user
    cpu_cycles_used = end_cpu_cycles - start_cpu_cycles
    return cpu_cycles_used


# main_script.py

# from cpu_cycle_counter import measure_cpu_cycles

# Define the function you want to measure (e.g., a simple loop)
def my_function():
    # Replace this with your actual function code
    total = 0
    for i in range(1, 1000001):
        total += i

if __name__ == "__main__":
    cpu_cycles_used = measure_cpu_cycles(my_function)
    print(f"Function used approximately {cpu_cycles_used} CPU cycles")
