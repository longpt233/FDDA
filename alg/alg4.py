import sys
import config.config as cf
import time
from alg2 import vertical_move
from broadcast_n_rcv import *
from entity.coordinate import Coordinate2D, Coordinate3D

sys.path.append("./")


def get_time_in_second():
    t = time.time()
    return int(t * 1000000)


def parallel_move(sensor_si):

    t_start = get_time_in_second()
    broadcast_cc_mess()  # quảng bá thông điệp cc 

    while get_time_in_second() - t_start < cf.T_CC:  # đợi mọt lúc
        if receive_CCack_mess():  # nếu thằng khác xác định là nó gần vi trí trống hơn 
            vertical_move(sensor_si) # thì thôi quay về alg2
            return
        time.sleep(cf.T_SLEEP)

    # đợi một lúc mà không ai phản hồi thì move ngang tới centerlize có vi trí trống đó 
    vp = sensor_si.VP[0]   # trả về Coordinate3D
    x_sensor = sensor_si.coor3D.x 
    sensor_si.move_to(Coordinate3D(x_sensor, vp.y, vp.z))

    vertical_move(sensor_si)

    return
