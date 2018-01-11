from math import sqrt

def primeSieve(n):
    """Uses the Sieve of Erastothenes to find all primes less than n."""
    primes = []
    for i in range(2,n):
        isPrime = True
        root = sqrt(i)
        for p in primes:
            if p > root:
                break
            if i%p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return primes

def sumPrimes(n):
    """Sums all primes under n."""
    primes = primeSieve(n)
    return sum(primes)

print(sumPrimes(2000000)) # 142913828922
