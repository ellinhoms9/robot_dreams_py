import time


def my_decorator(func):
    def wraper(*args, **kwargs):
        start_time = time.asctime()
        func(*args, **kwargs)
        with open("func_time.txt", "w") as file:
            file.write(f"The function {func.__name__} was called at {start_time}")
    return wraper


# an example of program execution
@my_decorator
def add_numbers(a, b):
    return a + b


add_numbers(1, 2)
with open("func_time.txt", "r") as file:
    print(file.read())
