import sys
from matplotlib.pyplot import get
sys.path.append('.')
import numpy as np
from entity.coordinate import Coordinate3D, Coordinate2D
import config.config as cf


def get_distance_2D(coor2D_a, coor2D_b):
    return np.linalg.norm((coor2D_a.x - coor2D_b.x, coor2D_a.y - coor2D_b.y))


def init_move(sensor, list_coor_sensor, path):
    global p_target
    x_sensor = sensor.coor3D.x
    y_sensor = sensor.coor3D.y
    z_sensor = sensor.coor3D.z
    coor2d_sensor = Coordinate2D(y_sensor, z_sensor)
    d_min = 2 * cf.LENGTH
    for hcp in cf.LIST_HCP:
        d_tmp = get_distance_2D(hcp, coor2d_sensor)
        if d_tmp < d_min:
            d_min = d_tmp
            p_target = hcp
    if not [x_sensor, p_target.x, p_target.y] in list_coor_sensor: 
        list_coor_sensor.append([x_sensor, p_target.x, p_target.y])
        path += sensor.count_path([x_sensor, p_target.x, p_target.y])
        sensor.set_path([x_sensor, p_target.x, p_target.y])
        sensor.move_to(Coordinate3D(x_sensor, p_target.x, p_target.y))
    else:
        k = 1
        while True:
            if not [x_sensor + k, p_target.x, p_target.y] in list_coor_sensor:
                break
            k += 1
        list_coor_sensor.append([x_sensor+k, p_target.x, p_target.y])
        path += sensor.count_path([x_sensor+k, p_target.x, p_target.y])
        sensor.set_path([x_sensor+k, p_target.x, p_target.y])
        sensor.move_to(Coordinate3D(x_sensor+k, p_target.x, p_target.y))
    return path
