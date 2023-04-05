# recursive print from n to 0
def recursive_print(n):
    print(n, end=" ")
    if n == 0:
        return None
    return recursive_print(n-1)


n = int(input("Please enter a positive number: "))
recursive_print(n)
