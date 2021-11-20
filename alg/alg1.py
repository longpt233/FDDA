import math

from entity.coordinate import Coordinate3D, Coordinate2D
import config.config as cf
from utils.visuallize import visualize2D

SQRT3 = math.sqrt(3)


# return num of colum
def f_c(w, r):
    tmp = (2 * (w - r)) / (3 * r)
    seil_tmp = int(math.ceil(tmp))
    return seil_tmp + 1


# return number of rows of odd number colum
def f_o(h, r):
    tmp = h / (r * SQRT3)
    seil_tmp = int(math.ceil(tmp))
    return seil_tmp


# return number of rows of even number colum
def f_e(h, r):
    numerator = h - (r * SQRT3) / 2
    denominator = r * SQRT3
    tmp = numerator / denominator
    seil_tmp = int(math.ceil(tmp))
    return seil_tmp + 1


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


def f_z(h, r, j, isOld):
    if isOld:
        return h - (r * SQRT3) / 2 - j * r * SQRT3
    else:
        return h - j * r * SQRT3


def get_hexagon_center_points(w, h, r):
    list_hcp = []

    num_col = f_c(w, r)

    num_old_row = f_o(h, r)
    num_even_row = f_e(h, r)

    for col_index in range(num_col):
        f_y = f_y(w, r, col_index)

        if col_index % 2 == 1:
            for row_index in range(num_old_row):
                f_z = f_z(h, r, row_index, isOld=True)
                list_hcp.append(Coordinate2D(f_y, f_z))

        else:
            for row_index in range(num_even_row):
                f_z = f_z(h, r, row_index, isOld=False)
                list_hcp.append(Coordinate2D(f_y, f_z))

    return list_hcp


def show_hcp():
    list_hcp = get_hexagon_center_points(cf.WIDTH, cf.HEIGHT, cf.RADIUS)
    x = []
    y = []
    for i in list_hcp:
        x.append(i.x)
        y.append(i.y)
    visualize2D(x, y)


def getDistance2D(corr2D_a, corr2D_b):
    tmp1 = corr2D_a.x - corr2D_b.x
    tmp2 = corr2D_a.y - corr2D_b.y
    tmp3 = tmp1 * tmp1 + tmp2 * tmp2
    return math.sqrt(tmp3)


def init_move(sensor):
    # get corr2D of sensor
    global p_target
    x_sensor = sensor.coor3D.x
    y_sensor = sensor.coor3D.y
    z_sensor = sensor.coor3D.z
    corr2d_sensor = Coordinate2D(y_sensor, z_sensor)

    # Coor2D list
    list_hcp = get_hexagon_center_points(cf.WIDTH, cf.HEIGHT, cf.RADIUS)

    hexagonnNum = len(list_hcp)
    dmin = 2 * cf.LENGTH
    for hcp in list_hcp:
        dtmp = getDistance2D(hcp, corr2d_sensor)
        if dtmp < dmin:
            dmin = dtmp
            p_target = hcp

    sensor.move_to(Coordinate3D(x_sensor, p_target.x, p_target.y))

    # call alg2 here

    return sensor


if __name__ == "__main__":
    show_hcp()
