from math import sqrt

if __name__ == "__main__":
    l = 2
    count = 0
    target = 10**6

    while count<target:
        l += 1
        for wh in range(3, 2*l+1):
            root = sqrt(wh*wh + l*l)
            if root == (int) (root):
                if wh <= l:
                    count += wh//2
                else:
                    count += (1+(l-(wh+1)//2))
    print(l) # 1818
