
def makeLargestPerm(num):
    """Returns the largest permutation of an input number."""
    digits = [0]*10
    output = 0
    while num > 0:
        digits[num%10] += 1
        num = num // 10
    for i in range(9,-1,-1):
        for j in range(digits[i]):
            output = output*10 + i
    return output

if __name__ == "__main__":
    permCount = {}
    permVal = {}
    i = 345
    found = False
    while not found:
        i += 1
        largePerm = makeLargestPerm(i*i*i)
        if largePerm in permCount:
            permCount[largePerm] += 1
            if permCount[largePerm] == 5:
                found = True
                print(permVal[largePerm]) # 127035954683
        else:
            permCount[largePerm] = 1
            permVal[largePerm] = i*i*i
