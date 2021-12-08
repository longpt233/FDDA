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
        if (abs(sensor_si.coor3D.x - sensor.coor3D.x) <=  cf.GAMMA and sensor_si.coor3D.x >= sensor.coor3D.x):
            C_si.append(sensor)
    return C_si


def vertical_move(sensor_si, list_ini_sensors):

    x_sensor = sensor_si.coor3D.x
    y_sensor = sensor_si.coor3D.y
    z_sensor = sensor_si.coor3D.z

    # lấy tất cả các sensor cùng senterlize 
    list_same_centerline_sensors = get_same_centerline_sensors(list_ini_sensors, sensor_si)

    # lọc ra những sensor gàn base hơn so với nó, tính theo GAMMA 
    list_closer_sensors = update_closer_sensors(list_same_centerline_sensors, sensor_si)

    # sensor đó sẽ chuyển động đến khi gặp sensor khác hoặc base layer thì thôi
    while len(list_closer_sensors) == 0 and sensor_si.coor3D.x != 0:
        sensor_si.move_to(Coordinate3D(x_sensor - cf.VELOCITY, y_sensor, z_sensor))      # chuyển động với một khoảng bằng vận tốc (lấy là 1 - đơn vị )
        list_closer_sensors = update_closer_sensors(list_same_centerline_sensors, sensor_si)
        # có thể đặt biến tính time chuyển động ở đây 

    # nếu nó gặp một sensor trước nó 
    # vì mình chỉ nhảy một lần 1 đơn vị, VÀ init theo trục x là số nguyên (bội của 1 )
    # hàm closer tính biên, tức là cách nhau đúng GAMMA là được, không cần <= GAMMA -1 
    if len(list_closer_sensors) > 0:

        # check fix sensor , lần đầu chạy thì chắc là không có rồi 
        # nếu có thì lùi ra xa một đoạn cho bằng GAMMA 
        if contain_fix_sensor(list_closer_sensors):

            closest_to_si_sensor = list_closer_sensors[-1]   # cần check xem cái nào gần nhất ? 
            while (sensor_si.coor3D.x - closest_to_si_sensor.coor3D.x < cf.GAMMA):
                sensor_si.coor3D.x += cf.VELOCITY    # cũng cách ra một đoạn bằng 1 

        # else thi đứng yên 
    
    
    # if not sensor_si.VP.empty():
    #     p0 = sensor_si.VP.queue[0]
    #     if sensor_si.coor3D.x == p0.x:
    #         broadcast_po_mess()
    
    # vacant_position_processing()


    return sensor_si
    
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
