from primeGen import getPrimes
from math import sqrt

def isPermutation(a, b):
    """Determines if strings a and b are permutations of each other."""
    l1 = [i for i in str(a)]
    l2 = [i for i in str(b)]
    list.sort(l1)
    list.sort(l2)
    return l1 == l2

if __name__ == "__main__":
    limit = 10**7
    primes = getPrimes((int) (1.2*sqrt(limit)))
    del primes[:int(0.6*len(primes))]

    do = True
    min_q, min_n, i = 2, 0, 0
    for p1 in primes:
        if do:
            i += 1
            for p2 in primes[i:]:
                if (p1+p2)%9 != 1:
                    continue
                n = p1 * p2
                if n > limit:
                    print(min_n) # 8319823
                    do = False
                    break
                phi = (p1-1) * (p2-1)
                q = n / float(phi)
                if isPermutation(phi, n) and min_q>q:
                    min_q, min_n = q, n
