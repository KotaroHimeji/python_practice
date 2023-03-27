def sumArgs(*args):
    V = 0
    for n in args:
        V += n
    return V

def argsDict(**args):
    print(args)

print(sumArgs(1,3,5,6,8))
print(argsDict(a=20,b=4,c =60,d=36))