# テキストからキーワードを探す
key = "！"
# 1行ずつ文章の読み出しを行う
with open("test.txt",encoding="utf-8") as tf:
    for i,line in enumerate(tf):
        if line.find(key)>=0:
            print(i+1, ":", line)