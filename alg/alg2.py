from typing import List
from alg.alg1 import get_hexagon_center_points
import config.config as cf
import math
from entity.coordinate import Coordinate2D, Coordinate3D
from entity.sensor import Sensor
from utils.gen_data import gen_list_sensor
from queue import PriorityQueue
from alg.broadcast_n_rcv import broadcast_po_mess
from alg.alg3 import vacant_position_processing
# all sensor in one center line or all sensor in space
list_ini_sensors = gen_list_sensor()


def contain_fix_sensor(list_sensor):
    for sensor in list_sensor:
        if sensor.is_fixed:
            return True
    return False


def get_same_centerline_sensors(list_sensor, sensor_si):
    list_x_centerlined_sensors = []
    same_centerlined_sensors = []
    y = sensor_si.coor3D.y
    z = sensor_si.coor3D.z 
    for sensor in list_sensor:
        x_i, y_i, z_i, id_i = sensor.coor3D.x, sensor.coor3D.y, sensor.coor3D.z, sensor.id
        if y_i == y and z_i == z:
            list_x_centerlined_sensors.append((x_i, id_i))
    list_x_centerlined_sensors = sorted(list_x_centerlined_sensors)
    for i in list_x_centerlined_sensors:
        same_centerlined_sensors.append(Sensor(Coordinate3D(i[0], y, z), i[1]))
    return same_centerlined_sensors
        

def update_closer_sensors(same_centerline_sensors, sensor_si):
    '''
        update list sensors closer to base layer than sensor s_i 
    '''
    C_si = []
    for sensor in same_centerline_sensors:
        if (abs(sensor_si.coor3D.x - sensor.coor3D.x) < cf.GAMMA and sensor_si.coor3D.x >= sensor.coor3D.x):
            C_si.append(sensor)
    return C_si


def vertical_move(sensor_si):
    x_sensor = sensor_si.coor3D.x
    y_sensor = sensor_si.coor3D.y
    z_sensor = sensor_si.coor3D.z
    list_same_centerline_sensors = get_same_centerline_sensors(list_ini_sensors, sensor_si)
    list_closer_sensors = update_closer_sensors(list_same_centerline_sensors, sensor_si)
    while len(list_closer_sensors) == 0 and sensor_si.coor3D.x != 0:
        sensor_si.move_to(Coordinate3D(x_sensor - cf.VELOCITY, y_sensor, z_sensor))
        update_closer_sensors(list_same_centerline_sensors, sensor_si)

    if len(list_closer_sensors) > 0:
        if contain_fix_sensor(list_closer_sensors):
            closest_to_si_sensor = list_closer_sensors[-1]
            while (sensor_si.coor3D.x - closest_to_si_sensor.coor3D.x < cf.GAMMA):
                sensor_si.coor3D.x += cf.VELOCITY
    
    if not sensor_si.VP.empty():
        p0 = sensor_si.VP.queue[0]
        if sensor_si.coor3D.x == p0.x:
            broadcast_po_mess()
    
    vacant_position_processing()
    
# list_demo = []
# sensor_si = Sensor(Coordinate3D(17, 3, 4), 1)
# for i in range(1, 5):
#     x = int(input("x = "))
#     y = int(input("y = "))
#     z = int(input("z = "))
#     s = Sensor(Coordinate3D(x, y, z), i)
#     s.VP.put(5)
#     list_demo.append(s)
# a = get_same_centerline_sensors(list_demo, sensor_si)
# b = update_closer_sensors(a, sensor_si)
# print(b)
