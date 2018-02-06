
def isPandigital(numString):
    """Determines if a product a*b=n is pandigital."""
    if len(numString) != 9: # Make sure the input is valid
        return False
    for i in [str(letter) for letter in range(1,10)]: # Check that each appears
        if i not in numString:
            return False
    return True

pandigitalSeeds = []
largestPandigital = 0
for i in range(1,9877):
    string = ""
    j = 1
    while len(string) < 9:
        string += str(i*j)
        j += 1
    if isPandigital(string):
        pandigitalSeeds.append(i)
        largestPandigital = max(int(string), largestPandigital)
print(pandigitalSeeds)
print(largestPandigital) # 932718654
