#!/usr/bin/env python3
# python3でスクリプトを実行できるようになる。（./find-text.py）

# 複数テキストファイルからテキストファイルを検索するスクリプト
import os 
import sys

# 引数の数を確認 
# 何もキーワードがなければ使い方を表示
if len(sys.argv)<=1:
    print("[USAGE] find-text.py (keyword)")
    sys.exit(0)

# コマンドライン引数からキーワードを得る
keyword = sys.argv[1]

# カレントディレクトリ以下のファイルをすべて処理する
for root, dirs, files in os.walk("."):
    for fi in files:
        result = []
        # テキストファイルを読む
        try:
            path = os.path.join(root,fi)
            with open(path, encoding="utf-8") as f:
                for no, line in enumerate(f):
                    if line.find(keyword) >= 0:
                        line = line.strip()
                        s = "| {0:>4}: {1}".format(no+1, line)
                        result.append(s)
        except:
            continue
        # resultに検索結果があれば結果を表示
        if len(result) > 0:
            print("+ file: {0}".format(fi))
            for li in result:
                print(li)