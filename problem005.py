def gcd(x, y):
    """Returns the greatest common denominator of two integers."""
    if y == 0:
        return x
    else:
        r = x % y
        return gcd(y, r)

def superLcm(num):
    """Returns the least common multiple of all numbers from 1 to num."""
    lcm = 1
    for i in range(2, num+1):
        if lcm%i == 0:
            continue
        else:
            gcdNumI = gcd(lcm,i)
            lcm = lcm*i//gcdNumI
    return lcm

print(superLcm(20))
