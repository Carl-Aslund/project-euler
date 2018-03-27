from primeGen import getPrimes

if __name__ == "__main__":
    primes = getPrimes(7072)
    target = 50000000
    powers = [primes, [], [], []]
    for i in range(1, 4):
        for j in range(len(primes)):
            powers[i].append(primes[j]*powers[i-1][j])
    numbers = set()
    for i in range(len(primes)):
        for j in range(len(primes)):
            for k in range(len(primes)):
                number = powers[1][i] + powers[2][j] + powers[3][k]
                if number > target:
                    break
                numbers.add(number)
    print(len(numbers)) # 1097343
