# tkinterをインポート
from tkinter import *

# テキスト文字数を数える関数
def counter(event):
    s = maintext.get(1.0, END)
    info_label.config(text="{0}文字".format(len(s)))
    
# メインウィンドウを作成
root = Tk()
root.title("テキストカウンタ")

# テキストボックスを作成
maintext = Text(root)
maintext.bind("<Key>", counter)
maintext.pack()

# 文字数を表示するラベルを作成
info_label = Label(root)
info_label.pack()

# メインループ
root.mainloop()