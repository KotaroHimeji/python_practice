def cal(T, n, p):
    per = 0
    if T == 14:
        if n >= 3:
            per = 1
    elif T == 15:
        if n >= 5:
            per = 2
    price = p*(10-per)/10
    return price


w = input("誰が？")
t = int(input("何時？"))
n = int(input("いくつ？"))
p = int(input("何円？"))

print("{0}の支払い金額は{1}円です。".format(w,cal(t,n,p)))