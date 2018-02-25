from math import log10

if __name__ == "__main__":
    num = 3
    den = 2
    count = 0
    for i in range(2,1001):
        num += 2*den
        den += (num-2*den)
        if int(log10(num)) > int(log10(den)):
            count += 1
    print(count) # 153
