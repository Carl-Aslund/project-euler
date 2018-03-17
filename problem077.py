from primeGen import getPrimes

if __name__ == "__main__":
    ways = [1]+[0]*100
    primes = getPrimes(100)

    for p in primes:
        for i in range(p, 101):
            ways[i] += ways[i-p]

    for i in range(101):
        if ways[i] > 5000:
            print(i) # 71
            break
