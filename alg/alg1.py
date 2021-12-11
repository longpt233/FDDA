import sys
from matplotlib.pyplot import get
sys.path.append('.')
import numpy as np
from entity.coordinate import Coordinate3D, Coordinate2D
import config.config as cf
from utils.visuallize import visualize2D
from cal_funcs import f_c, f_e, f_o, f_y, f_z, get_hexagon_center_points


def show_hcp():
    visualize2D(cf.LIST_HCP)


def get_distance_2D(coor2D_a, coor2D_b):
    return np.linalg.norm((coor2D_a.x - coor2D_b.x, coor2D_a.y - coor2D_b.y))


def init_move(sensor):
    # get corr2D of sensor
    global p_target
    x_sensor = sensor.coor3D.x
    y_sensor = sensor.coor3D.y
    z_sensor = sensor.coor3D.z
    coor2d_sensor = Coordinate2D(y_sensor, z_sensor)
    hexagonnNum = len(cf.LIST_HCP)
    d_min = 2 * cf.LENGTH
    for hcp in cf.LIST_HCP:
        d_tmp = get_distance_2D(hcp, coor2d_sensor)
        if d_tmp < d_min:
            d_min = d_tmp
            p_target = hcp

    sensor.move_to(Coordinate3D(x_sensor, p_target.x, p_target.y))


if __name__ == "__main__":
    show_hcp()
    # a = get_hexagon_center_points(cf.WIDTH, cf.HEIGHT, cf.RADIUS)
    # print(a)