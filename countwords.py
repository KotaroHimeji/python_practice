#単語の出現回数をカウント
text = """
Keep on asking, and it will be given you;
Keep on seeking, and you will find;
Keep on knocking , and it will be opened to you;
for everyone asking receives, and everyone seeking find,
and to everyone knocking,it will be opened.
"""

#単語を区切る
text = text.replace(',','')
text = text.replace(';','')
text = text.replace('.','')
word = text.split()

#単語を数える
counter = {}
for w in word:
    w = w.lower()
    if w in counter:
        counter[w] += 1
    else:  
        counter[w] = 1         

# 結果を表示
for w,n in counter.items():
    print(w, n)
