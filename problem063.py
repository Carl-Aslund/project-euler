from math import log10, ceil

if __name__ == "__main__":
    answers = 0
    for i in range(1,10):
        j = 1
        num = i
        while ceil(log10(num+1)) == j:
            answers += 1
            num *= i
            j += 1
    print(answers) # 49
        
