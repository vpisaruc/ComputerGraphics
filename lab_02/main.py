from functions import *
from tkinter import *
from tkinter.messagebox import *
from math import*


# задание
def Show_info():
	showinfo('Задание', 'Нарисовать дом и реализовать функции: перемещение, маштабирование,вращение, отменить последнее'
						'действие, вернуть исходный рисунок.')


def ff(a, b, t):
	return [-71 + a * cos(t) + ox, -71 + b * sin(t) + oy]


def get_ellipse(a, b):
	points = []

	start = -pi / 2  # Head
	end = 3 / 2 * pi  # Head

	step = 0.01

	while start < end:
		points.append(ff(a, b, start))
		start += step
	poin = []
	i = 0
	k = 0
	for i in range(len(points)):
		for j in range(len(points[i])):
			k = points[i][j]
			poin.append(k)

	return poin


# очистка холста
def Clean_canvas():
	canvas.delete("all")

# создание массива для отката на 1 шаг назад
def create_tmp_array(a):
	for i in range(len(a)):
		for j in range(len(a[i])):
			array_back_os[i][j] = a[i][j]



# смещение рисунка по осям
def image_moving(coef_x, coef_y):
	try:
		coef_x = float(coef_x)
		coef_y = float(coef_y)
		Clean_canvas()
		create_tmp_array(array_coordinate_work)

		for j in range(len(array_coordinate_work)):
			for i in range(0,len(array_coordinate_work[j]), 2):
				array_coordinate_work[j][i] = array_coordinate_work[j][i] + coef_x

		for j in range(len(array_coordinate_work)):
			for i in range(1,len(array_coordinate_work[j]), 2):
				array_coordinate_work[j][i] = array_coordinate_work[j][i] + coef_y

		Draw_graphic(array_coordinate_work)
	except ValueError:
		showerror('Error', 'Input numbers in input fields')

# поворот изображения
def image_rotate(angle, x, y):
	try:
		Clean_canvas()
		angle = float(angle)
		x = float(x) + x0
		y = float(y) + y0
		angle = -radians(angle)

		for i in range(len(array_coordinate_work)):
			for j in range(len(array_coordinate_work[i])):
				if j % 2 == 0:
					old_x = array_coordinate_work[i][j]
					array_coordinate_work[i][j] = x + (old_x - x) * cos(angle) - (array_coordinate_work[i][j + 1] - y) * sin(angle)
				else:
					old_y = array_coordinate_work[i][j]
					array_coordinate_work[i][j] = y + (old_x - x) * sin(angle) + (old_y - y) * cos(angle)

		Draw_graphic(array_coordinate_work)
	except ValueError:
		showerror('Error', 'Input numbers in input fields')




# масштабирование изображения
def image_scaling(coef_x, coef_y):
	try:
		coef_x = float(coef_x)
		coef_y = float(coef_y)
		Clean_canvas()
		create_tmp_array(array_coordinate_work)

		zx = (1040 - (array_coordinate_work[0][6] * coef_x - array_coordinate_work[0][0] * coef_x)) / 2
		zy = (640 - (array_coordinate_work[0][1] * coef_y - array_coordinate_work[0][5] * coef_y)) / 2
		smesh_x = array_coordinate_work[0][0] * coef_x - zx
		smesh_y = array_coordinate_work[0][5] * coef_y - zy

		if coef_x == 0 or coef_y == 0:
			showerror('Error', 'Коэффициент масштабирвоания не должен быть нулевым!')
		else:
			for j in range(len(array_coordinate_work)):
				for i in range(0, len(array_coordinate_work[j]), 2):
					array_coordinate_work[j][i] = array_coordinate_work[j][i] * coef_x - smesh_x

			for j in range(len(array_coordinate_work)):
				for i in range(1, len(array_coordinate_work[j]), 2):
					array_coordinate_work[j][i] = array_coordinate_work[j][i] * coef_y - smesh_y

		Draw_graphic(array_coordinate_work)
	except ValueError:
		showerror('Error', 'Input numbers in input fields')

# шаг назад
def Draw_back(b, n):
	if n == 1:
		for i in range(len(b)):
			for j in range(len(b[i])):
				array_coordinate_work[i][j] = b[i][j]

	Clean_canvas()

	# массивы координат
	osn = b[0]
	ln = b[1]
	lw = b[2]
	rw = b[3]
	hw = b[4]
	lw_l1 = b[5]
	lw_l2 = b[6]
	rw_l1 = b[7]
	rw_l2 = b[8]

	# основа дома
	canvas.create_polygon(osn, outline='red', fill='', width=2)
	canvas.create_line(ln, fill='red', width=2)

	# левое окно
	canvas.create_polygon(lw, outline='red', fill = '', width=2)
	canvas.create_line(lw_l1, fill='red', width=2)
	canvas.create_line(lw_l2, fill='red', width=2)

	# правое окно
	canvas.create_polygon(rw, outline='red', fill = '', width=2)
	canvas.create_line(rw_l1, fill='red', width=2)
	canvas.create_line(rw_l2, fill='red', width=2)

	# верхнее окно
	canvas.create_polygon(hw[0], hw[1], hw[2], hw[3], hw[4], hw[5], hw[6], hw[7], outline='red', fill='', width=2)
	canvas.create_line(hw[8], hw[9], hw[10], hw[11], fill='red', width=2)
	canvas.create_line(hw[12], hw[13], hw[14], hw[15], fill='red', width=2)



# отрисовка рисунка
def Draw_graphic(a):
	# массивы координат
	osn = a[0]
	ln = a[1]
	lw = a[2]
	rw = a[3]
	hw = a[4]
	lw_l1 = a[5]
	lw_l2 = a[6]
	rw_l1 = a[7]
	rw_l2 = a[8]

	# основа дома
	canvas.create_polygon(osn, outline='red', fill='', width=2)
	canvas.create_line(ln, fill='red', width=2)

	# левое окно
	canvas.create_polygon(lw, outline='red', fill = '', width=2)
	canvas.create_line(lw_l1, fill='red', width=2)
	canvas.create_line(lw_l2, fill='red', width=2)

	# правое окно
	canvas.create_polygon(rw, outline='red', fill = '', width=2)
	canvas.create_line(rw_l1, fill='red', width=2)
	canvas.create_line(rw_l2, fill='red', width=2)

	# верхнее окно
	canvas.create_polygon(hw[0], hw[1], hw[2], hw[3], hw[4], hw[5], hw[6], hw[7], outline='red', fill='', width=2)
	canvas.create_line(hw[8], hw[9], hw[10], hw[11], fill='red', width=2)
	canvas.create_line(hw[12], hw[13], hw[14], hw[15], fill='red', width=2)


# основная функция
def main():
	root = Tk()
	root.resizable(False, False)
	root.title('Menu')
	root.geometry('1320x640')
	# создание холста для отрисовки примитивов
	global canvas, x0, y0

	x0 = 520
	y0 = 320

	canvas = Canvas(root, width=1040, height=640, bg='#002')
	canvas.pack(side='right')

	# создание статических надписей
	label_x_move = Label(root, text='X ')
	label_x_move.place(x=50, y=50, )
	label_y_move = Label(root, text='Y ')
	label_y_move.place(x=200, y=50)
	label_x_scale = Label(root, text='X ')
	label_x_scale.place(x=50, y=145, )
	label_y_scale = Label(root, text='Y ')
	label_y_scale.place(x=200, y=145)
	label_y_scale = Label(root, text='Y ')
	label_y_scale.place(x=200, y=240)
	label_x_scale = Label(root, text='X ')
	label_x_scale.place(x=50, y=240, )
	label_rotate = Label(root, text='Введите угол поворота в градусах: ')
	label_rotate.place(x=15, y=335)

	# создание полей ввода
	entry_x_move = Entry(root)
	entry_x_move.place(x=15, y=75, width=90)

	entry_y_move = Entry(root)
	entry_y_move.place(x=165, y=75, width=90)

	entry_x_scale = Entry(root)
	entry_x_scale.place(x=15, y=170, width=90)

	entry_y_scale = Entry(root)
	entry_y_scale.place(x=165, y=170, width=90)

	entry_x_rotate = Entry(root)
	entry_x_rotate.place(x=15, y=265, width=90)

	entry_y_rotate = Entry(root)
	entry_y_rotate.place(x=165, y=265, width=90)

	entry_rotate = Entry(root)
	entry_rotate.place(x=210, y=335, width=60)

	# создание кнопок
	btn_task = Button(root, text='Задание', width=37)
	btn_task.bind('<Button-1>', lambda event: Show_info())
	btn_task.place(x=5, y=10)

	btn_move = Button(root, text='Переместить', width=20)
	btn_move.bind('<Button-1>', lambda event: image_moving(entry_x_move.get(), entry_y_move.get()))
	btn_move.place(x=65, y=105)

	btn_scale = Button(root, text='Масштабировать', width=20)
	btn_scale.bind('<Button-1>', lambda event: image_scaling(entry_x_scale.get(), entry_y_scale.get()))
	btn_scale.place(x=65, y=200)

	btn_rotate = Button(root, text='Повернуть', width=20)
	btn_rotate.bind('<Button-1>',
					lambda event:image_rotate(entry_rotate.get(), entry_x_rotate.get(), entry_y_rotate.get()))
	btn_rotate.place(x=65, y=365)

	btn_cancel = Button(root, text='Отменить последнее действие', width=37)
	btn_cancel.bind('<Button-1>', lambda event: Draw_back(array_back_os, 0))
	btn_cancel.place(x=5, y=405)

	btn_return = Button(root, text='Вернуть исходный рисунок', width=37)
	btn_return.bind('<Button-1>', lambda event: Draw_back(array_coordinate_back, 1))
	btn_return.place(x=5, y=445)

	Draw_graphic(array_coordinate_work)

	root.mainloop()


if __name__ == '__main__':
	main()
