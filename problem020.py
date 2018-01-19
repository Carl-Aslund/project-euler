from math import factorial

def factorialDigitSum(n):
    """Returns the sum of the digits of n!"""
    return sum([int(x) for x in str(factorial(n))])

print(factorialDigitSum(100)) # 648
