import sys
from alg.broadcast_n_rcv import broadcast_po_mess, broadcast_vp_mess, receive_po_mess, receive_vp_mess
import config.config as cf
import time
import os
import numpy as np


def vacant_position_processing(sensor_si):
    t_start = time.time()
    while(time.time() - t_start < cf.T_RCV):

        broadcast_vp_mess()         # quảng bá tất cả những thằng xung quanh vi trí trống mà nó biết  
        receive_po_mess()           # nhân lại sự xác định vị trí trống của ai đó quảng bá ở bước 2 
        vp_possition = receive_vp_mess()   # trả về 1 Coordinate3D do thằng khác trả về trongg 1 lần, vì là trong while lên trong môt khoảng thời gian nó có nhân nhiều lần 1 tọa độ này 
        
        
        if (sensor_si.VP.empty()):    # nếu nó đang không biết bất cứ vị trí trống nào   
            sensor_si.VP.put(vp_possition)   #  add vào hàng đơi VP của si vi trí trống nó nhân được        
        else:    # nếu mà hàng đợi của si không rỗng (nó  biết vị trí trống )
            x_min = sensor_si.VP[0]   # lay ra vi tri trống có x  nho nhat mà nó biết . cái VP này sẽ chứa tất cả các vị trí trống mà cùng 1 layyer (cùng x) (đọc code sẽ hiểu vì nó chỉ add thêm những vị trí trống cùng x )


        if  vp_possition.x ==  x_min :  # nếu vị trí trống mà nó biết bằng x với cái vị trí trống mà thằng khác quảng bá cho nó 
            sensor_si.VP.put(vp_possition)   # add thêm vị trí trống này vào VP của nó 
        elif vp_possition.x <  x_min :  # nếu vị trí trống mà nó nhận được gần base layer hơn những vị trí trống mà nó biết
            sensor_si.VP = None         # xóa VP 
            sensor_si.VP.put(vp_possition)  # add vị trí trống 
        else :
            # bỏ qua vp_possition này vì x của  vị trí trống đó xa hơn 
            pass

        time.sleep(cf.T_SLEEP)
    # end while 

    if sensor_si.VP.empty()  == False : # nếu hàng đợi vị trí trống của nó k rỗng 
        p_o = sensor_si.VP[0]
        if sensor_si.coor3D.x < p_o.x : # tất cả vị trí trống mà nó biết đều nằm xa base layyer hơn nó 
            # đứng yên và k làm gì cho bọn khác di chuyển bớt đi rồi nhân mới 
            time.sleep(np.random(0, cf.T_MD))
            # đợi một lúc thì bắt đầu call lại để tính toán vị trí trống xong quanh nó 
            # lại call lại chính  method này vacant_position_processing(sensor_si):
            return
        # end if

    else :   # nếu mà Vp của nó k rống, có vị trí gàn base hơn nó thì bắt đấu vào thuât toán 4 để di chuyển  
        # call alg 4
        return
    



    


        





        