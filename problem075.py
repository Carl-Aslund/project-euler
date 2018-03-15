from math import gcd, sqrt

if __name__ == "__main__":
    limit = 1500000
    triangles = [0]*(limit+1)
    result = 0
    mlimit = (int) (sqrt(limit/2))
    for m in range(2,mlimit):
        for n in range(1,m):
            if (((n + m) % 2) == 1 and gcd(n, m) == 1):
                a = m * m + n * n
                b = m * m - n * n
                c = 2 * m * n
                p = a + b + c
                while(p <= limit):
                    triangles[p] += 1
                    if (triangles[p] == 1): result += 1
                    if (triangles[p] == 2): result -= 1
                    p += a+b+c
    print(result) # 161667
