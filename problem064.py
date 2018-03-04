from math import sqrt

if __name__ == "__main__":
    result = 0
    for i in range(2, 10001):
        limit = (int) (sqrt(i))
        if limit*limit == i:
            continue
        period = 0
        d = 1
        m = 0
        a = limit
        while True:
            m = d*a - m
            d = (i-m*m)//d
            a = (limit + m)//d
            period += 1
            if a==2*limit:
                break
        if period%2 == 1:
            result += 1
    print(result) # 1322
