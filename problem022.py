
def scoreName(name):
    """Compute the letter score of an input fully-capitalized name."""
    total = 0
    for letter in name:
        total += (ord(letter) - 64)
    return total

def readNames():
    """Reads and processes names from the corresponding text file."""
    file = open("problem022names.txt", "r")
    rawNames = file.readline()
    nameList = eval("["+rawNames+"]")
    sortedList = sorted(nameList)
    return sortedList

def computeScore():
    """Computes the total name scores of all the names in the name file."""
    nameList = readNames()
    total = 0
    for i in range(len(nameList)):
        total += ( (i+1) * scoreName(nameList[i]) )
    return total

print(computeScore()) # 871198282
