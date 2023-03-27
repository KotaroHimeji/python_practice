#ファイルを開く
a_file = open("test.txt", mode = "a", encoding="utf-8")

#ファイルに書き込む
a_file.write ("お腹が空いた\n")
a_file.write("あーした天気になーれ！")
a_file.write ("カレーが食べたい\n")
a_file.write ("スパイスの香りがする\n")

#ファイルを閉じる
a_file.close()