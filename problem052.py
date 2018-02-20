
def isPermutation(a, b):
    """Determines if strings a and b are permutations of each other."""
    l1 = [i for i in str(a)]
    l2 = [i for i in str(b)]
    list.sort(l1)
    list.sort(l2)
    return l1 == l2

if __name__ == "__main__":
    start = 10000
    notFound = True
    answer = 0

    while notFound:
        start *= 10
        for i in range(start, (start*10)//6):
            notFound = False
            for j in range(2,7):
                if not isPermutation(i, i*j):
                    notFound = True
                    break
            if not notFound:
                answer = i
                break

    print(answer) # 142857
