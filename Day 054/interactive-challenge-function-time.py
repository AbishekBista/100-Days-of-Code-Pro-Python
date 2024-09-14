import time


def calculate_time(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Function took {time_taken} seconds")
    
    return wrapper_function

@calculate_time
def count_to_10000():
    for i in range(10000):
        print(i)

count_to_10000()