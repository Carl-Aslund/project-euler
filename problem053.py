
if __name__ == "__main__":
    fac = [1]
    for i in range(1,101):
        fac.append(fac[-1]*i)
    count = 0
    for n in range(1,101):
        for r in range(1,n):
            choose = fac[n]/fac[n-r]/fac[r]
            if choose > 1000000:
                count += 1
    print(count) # 4075
