
if __name__ == "__main__":
    ways = [1]+[0]*100
    print(len(ways))

    for i in range(1,100):
        for j in range(i,101):
            ways[j] += ways[j-i]

    print(ways[100]) # 190569291
