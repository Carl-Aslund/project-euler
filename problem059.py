
def decrypt(message, key):
    decrypted = []
    keyLength = len(key)
    for i in range(len(message)):
        decrypted.append(message[i] ^ key[i%keyLength])
    return decrypted

def analysis(message, keyLength):
    maxSize = 0
    for i in message:
        if i > maxSize:
            maxSize = i
    aMessage = [[0]*(maxSize+1) for _ in range(keyLength)]
    key = [0]*keyLength

    for i in range(len(message)):
        j = i % keyLength
        aMessage[j][message[i]] += 1
        if (aMessage[j][message[i]] > aMessage[j][key[j]]):
            key[j] = message[i]
    space = 32
    for i in range(keyLength):
        key[i] = key[i] ^ space
    return key

        

if __name__ == "__main__":
    file = open("cipher.txt")
    message = eval(file.read())
    file.close()
    keyLength = 3

    key = analysis(message, keyLength)
    decrypted = decrypt(message, key)
    result = sum(decrypted)
    print(result) # 107359
