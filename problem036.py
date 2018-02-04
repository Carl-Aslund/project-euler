
def isPalindrome(n, b):
    """Determines if n is a palindrome in base b."""
    nCopy = n
    nReverse = 0
    while (nCopy > 0):
        nReverse = nReverse*b + nCopy%b
        nCopy = nCopy // b
    return (n == nReverse)

def findPalindromes(n, a, b):
    """Finds all numbers up to n that are palindromes base a and base b."""
    palindromes = []
    for i in range(1,n):
        if isPalindrome(i, a) and isPalindrome(i, b):
            palindromes.append(i)
    return palindromes

palindromes = findPalindromes(1000000, 2, 10)
print(sum(palindromes)) # 872187
