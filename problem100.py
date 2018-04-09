
if __name__ == "__main__":
    b = 15
    n = 21
    target = 10**12

    while(n < target):
        btemp = 3*b + 2*n - 2
        n = 4*b + 3*n - 3
        b = btemp

    print(b) # 756872327473

    
