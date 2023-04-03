# n in fibonacci sequence
def fibonacci_numbers(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)


n = int(input("Please enter a positive number: "))
print(f"The {n}th number in the Fibonacci sequence is {fibonacci_numbers(n)}.")
