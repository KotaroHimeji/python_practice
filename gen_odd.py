def genOdd(N):
    i = 2
    while i<=N:
        yield i
        i +=2

it = genOdd(30)
for n in it:
    print(n,end=",")