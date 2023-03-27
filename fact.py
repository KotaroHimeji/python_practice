# 階乗を求める
def fact(n=8):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(3))
print(fact(10))
print(fact())