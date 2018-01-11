
def sumAll(num, maximum):
    """Computes the sum of all multiples of num under maximum."""
    multipleCount = maximum // num
    return num*multipleCount*(multipleCount+1)/2

def sumMultiples(x, y, maximum):
    """Computes the sum of all multiples of x and y under maximum."""
    sumX = sumAll(x, maximum)
    sumY = sumAll(y, maximum)
    sumXY = sumAll(x*y, maximum)
    return sumX + sumY - sumXY

print(sumMultiples(3,5,999)) # 233168
