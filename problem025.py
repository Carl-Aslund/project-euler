
def fibonacciDigitIndex(n):
    """Returns the index of the first fibonacci number with n digits."""
    a = 1
    b = 1
    index = 2
    while len(str(a)) < n:
        a, b = a+b, a
        index += 1
    return index

print(fibonacciDigitIndex(1000)) # 4782
