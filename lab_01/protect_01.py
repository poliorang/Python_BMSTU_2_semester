# складывать целые числа в троичной
# 2 поля ввода, поле вывода и кнопка сложить
import tkinter as tk

# def check_three(ch):
#     zn = ['0', '1', '2']
#     for el in ch:
#         if el not in zn:
#             return False
#     return True


def plus_(f, s):
    f = (str(f))[::-1]
    s = (str(s))[::-1]
    if len(f) > len(s):
        max = len(f)
        s += '0'*(len(f) - len(s))
    else:
        max = len(s)
        f += '0' * (len(s) - len(f))
    ost = 0
    new = ''
    for i in range(max):
        new += str((int(f[i]) + int(s[i]) + ost) % 3 )
        ost = (int(f[i]) + int(s[i]) + ost) // 3
    if ost != 0:
        new += str(ost)
    output_str.delete(0, tk.END)
    output_str.insert(0, new[::-1])




win = tk.Tk('Сложение в троичной сс')
win.geometry('300x300+700+300')
win.title('Сложение в троичной СС')
input_str_1 = tk.Entry(win, justify = tk.RIGHT)
input_str_2 = tk.Entry(win, justify = tk.RIGHT)
input_str_1.place(x = 50, y = 40)
input_str_2.place(x = 50, y = 100)
output_str = tk.Entry(win, justify = tk.RIGHT)
output_str.place(x = 50, y = 200)
lbl1 = tk.Label(text = 'Result').place(x = 124, y = 178)

tk.Button(text = '+', command = lambda : plus_(input_str_1.get(), input_str_2.get())).place(x = 140, y = 70)

win.mainloop()


cursor =