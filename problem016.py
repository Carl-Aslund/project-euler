
def sumPowerDigits(x, y):
    """Sums the digits of x^y."""
    return sum([int(i) for i in str(x**y)])

print(sumPowerDigits(2,1000)) # 1366
