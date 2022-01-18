import math

from entity.coordinate import Coordinate2D, Coordinate3D
SQRT3 = math.sqrt(3)


# return num of colum
def f_c(w, r):
    return math.ceil((2 * (w - r)) / (3 * r)) + 1


# return number of rows of odd number colum
def f_o(h, r):
    return math.ceil(h / (r * SQRT3))


# return number of rows of even number colum
def f_e(h, r):
    numerator = h - (r * SQRT3) / 2
    denominator = r * SQRT3
    return math.ceil(numerator / denominator) + 1


# y coordnate of each column where i denotes the ith column
def f_y(w, r, i):
    if i == 0:
        return r / 2
    else:
        compare_with_w = r / 2 + (f_c(w, r) - 1) * r / 2
        if compare_with_w < w:
            return r / 2 + i * 3 * r / 2
        else:
            return w


def f_z(h, r, j, is_odd):
    if is_odd:
        return h - (r * SQRT3) / 2 - j * r * SQRT3
    else:
        return h - j * r * SQRT3

def f_s(w, h, r):
    return f_o(h, r) * math.ceil(f_c(w, r) / 2) + f_e(h, r) * math.floor(f_c(w, r) / 2)

def get_hexagon_center_points(w, h, r):
    list_hcp = []

    num_col = f_c(w, r)
    num_odd_row = f_o(h, r)
    num_even_row = f_e(h, r)

    for col_index in range(num_col):
        y = f_y(w, r, col_index)

        if col_index % 2 == 1:
            for row_index in range(num_odd_row):
                z = f_z(h, r, row_index, is_odd=True)
                list_hcp.append(Coordinate2D(y, z))
        else:
            for row_index in range(num_even_row):
                z = f_z(h, r, row_index, is_odd=False)
                list_hcp.append(Coordinate2D(y, z))

    return list_hcp

def distance3D(a, b):
    x1, y1, z1 = a[0], a[1], a[2]
    x2, y2, z2 = b[0], b[1], b[2]
    d = math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) +
                math.pow(z2 - z1, 2)* 1.0)
        
    return d

a = [2, -5, 7]
b = [3, 4, 5]
# print(distance3D(a, b))