lengthDict = {1:1} # Stores the lengths of Collatz sequences found

def sequenceLength(n):
    """Computes the length of a Collatz sequence starting at n."""
    if n in lengthDict:
        return lengthDict[n]
    elif n%2 == 0:
        length = 1 + sequenceLength(n//2)
        lengthDict[n] = length
        return length
    else:
        length = 1 + sequenceLength(3*n + 1)
        lengthDict[n] = length
        return length

def longestSequence(limit):
    """Returns the number under limit that starts the longest Collatz sequence."""
    maxLength = 1
    maxEntry = 1
    for n in range(2,limit):
        length = sequenceLength(n)
        if length > maxLength:
            maxLength = length
            maxEntry = n
    return maxEntry

print(longestSequence(1000000)) # 837799
