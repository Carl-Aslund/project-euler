
def readPrimes():
    """Reads in a list of primes from primeList.txt"""
    file = open("primeList.txt", "r")
    primes = eval(file.readline())
    return primes

def isValid(n):
    """Checks if a prime could not possibly be a dual-truncatable prime."""
    strNum = str(n)
    if len(strNum) == 1:
        return False
    if (('0' in strNum) or ('2' in strNum[1:]) or ('4' in strNum) or
        ('5' in strNum[1:]) or ('6' in strNum) or ('8' in strNum) or
        (strNum[0] == '1') or (strNum[0] == '9')):
        return False
    return True

def leftTruncatable(n, primes):
    """Determines if a number is a left-truncatable prime."""
    digits = len(str(n))
    for i in range(1, digits):
        if (n % (10**i)) not in primes:
            return False
    return True

def rightTruncatable(n, primes):
    """Determines if a number is a right-truncatable prime."""
    digits = len(str(n))
    for i in range(digits-1):
        n = n//10
        if n not in primes:
            return False
    return True

primes = readPrimes()
truncatables = []
for p in primes:
    if not isValid(p):
        continue
    elif not leftTruncatable(p, primes):
        continue
    elif not rightTruncatable(p, primes):
        continue
    else:
        truncatables.append(p)

print(len(truncatables)) # 11
print(sum(truncatables)) # 748317
