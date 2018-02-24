
if __name__ == "__main__":
    powers = []
    for i in range(1,100):
        for j in range(1,100):
            powers.append(i**j)
    print(max([sum([int(i) for i in str(j)]) for j in powers])) # 972
