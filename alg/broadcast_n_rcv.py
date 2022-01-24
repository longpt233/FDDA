# import time
# from entity.message import POMess
# from entity.sensor import Sensor
# import config.config as cf


# for alg 2,3 
def broadcast_vp_mess(sensor_si):

    pass


def broadcast_po_mess(sensor_si):
    pass
    # po_mess = POMess(sensor_si.id, time.time(), sensor_si.coor3D.x)
    # for i in range(cf.MAX_LAYERS):
    #     if (cf.LAYERS[i].list_VP[0].x == sensor_si.coor3D.x): # chỉ cần xét x của thằng phần tử bất kì tại layer i. Ở đây chọn phần tử đầu tiên
    #         cf.LAYERS[i].list_VP.remove(sensor_si.coor3D)
    #         sensor_si.is_fixed = True
    #         if (len(cf.LAYERS[i]) == 0): # không còn vị trí trống nào trên layer này cả
    #             cf.LAYERS[i].set_flag(2) # set cờ thành constructed layer
    #         else: 
    #             cf.LAYERS[i].set_flag(1) # set cờ thành constructing layer
        


def receive_po_mess(): #no need
    pass


def receive_vp_mess():
    
    return None


# for alg 4 

# Confirm the Closest
def broadcast_cc_mess():
    pass


# CC - ack
def receive_CCack_mess():
    pass