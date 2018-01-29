
def sumOfPowers(n):
    """Determines if a number is the sum of the fifth powers of its digits."""
    return (n == sum([int(x)**5 for x in str(n)]))

def sumPowerFinder(n):
    """Finds all numbers up to n that satisfy sumOfPowers()."""
    L = []
    for i in range(10,n+1):
        if sumOfPowers(i):
            L.append(i)
    return L
    
L = sumPowerFinder(300000)
print(sum(L)) # 443839
