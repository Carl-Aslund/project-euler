
if __name__ == "__main__":
    file = open("matrix81.txt")
    data = file.read()
    file.close()
    grid = [[int(x) for x in line.split(",")] for line in data.split("\n")]
    sol = [0]*80
    for i in range(80):
        sol[i] = grid[i][79]
    for i in range(78,-1,-1):
        sol[0] += grid[0][i]
        for j in range(1,80):
            sol[j] = grid[j][i] + min(sol[j-1], sol[j])
        for j in range(78, -1, -1):
            sol[j] = min(sol[j], sol[j+1]+grid[j][i])
    print(min(sol)) # 260324
