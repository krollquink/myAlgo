


number= list(range(1,100000000+1))
sieve = [True] * 100000000
prime = []

for i in range(1,150000):
    if sieve[i] == True:
        res = number[i]
        for j in range(2,200000000):
            if j * res > len(sieve)-1:
                break
            sieve[(j*res)-1]=False 
    else:
        continue


for j in range(1,len(sieve)-1):
    if sieve[j] == True:
        prime.append(number[j])

print("There are",len(prime)-1,"prime number")
print(prime[10001-1])
