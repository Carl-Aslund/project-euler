
def findTriangles(p):
    """Finds all right triangles with perimeter p."""
    triangleCount = 0
    for a in range(3, p//3 + 1):
        for b in range(a+1, p//2):
            c = p - (a+b)
            if (a**2 + b**2) == c**2:
                triangleCount += 1
    return triangleCount

if __name__ == "__main__":
    maxNum = 12
    maxCount = 1
    for i in range(13, 1001):
        newCount = findTriangles(i)
        if newCount > maxCount:
            maxNum = i
            maxCount = newCount
    print(maxNum) # 840
    print(maxCount) # 8
