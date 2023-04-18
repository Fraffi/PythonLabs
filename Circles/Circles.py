'''
На плоскости задано множество точек и множество окружностей. Найти такую окружность,
разница между количествами точек внутри и вне которой минимальна.
'''


from tkinter import *
from tkinter import messagebox

y_coord = []
x_coord = []
y_coord_c = []
x_coord_c = []

def change_mode():
    global count
    count += 1
    if (count % 2 == 0):
        point.config(text = 'Добавить точку', command = add_point)
        change.config(text = '.')
    else:
        point.config(text = 'Добавить окружность', command = add_circle)
        change.config(text = 'O')
    
    

def clear():
	canvas.delete("all")
	x_coord.clear()
	y_coord.clear()
	x_coord_c.clear()
	y_coord_c.clear()

def paint(event):
    global count
    if (count % 2 == 0):
        x, y = (event.x), (event.y)
        canvas.create_oval(x, y, x, y, width = 0, fill = "black")
        if x not in x_coord and y not in y_coord:
            x_coord.append(x)
            y_coord.append(y)
    else:
        x, y = (event.x - 50), (event.y - 50)
        canvas.create_oval(x, y, (x + 100), (y + 100), width = 1, outline = 'black')
        x_coord_c.append(x)
        y_coord_c.append(y)
        

def add_point():
    try:
        x = float(X.get())
        y = float(Y.get())
        if x > 700 or x < 0 or y > 400 or y < 0:
            messagebox.showerror('Ошибка', 'Точка вне зоны холста.')
        canvas.create_oval(x, y, x, y, width = 0, fill = "black")
        if x not in x_coord and y not in y_coord:
            x_coord.append(x)
            y_coord.append(y)
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод')

def add_circle():
    try:
        x = float(X.get())
        y = float(Y.get())
        if x > 700 or x < 0 or y > 400 or y < 0:
            messagebox.showerror('Ошибка', 'Окружность вне зоны холста.')
        canvas.create_oval(x, y, (x + 100), (y + 100), width = 1, outline = 'black')
        x_coord_c.append(x)
        y_coord_c.append(y)
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод')

def find_circle():
    if len(x_coord) < 1 or len(y_coord) < 1 or len(x_coord_c) < 1 or len(y_coord_c) < 1:
        messagebox.showerror('Ошибка', 'Некорректный ввод')
    else:
        count_sum = []
        count_in = 0
        count_out = len(x_coord)
        circles = len(x_coord_c)
        dots = len(x_coord)
        for j in range(circles):
            for i in range(dots):
                if x_coord[i] > x_coord_c[j] and y_coord[i] > y_coord_c[j] and x_coord[i] < (x_coord_c[j] + 100) and y_coord[i] < (y_coord_c[j] + 100):
                    count_in += 1
                    count_out -= 1
            count_sum.append(abs(count_in - count_out))
            count_in = 0
            count_out = len(x_coord)
        for g in range(len(count_sum)):
            if min(count_sum) == count_sum[g]:
                this_is_our_circle_coordinates = g
        xc = x_coord_c[this_is_our_circle_coordinates]
        yc = y_coord_c[this_is_our_circle_coordinates]
        canvas.create_oval(xc, yc, (xc + 100), (yc + 100), width = 1, outline = 'red')
    

# Window
root = Tk()
root.title("Лабораторная работа 4")
root.geometry('740x700')
label_task = Label(text = 'На плоскости задано множество точек и множество окружностей.\nНайти такую окружность, \
разница между количествами точек внутри\nи вне которой минимальна.', font = 12, justify = LEFT)
label_task.place(x = 22, y = 20)
# Entry
X = Entry()
X.place(x = 62, y = 120, width = 100, height = 30)
Y = Entry()
Y.place(x = 220, y = 120, width = 100, height = 30)
text_x = Label(text = "x = ", font = 12)
text_x.place(x = 22, y = 120)
text_y = Label(text = "y = ", font = 12)
text_y.place(x = 180, y = 120)
# Buttons
point = Button(text = "Добавить точку", bg = "light green", activebackground = "dark green", command = add_point)
point.place(x = 355, y = 210, width = 300, height = 50)
count = 0
change = Button(text = ".", bg = "light green", activebackground = "dark green", command = change_mode)
change.place(x = 656, y = 210, width = 50, height = 50)
process = Button(text = "Найти окружность", bg = "light green", activebackground = "dark green", command = find_circle)
process.place(x = 22, y = 210, width = 300, height = 50)
clear = Button(text = "Очистить холст", bg = "light green", activebackground = "dark green", command = clear)
clear.place(x = 355, y = 120, width = 300, height = 50)
# Canvas
canvas = Canvas(width = 700, height = 400, bg = "white")
canvas.place(x = 20, y = 280)
canvas.bind("<Button-1>", paint)
mainloop()
