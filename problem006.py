
def sqSumDiff(num):
    """Finds the difference between the sum square and sqaure sum of 1-num."""
    sumSq = num*(num+1)*(2*num+1)//6
    sqSum = (num*(num+1)//2)**2
    return sqSum - sumSq

print(sqSumDiff(100)) # 25164150
