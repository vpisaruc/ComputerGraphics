from  functions import*
from tkinter import*
from tkinter.messagebox import*

# задание
def Show_info():
	showinfo('Задание', 'Нарисовать дом и реализовать функции: перемещение, маштабирование,вращение, отменить последнее'
	                    'действие, вернуть исходный рисунок.')

# очистка холста
def Clean_canvas():
	canvas.delete("all")

# отрисовка рисунка
def Draw_graphic():
	# основа дома
	canvas.create_polygon(420, 395, 420, 245, 520, 195, 620, 245, 620, 395, outline = 'red', fill = '' ,width = 2)
	canvas.create_line(420, 245, 620, 245, fill = 'red', width = 2)

	# левое окно
	canvas.create_oval(450, 275, 490, 315, outline = 'red', width = 2)
	canvas.create_line(470, 275, 470, 315, fill = 'red', width = 2)
	canvas.create_line(450, 295, 490, 295, fill = 'red', width = 2)

	# правое окно
	canvas.create_oval(590, 275, 550, 351, outline = 'red', width = 2)
	canvas.create_line(590, 313, 550, 313, fill = 'red', width = 2)
	canvas.create_line(570, 275, 570, 351, fill = 'red', width = 2)

	# верхнее окно
	canvas.create_polygon(505, 230, 505, 210, 535, 210, 535, 230, outline = 'red', fill = '' ,width = 2)
	canvas.create_line(505, 220, 535, 220, fill = 'red', width = 2)
	canvas.create_line(520, 230, 520, 210, fill = 'red', width = 2)


# основная функция
def main():
	root = Tk()
	root.resizable(False,False)
	root.title('Menu')
	root.geometry('1320x640')
	# создание холста для отрисовки примитивов
	global canvas
	canvas = Canvas(root, width=1040, height=640, bg='#002')
	canvas.pack(side='right')

	# создание статических надписей
	label_x_move = Label(root, text = 'X ')
	label_x_move.place(x = 50, y = 50, )
	label_y_move = Label(root, text = 'Y ')
	label_y_move.place(x = 200, y = 50)
	label_x_scale = Label(root, text = 'X ')
	label_x_scale.place(x = 50, y = 145, )
	label_y_scale = Label(root, text = 'Y ')
	label_y_scale.place(x = 200, y = 145)
	label_rotate = Label(root, text = 'Введите угол поворота в градусах: ')
	label_rotate.place(x = 15, y = 240)

	# создание полей ввода
	entry_x_move = Entry(root)
	entry_x_move.place(x = 15, y = 75, width = 90)

	entry_y_move = Entry(root)
	entry_y_move.place(x = 165, y = 75, width = 90)

	entry_x_scale = Entry(root)
	entry_x_scale.place(x = 15, y = 170, width = 90)

	entry_y_scale = Entry(root)
	entry_y_scale.place(x = 165, y = 170, width = 90)

	entry_rotate = Entry(root)
	entry_rotate.place(x = 210, y = 240, width = 60)

	# создание кнопок
	btn_task = Button(root, text='Задание', width=37)
	btn_task.bind('<Button-1>',lambda event: Show_info())
	btn_task.place(x=5, y=10)

	btn_move = Button(root, text = 'Переместить', width = 20)
	btn_move.bind('<Button-1>')
	btn_move.place(x = 65, y = 105)

	btn_scale = Button(root, text = 'Масштабировать', width = 20)
	btn_scale.bind('<Button-1>')
	btn_scale.place(x = 65, y = 200)

	btn_rotate = Button(root, text = 'Повернуть', width = 20)
	btn_rotate.bind('<Button-1>')
	btn_rotate.place(x = 65, y = 270)

	btn_cancel = Button(root, text = 'Отменить последнее действие', width = 37)
	btn_cancel.bind('<Button-1>')
	btn_cancel.place(x = 5, y = 310)

	btn_return = Button(root, text = 'Вернуть исходный рисунок', width = 37)
	# btn_return.bind('<Button-1>', lambda event: draw_graphics(root))
	btn_return.place(x = 5, y = 350)

	Draw_graphic()

	root.mainloop()

if __name__ == '__main__':
	main()