
def isPalindrome(num):
    """Determines whether or not an input number is a palindrome."""
    numString = str(num)
    for i in range(len(numString)//2):
        if numString[i] != numString[-i-1]:
            return False
    return True

def isLychrel(num):
    """Determines if a number is Lychrel (only 50 iterations tested)."""
    for i in range(50):
        reverseNum = int(str(num)[::-1])
        num += reverseNum
        if isPalindrome(num):
            return False
    return True

if __name__ == "__main__":
    count = 0
    for i in range(1,10000):
        if isLychrel(i):
            count += 1
    print(count) # 249
