# import sys
# from entity.coordinate import Coordinate3D
# from entity.sensor import Sensor
from alg.cal_funcs import distance3D
# from alg.broadcast_n_rcv import broadcast_po_mess, broadcast_vp_mess, receive_po_mess, receive_vp_mess
import config.config as cf
# import time
# import os
import numpy as np


def vacant_position_processing(sensor_si, curr_layer):
    '''
    Alg3: Phần này đã được sửa lại khá nhiều. 
    Không theo thuật toán chi tiết của họ nữa.
    Mục tiêu của phần này là cập nhật lại toàn bộ listVP của từng thằng sensor. 
    (Ở đây là xét riêng cho sensor si)  
    Cần phải lưu lại biến curr_layer để biết tầng nào đang thực hiện.
    '''
    # t_start = time.time()
    if sensor_si.is_fixed:
        return sensor_si
    else:
        sensor_si_coor3D_list = [sensor_si.coor3D.x, sensor_si.coor3D.y, sensor_si.coor3D.z]
        # while(time.time() - t_start < cf.T_RCV):
        # print("Current layer haha: ", curr_layer)
        # phần này sẽ cố gắng lấy ra những vị trí trống trong cf.LAYERS để gán lại cho từng thằng sensor. 
        temp_VP = cf.LAYERS[curr_layer - 1].list_VP  
        temp_dict_VP = {}
        for i in range(len(temp_VP)):
            temp_dict_VP[i] = temp_VP[i]
        # chú ý là phải sort lại dict để vị trí trống đầu tiên của các sensor là vị trí gần với nó nhất 
        temp_dict_VP = {k: v for k, v in sorted(temp_dict_VP.items(), key=lambda item: distance3D(sensor_si_coor3D_list, item[1]))}
        sensor_si.set_vp(list(temp_dict_VP.values()))
        # print("\nLen of VP after vpp of sensor si: ", len(sensor_si.VP))
        return sensor_si

# sensor_si = Sensor(Coordinate3D(30, 35, 50), 3)
# sensor_si = vacant_position_processing(sensor_si, 2)
# for i in sensor_si.VP:
#     print(distance3D(i, sensor_si.coor3D))
# print(len(sensor_si.VP))
# print(len(cf.LAYERS[1].list_VP))
# print(sensor_si.VP)



    


        





        