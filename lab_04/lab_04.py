import tkinter as tk
from tkinter import *
from tkinter import messagebox
from math import *
from itertools import *


def add_(ch):
    input_str.insert(input_str.index(tk.INSERT), ch)


def delete_():
    input_str.delete(0, tk.END)
    output_str.delete(0, tk.END)

def create(entry1, entry2):
    def list_get(rang):
        try:
            list_a_b = [float(x) for x in rang.get().strip().split()]
            # isinstance проверяет приналежность классу
            if len(list_a_b) == 0 or isinstance(list_a_b, (str, type(None))):
                raise ValueError
            return list_a_b
        except:
            messagebox.showerror('Ошибка ввода данных ',
                                 'Некоректные данные.\n'
                                 'Проверьте введенные данные.')

    def triangle_side(a, b, c):
        a_side = hypot(a[0] - b[0], a[1] - b[1])
        b_side = hypot(b[0] - c[0], b[1] - c[1])
        c_side = hypot(a[0] - c[0], a[1] - c[1])
        return a_side, b_side, c_side

    def is_triangle(a, b, c):
        if (a + b) > c and (a + c) > b and (b + c) > a:
            return True
        else:
            return False

    entry_1 = list_get(entry1)
    entry_2 = list_get(entry2)

    '''Проверка на полноту координат'''
    if entry_1 and entry_2:
        if ((len(entry_1) % 2) or (len(entry_2) % 2)):
            messagebox.showerror('Неполные данные',
                                 'Координаты точек введены '
                                 'неполностью.\nПроверьте '
                                 'введенные данные')
            return False

        '''Разделенее на координаты X и Y'''
        entry_1_x = entry_1[::2]
        entry_1_y = entry_1[1::2]

        entry_2_x = entry_2[::2]
        entry_2_y = entry_2[1::2]

        all_entry_x = entry_1_x + entry_2_x
        all_entry_y = entry_1_y + entry_2_y

        entry_1_xy = [(entry_1_x[i], entry_1_y[i])
                      for i in range(len(entry_1_x))]
        entry_2_xy = [(entry_2_x[i], entry_2_y[i])
                      for i in range(len(entry_2_x))]
        rez_xy = None

        ''' Подборка координат теругольника и проверка
            кол-ва точек внутри треугольника из 1 и 2 множества'''

        # itertools.combinations(iterable, [r]) - комбинации длиной r из iterable без повторяющихся элементов
        for trin_xy in combinations(entry_1_xy, 3):
            count_1 = list()
            count_2 = list()
            triangle_sides = triangle_side(*trin_xy)
            if is_triangle(*triangle_sides):
                for i in range(len(entry_1_xy)):
                    first_c = ((trin_xy[0][0] - entry_1_xy[i][0]) * (trin_xy[1][1] - trin_xy[0][1]) -
                               (trin_xy[1][0] - trin_xy[0][0]) * (trin_xy[0][1] - entry_1_xy[i][1]))
                    second_c = ((trin_xy[1][0] - entry_1_xy[i][0]) * (trin_xy[2][1] - trin_xy[1][1]) -
                                (trin_xy[2][0] - trin_xy[1][0]) * (trin_xy[1][1] - entry_1_xy[i][1]))
                    third_c = ((trin_xy[2][0] - entry_1_xy[i][0]) * (trin_xy[0][1] - trin_xy[2][1]) -
                               (trin_xy[0][0] - trin_xy[2][0]) * (trin_xy[2][1] - entry_1_xy[i][1]))
                    if ((first_c > 0 and second_c > 0 and third_c > 0) or
                            (first_c < 0 and second_c < 0 and third_c < 0)):
                        count_1.append(entry_1_xy[i])

                for i in range(len(entry_2_xy)):
                    first_c = ((trin_xy[0][0] - entry_2_xy[i][0]) * (trin_xy[1][1] - trin_xy[0][1]) -
                               (trin_xy[1][0] - trin_xy[0][0]) * (trin_xy[0][1] - entry_2_xy[i][1]))
                    second_c = ((trin_xy[1][0] - entry_2_xy[i][0]) * (trin_xy[2][1] - trin_xy[1][1]) -
                                (trin_xy[2][0] - trin_xy[1][0]) * (trin_xy[1][1] - entry_2_xy[i][1]))
                    third_c = ((trin_xy[2][0] - entry_2_xy[i][0]) * (trin_xy[0][1] - trin_xy[2][1]) -
                               (trin_xy[0][0] - trin_xy[2][0]) * (trin_xy[2][1] - entry_2_xy[i][1]))
                    if ((first_c > 0 and second_c > 0 and third_c > 0) or
                            (first_c < 0 and second_c < 0 and third_c < 0)):
                        count_2.append(entry_2_xy[i])

                if (len(count_1) == len(count_2) and
                        len(count_1) + len(count_2) != 0):
                    rez_xy = trin_xy
                    break

        '''Если не найден треугольник'''
        if rez_xy is None:
            messagebox.showinfo(
                'Треугольник не найден. \n'
                'Попробуйте ввести другие точки')
            return False

        '''Окно для рисования треугольника'''
        draw_root = tk.Toplevel()
        draw_root.grab_set()
        draw_root.geometry('600x650+500+0')
        draw_root.title('Create a picture')

        canv = Canvas(draw_root, width=600, height=600)
        canv.pack()

        '''Маштабирование'''
        xmax = all_entry_x[0]
        xmin = all_entry_x[0]
        ymax = all_entry_y[0]
        ymin = all_entry_y[0]

        for i in range(len(all_entry_x)):
            if all_entry_x[i] > xmax:
                xmax = all_entry_x[i]
            if all_entry_x[i] < xmin:
                xmin = all_entry_x[i]
            if all_entry_y[i] > ymax:
                ymax = all_entry_y[i]
            if all_entry_y[i] < ymin:
                ymin = all_entry_y[i]

        s_x = (600 - 50) / (xmax - xmin)
        s_y = (600 - 50) / (ymax - ymin)
        o_x = -xmin * s_x + 25
        o_y = -ymin * s_y + 25

        '''Прорисовка точек из 1 и 2 множества'''
        for i in range(len(entry_1_x)):
            x = entry_1_x[i] * s_x + o_x
            y = 600 - (entry_1_y[i] * s_y + o_y)
            canv.create_oval(x - 6, y - 6, x + 6, y + 6, fill='#ffc0cb')
        for i in range(len(entry_2_x)):
            x = entry_2_x[i] * s_x + o_x
            y = 600 - (entry_2_y[i] * s_y + o_y)
            canv.create_oval(x - 6, y - 6, x + 6, y + 6, fill='#aaf0d1')

        '''Рисование треугольника'''
        rez_draw_xy = list()
        for i in range(len(rez_xy)):
            rez_draw_xy.append(rez_xy[i][0] * s_x + o_x)
            rez_draw_xy.append(600 - (rez_xy[i][1] * s_y + o_y))

        canv.create_line(rez_draw_xy[0], rez_draw_xy[1], rez_draw_xy[2], rez_draw_xy[3], width=1, fill='black')
        canv.create_line(rez_draw_xy[2], rez_draw_xy[3], rez_draw_xy[4], rez_draw_xy[5], width=1, fill='black')
        canv.create_line(rez_draw_xy[4], rez_draw_xy[5], rez_draw_xy[0], rez_draw_xy[1], width=1, fill='black')

        '''Вывод информации про треугольник '''
        points = Label(draw_root, text='Розовые точки - точки первого множества\n'
                       'Голубые точки - точки второго множества', font='AvantGardeC')
        points.pack()

''' Для DRAW'''

set_one = []
set_two = []

def draw():
    root = Toplevel()
    root.title('Draw')
    c = Canvas(root, width=700, height=800, bg='grey')
    c.pack()
    var = IntVar()

    def click(event):
        global set_one, set_two
        flag = 0
        if event.x < 40 or event.x > 690 or event.y < 210 or event.y > 750:
            return

        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        if var.get():
            c.create_oval(x1, y1, x2, y2, outline='#aaf0d1', fill='#aaf0d1', width=4, tag='dot')
        else:
            c.create_oval(x1, y1, x2, y2, outline='#ffc0cb', fill='#ffc0cb', width=4, tag='dot')

        if var.get():
            flag += 1
        if flag % 3 == 0:
            set_one.append((event.x, event.y))
        else:
            set_two.append((event.x, event.y))
        print(set_one, set_two)

    def points_inside(set1, set2, a, b, c):
        count1 = 0
        count2 = 0
        x1, y1 = a
        x2, y2 = b
        x3, y3 = c

        for dot in set1:
            x0, y0 = dot
            k1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
            k2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
            k3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
            if k1 > 0 and k2 > 0 and k3 > 0 or k1 < 0 and k2 < 0 and k3 < 0:
                count1 += 1

        for dot in set2:
            x0, y0 = dot
            k1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
            k2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
            k3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
            if k1 > 0 and k2 > 0 and k3 > 0 or k1 < 0 and k2 < 0 and k3 < 0:
                count2 += 1

        return count1 == count2 and count1

    def triangle_find(set_one, set_two):
        flag = False
        for i in range(len(set_one) - 2):
            for j in range(i + 1, len(set_one) - 1):
                for k in range(j + 1, len(set_one)):
                    set_without = set_one[:]
                    del set_without[i], set_without[j - 1], set_without[k - 2]
                    if points_inside(set_without, set_two, set_one[i], set_one[j], set_one[k]):
                        flag = True
                        c.create_line(set_one[i], set_one[j], set_one[k], set_one[i], fill='white', width=2,
                                      activefill='lightgreen', tag='tr')
        if not flag:
            messagebox.showinfo('Некорректные данные', 'Треугольники не найдены')

    def clean_triangle():
        triangls = c.find_withtag('tr')
        for tri in triangls:
            c.delete(tri)

    def clean_all():
        global set_one, set_two
        clean_triangle()
        dotts = c.find_withtag('dot')
        for dot in dotts:
            c.delete(dot)
        set_one = []
        set_two = []

    ''' Выбор поля '''
    var.set(0)
    Radiobutton(root, text="Первое множество", fg='white', bg='grey', font='AvantGardeC',
                variable=var, value=0).place(x=280, y=28)
    Radiobutton(root, text="Второе множество", fg='white', bg='grey', font='AvantGardeC',
                variable=var, value=1).place(x=280, y=50)

    ''' Поле-решеточка'''
    c.create_line(33, 210, 690, 210, fill='white', width=3, arrow=LAST)
    c.create_line(40, 203, 40, 750, fill='white', width=3, arrow=LAST)
    c.create_line(690, 210, 690, 750, fill='white', width=1, dash=(5, 9))
    c.create_line(40, 750, 690, 750, fill='white', width=1, dash=(5, 9))
    c.create_text(27, 197, text='0', font='AvantGardeC', fill='white')

    for i in range(90, 670, 50):
        c.create_line(i, 203, i, 217, fill='white', width=2)
        c.create_line(i, 220, i, 750, fill='white', width=1, dash=(1, 9))
        c.create_text(i, 193, text=f'{i - 40}', font='AvantGardeC', fill='white')

    for i in range(260, 730, 50):
        c.create_line(33, i, 47, i, fill='white', width=2)
        c.create_line(50, i, 690, i, fill='white', width=1, dash=(1, 9))
        c.create_text(18, i, text=f'{i - 210}', font='AvantGardeC', fill='white')

    c.create_text(680, 190, text='X', font='AvantGardeC', fill='white')
    c.create_text(20, 740, text='Y', font='AvantGardeC', fill='white')

    Button(root, text='Найти треугольники', bg='grey', font='AvantGardeC',
           command=lambda: triangle_find(set_one, set_two)).place(x=50, y=90, width=620)
    Button(root, text='Удалить треугольники', bg='grey', font='AvantGardeC',
           command=lambda: clean_triangle()).place(x=50, y=120, width=620)
    Button(root, text='Удалить все объекты', bg='grey', font='AvantGardeC',
           command=lambda: clean_all()).place(x=50, y=150, width=620)
    c.bind('<1>', click)

    root.mainloop()


''' Создание окна, строк ввода и вывода, надписей '''
win = tk.Tk()
win.geometry('560x350+500+200')
win.title('Triangle')

lbl_input = Label(win, text = 'Points of the first set', font = 'AvantGardeC')
lbl_input.place(x = 90, y = 35)

lbl_output = Label(win, text = 'Points of the second set', font = 'AvantGardeC')
lbl_output.place(x = 80, y = 82)

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
tk.Button(text = '0', font = 'AvantGardeC', command = lambda : add_('0')).place(x = 300, y = 245, width = 30, height = 65)
tk.Button(text = '.', font = 'AvantGardeC', command = lambda : add_('.')).place(x = 370, y = 245, width = 30, height = 65)
tk.Button(text = '-', font = 'AvantGardeC', command = lambda : add_('-')).place(x = 405, y = 245, width = 30, height = 65)
tk.Button(text = 'C', font = 'AvantGardeC', command = lambda : delete_()).place(x = 440, y = 245, width = 30, height = 65)
tk.Button(text = ' ', font = 'AvantGardeC', command = lambda : add_(' ')).place(x = 335, y = 245, width = 30, height = 65)
tk.Button(text = '<-', command = lambda : input_str.delete(input_str.index(tk.INSERT) - 1, input_str.index(tk.INSERT))).place(x = 475, y = 245, width = 30, height = 65)
tk.Button(text = 'Create a picture', font = 'AvantGardeC', command=lambda : create(input_str, output_str)).place(x = 90, y = 200, width = 130, height = 35)
tk.Button(text = 'Draw points', font = 'AvantGardeC', command=lambda : draw()).place(x = 90, y = 260, width = 130, height = 35)


''' Меню '''
mmenu = Menu(win)

fmenu = Menu(mmenu)
fmenu.add_command(label = 'Clear the first field', command = lambda : input_str.delete(0, tk.END))
fmenu.add_command(label = 'Clear the second field', command = lambda : output_str.delete(0, tk.END))
fmenu.add_command(label = 'Clear both fields', command = lambda : delete_())
fmenu.add_separator()
fmenu.add_command(label = 'Exit', command = exit)
mmenu.add_cascade(label = 'Clean', menu = fmenu)

smenu = Menu(mmenu)
smenu.add_command(label = 'Create a picture', command = lambda : create(input_str, output_str))
smenu.add_command(label = 'Draw points', command = lambda : draw())
mmenu.add_cascade(label = 'Operations', menu = smenu)

thmenu = Menu(mmenu)
thmenu.add_command(label = 'About progpam and author', command = lambda : messagebox.showinfo('About program',
                         'Данная программа предназначена\n'
                                  'для нахождения треугольника \nс вершинами '
                                  'из первого множества, внутри которого '
                                  'находится одинаковое количество точек '
                                  'из первого и второго множеств.\n'
                                  '\nАвтор: Егорова Полина ИУ7-24Б'))
mmenu.add_cascade(label = 'Help', menu = thmenu)

win.config(menu = mmenu)

win.mainloop()
