from math import log

def makeTuple(line, i):
    parts = [int(x) for x in line.split(',')]
    return (log(parts[0])*parts[1], i+1)

if __name__ == "__main__":
    file = open("base_exp.txt")
    data = file.read()
    file.close()
    lines = data.split('\n')
    nums = [makeTuple(lines[i], i) for i in range(len(lines))]
    print(max(nums)[1]) # 709
