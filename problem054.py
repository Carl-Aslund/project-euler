cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10,
             'J':11, 'Q':12, 'K':13, 'A':14}

def isFlush(hand):
    """Returns if a hand is a flush."""
    suit = hand[1]
    for i in range(4, 15, 3):
        if hand[i] != suit:
            return False
    return True

def isStraight(values):
    """Returns if some set of values makes a straight."""
    if values == [2,3,4,5,14]:
        return True
    else:
        start = values[0]
        for i in range(1,5):
            if values[i]-i != start:
                return False
        return True

def cardNumbers(values):
    counter = {}
    for v in values:
        if v in counter:
            counter[v] += 1
        else:
            counter[v] = 1
    outList = [[value, key] for key, value in counter.items()]
    outList.sort()
    return outList[::-1]

def scoreHand(hand):
    values = [cards[hand[i]] for i in range(0, 15, 3)]
    values.sort()
    countL = cardNumbers(values)
    if isFlush(hand):
        if isStraight(values):
            return [8, values[4]] # Doesn't appear
        else:
            return [5] + values[::-1]
    else:
        if countL[0][0] == 4:
            return [7, countL[0][1]]
        elif countL[0][0] == 3:
            if countL[1][0] == 2:
                return [6, countL[0][1]]
            else:
                return [3, countL[0][1]]
        elif countL[0][0] == 2:
            if countL[1][0] == 2:
                return [2, countL[0][1], countL[1][1], countL[2][1]]
            else:
                return [1, countL[0][1],countL[1][1],countL[2][1],countL[3][1]]
        elif isStraight(values): # Doesn't appear
            if values[4] == 14:
                return [4, 5]
            else:
                return [4, values[4]]
        else:
            return [0] + values[::-1]

if __name__ == "__main__":
    file = open("poker.txt")
    data = file.read()
    file.close()
    rounds = data.split('\n')
    win1 = 0
    for r in rounds:
        s1 = scoreHand(r[:14])
        s2 = scoreHand(r[15:])
        if s1 > s2:
            win1 += 1
    print(win1) # 376
