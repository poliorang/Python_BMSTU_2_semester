from math import *
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from random import *
import tkinter.messagebox as box
from time import *

window = Tk()
window.title('Уточнение корней')
window.geometry('800x400+300+400')
label_ans = Label()
rootss = []
borders = [0, 0]

def f(x):
    return sin(x)

def phi(x):
    return x - f(x)/cos(x)

def solve():
    global borders
    borders = [0, 0]
    try:
        a = float(ent_a.get())
        b = float(ent_b.get())
        borders[0] = a
        borders[1] = b
        roots(a, b)
    except:
        box.showinfo('Error', 'Некорректные данные!')

def roots(a, b):
    # try:
    btn1 = Button(window, text='график', fg='orange', command=window.quit)
    global rootss
    rootss = []
    x = a
    dx = 1e10
    while abs(dx) > 1e-13:
        xlast = x
        x = phi(x)
        dx = x-xlast
    if a <= x <= b:
        rootss.append(x)
    else:
        box.showinfo('Error', 'Слишком большой отрезок!')
        return

    label_ans.config(text=f'x = {rootss[0]}', font='Arial 15')
    btn1.place(x=700, y=200)
    # except:
    #     box.showinfo('Error', 'Некорректные данные!')
label_name = Label(text='Уравнение: sin(x) = 0', font='Arial 20')
label_otr = Label(text='Отрезок от            до', font='Arial 20')
btn = Button(window, text='решить', command=lambda: solve())

ent_a = Entry(width=5)
ent_b = Entry(width=5)

label_name.place(x=250, y=0)
label_otr.place(x=220, y=40)
label_ans.place(x=10, y=110)
btn.place(x=400, y=70)

ent_a.place(x=330, y=41)
ent_b.place(x=420, y=41)

window.mainloop()

delta = (borders[1] - borders[0])/2
plt.axis([borders[0]-delta, borders[1]+delta, -2, 2])
x = np.arange(borders[0]-delta, borders[1]+delta, 0.001)
yr = []
for el in rootss:
    yr.append(f(el))
y = []
for el in x:
    y.append(f(el))
plt.plot(x, y, lw=2)
ax = plt.gca()
# ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.plot(rootss, yr, 'ko', color='red')
plt.grid(True)
plt.show()