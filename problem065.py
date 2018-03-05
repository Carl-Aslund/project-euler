
if __name__ == "__main__":
    d = 1
    n = 2
    for i in range(2,101):
        temp = d
        c = 1
        if i%3 == 0:
            c = 2 * (i//3)
        d = n
        n = c*d + temp
    print(sum([int(i) for i in str(n)])) # 272
