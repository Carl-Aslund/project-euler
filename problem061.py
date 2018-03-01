
solution = [0]*6

def genNums(i):
    nums = []
    num = 0
    n = 0
    while num<10000:
        n += 1
        if i==0: # Triangle numbers
            num = (n*(n+1))//2
        elif i==1: # Square numbers
            num = n*n
        elif i==2: # Pentagon numbers
            num = (n*(3*n-1))//2
        elif i==3: # Hexagon numbers
            num = n*(2*n-1)
        elif i==4: # Heptagon numbers
            num = (n*(5*n-3))//2
        elif i==5: # Octagon numbers
            num = n*(3*n-2)
        if num > 999 and num < 10000:
            nums.append(num)
    return nums

def findNext(last, length, numbers):
    for i in range(6):
        if solution[i] != 0:
            continue
        for j in range(len(numbers[i])):
            unique = True
            for k in range(6):
                if numbers[i][j] == solution[k]:
                    unique = False
                    break
            if unique and (numbers[i][j]//100) == (solution[last]%100):
                solution[i] = numbers[i][j]
                if length == 5:
                    if solution[5]//100 == solution[i]%100:
                        return True
                if findNext(i, length+1, numbers):
                    return True
        solution[i] = 0
    return False

if __name__ == "__main__":
    numbers = []
    for i in range(6):
        numbers.append(genNums(i))
    for i in range(len(numbers[5])):
        solution[5] = numbers[5][i]
        if findNext(5,1,numbers):
            break
    print(sum(solution)) # 28684
    print(solution) # [8256, 5625, 2882, 8128, 2512, 1281]
