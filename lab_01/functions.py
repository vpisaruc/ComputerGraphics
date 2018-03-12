from math import*

# class for drawing triangle and round
def triangle_side_lenght(x1,y1,x2,y2):
    return abs(sqrt(pow((x2 - x1),2) + pow((y2 - y1),2)))

# If triangle exist return 1 else return 0
def triangle_condition(x1, y1, x2, y2, x3, y3):
    side1 = triangle_side_lenght(x1, y1, x2, y2)
    side2 = triangle_side_lenght(x2, y2, x3, y3)
    side3 = triangle_side_lenght(x1, y1, x3, y3)

    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return 1
    else:
        return 0

def triangle_square(side1, side2, side3):
    half_perimetr = (side1 + side2 + side3)/2
    square = sqrt(half_perimetr * (half_perimetr - side1) * (half_perimetr - side2) * (half_perimetr - side3))
    return square


def find_min_triangle(array_x, array_y):

    array_triangles = []    # array for triangles

    if len(array_x) < 3 or len(array_y) < 3:
        return 0
    else:
        # filling array with points
        for i in range(len(array_x)):
            for j in range(len(array_x)):
                for z in range(len(array_x)):
                    array_triangle_points = []  # array for triangle coordinate points [(x,y),(x,y),...]
                    point1_x = array_x[i]
                    point1_y = array_y[i]
                    array_triangle_points.append(point1_x)
                    array_triangle_points.append(point1_y)
                    point2_x = array_x[j]
                    point2_y = array_y[j]
                    array_triangle_points.append(point2_x)
                    array_triangle_points.append(point2_y)
                    point3_x = array_x[z]
                    point3_y = array_y[z]
                    array_triangle_points.append(point3_x)
                    array_triangle_points.append(point3_y)
                    array_triangles.append(array_triangle_points)

        # remove from array extra coordinates

        cnt = 0    # counter
        average_area_array = []
        index_array = []

        for i in range(0, len(array_triangles) - 1, 1):
            x1 = array_triangles[i][0]
            y1 = array_triangles[i][1]
            x2 = array_triangles[i][2]
            y2 = array_triangles[i][3]
            x3 = array_triangles[i][4]
            y3 = array_triangles[i][5]
            retVal = triangle_condition(x1, y1, x2, y2, x3, y3)
            if retVal == 1:
                # triangle sides
                side1 = triangle_side_lenght(x1, y1, x2, y2)
                side2 = triangle_side_lenght(x2, y2, x3, y3)
                side3 = triangle_side_lenght(x1, y1, x3, y3)

                triangle_sq = triangle_square(side1, side2, side3)

                # circle area
                radius = (side1 * side2 * side3)/(4 * triangle_sq)
                circle_sq = pi * (radius ** 2)

                # average area
                average_area = circle_sq - triangle_sq

                average_area_array.append(average_area)
                index_array.append(i)
                cnt += 1

        # проверка на условия треугольников
        if cnt == 0:
            return -1
        else:


            # find minimum delta square

            min_val = average_area_array[0]
            min_idx = index_array[0]

            for i in range(len(average_area_array)):
                if average_area_array[i] < min_val:
                    min_val = average_area_array[i]
                    min_idx = index_array[i]

            min_sq_coordinate = []
            min_sq_coordinate.append(min_val)
            # координаты минимального треугольника
            min_sq_coordinate.append(array_triangles[min_idx])




            return min_sq_coordinate



