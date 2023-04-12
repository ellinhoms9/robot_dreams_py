import time


# my decorator with own parameter
def func_and_time(times):
    def wraper(func):
        def inner(*args, **kwargs):
            for i in range(times):
                start_time = time.asctime()
                func(*args, **kwargs)
                print(f"The function {func.__name__} was called at {start_time}")
        return inner
    return wraper


# an example of program execution
@func_and_time(times=6)
def sum_two_numbers(a, b):
    return a + b


sum_two_numbers(1, 2)
