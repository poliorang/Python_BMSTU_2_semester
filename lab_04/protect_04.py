import tkinter as tk
from tkinter import *

root = Tk()
c = Canvas(root, width=700, height=800)
c.pack()
set = [] #мн-во точек

input_str = tk.Entry(root, justify = tk.RIGHT, width = 25)
input_str.place(x = 205, y = 55)


def click(event):
    global set
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    if event.x < 40 or event.x > 690 or event.y < 210 or event.y > 750:
        return
    c.create_oval(x1, y1, x2, y2, width=4, tag = 'dot')
    set.append((event.x, event.y))
    print(set)

def is_rectangle(points): # координаты четвертой вершины прямоугольника
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    eps = 4
    if (x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1) < eps:
        x4 = x1 + (x2 - x1) + (x3 - x1)
        y4 = y1 + (y2 - y1) + (y3 - y1)
    elif (x1 - x2) * (x3 - x2) + (y1 - y2) * (y3 - y2) < eps:
        x4 = x2 + (x1 - x2) + (x3 - x2)
        y4 = y2 + (y1 - y2) + (y3 - y2)
    else:
        x4 = x3 + (x1 - x3) + (x2 - x3)
        y4 = y3 + (y1 - y3) + (y2 - y3)

    print(x4, y4)
    if (abs(points[3][0] - x4)) == 0 and (abs(points[3][1] - y4)) == 0:
        print(1)
        return 1
    else:
        print(0)
        return 0




''' Поле'''
c.create_line(33, 210, 690, 210, fill='black', width=3, arrow=LAST)
c.create_line(40, 203, 40, 750, fill='black', width=3, arrow=LAST)
c.create_line(690, 210, 690, 750, fill='black', width=1, dash=(5, 9))
c.create_line(40, 750, 690, 750, fill='black', width=1, dash=(5, 9))
c.create_text(27, 197, text='0', font='AvantGardeC', fill='black')

for i in range(90, 670, 50):
    c.create_line(i, 203, i, 217, fill='black', width=2)
    c.create_line(i, 220, i, 750, fill='black', width=1, dash=(1, 9))
    c.create_text(i, 193, text=f'{i - 40}', font='AvantGardeC', fill='black')

for i in range(260, 730, 50):
    c.create_line(33, i, 47, i, fill='black', width=2)
    c.create_line(50, i, 690, i, fill='black', width=1, dash=(1, 9))
    c.create_text(18, i, text=f'{i - 210}', font='AvantGardeC', fill='black')

c.create_text(680, 190, text='X', font='AvantGardeC', fill='black')
c.create_text(20, 740, text='Y', font='AvantGardeC', fill='black')

Button(root, text='Найти прямоугольники', bg='grey', font='AvantGardeC',
           command=lambda: is_rectangle(set)).place(x=50, y=90, width=620)

c.bind('<1>', click)



c.pack()
root.mainloop()
