from primeGen import getPrimes
from problem058 import miller_rabin as isPrime

def pairUp(n, primes):
    pairs = set()
    p1 = primes[n]
    for i in range(n+1, len(primes)):
        p2 = primes[i]
        n1 = int(str(p1)+str(p2))
        n2 = int(str(p2)+str(p1))
        if isPrime(n1) and isPrime(n2):
            pairs.add(i)
    return pairs

if __name__ == "__main__":
    pairs = {}
    result = 10**100
    primes = getPrimes(10000)
    lim = len(primes)
    for a in range(1,lim):
        if a not in pairs:
            pairs[a] = pairUp(a, primes)
        for b in range(a+1,lim):
            if b not in pairs[a]:
                continue
            if b not in pairs:
                pairs[b] = pairUp(b, primes)
            for c in range(b+1,lim):
                if c not in pairs[a]:
                    continue
                if c not in pairs[b]:
                    continue
                if c not in pairs:
                    pairs[c] = pairUp(c, primes)
                for d in range(c+1,lim):
                    if d not in pairs[a]:
                        continue
                    if d not in pairs[b]:
                        continue
                    if d not in pairs[c]:
                        continue
                    if d not in pairs:
                        pairs[d] = pairUp(d, primes)
                    for e in range(d+1,lim):
                        if e not in pairs[a]:
                            continue
                        if e not in pairs[b]:
                            continue
                        if e not in pairs[c]:
                            continue
                        if e not in pairs[d]:
                            continue
                        total=primes[a]+primes[b]+primes[c]+primes[d]+primes[e]
                        if total < result:
                            result = total
                            print(result) # 26033
