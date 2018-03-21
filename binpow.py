def binpow(a, b):
    res = 1
    cur = a
    while b > 0:
        if b & 1:
            res *= cur
            print("res is",res)

        cur *= cur
        print("cur is",cur)
        b >>= 1
    return res

print(binpow(2,2))
