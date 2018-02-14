from primeGen import getPrimes
from math import sqrt

if __name__ == "__main__":
    notFound = True
    answer = 0
    primes = getPrimes(6000)[1:]
    i = 7

    while notFound:
        i += 2
        if i > 50000:
            print("Insufficient primes.")
            break
        if i in primes:
            continue
        for p in primes:
            if p > i:
                notFound = False
                break
            else:
                square = (i-p)//2
                root = sqrt(square)
                if root == (int) (root):
                    break
        if not notFound:
            answer = i
    print(answer) # 5777
