
numberLengths = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6,
                 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6,
                 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 1000:11}

def numberLength(n):
    """Computes the number of letters in some number between 1 and 1000."""
    if n in numberLengths:
        return numberLengths[n]
    elif n%100 == 0: # Multiples of 100
        return numberLength(n//100) + 7
    elif n >= 100: # 101-999, no multiples of 100
        return numberLength(n//100) + 10 + numberLength(n%100)
    else: #21-99, no multiples of 10
        remainder = n%10
        return numberLength(n-remainder) + numberLength(remainder)

letterSum = 0

for i in range(1,1001):
    letterSum += numberLength(i)

print(letterSum) # 21124
