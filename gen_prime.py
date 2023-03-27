def genPrime(N):
    i = 2
    while i<=N:
        tf = True
        for j in range(2,i):
            if i%j==0:
                tf = False
                break
        if (tf):
            yield i
        i += 1

i = genPrime(50)
for j in i:
    print(j,end=",")