class User:
    def __init__(self, name):
        self.name = name


    def __eq__(self, other):
        if isinstance(other, User):
            return self.name.lower() == other.name.lower()

        return False


# checking the correctness of the work program
first_user = User("OLEKSII")
second_user = User("Oleksii")
print(first_user == second_user)
