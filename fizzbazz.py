for i in range(50):
    if i%15==0:
        print("fizzbazz")
        continue
    if i%3 == 0:
        print("fizz")
        continue
    if i%5 == 0:
        print("bazz")
        continue
    print(i)
    