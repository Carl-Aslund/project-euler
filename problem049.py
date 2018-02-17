from primeGen import getPrimes

def isPermutation(a, b):
    """Determines if strings a and b are permutations of each other."""
    l1 = [i for i in str(a)]
    l2 = [i for i in str(b)]
    list.sort(l1)
    list.sort(l2)
    return l1 == l2

if __name__ == "__main__":
    primes = getPrimes(10000)[236:]
    length = len(primes)
    isFound = False
    for i in range(length):
        a = primes[i]
        if isFound:
            break
        for j in range(i+1, length):
            b = primes[j]
            if isPermutation(a, b):
                c = 2*b - a
                if c in primes:
                    if isPermutation(a, c):
                        print(str(a)+str(b)+str(c)) # 296962999629
                        isFound = True
                        break
