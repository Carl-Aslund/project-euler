from math import sqrt

def isPentagonal(n):
    """Determines if a number is Pentagonal."""
    test = (sqrt(1+24*n)+1)/6
    return test == (int) (test)

if __name__ == "__main__":
    answer = 0
    i = 1
    notFound = True

    while(notFound):
        i += 1
        m = i*(3*i-1)//2

        for j in range(i-1, 0, -1):
            n = j*(3*j-1)//2
            if isPentagonal(m+n) and isPentagonal(m-n):
                answer = m-n
                notFound = False
                break

    print(i) # 2167
    print(j) # 1020
    print(answer) # 5482660
