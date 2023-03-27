from tkinter import *

w = Canvas(Tk(), width=900,height=400)
w.pack()
for i in range(300):
    x = i *3
    if i%3 == 0:
        w.create_line(x, 0, x, 400, fill="#FF0000")
    elif i%3 == 1:
        w.create_line(x, 0, x, 400, fill="#00ff00")
    else:
        w.create_line(x, 0, x, 400, fill="#0000ff")
mainloop()