
if __name__ == "__main__":
    error = 10**10
    area = 0
    target = 2*(10**6)

    x = 2000
    y = 1

    while x>=y:
        rects = (x*(x+1)*y*(y+1))//4
        if abs(rects-target) < error:
            error = abs(rects-target)
            area = x * y
        if rects < target:
            y += 1
        else:
            x -= 1

    print(area) # 2772
