
if __name__ == "__main__":
    file = open("matrix81.txt")
    data = file.read()
    file.close()
    sizes = [[int(x) for x in line.split(",")] for line in data.split("\n")]
    paths = [[0 for x in range(80)] for y in range(80)]
    paths[0][0] = sizes[0][0]
    for i in range(1,80):
        paths[i][0] = sizes[i][0] + paths[i-1][0]
        paths[0][i] = sizes[0][i] + paths[0][i-1]
    for x in range(1,80):
        for y in range(1,80):
            paths[x][y] = sizes[x][y] + min(paths[x-1][y], paths[x][y-1])
    print(paths[79][79]) # 427337
