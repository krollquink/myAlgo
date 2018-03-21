
def dice(n):

    f = []
    max = 1000
    f.append(0)
    for i in range(1,max):
        app = 1
        if i > 6:
            app = 0
            for j in range (1,7):
                app += f[i-j] 
        elif i <= 6:
            for j in range (1,i):
                app += f[i-j] 
                
        f.append(app)
    print("number of ways is ",f[n])

#change the number below
dice(610)
