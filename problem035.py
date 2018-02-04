
def readPrimes():
    """Reads in a list of primes from primeList.txt"""
    file = open("primeList.txt", "r")
    primes = eval(file.readline())
    return primes

def isValid(n):
    """Checks if a prime could not possibly be a cycle prime."""
    strNum = str(n)
    if ('0' in strNum) or ('2' in strNum) or ('4' in strNum) or ('5' in strNum) or ('6' in strNum) or ('8' in strNum):
        return False
    return True

def cycleNum(n):
    """Cycles an input number by one iteration."""
    strNum = str(n)
    newNum = strNum[1:] + strNum[0]
    return int(newNum)



primes = readPrimes()
cyclePrimes = [2,5]
for p in primes:
    n = p
    if not isValid(n):
        continue
    isCyclic = True
    for i in range(len(str(p))):
        n = cycleNum(n)
        if n not in primes:
            isCyclic = False
            break
    if isCyclic:
        cyclePrimes.append(p)

print(len(cyclePrimes)) # 55
print(cyclePrimes)
