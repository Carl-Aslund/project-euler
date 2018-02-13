from math import sqrt

def isPentagonal(n):
    """Determines if a number is pentagonal."""
    test = (sqrt(1+24*n)+1)/6
    return test == (int) (test)

def isHexagonal(n):
    """Determines if a number is hexagonal."""
    test = (sqrt(1+8*n)+1)/4
    return test == (int) (test)

if __name__ == "__main__":
    triangleNum = 0
    i = 285
    while True:
        i += 1
        triangle = i*(3*i-1)//2

        if isPentagonal(triangle) and isHexagonal(triangle):
            triangleNum = triangle
            break
    print(i) # 31977
    print(triangleNum) # 1533776805
