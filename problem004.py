
def isPalindrome(num):
    """Determines whether or not an input number is a palindrome."""
    numString = str(num)
    for i in range(len(numString)//2):
        if numString[i] != numString[-i-1]:
            return False
    return True

def findLargestPalindrome():
    """Finds the largest palindrome multiple of two 3-digit numbers. Assumes
that there exists some palindrome multiple that starts (and ends) with a 9."""
    largestPalindrome = -1
    for i in range(903, 1000, 10):
        for j in range(903, 1000, 10):
            product = i*j
            if isPalindrome(product):
                if product > largestPalindrome:
                    largestPalindrome = product
    for i in range(901, 1000, 10):
        for j in range(909, 1000, 10):
            product = i*j
            if isPalindrome(product):
                if product > largestPalindrome:
                    largestPalindrome = product
    return largestPalindrome

print(findLargestPalindrome())
