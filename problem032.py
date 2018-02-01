
# Possible options are 2*3=4 and 1*4=4

def isPandigital(a, b, n):
    """Determines if a product a*b=n is pandigital."""
    numString = str(a) + str(b) + str(n)
    if len(numString) != 9: # Make sure the input is valid
        return False
    for i in [str(letter) for letter in range(1,10)]: # Check that each appears
        if i not in numString:
            return False
    return True

def bashCombos():
    """Bash through all combinations to find 1-9 pandigital products."""
    pandigitals = set()
    for i in range(2,50):
        for j in range(123,2000):
            n = i*j
            if n in pandigitals:
                continue
            elif isPandigital(i,j,n):
                pandigitals.add(n)
    return pandigitals

pandigitals = bashCombos()
print(pandigitals) # {5346, 5796, 6952, 7852, 4396, 7632, 7254}
print(sum(pandigitals)) # 45228
