
def fillFactorial(n):
    """Creates a list of factorials from 0 to n (inclusive)."""
    factorials = [1]
    for i in range(1,n+1):
        factorials.append(factorials[-1]*i)
    return factorials

def sumOfFactorials(n, factorials):
    """Determines if a number is the sum of the factorials of its digits."""
    return (n == sum([factorials[int(x)] for x in str(n)]))

def sumFactorialFinder(n):
    """Finds all numbers up to n that satisfy sumOfFactorials()."""
    L = []
    factorials = fillFactorial(9)
    for i in range(10,n+1):
        if sumOfFactorials(i, factorials):
            L.append(i)
    return L

L = sumFactorialFinder(250000)
print(L) # [145, 40585]
print(sum(L)) # 40730 
