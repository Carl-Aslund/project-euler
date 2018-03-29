if __name__ == "__main__":
    file = open("roman.txt")
    data = file.read()
    file.close()
    original = len(data)
    data = data.replace("DCCCC", "CM")
    data = data.replace("LXXXX", "XC")
    data = data.replace("VIIII", "IX")
    data = data.replace("CCCC", "CD")
    data = data.replace("XXXX", "XL")
    data = data.replace("IIII", "IV")
    print(original - len(data)) # 743
