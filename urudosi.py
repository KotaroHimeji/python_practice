tosi = input("年は？")
tosi = int(tosi)

msg = "{0}年は閏年ではない"
if tosi%4 == 0:
    if tosi%100 != 0:
        msg = "{0}年は閏年である"
    else:    
        if tosi%400 == 0:
            msg = "{0}年は閏年である"

print(msg.format(tosi))




