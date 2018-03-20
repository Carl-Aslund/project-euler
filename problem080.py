
def sqrt(n, digits):
    limit = 10**(digits+1)
    a = 5*n
    b = 5
    while b<limit:
        if a>=b:
            a -= b
            b += 10
        else:
            a *= 100
            b = (b//10)*100+5
    return b//100

def digitSum(n):
    return sum([int(x) for x in str(n)])

if __name__ == "__main__":
    result = 0
    j = 1
    for i in range(1, 101):
        if (j*j==i):
            j += 1
            continue
        result += digitSum(sqrt(i, 100))
    print(result) # 40886
