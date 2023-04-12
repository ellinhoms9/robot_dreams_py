import time


# my decorator
def func_and_time(func):
    def wraper(*args, **kwargs):
        start_time = time.asctime()
        func(*args, **kwargs)
        print(f"The function {func.__name__} was called at {start_time}")
    return wraper


# an example of program execution
@func_and_time
def sum_two_numbers(a, b):
    return a + b


sum_two_numbers(1, 2)
