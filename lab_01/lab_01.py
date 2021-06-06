## Егорова Полина ИУ7-24Б - оконное приложение - перевод из семеричной системы счисления в десятичную и обратно

import tkinter as tk
from tkinter import messagebox, Menu, Label

def check_float(x):
    znaki = ['1','2','3','4','5','6','7','8','9','-','+','0','e','.']
    line = str(x)
    num = len(line)

    flag = True
    for i in line: #проверка на допустимые знаки внутри строки
        if not (i in znaki):
            flag = False
    if flag:
        num_e = 0
        for i in line: #подсчет количества 'e' внутри строки
            if i == 'e':
                num_e += 1
        if num_e > 1: #если количество 'e' больше 1, то это строка
            flag = False
        if flag:
            num_t = 0
            for i in line: #подсчет количества '.' внутри строки
                if i == '.':
                    num_t += 1
            if num_t > 1: #если количество '.' больше 1, то это строка
                flag = False
            if flag: #если в строке есть 'e' делю ее на две, иначе не делю
                #если 'e' в строке нет
                if len(line) == 1 and (line[0] == '+' or line[0] == '-' or line[0] == '.'):
                    flag = False
                if flag:
                    if num_e == 0: #+ или - только на первом месте, если строки из одного символа знаков "+","-","." в ней быть не должно
                        for i in range(1,len(line)):
                            if line[i] == '+' or line[i] == '-':
                                flag = False
                    #если 'e' в строке есть, делю строку на две
                    elif num_e == 1:
                        if line.index('e') == 0 or line.index('e') == len(line)-1: #если "е" находится на краях строки
                            flag = False
                        if flag:
                            #если длина строки до или после "е" равна 1 и там находятся только символы "+","-","."
                            if (line.index('e') == 1 and (line[0] == '+' or line[0] == '-' or line[0] == '.'))\
                            or (line.index('e') == len(line) - 2 and (line[len(line) - 1] == '+' or line[len(line) - 1] == '-' or line[len(line) - 1] == '.')):
                                flag = False
                            if flag:
                                for i in range (line.index('e')): #проверка числа перед "е"
                                    #знаки "+","-" могут стоять только на первой позиции строки, точка - где угодно
                                    if i != 0 and (line[i] == '+' or line[i] == '-'):
                                        flag = False
                                    if flag:
                                        #в строкe справа от "е" точек быть не может, заки "+","-" могут находится только на первой позиции в строке
                                        for i in range (line.index('e')+1, len(line)):
                                            if line[i] == '.' or (i>=line.index('e')+2 and(line[i] == '+' or line[i] == '-')):
                                                flag = False
                    else:
                        flag = False
    return flag

def check_seven(x):
    zn = ['0', '1', '2', '3', '4', '5', '6', '.', '-']
    for el in str(x):
        if el not in zn:
            return False
    return True

def add_(ch):
    input_str.insert(input_str.index(tk.INSERT), ch)

def ten_to_seven(number):
    if not check_float(number):
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте правильность введенных данных')
        input_str.delete(0, tk.END)
    else:
        minus = False
        if number[0] == '-':
            number = number[1:]
            minus = True
        number = float(number)
        n_l, n_r = str(number).split('.')
        n_l = int(n_l)
        n_r = int(n_r)
        n_l_7 = ''
        n_r_7 = ''
        # перевод целой части
        while n_l >= 7:
            n_l_7 = str(n_l % 7) + n_l_7
            n_l = n_l // 7
        n_l_7 = str(n_l) + n_l_7
        # перевод дробной части
        lengh = int('1' + '0' * len(str(n_r)))
        n = 0
        while n_r != 0:
            n_r_7 += str((n_r * 7) // lengh)
            n_r = (n_r * 7) % lengh
            n += 1
            if n > 10:
                break
        if n_r == 0:
            number_7 = int(n_l_7)
        else:
            number_7 = float(str(n_l_7) + '.' + str(n_r_7))
        if minus:
            number_7 = -number_7
        output_str.delete(0, tk.END)
        output_str.insert(0, number_7)

def seven_to_ten(number):
    if not check_float(number):
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные')
        input_str.delete(0, tk.END)
    elif not check_seven(number):
        messagebox.showerror('Ошибка ввода данных',
                             'Данное число не является семеричным')
        input_str.delete(0, tk.END)
    else:
        minus = False
        if number[0] == '-':
            number = number[1:]
            minus = True
        number = float(number)
        n_l, n_r = str(number).split('.')
        n_l = int(n_l)
        n_r = int(n_r)
        lengh_1 = len(str(n_l))
        lengh_2 = len(str(n_r))
        n_l_7 = 0
        n_r_7 = 0
        # перевод целой части
        for i in range(lengh_1):
            n_l_7 += (n_l % 10) * (7 ** i)
            n_l = n_l // 10
        # перевод дробной части
        if n_r == 0:
            number_10 = n_l_7
        else:
            n_r = int(str(n_r)[::-1])
            for i in range(1, lengh_2 + 1):
                n_r_7 += (n_r % 10) * (7 ** (-i))
                n_r = n_r // 10
            number_10 = n_l_7 + n_r_7
        if minus:
            number_10 = - number_10
        output_str.delete(0, tk.END)
        output_str.insert(0, number_10)

def delete_():
    input_str.delete(0, tk.END)
    output_str.delete(0, tk.END)

''' Создание окна, строк ввода и вывода, надписей '''
win = tk.Tk()
win.geometry('560x350+500+200')
win.title('7 <--> 10')

lbl_input = Label(win, text = 'Input', font = 'AvantGardeC')
lbl_input.place(x = 136, y = 35)

lbl_output = Label(win, text = 'Output', font = 'AvantGardeC')
lbl_output.place(x = 130, y = 82)

input_str = tk.Entry(win, justify = tk.RIGHT, width = 25)
output_str = tk.Entry(win, justify = tk.RIGHT, width = 25)
input_str.place(x = 35, y = 55)
output_str.place(x = 35, y = 100)

''' Кнопочки '''
tk.Button(text = '1', font = 'AvantGardeC', command = lambda : add_('1')).place(x = 300, y = 35, width = 65, height = 65)
tk.Button(text = '2', font = 'AvantGardeC', command = lambda : add_('2')).place(x = 370, y = 35, width = 65, height = 65)
tk.Button(text = '3', font = 'AvantGardeC', command = lambda : add_('3')).place(x = 440, y = 35, width = 65, height = 65)
tk.Button(text = '4', font = 'AvantGardeC', command = lambda : add_('4')).place(x = 300, y = 105, width = 65, height = 65)
tk.Button(text = '5', font = 'AvantGardeC', command = lambda : add_('5')).place(x = 370, y = 105, width = 65, height = 65)
tk.Button(text = '6', font = 'AvantGardeC', command = lambda : add_('6')).place(x = 440, y = 105, width = 65, height = 65)
tk.Button(text = '7', font = 'AvantGardeC', command = lambda : add_('7')).place(x = 300, y = 175, width = 65, height = 65)
tk.Button(text = '8', font = 'AvantGardeC', command = lambda : add_('8')).place(x = 370, y = 175, width = 65, height = 65)
tk.Button(text = '9', font = 'AvantGardeC', command = lambda : add_('9')).place(x = 440, y = 175, width = 65, height = 65)
tk.Button(text = '0', font = 'AvantGardeC', command = lambda : add_('0')).place(x = 300, y = 245, width = 65, height = 65)
tk.Button(text = '.', font = 'AvantGardeC', command = lambda : add_('.')).place(x = 370, y = 245, width = 30, height = 65)
tk.Button(text = '-', font = 'AvantGardeC', command = lambda : add_('-')).place(x = 405, y = 245, width = 30, height = 65)
tk.Button(text = 'C', font = 'AvantGardeC', command = lambda : delete_()).place(x = 440, y = 245, width = 30, height = 65)
tk.Button(text = '<-', command = lambda : input_str.delete(input_str.index(tk.INSERT) - 1, input_str.index(tk.INSERT))).place(x = 475, y = 245, width = 30, height = 65)
tk.Button(text = '10 --> 7', font = 'AvantGardeC', command = lambda : ten_to_seven(input_str.get())).place(x = 90, y = 200, width = 130, height = 35)
tk.Button(text = '7 --> 10', font = 'AvantGardeC', command = lambda : seven_to_ten(input_str.get())).place(x = 90, y = 260, width = 130, height = 35)


''' Меню '''
mmenu = Menu(win)

fmenu = Menu(mmenu)
fmenu.add_command(label = 'Clear the input field', command = lambda : input_str.delete(0, tk.END))
fmenu.add_command(label = 'Clear the output field', command = lambda : output_str.delete(0, tk.END))
fmenu.add_command(label = 'Clear both fields', command = lambda : delete_())
fmenu.add_separator()
fmenu.add_command(label = 'Exit', command = exit)
mmenu.add_cascade(label = 'Clean', menu = fmenu)

smenu = Menu(mmenu)
smenu.add_command(label = '10 --> 7', command = lambda : ten_to_seven(input_str.get()))
smenu.add_command(label = '7 --> 10', command = lambda : seven_to_ten(input_str.get()))
mmenu.add_cascade(label = 'Operations', menu = smenu)

thmenu = Menu(mmenu)
thmenu.add_command(label = 'About progpam and author', command = lambda : messagebox.showinfo('About program',
                         'Данная программа предназначена\n'
                                  'для нахождения треугольника с вершинами\n'
                                  'из первого множества, внутри которого\n'
                                  'находится одинаковое количество точек\n'
                                  'из первого и второго множеств.\n'
                                  '\n\nАвтор: Егорова Полина ИУ7-24Б\n'))
mmenu.add_cascade(label = 'Help', menu = thmenu)

win.config(menu = mmenu)

win.mainloop()