import sys
sys.path.append("./")

import config.config as cf
import time

T_RCV = None 

def GetTimeInSecond():
    t = time.time()
    return int(t * 1000000) 

def BroadcastVP():

    raise Exception("method not implement")

def ReceivePOAndVPMess():

    raise Exception("method not implement")

def VacantProcess(sensor):
    t_start = GetTimeInSecond()

    while GetTimeInSecond() - t_start < T_RCV:
        BroadcastVP()
        ReceivePOAndVPMess()

        



