from functools import reduce

def isTriplet(a,b,c):
    """Checks if a^2 + b^2 = c^2 for a given three integers."""
    return a**2 + b**2 == c**2

def findTriplet(n):
    """Finds a triplet where a+b+c = n."""
    for a in range(1,n//2):
        for b in range(a, n//2):
            c = n - a - b
            if isTriplet(a,b,c):
                return [a,b,c]
    return "No triplets found."

def tripletProduct(n):
    """Returns the product of some triplet where a+b+c = n."""
    triplet = findTriplet(n)
    return reduce(lambda x,y: x*y, triplet)
    

print(tripletProduct(1000)) # 31875000
