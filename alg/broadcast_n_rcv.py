import time
from entity.message import POMess
from entity.sensor import Sensor
import config.config as cf


# for alg 2,3 
def broadcast_vp_mess():
    pass


def broadcast_po_mess(sensor_si, optimal_pos):
    po_mess = POMess(sensor_si.id, time.time(), optimal_pos)
    for i in range(cf.MAX_LAYERS):
        if (cf.LAYERS[i].list_VP[0].x == sensor_si.coor3D.x):
            cf.LAYERS[i].list_VP.remove(sensor_si.coor3D)


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