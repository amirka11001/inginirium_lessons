import tkinter

print('start')
win = tkinter.Tk()

canvas = tkinter.Canvas(win, bg='white', width=400, height=400)

for i in range(1, 8, 1):
    canvas.create_line((50 * i, 0), (50 * i, 400), fill='black')
    canvas.create_line((0, 50 * i), (400, 50 * i), fill='black')
canvas.pack()

win.mainloop()
print('stop')