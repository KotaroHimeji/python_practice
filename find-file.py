import sys
import os
import fnmatch
import datetime
import math

# 引数の確認と使い方の表示
if len(sys.argv) <= 1:
    print("[USAGE] find-file.py [--name] [--wile] [--desc] name")
    sys.exit(0)

# オプションの初期設定
search_mode = "name"
search_func = lambda target, name : (target==name)
name = ""
desc_mode = False

# オプションの判定
for v in sys.argv:
    if v=="--name":
        search_mode = "name"
        search_func = lambda target, name : (target==name)
    elif v=="--wild":
        search_mode = "wild"
        search_func = lambda target, pat : fnmatch.fnmatch(target,pat)
    elif v=="--desc":
        desc_mode = True
    else:
        name = v

# オプションの判定結果を表示
print("+ option")
print("| search_mode: [", search_mode, "]", name)
print("| desc_mode  : ",desc_mode)

# ファイル検索
for root, dirs, files in os.walk("."):
    for fname in files:
        j = search_func(fname, name)
        path = os.path.join(root, fname)
        if j==False:
            continue
        if desc_mode:
            info = os.stat(path)
            kb = math.ceil(info.st_size/1024)
            dt = datetime.datetime.fromtimestamp(info.st_mtime)
            s = "{0}, {1}KB, {2}".format(path, kb, dt.strftime("%Y-%m-%d"))
            print(s)
        else:
            print(path)