import numpy as np
from entity.coordinate import Coordinate3D, Coordinate2D
import config.config as cf
from utils.visuallize import visualize2D
from cal_funcs import f_c, f_e, f_o, f_y, f_z


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


def show_hcp():
    list_hcp = get_hexagon_center_points(cf.WIDTH, cf.HEIGHT, cf.RADIUS)
    visualize2D(list_hcp)


def get_distance_2D(coor2D_a, coor2D_b):
    return np.linalg.norm((coor2D_a.x - coor2D_b.x, coor2D_a.y - coor2D_b.y))


def init_move(sensor):
    # get corr2D of sensor
    global p_target
    x_sensor = sensor.coor3D.x
    y_sensor = sensor.coor3D.y
    z_sensor = sensor.coor3D.z
    coor2d_sensor = Coordinate2D(y_sensor, z_sensor)

    # Coor2D list
    list_hcp = get_hexagon_center_points(cf.WIDTH, cf.HEIGHT, cf.RADIUS)

    hexagonnNum = len(list_hcp)
    d_min = 2 * cf.LENGTH
    for hcp in list_hcp:
        d_tmp = get_distance_2D(hcp, coor2d_sensor)
        if d_tmp < d_min:
            d_min = d_tmp
            p_target = hcp

    sensor.move_to(Coordinate3D(x_sensor, p_target.x, p_target.y))

    # call alg2 here

    return sensor


if __name__ == "__main__":
    show_hcp()
