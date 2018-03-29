


number= []
sieve = []
prime = []

for i in range(1,1000000+1):
    number.append(i)
    sieve.append(True)

for i in range(2,9):
    res = 2
    while res *i <1000000+1:
        sieve[( i * res )-1 ]=False 
        res += 1
#print(number)
#print(sieve)


for j in range(0,len(sieve)-1):
    if sieve[j] == True:
        prime.append(number[j])

print("There are",len(prime)-1,"prime number")
print(prime[1:10001])
