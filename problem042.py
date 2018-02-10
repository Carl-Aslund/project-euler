
def readWords():
    """Read in a list of words from words.txt."""
    file = open("words.txt", "r")
    words = eval(file.readline())
    return words

def letterScore(word):
    """Returns the sum of indices of the letters in a word."""
    return sum([(ord(letter)-64) for letter in word])

def triangleNumber(n):
    """Returns the nth triangular number."""
    return n * (n+1) // 2

if __name__ == "__main__":
    triangleNums = [triangleNumber(i) for i in range(30)]
    words = readWords()
    triangleWords = 0
    for word in words:
        if letterScore(word) in triangleNums:
            triangleWords += 1
    print(triangleWords) # 162
