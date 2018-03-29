k = []
for i in range(1,101):
    k.append(i)

total = 0
totalz = 0
for i in range(0,len(k)):
    total += k[i]
    totalz += k[i]*k[i]
   


print(total*total)
print(totalz)
print((total*total)-totalz)
