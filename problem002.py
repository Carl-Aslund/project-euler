def sumEvenFibonacci(limit):
    """Computes the sum of all even Fibonacci numbers up to the limit."""
    total = 0
    a = 1
    b = 1
    c = 2
    while (c <= limit):
        total += c
        a = b+c
        b = a+c
        c = a+b
    return total

print(sumEvenFibonacci(4000000)) # 4613732
