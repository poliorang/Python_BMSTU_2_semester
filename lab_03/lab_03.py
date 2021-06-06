from math import *
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter.messagebox as box

window = Tk()
window.geometry('700x400+500+200')
label_ans = Label()
rootss = []
def phi(x):
    if x >= 2.5:
        return (sqrt(x*5 - 4))
    return ((x*x + 4) / 5)

def f(x):
    return (x*x - 5*x + 4)

def f_extr(x):
    return (2*x - 5)

def segments():
    try:
        a = float(ent_a.get())
        b = float(ent_b.get())
        h = float(ent_h.get())
        roots(a, b, h)
    except:
        box.showinfo('Error', 'Некорректные данные')

def roots(a, b, h):
    try:
        btn_ = Button(window, text='Построить график', widt=75, command=window.quit)
        global all_roots
        global ex
        all_roots = []
        ans = ''
        n = 0

        while (a < b):
            c = a + h
            if f(a)*f(c) > 0:
                a += h
                continue
            dx = 1e10
            x = a
            x_= a
            n1 = 0
            if phi(x) > x:
                while dx > 1e-13:
                    xlast = x
                    x = phi(x)
                    dx = x-xlast
                    n1 += 1
            else:
                while dx > 1e-13:
                    xlast_ = x_
                    x_ = f_extr(x_)
                    dx = x_-xlast_
                    n1 += 1
                ex = x_
            n += 1
            all_roots.append(x)
            str_one = f'[{a:g}; {c:g}]'
            str_zero = f'{n:^30d}' + f'{str_one:^30}' + f'{x:^30g}' + f'{f(x):^25g}' + f'{n1:^55d}' + f'{0:^35}\n'
            print(str_zero)
            ans += str_zero
            a += h
        label_ans.config(text=ans, font='AvantGardeC')
        ex = 2.5
        if all_roots[0]:
            btn_.place(x=10, y=350)
    except:
        box.showinfo('Error', 'Некорректные данные')



label_method = Label(text = 'Метод простых итераций', font='AvantGardeC 14')
label_name = Label(text = 'Уравнение\nx*x - 5*x + 4 = 0  ', font='AvantGardeC')
label_otr = Label(text = 'Отрезок от                                 до                              с шагом', font='AvantGardeC')
label_gran = Label(text = '-'*110)
label_head = Label(text = 'Номер корня    |           [Xi; Xi+1]           |           x           |             f(x)             |  Количество итераций  | Код ошибки', font='AvantGardeC')
label_gran_one = Label(text = '-'*110)
btn = Button(window, text='Решить', fg = "red", font='AvantGardeC', command=lambda: segments())

ent_a = Entry(width=5)
ent_b = Entry(width=5)
ent_h = Entry(width=5)

label_method.place(x=250, y=10)
label_name.place(x=50, y=40)
label_otr.place(x=220, y=40)
label_head.place(x=10, y=110)
label_gran.place(x=10, y=90)
label_gran_one.place(x=10, y=130)
label_ans.place(x=10, y=150)
btn.place(x=220, y=70, widt=400)

ent_a.place(x=300, y=40)
ent_b.place(x=420, y=40)
ent_h.place(x=560, y=40)

window.mainloop()

''' График '''
plt.axis([-4,9,-4,4])
x = np.arange(-4, 8, 0.001)
y = []
for el in x:
    y.append(f(el))

all_y = []
for el in all_roots:
    all_y.append(f(el))

plt.plot(x, y, lw=2)
ax = plt.gca()
ax.spines['bottom'].set_position('center')
plt.plot(all_roots, all_y, 'ko', color='red')
plt.plot(ex, f(ex), 'ko', color='blue')
plt.grid(True)
plt.show()