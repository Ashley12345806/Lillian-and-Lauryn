def factorial(n):
    if n < 0:
        raise ValueError("Factorial doesnot support negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)