#時給は？
jikyu = input("時給は？")
jikyu = int(jikyu)

#時間は？
t = input("時間は？")
t = int(t)

#週に何回？
n = input("how many times in a week")
n = int(n)

#何週間？
N = 365//7

#年収は
income = jikyu*t*n*N

#結果の表示
msg =  """
時給は{0}円で1日の労働時間は{1}時間、
週に{2}回で、{3}週間分なので、、、
年収は{4}円です。\
"""
print(msg.format(jikyu, t, n, N, income))