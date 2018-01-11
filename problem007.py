def primeSieve(n):
    """Uses the Sieve of Erastothenes to find the first n primes."""
    primes = []
    i = 2
    while len(primes) < n:
        isPrime = True
        for p in primes:
            if i%p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        i += 1
    return primes

def nthPrime(n):
    """Computes the nth prime."""
    primes = primeSieve(n)
    return primes[-1]

print(nthPrime(10001)) # 104743
