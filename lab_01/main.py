from tkinter import *
from functions import*
from tkinter.messagebox import*


# очистка холста
def Clean_label():
	entry_x.delete(0, END)
	entry_y.delete(0, END)

# добавление координат
def Add_coordinate(x, y):
	try:
		x = float(x)
		y = float(y)
		array_x.append(x)
		array_y.append(y)
		list_box.insert(END,('(',x, ',', y,')'))
	except ValueError:
		showerror('Error', 'Input numbers in input fields')

# функция удаления точки
def Delete_dot():
	line_number = list_box.curselection()
	if len(line_number) > 0:
		del array_x[line_number[0]]
		del array_y[line_number[0]]
		list_box.delete(line_number[0])
	else:
		showerror('Error', 'Select item from list')

# удаление всех точек
def Delete_all_dots(s):
	if(s != 0):
		cnt = 0
		while(len(array_x) != 0):
			del array_x[0]
			list_box.delete(cnt)
	else:
		showerror('Error', 'There are no dots')



# функция изменения точки
def Change_dot(new_x, new_y):
	try:
		new_x = float(new_x)
		new_y = float(new_y)
		line_number = list_box.curselection()
		if len(line_number) > 0:
			array_x[line_number[0]] = new_x
			array_y[line_number[0]] = new_y
			list_box.delete(line_number[0])
			list_box.insert(line_number[0], ('(', new_x, ',', new_y, ')'))
		else:
			showerror('Error', 'Select item from list')
	except ValueError:
		showerror('Error', 'Input numbers in input fields')



# функция отрисовки графических примитивов
def draw_graphics(root):
	min_sq_coordinate = find_min_triangle(array_x, array_y)
	if min_sq_coordinate == -1:
		showerror('Error', 'Cant find triangles, add dots')
	elif (min_sq_coordinate == 0):
		showerror('Error', 'Add more dots, there are less then 3 dots')
	else:
		# активация кнопки отчистки canvas
		btn_clean = Button(root, text='Clean canvas', command=Clean_canvas, width=37)
		btn_clean.bind('<Button-1>')
		btn_clean.place(x=5, y=570)

		entry_sq = Entry(root)
		entry_sq.place(x=138, y=330)
		entry_coord = Entry(root)
		entry_coord.place(x=138, y=370)
		entry_sq_circle = Entry(root)
		entry_sq_circle.place(x=138, y=410)
		entry_sq_triangle = Entry(root)
		entry_sq_triangle.place(x=138, y=450)
		entry_coord_center = Entry(root)
		entry_coord_center.place(x=138, y=490)

		coord = min_sq_coordinate[1]

		# координаты треугольника
		x1 = coord[0]
		y1 = coord[1]
		x2 = coord[2]
		y2 = coord[3]
		x3 = coord[4]
		y3 = coord[5]

		# нахождение координат центра описанной окружности
		D = 2*(x1 *(y2 - y3) + x2 * (y3 - y1) + x3*(y1 - y2))
		U_x = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / D
		U_y = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / D

		# стороны треугольника и радиус описанной окружности
		side1 = triangle_side_lenght(coord[0],coord[1],coord[2],coord[3])
		side2 = triangle_side_lenght(coord[0],coord[1],coord[4],coord[5])
		side3 = triangle_side_lenght(coord[2],coord[3],coord[4],coord[5])
		radius = (side1 * side2 * side3) / (4 * triangle_square(side1, side2, side3))
		circle_sq = pi * (radius ** 2)

		global line1, line2, line3, oval1
		# создание треугольника
		line1 = canvas.create_line(coord[0]*20 + 520, -coord[1]*20 + 310, coord[2]*20 + 520, -coord[3]*20 + 310, width = 3,
		fill = 'yellow')
		line2 = canvas.create_line(coord[2]*20 + 520, -coord[3]*20 + 310, coord[4]*20 + 520, -coord[5]*20 + 310, width = 3,
		fill = 'yellow')
		line3 = canvas.create_line(coord[0]*20 + 520, -coord[1]*20 + 310, coord[4]*20 + 520, -coord[5]*20 + 310, width = 3,
		fill = 'yellow')

		entry_coord.insert(0, coord[5])
		entry_coord.insert(0, ' , ')
		entry_coord.insert(0, coord[4])
		entry_coord.insert(0, ' , ')
		entry_coord.insert(0, coord[3])
		entry_coord.insert(0, ' , ')
		entry_coord.insert(0, coord[2])
		entry_coord.insert(0, ' , ')
		entry_coord.insert(0, coord[1])
		entry_coord.insert(0, ' , ')
		entry_coord.insert(0, coord[0])
		entry_sq.insert(0, round(min_sq_coordinate[0],2))
		entry_sq_circle.insert(0, round(circle_sq,2))
		entry_sq_triangle.insert(0, round(triangle_square(side1, side2, side3),2))
		entry_coord_center.insert(0, round(U_x,2))
		entry_coord_center.insert(0, ',')
		entry_coord_center.insert(0, round(U_y,2))

		# отрисовка окружности
		oval1 = canvas.create_oval(((U_x) * 20 + 520 + radius * 20, -(U_y) * 20 + 310 + radius * 20),
		        ((U_x)  * 20 + 520 - radius * 20, -(U_y) * 20 + 310 - radius * 20), width = 3, outline = 'green')


def Clean_canvas():
	canvas.delete(line1)
	canvas.delete(line2)
	canvas.delete(line3)
	canvas.delete(oval1)
	entry_sq = Entry(root, state='readonly')
	entry_sq.place(x=138, y=330)
	entry_coord = Entry(root, state='readonly')
	entry_coord.place(x=138, y=370)
	entry_sq_circle = Entry(root, state='readonly')
	entry_sq_circle.place(x=138, y=410)
	entry_sq_triangle = Entry(root, state='readonly')
	entry_sq_triangle.place(x=138, y=450)
	entry_coord_center = Entry(root, state='readonly')
	entry_coord_center.place(x=138, y=490)

	# дезактивация кнопки Clean canvas
	btn_clean = Button(root, text='Clean canvas', command=Clean_canvas, width=37, state='disabled')
	btn_clean.bind('<Button-1>')
	btn_clean.place(x=5, y=570)




# отрисвока меню
root = Tk()
root.title('Menu')
root.geometry('1320x640')
global canvas, entry_x, entry_y, array_x, array_y, list_box


array_x = []
array_y = []

# создание холста для отрисовки примитивов
canvas = Canvas(root, width = 1040, height = 640, bg = '#002')
canvas.pack(side='right')

# координатная сетка
canvas.create_line(520, 0, 520, 640, width = 1, arrow = FIRST, fill = 'white') # ось Y
canvas.create_line(0, 310, 1040, 310, width = 1, arrow = LAST, fill = 'white') # ось Х

canvas.create_text(533,300, text = '0', fill = 'red')


# создание статических надписей
label_x1 = Label(root, text = 'X coordinate: ')
label_x1.place(x = 0, y = 10, )
label_y1 = Label(root, text = 'Y coordinate: ')
label_y1.place(x = 0, y = 50)
label_sq = Label(root, text='Minimal delta square: ')
label_sq.place(x=0, y=330)
label_sq = Label(root, text='Triangle coordinates(x,y): ')
label_sq.place(x=0, y=370)
label_y1 = Label(root, text = 'Circle square: ')
label_y1.place(x = 0, y = 410)
label_sq = Label(root, text='Triangle square: ')
label_sq.place(x=0, y=450)
label_sq = Label(root, text='Circle center coordinates: ')
label_sq.place(x=0, y=490)
label_changed_x = Label(root, text = 'X')
label_changed_x.place(x = 165, y = 220)
label_changed_y = Label(root, text = 'Y')
label_changed_y.place(x = 218, y = 220)

# создание полей ввода
entry_x = Entry(root)
entry_x.place(x = 80, y = 10)
entry_y = Entry(root)
entry_y.place(x = 80, y = 50)
entry_sq = Entry(root, state='readonly')
entry_sq.place(x=138, y=330)
entry_coord = Entry(root, state='readonly')
entry_coord.place(x=138, y=370)
entry_sq_circle = Entry(root, state='readonly')
entry_sq_circle.place(x=138, y=410)
entry_sq_triangle = Entry(root, state='readonly')
entry_sq_triangle.place(x=138, y=450)
entry_coord_center = Entry(root, state='readonly')
entry_coord_center.place(x=138, y=490)
entry_changed_dot_x = Entry(root)
entry_changed_dot_x.place(x = 160, y = 250, width = 25)
entry_changed_dot_y = Entry(root)
entry_changed_dot_y.place(x = 213, y = 250, width = 25)

# создание кнопок
btn_add = Button(root, text = 'Add coordinate', command = Clean_label, width = 17)
# создание действия для кнопки
btn_add.bind('<Button-1>', lambda event: Add_coordinate(entry_x.get(), entry_y.get()))
btn_add.place(x = 5, y = 90)
btn_del = Button(root, text = 'Delete all dots', width = 17)
# создание действия для кнопки
btn_del.bind('<Button-1>', lambda event: Delete_all_dots(len(array_x)))
btn_del.place(x = 142, y = 90)
btn_clean = Button(root, text = 'Clean canvas', command = Clean_canvas, width = 37, state='disabled')
btn_clean.bind('<Button-1>')
btn_clean.place(x = 5, y = 570)
btn_draw = Button(root, text = 'Result', width = 37)
btn_draw.bind('<Button-1>', lambda event: draw_graphics(root))
btn_draw.place(x = 5, y = 600)
btn_delete = Button(root, text = 'Delete dot', command = Delete_dot, width = 10)
btn_delete.bind('<Button-1>')
btn_delete.place(x = 160, y = 150)
btn_change = Button(root, text = 'Change dot', width = 10)
btn_change.bind('<Button-1>',
                lambda event: Change_dot(entry_changed_dot_x.get(), entry_changed_dot_y.get()))
btn_change.place(x = 160, y = 180)

#создание пустого списка

list_box = Listbox(root, yscrollcommand = '.set')
list_box.place(x = 5, y = 130)

root.mainloop()



