from math import ceil, floor

if __name__ == "__main__":
    rf = {1/3, 1/2}
    for d in range(5,12001):
        lower = floor(d/3)+1
        upper = ceil(d/2)
        for n in range(lower, upper):
            rf.add(n/d)
    print(len(rf)-2) # 7295372
