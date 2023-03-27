#!/usr/bin/env python3
# web上で足し算をするプログラム
import cgi
import cgitb
cgitb.enable()

#ヘッダの出力
print("Content-Type:text/html; charset=utf-8")
print("")
#送信されたフォームデータを取得する
form = cgi.FieldStorage()

# フォームにv1とv2のデータが含まれるか？
if (not 'v1' in form) or (not 'v2' in form):
    # 含まれないので、フォームを表示
    print("""
    <form>
    <input type="text" name="v1"> + 
    <input type="text" name="v2">
    <input type="submit" name="計算">
    </form>
    """)
else:
    # フォームの値を取得して計算結果を表示
    v1 = form.getvalue("v1")
    v2 = form.getvalue("v2")
    try:
        ans = int(v1)+int(v2)
    except:
        ans = 2
    print("<h1>",ans,"</h1>")
