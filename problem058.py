from random import randrange

def miller_rabin(n, k=10):
    """An implementation of the Miller-Rabin primality test."""
    if n == 2 or n == 3:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def numSpiralPrimes(n):
    """Counts the primes on the nth loop."""
    i = 2*n - 1
    c1 = i**2 + 2*n
    c2 = c1 + 2*n
    c3 = c2 + 2*n
    return miller_rabin(c1) + miller_rabin(c2) + miller_rabin(c3)

if __name__ == "__main__":
    num = 1
    den = 1
    i = 0
    while (num/den) >= 0.1:
        i += 1
        num += numSpiralPrimes(i)
        den += 4
    print(i) # 13123
    print(i*2-5)




        
    
