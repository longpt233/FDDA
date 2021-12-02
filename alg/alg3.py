import sys
from alg.broadcast_n_rcv import broadcast_po_mess, broadcast_vp_mess, receive_mess
import config.config as cf
import time
import os


def vacant_position_processing(sensor_si):
    t_start = time.time()
    while(time.time() - t_start < cf.T_RCV):
        broadcast_vp_mess()
        receive_mess()
        if (sensor_si.VP.empty()):
            sensor_si.VP.put()


