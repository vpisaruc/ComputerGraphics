from math import*

ox = 520
oy = 320

# большое окно
def ff(a, b, t):
	return [49 + a * cos(t) + ox, -7 + b * sin(t) + oy]
# маленькое окно
def f(a, b, t):
	return [-51 + a * cos(t) + ox, -25 + b * sin(t) + oy]


def get_ellipse_1(a, b):
	points = []

	start = -pi / 2
	end = 3 / 2 * pi

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

def get_ellipse_2(a, b):
	points = []

	start = -pi / 2  # Head
	end = 3 / 2 * pi  # Head

	step = 0.01

	while start < end:
		points.append(f(a, b, start))
		start += step
	poin = []
	i = 0
	k = 0
	for i in range(len(points)):
		for j in range(len(points[i])):
			k = points[i][j]
			poin.append(k)

	return poin

# основание дома
osn = [420, 395, 420, 245, 520, 195, 620, 245, 620, 395]
# линии в основании
ln = [ 420, 245, 620, 245]
# левое окно
lw = get_ellipse_1(20, 39)
# линия левого окна 1
lw_l1 = [470, 275, 470, 315]
lw_l2 = [450, 295, 490, 295]
# правое окно
rw = get_ellipse_2(20, 20)
# линии правого окна
rw_l1 = [590, 313, 550, 313]
rw_l2 = [570, 275, 570, 351]
# верхнее окно
hw = [505, 230, 505, 210, 535, 210, 535, 230, 505, 220, 535, 220, 520, 230, 520, 210]

# изначальные координаты рисунка
array_coordinate_work = []
array_back_os = []
array_coordinate_back = []

array_coordinate_work.append(osn)
array_coordinate_work.append(ln)
array_coordinate_work.append(lw)
array_coordinate_work.append(rw)
array_coordinate_work.append(hw)
array_coordinate_work.append(lw_l1)
array_coordinate_work.append(lw_l2)
array_coordinate_work.append(rw_l1)
array_coordinate_work.append(rw_l2)

for i in range(len(array_coordinate_work)):
    array_back_os.append([])
    for j in range(len(array_coordinate_work[i])):
        array_back_os[i].append(array_coordinate_work[i][j])

for i in range(len(array_coordinate_work)):
    array_coordinate_back.append([])
    for j in range(len(array_coordinate_work[i])):
        array_coordinate_back[i].append(array_coordinate_work[i][j])
