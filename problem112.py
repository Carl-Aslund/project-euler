
def isBouncy(n):
    last = n%10
    n = n//10
    
    inc = False
    dec = False

    while n>0:
        nextN = n%10
        n = n//10
        if nextN < last:
            inc = True
        elif nextN > last:
            dec = True
        last = nextN
        if inc and dec:
            return True
    return inc and dec

if __name__ == "__main__":
    i = 99
    bouncies = 0
    while (100*bouncies < 99*i):
        i += 1
        if isBouncy(i):
            bouncies += 1
    print(i) # 1587000
