from fractions import gcd
from functools import reduce

nums = []
denoms = []

for i in range(1,10):
    for j in range(i+1,10):
        for k in range(i+2,10):
            if (i*10+j)/(j*10+k) == i/k:
                nums.append(i)
                denoms.append(k)

numerator =  reduce((lambda x, y: x * y), nums)
denominator =  reduce((lambda x, y: x * y), denoms)

print(denominator // gcd(numerator, denominator)) # 100
