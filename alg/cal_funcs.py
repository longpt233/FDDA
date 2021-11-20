import math
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
