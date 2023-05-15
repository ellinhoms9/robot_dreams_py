class MyStr(str):
    def __str__(self):
        return super().__str__().upper()


# checking the correctness of the work program
my_str = MyStr("test")
print(my_str)
