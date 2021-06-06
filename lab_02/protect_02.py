# защита второй лабораторной

import tkinter as tk

win = tk.Tk()
win.geometry("400x340+200+300")

q = tk.Text(win, width = 13, height = 20)
q.place(x = 25, y = 25)


def bubblesort(arr, arr_2):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                arr_2[j], arr_2[j+1] = arr_2[j+1], arr_2[j]
                print('1', arr, arr_2)
            elif arr[j] == arr[j + 1]:
                for k in range(len(arr_2[j])):
                    if arr_2[j][k] > arr_2[j + 1][k]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        arr_2[j], arr_2[j + 1] = arr_2[j + 1], arr_2[j]
                        print('2', arr, arr_2, k)
                    break
    print(arr)
    return arr


def st():
    new = q.get(1.0, tk.END)
    elem = ''
    sum = 0
    s = []
    mas = [[]]
    i = 0
    for el in new:
        if el != ' ' and el != '\n':
            elem += el
        elif el == '\n':
            mas[i].append(int(elem))
            sum += int(elem)
            mas.append([])
            i += 1
            s.append(sum)
            sum = 0
            elem = ''
        else:
            mas[i].append(int(elem))
            sum += int(elem)
            elem = ''
    mas.pop()
    bubblesort(s, mas)
    n = ''
    for el in mas:
        for elem in el:
            n += str(elem)
            n += ' '
        n += '\n'
    w.insert(1.0, n)


w = tk.Text(win, width = 13, height = 20)
w.place(x = 285, y = 25)
tk.Button(text = 'go', command = lambda : st()).place(x = 177, y = 67, width = 45, height = 45)

win.mainloop()
