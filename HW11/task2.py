class MyCustomException(Exception):
    def __init__(self):
        self.messege = "Custom exception is occurred"
        super().__init__(self.messege)
