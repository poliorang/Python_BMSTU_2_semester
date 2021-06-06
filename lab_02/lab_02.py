## Егорова Полина ИУ7-24Б - оконное приложение - время для метода пузырька с флагом

'''
пробегаемся по списку, (с каждой новой итерацией внешнего фора) уменьшая диапозон на 1 с конца
за каждый пробег меняем местами эл-ты, если предыдущий больше следующего
в отличае от обычной сортировки останавливаем внешний фор как только за последний пробег ничего не изменилось
(т.е. когда список уже стал отсортированным)
'''

import tkinter as tk
import random as rm
import time as tm
from tkinter import messagebox, Menu, Label
# from tkinter.ttk import Combobox as cm

def bswf(arr): #BubbleSortWithFlag
    n = len(arr)
    for i in range(n-1):
        flag = True
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
        if flag:
            break
    return arr

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

def error(i, ti):
    if i == 1:
        ent = ent_l1
    if i == 2:
        ent = ent_l2
    if i == 3:
        ent = ent_l3
    ent.delete(0, tk.END)
    for i in range(3):
        ti.append(0.0)
    messagebox.showerror('Ошибка ввода данных',
                         'Проверьте правильность введенных данных')

def error_2(i, com):
    if i == 1:
        ent = ent_l1
    if i == 2:
        ent = ent_l2
    if i == 3:
        ent = ent_l3
    ent.delete(0, tk.END)
    com.delete(0, tk.END)
    com.insert(0, '5')
    messagebox.showerror('Ошибка ввода данных',
                         'Введите целое положительное число')

def error_3(i, ran):
    if i == 1:
        ent = ent_l1
    if i == 2:
        ent = ent_l2
    if i == 3:
        ent = ent_l3
    ent.delete(0, tk.END)
    ran.delete(0, tk.END)
    ran.insert(0, '-50 50')
    messagebox.showerror('Ошибка ввода данных',
                         'Введите два числа через пробел')

def create(num):
    if num == 1:
        ran = range_1
        com = rng_1
        ent = ent_l1
    if num == 2:
        ran = range_2
        com = rng_2
        ent = ent_l2
    if num == 3:
        ran = range_3
        com = rng_3
        ent = ent_l3
    l = []
    pr = False
    for el in ran.get():
        if el == ' ':
            pr = True
    if pr:
        minn, maxx = ran.get().split()
        if minn == '-' or maxx == '-' or (check_float(minn) and check_float(maxx)):
            min = int(minn)
            max = int(maxx)
            if not check_float(com.get()) or int(com.get()) < 0:
                error_2(num, com)
            else:
                for i in range(int(com.get())):
                    l.append(round(rm.uniform(min, max), 2))
                ent.delete(0, tk.END)

            for el in l:
                ent.insert(0, str(el) + ' ')
        else:
            error_3(num, ran)
    else:
        error_3(num, ran)

def generate(num):
    if num == 1:
        com = rng_1
        ent = ent_l1
    if num == 2:
        com = rng_2
        ent = ent_l2
    if num == 3:
        com = rng_3
        ent = ent_l3
    com.delete(0, tk.END)
    com.insert(0, rm.randint(1, 10))
    ent.delete(0, tk.END)
    create(num)

def generate_all():
    for num in range(1, 4):
        generate(num)

def clear(num):
    if num == 1:
        com = rng_1
        ent = ent_l1
    if num == 2:
        com = rng_2
        ent = ent_l2
    if num == 3:
        com = rng_3
        ent = ent_l3
    com.delete(0, tk.END)
    com.insert(0, '5')
    ent.delete(0, tk.END)

def clear_all():
    for num in range(1, 4):
        clear(num)

def result_1(m):
    Label(win, text=m[1], font='AvantGardeC').place(x=500, y=320)
    Label(win, text=m[0], font='AvantGardeC').place(x=500, y=350)
    Label(win, text=m[2], font='AvantGardeC').place(x=500, y=380)

def result_2(m):
    Label(win, text=m[1], font='AvantGardeC').place(x=550, y=320)
    Label(win, text=m[0], font='AvantGardeC').place(x=550, y=350)
    Label(win, text=m[2], font='AvantGardeC').place(x=550, y=380)

def result_3(m):
    Label(win, text=m[1], font='AvantGardeC').place(x=595, y=320)
    Label(win, text=m[0], font='AvantGardeC').place(x=595, y=350)
    Label(win, text=m[2], font='AvantGardeC').place(x=595, y=380)

def time_():
    ti_1 = []
    ti_2 = []
    ti_3 = []
    for i in range(1, 4):
        if i == 1:
            ti = ti_1
            ent = ent_l1
        if i == 2:
            ti = ti_2
            ent = ent_l2
        if i == 3:
            ti = ti_3
            ent = ent_l3
        mass = ent.get()
        new = []
        new_el = ''
        flag = True
        elem = False
        for el in mass:
            elem = True
            if el in ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                new_el += el
            elif el == ' ':
                if not check_float(new_el):
                    error(i, ti)
                    break
                else:
                    new.append(float(new_el))
                    new_el = ''
            else:
                error(i, ti)
                flag = False
                break
        if flag and elem:
            start = tm.time()
            sorted_list = bswf(new)
            stop = tm.time()
            ti.append(round((stop - start) * 1e6, 2))
            start = tm.time()
            double_sort = bswf(sorted_list)
            stop = tm.time()
            ti.append(round((stop - start) * 1e6, 2))
            rev_sort_list = list(reversed(double_sort))
            start = tm.time()
            bswf(rev_sort_list)
            stop = tm.time()
            ti.append(round((stop - start) * 1e6, 2))
        if not elem:
            for i in range(3):
                ti.append(0.0)
        # print(ti_1, ti_2, ti_3)
    result_1(['         ', '          ', '         '])
    result_1(ti_1)
    result_2(['         ', '          ', '         '])
    result_2(ti_2)
    result_3(['          ', '         ', '         '])
    result_3(ti_3)

win = tk.Tk()
win.geometry('660x450+500+200')
win.title('Time for bubble sort with flag')

''' Надписи и поле ввода-вывода '''
lbl_one = Label(win, text = 'List \ndimension', font = 'AvantGardeC').place(x = 27, y = 20)
lbl_two = Label(win, text = 'List elements', font = 'AvantGardeC').place(x = 290, y = 32)
lbl_th = Label(win, text = 'Range of values', font = 'AvantGardeC').place(x = 525, y = 32)

lbl_n1 = Label(win, text = 'N1', font = 'AvantGardeC').place(x = 10, y = 70)
lbl_n2 = Label(win, text = 'N2', font = 'AvantGardeC').place(x = 10, y = 100)
lbl_n3 = Label(win, text = 'N3', font = 'AvantGardeC').place(x = 10, y = 130)

rng_1 = tk.Entry(win, justify = tk.RIGHT, width = 6, font = 'AvantGardeC')
rng_1.insert(0, str(5))
rng_1.place(x = 40, y = 66)

rng_2 = tk.Entry(win, justify = tk.RIGHT, width = 6, font = 'AvantGardeC')
rng_2.insert(0, str(5))
rng_2.place(x = 40, y = 96)

rng_3 = tk.Entry(win, justify = tk.RIGHT, width = 6, font = 'AvantGardeC')
rng_3.insert(0, str(5))
rng_3.place(x = 40, y = 126)

# combo_1 = cm(win, justify = tk.CENTER, width = 3, font = 'AvantGardeC')
# combo_1['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# combo_1.current(4)
# combo_1.place(x = 40, y = 66)
#
# combo_2 = cm(win, justify = tk.CENTER, width = 3, font = 'AvantGardeC')
# combo_2['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# combo_2.current(4)
# combo_2.place(x = 40, y = 96)
#
# combo_3 = cm(win, justify = tk.CENTER, width = 3, font = 'AvantGardeC')
# combo_3['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# combo_3.current(4)
# combo_3.place(x = 40, y = 126)

ent_l1 = tk.Entry(win, justify = tk.RIGHT, width = 46, font = 'AvantGardeC')
ent_l1.place(x = 150, y = 65)
ent_l2 = tk.Entry(win, justify = tk.RIGHT, width = 46, font = 'AvantGardeC')
ent_l2.place(x = 150, y = 95)
ent_l3 = tk.Entry(win, justify = tk.RIGHT, width = 46, font = 'AvantGardeC')
ent_l3.place(x = 150, y = 125)

range_1 = tk.Entry(win, justify = tk.RIGHT, width = 10, font = 'AvantGardeC')
range_1.place(x = 530, y = 65)
range_2 = tk.Entry(win, justify = tk.RIGHT, width = 10, font = 'AvantGardeC')
range_2.place(x = 530, y = 95)
range_3 = tk.Entry(win, justify = tk.RIGHT, width = 10, font = 'AvantGardeC')
range_3.place(x = 530, y = 125)

range_1.insert(0, '-50 50')
range_2.insert(0, '-50 50')
range_3.insert(0, '-50 50')

lbl_n11 = Label(win, text = 'for \nlist N1', font = 'AvantGardeC 14')
lbl_n11.place(x = 27, y = 180)
lbl_n22 = Label(win, text = 'for \nlist N2', font = 'AvantGardeC 14')
lbl_n22.place(x = 27, y = 270)
lbl_n33 = Label(win, text = 'for \nlist N3', font = 'AvantGardeC 14')
lbl_n33.place(x = 27, y = 360)

lbl_res_one = Label(win, text = 'Упорядоченный массив', font = 'AvantGardeC').place(x = 311, y = 320)
lbl_res_two = Label(win, text = 'Случайный массив', font = 'AvantGardeC').place(x = 342, y = 350)
lbl_res_th = Label(win, text = 'Обратно упорядоченный массив', font = 'AvantGardeC').place(x = 250, y = 380)

lbl_res_one_n = Label(win, text = 'N1', font = 'AvantGardeC').place(x = 510, y = 290)
lbl_res_two_n = Label(win, text = 'N2', font = 'AvantGardeC').place(x = 555, y = 290)
lbl_res_th_n = Label(win, text = 'N3', font = 'AvantGardeC').place(x = 602, y = 290)

result_1([0.0, 0.0, 0.0])
result_2([0.0, 0.0, 0.0])
result_3([0.0, 0.0, 0.0])


''' Кнопочки '''
tk.Button(text = 'create', font = 'AvantGardeC 10', command = lambda : create(1)).place(x = 100, y = 67, width = 45, height = 25)
tk.Button(text = 'create', font = 'AvantGardeC 10', command = lambda : create(2)).place(x = 100, y = 97, width = 45, height = 25)
tk.Button(text = 'create', font = 'AvantGardeC 10', command = lambda : create(3)).place(x = 100, y = 127, width = 45, height = 25)

tk.Button(text = 'Generate', font = 'AvantGardeC 11', command = lambda : generate(1)).place(x = 95, y = 178, width = 115, height = 25)
tk.Button(text = 'Clear', font = 'AvantGardeC 11', command = lambda : clear(1)).place(x = 95, y = 207, width = 115, height = 25)

tk.Button(text = 'Generate', font = 'AvantGardeC 11', command = lambda : generate(2)).place(x = 95, y = 268, width = 115, height = 25)
tk.Button(text = 'Clear', font = 'AvantGardeC 11', command = lambda : clear(2)).place(x = 95, y = 297, width = 115, height = 25)

tk.Button(text = 'Generate', font = 'AvantGardeC 11', command = lambda : generate(3)).place(x = 95, y = 358, width = 115, height = 25)
tk.Button(text = 'Clear', font = 'AvantGardeC 11', command = lambda : clear(3)).place(x = 95, y = 387, width = 115, height = 25)

tk.Button(text = 'Generate all', font = 'AvantGardeC 11', command = lambda : \
    generate_all()).place(x = 245, y = 178, width = 185, height = 25)
tk.Button(text = 'Clear all', font = 'AvantGardeC 11', command = lambda : \
    clear_all()).place(x = 435, y = 178, width = 185, height = 25)
tk.Button(text = 'Sort and calculate time', font = 'AvantGardeC 11', fg = "red", command = lambda : \
    time_()).place(x = 245, y = 207, width = 376, height = 25)
tk.Button(text = 'Exit', font = 'AvantGardeC 11', command = lambda : \
    exit()).place(x = 245, y = 238, width = 376, height = 25)


''' Менюха '''
mmenu = Menu(win)

fmenu = Menu(mmenu)
fmenu.add_command(label = 'Create N1', command = lambda : create(1))
fmenu.add_command(label = 'Create N2', command = lambda : create(2))
fmenu.add_command(label = 'Create N3', command = lambda : create(3))
mmenu.add_cascade(label = 'Create for a given size', menu = fmenu)

smenu = Menu(mmenu)
smenu.add_command(label = 'Generate the first list', command = lambda : generate(1))
smenu.add_command(label = 'Generate the second list', command = lambda : generate(2))
smenu.add_command(label = 'Generate the third list', command = lambda : generate(2))
smenu.add_separator()
smenu.add_command(label = 'Generate all', command = lambda : generate_all())
mmenu.add_cascade(label = 'Generate', menu = smenu)

tmenu = Menu(mmenu)
tmenu.add_command(label = 'Clear the first list', command = lambda : clear(1))
tmenu.add_command(label = 'Clear the second list', command = lambda : clear(2))
tmenu.add_command(label = 'Clear the third list', command = lambda : clear(3))
tmenu.add_separator()
tmenu.add_command(label = 'Clear all', command = lambda : clear_all())
mmenu.add_cascade(label = 'Clear', menu = tmenu)

fomenu = Menu(mmenu)

fomenu.add_command(label = 'About program and author', command = lambda : messagebox.showinfo('About program',
                         'Данная программа вычисляет время '
                         'сортировки списков разных '
                         'размерностей методом сортировки '
                         'пузырька с флагом '
                         '\nЕгорова Полина ИУ7-24Б'))
fomenu.add_separator()
fomenu.add_command(label = 'Exit', command = lambda : exit())
mmenu.add_cascade(label = 'Help', menu = fomenu)

win.config(menu = mmenu)

win.mainloop()
