
if __name__ == "__main__":
    a = 3
    b = 7
    r = 0
    s = 1
    limit = 10**6

    for q in range(limit, 2, -1):
        p = (a*q-1)//b
        if p*s > r*q:
            s=q
            r=p

    print(r) # 428570
