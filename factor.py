res = []
def factorize(a):

    half=a//2
    print("half is",half)
    for i in range(1,half+1):
        if a % i == 0:
            if res.count(a//i) == 0:
                res.append(a//i)
            if res.count(i) == 0:
                res.append(i)
    
factorize(600851475143)
print(res)
        
