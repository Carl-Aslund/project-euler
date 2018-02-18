from primeGen import getPrimes

if __name__ == "__main__":
    primes = getPrimes(1000000)
    primeSum = [0]
    numPrimes = 0
    result = 0
    for p in primes:
        primeSum.append(p+primeSum[-1])
    for i in range(numPrimes, len(primeSum)):
        for j in range((i-numPrimes-1), -1, -1):
            newSum = primeSum[i] - primeSum[j]
            if newSum > 1000000:
                break
            elif newSum in primes:
                numPrimes = i-j
                result = newSum
    print(numPrimes) # 543
    print(result) # 997651
