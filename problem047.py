from primeGen import getPrimes

def countFactors(n, primes):
    """Count the number of distinct prime factors of n."""
    count = 0
    primeFound = True
    for i in range(len(primes)):
        if primes[i]**2 > n:
            return count + 1
        primeFound = False
        while n % primes[i] == 0:
            primeFound = True
            n = n // primes[i]
        if primeFound:
            count += 1
        if n == 1:
            return count

if __name__ == "__main__":
    primes = getPrimes(1000000)
    streak = 0
    resultFound = False
    for i in range(1000000):
        if countFactors(i, primes) > 3:
            streak += 1
            if streak == 4:
                print(i-3) # 134043
                resultFound = True
                break
        else:
            streak = 0
    if not resultFound:
        print("Insufficient primes given.")
