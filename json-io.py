import json     

# 辞書型データ
data={
    "no":5,
    "code":("jas",1,19),
    "scr":"be quick to listen, slow to speak, slownto anger"
}

# ファイルに書き込み
filename = "test.json"
with open(filename,"w") as fp:
    json.dump(data, fp)

# ファイルからの読み出し
with open(filename,"r") as fp:
    r = json.load(fp)
    print(r["no"])
    print(r["code"])
    print("scr = ", r["scr"])