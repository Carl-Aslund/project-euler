
def sumDivisors(n):
    """Adds up all the proper divisors of n."""
    total = 0
    for i in range(1, n):
        if n%i == 0:
            total += i
    return total

def isAbundant(n):
    """Determines whether or not n is an abundant number."""
    divisorSum = sumDivisors(n)
    return divisorSum > n

def abundantList(n):
    """Generates a list of all abundant numbers less than n."""
    abundants = []
    for i in range(12,n):
        if isAbundant(i):
            abundants.append(i)
    return abundants

def isAbundantSum(n, abundants):
    """Determines if n is the sum of abundant numbers."""
    for abundant in abundants:
        if (n-abundant) in abundants:
            return True
        elif abundant > n:
            return False
    return False # Only runs if no pair is found

def nonAbundantSums(n):
    """Computes the sum of all numbers less than n that aren't abundant sums."""
    abundants = abundantList(n)
    total = 0
    for i in range(1,n):
        if not isAbundantSum(i, abundants):
            total += i
    return total
    
print(nonAbundantSums(28124)) # 4179871
