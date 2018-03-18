
if __name__ == "__main__":
    p = [1]
    n = 1

    while True:
        i=0
        penta=1
        p.append(0)
        while penta <= n:
            if i%4 > 1:
                sign = -1
            else:
                sign = 1
            p[n] += sign * p[n - penta]
            p[n] %= 1000000
            i += 1
            if i%2 == 0:
                j = i//2 + 1
            else:
                j = -(i//2 + 1)
            penta = j * (3 * j - 1) // 2
        if p[n] == 0:
            break
        n += 1
    print(n) # 55374
