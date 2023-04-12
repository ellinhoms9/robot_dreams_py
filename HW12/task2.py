class MyManager:
    def __enter__(self):
        print("==========")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == ValueError:
            print(f"Error. Please input an integer. {exc_type}")
        print("========")
        return exc_tb


with MyManager() as my_manager:
    number = int(input("Please enter a number "))
    print(number)
