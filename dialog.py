# ダイアログを表示するために必要なモジュール
import tkinter.messagebox as mb

# ダイアログを表示
ans = mb.askyesno("質問","ラーメンは好きですか？")
if ans == True:
    # OKボタンだけのダイアログを表示
    mb.showinfo("同意","私も好きです。")
else:
    mb.showinfo("本当？","まさかラーメンが嫌いだなんて")
