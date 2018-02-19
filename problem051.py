from primeGen import getPrimes

patterns = [ # All possible six-digit patterns: 1's are unique, 0's repeat
    [1,1,0,0,0,1],
    [1,0,1,0,0,1],
    [1,0,0,1,0,1],
    [1,0,0,0,1,1],
    [0,1,1,0,0,1],
    [0,1,0,1,0,1],
    [0,1,0,0,1,1],
    [0,0,1,1,0,1],
    [0,0,1,0,1,1],
    [0,0,0,1,1,1]]

def fillPattern(pattern, num):
    """Replaces ones with unique values, and replace 0's with -1's."""
    reverse = pattern[::-1]
    for i in range(6):
        if reverse[i] == 1:
            reverse[i] = num%10
            num = num//10
        else:
            reverse[i] = -1
    return reverse[::-1]

def generateNumber(repeat, filledPattern):
    """Generates a number from a repeating digit and filled pattern."""
    newNum = 0
    for i in range(6):
        newNum *= 10
        if filledPattern[i] == -1:
            newNum += repeat
        else:
            newNum += filledPattern[i]
    return newNum

def familySize(filledPattern, primes):
    count = 0
    smallest = 0
    for i in range(1,10):
        num = generateNumber(i, filledPattern)
        if num in primes:
            count += 1
            if count == 1:
                smallest = num
    if count >= 8:
        print(smallest)
    return

if __name__ == "__main__":
    primes = getPrimes(1000000)
    for i in range(101, 1000, 2):
        for pat in patterns:
            filledPattern = fillPattern(pat, i)
            familySize(filledPattern, primes)

"""The output numbers was 121313, so it must be the answer."""
