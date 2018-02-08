'''
a = (9-0)*1                 #1-9: 1-9
b = a + (99-9)*2            #10-99: 10-189
c = b + (999-99)*3          #100-999: 190-2,889
d = c + (9999-999)*4        #1000-9999: 2,890-38,889
e = d + (99999-9999)*5      #10000-99999: 38,890-488,889
f = e + (999999-99999)*6    #100000-999999: 488,890-5,888,889
print([a,b,c,d,e,f])
'''

# Calculation for d1
d1 = 1
# Calculation for d10
d10 = 1
# Calculation for d100
d100 = 5
# Calculation for d1000
d1000 = 3
# Calculation for d10000
d10000 = 7
# Calculation for d100000
d100000 = 2
# Calculation for d1000000
d1000000 = 1

#Product
print(1*1*5*3*7*2*1) # 210
