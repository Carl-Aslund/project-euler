from primeGen import getPrimes

def isPandigital(numString):
    """Determines if a product a*b=n is pandigital."""
    if len(numString) > 9: # Make sure the input is valid
        return False
    for i in [str(letter) for letter in range(1,len(numString)+1)]:
        # Check that each of 1-n appears in the number
        if i not in numString:
            return False
    return True

if __name__ == "__main__":
    primes = getPrimes(7654322)
    largestPandigital = 0
    for p in primes:
        if isPandigital(str(p)):
            largestPandigital = p
    print(largestPandigital) # 7652413
