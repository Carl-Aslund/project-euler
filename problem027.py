
def readPrimes():
    """Reads in a list of primes from primeList.txt"""
    file = open("primeList.txt", "r")
    primes = eval(file.readline())
    return primes

def evalPolynomial(n,a,b):
    """Evaluates n^2 + an + b"""
    return n**2 + a*n + b

def findPrimeGen():
    """Finds the best prime-generating quadratic for |a|,|b|<1000."""
    primeList = readPrimes()
    primes1000 = primeList[:168] # List of primes under 1000
    longestCycle = 0
    longestPair = (0,0)
    for a in range(-999, 1000, 2):
        for b in primes1000:
            n = 0
            while evalPolynomial(n,a,b) in primeList:
                n += 1
            if n > longestCycle:
                longestCycle = n
                longestPair = (a,b)
    return longestPair

pair = findPrimeGen() # (-61, 971)
print(pair[0]*pair[1]) # -59231
