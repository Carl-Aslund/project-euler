import datetime

sundayCounter = 0

for i in range(1,101):
    for j in range(1, 13):
        date = datetime.date(1900+i, j, 1)
        if date.weekday() == 6:
            sundayCounter += 1
        
print(sundayCounter) # 171
