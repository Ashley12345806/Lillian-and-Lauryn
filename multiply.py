def multiply(a, b):
    return 1


def multiply(a, b):
    return a * b

#or
def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    return result if b >= 0 else -result