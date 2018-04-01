s1 = {1}
s89 = {89}

def sqSum(n):
    return sum([int(i)**2 for i in str(n)])

def is1(n):
    if n in s1:
        return True
    elif n in s89:
        return False
    else:
        result = is1(sqSum(n))
        if result:
            s1.add(n)
        else:
            s89.add(n)
        return result

if __name__ == "__main__":
    count = 0
    for i in range(1, 10**7):
        if not is1(i):
            count += 1
    print(count) # 8581146
