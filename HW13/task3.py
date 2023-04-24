import time


class MyCustomException(Exception):
    def __init__(self):
        self.message = "Custom exception is occurred"
        start_time = time.asctime()
        super().__init__(self.message)
        with open("error_time.txt", "w") as file:
            file.write(f"The error {self.message} was called at {start_time}")
