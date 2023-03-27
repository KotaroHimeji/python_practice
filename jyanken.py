import random


print("--じゃんけんをしましょう--")
hand = ["グー","チョキ","パー"]
for i,h in enumerate(hand):
    print(i,":",h)
print(3,":終了")
print("----------------------")


while True:
# じゃんけんで出す手を決める（システム側）
    sys = random.randint(0,2)
    sys_hand = hand[sys]

# じゃんけんで出す手を決める（ユーザー）
    user = int(input("何を出す？(1~3の中から選択)"))

# 勝敗判定
    if user==3:
        print("""
        じゃんけんを終了しました。
        """)
        break
    else:
        user_hand = hand[user]
        flag = user-sys
        if flag==0:
            result = "あいこ"
        elif (flag+1)%3==0:
            result = "勝ち"
        else:
            result = "負け"

        print("""
        自分：{0}
        相手：{1}
        貴方の{2}です
        """.format(user_hand, sys_hand,result))