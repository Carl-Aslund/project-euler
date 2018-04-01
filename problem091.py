
if __name__ == "__main__":
    limit = 50
    numTri = 0
    for x1 in range(limit+1):
        for y1 in range(limit+1):
            if x1==0 and y1==0:
                continue
            for x2 in range(limit+1):
                for y2 in range(limit+1):
                    if x2==0 and y2==0:
                        continue
                    elif x1==x2 and y1==y2:
                        continue
                    D1 = x1**2 + y1**2
                    D2 = x2**2 + y2**2
                    D3 = (x1-x2)**2 + (y1-y2)**2
                    maxD = max(D1, D2, D3)
                    if maxD == (D1+D2+D3 - maxD):
                        numTri += 1
    print(numTri//2) # 14234
