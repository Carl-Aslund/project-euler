import math

def primeFactorize(num):
    """Finds all prime factors of a number."""
    factors = []
    root = int(math.sqrt(num) + 0.5)
    for i in range(2, root):
        if num%i == 0:
            while num%i == 0:
                num /= i
                factors.append(i)
        if num == 1:
            return factors
    if len(factors) == 0:
        return [num]

def greatestPrime(num):
    return max(primeFactorize(num))

print(greatestPrime(600851475143))
