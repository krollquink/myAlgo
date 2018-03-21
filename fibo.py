#init
f_zero = 0
f_one = 1
multiplier = [ 1 , 1 ,
               1 , 0 ]
def fibo(n):
    #calculate fibo using multiple expo
    fibo = [0,0]
    if n > 1:
        expo = matpow(multiplier,n-1) 
        fibo[0] = (expo[0]*f_one)+(expo[1]*f_zero)
        fibo[1] = (expo[2]*f_one)+(expo[3]*f_zero)
    elif n <= -1:
        return "cant handle negative number"
    else:
        fibo[0] = n
    return fibo[0]

def matrixmulti(b,a):
    #calculate the matrix expo
    c = [0,0,0,0]
    c[0]=(b[0]*a[0])+(b[1]*a[2])
    c[1]=(b[0]*a[1])+(b[1]*a[3])
    c[2]=(b[2]*a[0])+(b[3]*a[2])
    c[3]=(b[2]*a[1])+(b[3]*a[3])
    return c 

def matpow(a, b):
    #calculate mutiplier in power b 
    res = [1,0,0,1]
    cur = a
    while b > 0:
        if b & 1:
            res = matrixmulti(cur,res)
        cur = matrixmulti(cur,cur)
        b >>= 1
    return res
#give result of fibo in nth
print(fibo(10))

