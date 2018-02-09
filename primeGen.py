import math

def getPrimes(MAX_VAL):
    primes = [True]*MAX_VAL
    go_up_to = math.ceil(MAX_VAL**.5)
    for index in range(2, go_up_to + 1):
        if primes[index]:
            for i in range(index**2, MAX_VAL, index):
                primes[i] = False
    return [index for index in range(2,MAX_VAL) if primes[index]]
