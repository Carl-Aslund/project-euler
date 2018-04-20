result = 0

for line in open('triangles_102.txt'):
    ax, ay, bx, by, cx, cy = map(int, line.split(','))
    a = ax*by - ay*bx > 0
    b = bx*cy - by*cx > 0
    c = cx*ay - cy*ax > 0

    result += a==b==c

print(result) # 228
