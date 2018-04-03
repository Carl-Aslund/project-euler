
if __name__ == "__main__":
    result = 0
    x = 2
    y = 1
    limit = 10**9

    while True:
        a3 = 2*x-1
        area3 = y*(x-2)
        if a3 > limit:
            break
        if a3 > 0 and area3 > 0 and a3%3 == 0 and area3%3 == 0:
            a = a3 // 3
            area = area3 // 3
            result += 3*a+1

        a3 = 2*x+1
        area3 = y*(x+2)
        if a3 > 0 and area3 > 0 and a3%3 == 0 and area3%3 == 0:
            a = a3 // 3
            area = area3 // 3
            result += 3*a-1

        nextX = 2*x + y*3
        nextY = y*2 + x
        x=nextX
        y=nextY

    print(result) # 518408346
