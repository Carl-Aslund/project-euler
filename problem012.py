from math import sqrt

def countFactors(n):
    """Counts the number of factors of an input n."""
    factors = 0
    for i in range(1, int(sqrt(n))):
        if n%i == 0:
            if i**2 == n:
                factors += 1
            else:
                factors += 2
    return factors

def triangularNumber(n):
    """Computes the nth triangular number."""
    return n*(n+1)//2

def findTriangleFactors(n):
    """Computes the first triangle number with over n factors."""
    index = 1
    while True:
        triNum = triangularNumber(index)
        numFactors = countFactors(triNum)
        if numFactors > n:
            return triNum
        index += 1

print(findTriangleFactors(500)) # 76576500
