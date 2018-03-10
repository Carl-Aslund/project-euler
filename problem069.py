from primeGen import getPrimes

if __name__ == "__main__":
    result = 1
    primes = getPrimes(200)
    i = 0
    limit = 10**6

    while result*primes[i] < limit:
        result *= primes[i]
        i += 1
    
    print(result) # 510510
