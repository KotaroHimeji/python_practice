den = {
    "omuraisu":990,
    "cutstake":1800,
    "childlunch":600,
    "meetspa":990,
    "gapaorice":1200,
    "chickenj":1500
}

#合計を求める
sum = 0
for i in den.values():
    sum += i

#平均点を計算して結果を表示
ave = sum/len(den)
print("合計は{0}円".format(sum))
print("平均は{0}円".format(ave))

#成績データの一覧と平均点との差を表示
fmt = "|{0:<10}|{1:>6}|{2:>6}|"
print("メニュー｜金額｜差額｜")
for name,v in den.items():
    g = v-ave
    g = round(g,1)
    print(fmt.format(name,v,g))