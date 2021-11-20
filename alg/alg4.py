import sys
import config.config as cf
import time
from alg2 import VerMove

sys.path.append("./")


def GetTimeInSecond():
    t = time.time()
    return int(t * 1000000)


# Confirm the Closest
def BroadcastCC():
    raise Exception("method not implement")


# CC - ack
def ReceiveCCackMess():
    raise Exception("method not implement")


def ParallelMove(sensor):
    t_start = GetTimeInSecond()
    BroadcastCC()
    while GetTimeInSecond() - t_start < cf.T_CC:
        if ReceiveCCackMess():
            VerMove(sensor)
            return
        time.sleep(cf.T_SLEEP)

    vp = None  # vp = VP(si)[0]
    sensor.move_to()

    VerMove(sensor)
    return
