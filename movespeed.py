# 車種と最高速度
car_speed = {
    "DBSスーパーレッジーラ":340,"フェラーリ:812GTS":340,
    "マクラーレン720a":341,"フェアレディ":285,
    "アヴェンタドール":355,"ブガッティ・シロン":420
}

# 都市と東京からの距離
sity ={
    "ソウル":1157,"北京":2100,
    "パリキール":3702,"イスラマバード":5991,
    "モスクワ":7497,"ストックホルム":8190
}

# 時間計算
def howlong(dis, speed):
    return round(dis/speed,1)

# 結果出力のための関数
def tokyo_to_sity_by_car(car,speed,sity):
    output = "|" + car
    for name in sorted(sity.keys()):
        dis = sity[name]
        Time  = howlong(dis, speed)
        output += "|{0:>6}".format(Time)
    output += "|" 
    return output

# 表のフォーマットを作る
print("+------+------+------+------+------+------+------+")
print("|車種", end = "")
for name in sorted(sity.keys()):
    print("|", name, end = "")
print("|")
print("+------+------+------+------+------+------+------+")

# 結果を表として出力 
for car,speed in car_speed.items():
    out = tokyo_to_sity_by_car(car,speed,sity)
    print(out)
print("+------+------+------+------+------+------+------+")