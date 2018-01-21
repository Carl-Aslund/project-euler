divisorSums = {}

def sumDivisors(n):
    """Adds up all the proper divisors of n."""
    if n in divisorSums:
        return divisorSums[n]
    else:
        total = 0
        for i in range(1,n):
            if n%i == 0:
                total += i
        divisorSums[n] = total
        return total

def isAmicable(n):
    """Determines if n is an amicable number."""
    pair = sumDivisors(n)
    if pair == n:
        return False
    return (sumDivisors(pair) == n)

def amicableSum(n):
    """Computes the sum of all amicable numbers up to n."""
    total = 0
    for i in range(1,n):
        if isAmicable(i):
            total += i
    return total

print(amicableSum(10000)) # 31626
