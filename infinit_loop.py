while True:
    a = input("1つ目は？")
    if a == "" or a == "q": break
    a = int(a)

    b = input("2つ目は？")
    if b == "" or b == "q": break
    b = int(b)

    c = a*b
    print(a, "×", b, "=", c)