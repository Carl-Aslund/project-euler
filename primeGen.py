
def readPrimes():
    return

def writePrimes(n, primes=[]):
    """Write all primes up to n to a text file."""
    if primes==[]:
        primes.append(2)
    for i in range(primes[-1], n+1):
        isPrime = True
        for p in primes:
            if i%p==0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    file = open('primeList.txt', 'w')
    file.write("[")
    for p in primes:
        file.write(str(p)+",")
    file.write("]")
    file.close()

writePrimes(1000)
