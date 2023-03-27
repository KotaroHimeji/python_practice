while True:
    try:
        weight = float(input("体重は何キロですか？"))
        height = float(input("身長は何センチですか？"))
        bmi = weight / (height/100)**2
        break
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except:
        print("入力に誤りがあります。再度入力をお願いします。")


if bmi < 18.5:
    result = "痩せ型"
elif bmi < 25:
    result = "標準"
elif bmi < 30:
    result = "肥満（軽）"
else:
    result = "肥満（重）"

print("BMI :", bmi)
print("判定 :", result)