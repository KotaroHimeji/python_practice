def inzei(p, r, n):
    """又吉、印税だけで3億近く稼いだらしい"""
    
    return p*r*n/100*10000

p = input("本の値段は？")
p = int(p)
r = input("印税率は？")
r = int(r)
n = input("発行部数は何万部？")
n = int(n)

P = inzei(p,r,n)
help(inzei)
print("印税の合計は{0}円です".format(P))