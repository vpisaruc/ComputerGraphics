from functions import *
from tkinter import *
from tkinter.messagebox import *
from math import*


# задание
def Show_info():
	showinfo('Задание', 'Нарисовать дом и реализовать функции: перемещение, маштабирование,вращение, отменить последнее'
						'действие, вернуть исходный рисунок.')


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
		x = float(x)
		y = float(y)
		if angle >= 0:
			angle = (angle * pi)/180     # перевод градусов в радианы
		else:
			angle = -(angle * pi)/180

		print(array_coordinate_work)

		for i in range(len(array_coordinate_work)):
			for j in range(0, len(array_coordinate_work[i]), 2):
				array_coordinate_work[i][j] = (array_coordinate_work[i][j] - x)* cos(angle) - \
											  (array_coordinate_work[i][j + 1] - y) * sin(angle)
				array_coordinate_work[i][j+1] = (array_coordinate_work[i][j] - x) * sin(angle) + \
										  (array_coordinate_work[i][j + 1] - y) * cos(angle)

		for i in range(len(array_coordinate_work)):
			for j in range(0, len(array_coordinate_work[i]), 2):
				array_coordinate_work[i][j] = array_coordinate_work[i][j] + x
				array_coordinate_work[i][j+1] = array_coordinate_work[i][j+1] + y

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
	lw = b[1]
	rw = b[2]
	hw = b[3]

	# основа дома
	canvas.create_polygon(osn[0], osn[1], osn[2], osn[3], osn[4],
						  osn[5], osn[6], osn[7], osn[8], osn[9], outline='red', fill='', width=2)
	canvas.create_line(osn[10], osn[11], osn[12], osn[13], fill='red', width=2)

	# левое окно
	canvas.create_oval(lw[0], lw[1], lw[2], lw[3], outline='red', width=2)
	canvas.create_line(lw[4], lw[5], lw[6], lw[7], fill='red', width=2)
	canvas.create_line(lw[8], lw[9], lw[10], lw[11], fill='red', width=2)

	# правое окно
	canvas.create_oval(rw[0], rw[1], rw[2], rw[3], outline='red', width=2)
	canvas.create_line(rw[4], rw[5], rw[6], rw[7], fill='red', width=2)
	canvas.create_line(rw[8], rw[9], rw[10], rw[11], fill='red', width=2)

	# верхнее окно
	canvas.create_polygon(hw[0], hw[1], hw[2], hw[3], hw[4], hw[5], hw[6], hw[7], outline='red', fill='', width=2)
	canvas.create_line(hw[8], hw[9], hw[10], hw[11], fill='red', width=2)
	canvas.create_line(hw[12], hw[13], hw[14], hw[15], fill='red', width=2)



# отрисовка рисунка
def Draw_graphic(a):
	# массивы координат
	osn = a[0]
	lw = a[1]
	rw = a[2]
	hw = a[3]

	# основа дома
	canvas.create_polygon(osn[0], osn[1], osn[2], osn[3], osn[4],
						  osn[5], osn[6], osn[7], osn[8], osn[9], outline='red', fill='', width=2)
	canvas.create_line(osn[10], osn[11], osn[12], osn[13], fill='red', width=2)

	# левое окно
	canvas.create_oval(lw[0], lw[1], lw[2], lw[3], outline='red', width=2)
	canvas.create_line(lw[4], lw[5], lw[6], lw[7], fill='red', width=2)
	canvas.create_line(lw[8], lw[9], lw[10], lw[11], fill='red', width=2)

	# правое окно
	canvas.create_oval(rw[0], rw[1], rw[2], rw[3], outline='red', width=2)
	canvas.create_line(rw[4], rw[5], rw[6], rw[7], fill='red', width=2)
	canvas.create_line(rw[8], rw[9], rw[10], rw[11], fill='red', width=2)

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
	global canvas, array_coordinate_work, array_back_os

	array_back_os = [[420, 395, 420, 245, 520, 195, 620, 245, 620, 395, 420, 245, 620, 245],
					 [450, 275, 490, 315,470, 275, 470, 315, 450, 295, 490, 295],
					 [590, 275, 550, 351, 590, 313, 550, 313, 570, 275, 570, 351],
					 [505, 230, 505, 210, 535, 210, 535, 230, 505, 220, 535, 220, 520, 230, 520, 210]]

	# изначальные координаты рисунка
	array_coordinate_work = [[420, 395, 420, 245, 520, 195, 620, 245, 620, 395, 420, 245, 620, 245],
							 [450, 275, 490, 315,470, 275, 470, 315, 450, 295, 490, 295],
							 [590, 275, 550, 351, 590, 313, 550, 313, 570, 275, 570, 351],
							 [505, 230, 505, 210, 535, 210, 535, 230, 505, 220, 535, 220, 520, 230, 520, 210]]

	# координаты  для возвращения рисунка в изначальное состояние
	array_coordinate_back = [[420, 395, 420, 245, 520, 195, 620, 245, 620, 395, 420, 245, 620, 245],
							 [450, 275, 490, 315,470, 275, 470, 315, 450, 295, 490, 295],
							 [590, 275, 550, 351, 590, 313, 550, 313, 570, 275, 570, 351],
							 [505, 230, 505, 210, 535, 210, 535, 230, 505, 220, 535, 220, 520, 230, 520, 210]]

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
