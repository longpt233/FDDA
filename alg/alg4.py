import sys
from alg.cal_funcs import distance3D
import config.config as cf
from broadcast_n_rcv import *
from entity.coordinate import Coordinate3D

sys.path.append("./")


def parallel_move(sensor_si, list_sensor, list_coor_sensor, path):
    optimal_VP_si = sensor_si.VP[0]
    # CCack_mess = False 
    for sensor in list_sensor:
        if sensor.is_fixed: 
            continue
        optimal_VP = sensor.VP[0]
        if optimal_VP_si == optimal_VP: # nếu mà có 2 thằng, sensor si và 1 đứa nữa có cùng vị trí trống tối ưu => phải so sánh
            distance_sensor_si = distance3D(optimal_VP_si, [sensor_si.coor3D.x, sensor_si.coor3D.y, sensor_si.coor3D.z])
            distance_sensor = distance3D(optimal_VP_si, [sensor.coor3D.x, sensor.coor3D.y, sensor.coor3D.z])
            if distance_sensor_si > distance_sensor: 
                receive_CCack_mess()
                return sensor_si, list_sensor, path
        else:
            continue

    # Trường hợp này là sau khi xét toàn bộ chúng nó rồi mà không có thằng nào gần vị trí trống tối ưu hơn so với sensor si
    if [sensor_si.coor3D.x, optimal_VP_si[1], optimal_VP_si[2]] in list_coor_sensor:
        k = 1
        while True:
            if [sensor_si.coor3D.x + k, optimal_VP_si[1], optimal_VP_si[2]] in list_coor_sensor:
                k += 1
            else:
                break

        path += sensor_si.count_path([sensor_si.coor3D.x + k, optimal_VP_si[1], optimal_VP_si[2]])
        sensor_si.set_path([sensor_si.coor3D.x + k, optimal_VP_si[1], optimal_VP_si[2]])
        sensor_si.move_to(Coordinate3D(sensor_si.coor3D.x + k, optimal_VP_si[1], optimal_VP_si[2]))
    else:
        path += sensor_si.count_path([sensor_si.coor3D.x, optimal_VP_si[1], optimal_VP_si[2]])
        sensor_si.set_path([sensor_si.coor3D.x, optimal_VP_si[1], optimal_VP_si[2]])
        sensor_si.move_to(Coordinate3D(sensor_si.coor3D.x, optimal_VP_si[1], optimal_VP_si[2]))
    return sensor_si, list_sensor, path



