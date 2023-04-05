# recursive factorial n
def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)


n = int(input("Please enter a positive number: "))
print(f"Factorial of {n} is {recursive_factorial(n)}.")
