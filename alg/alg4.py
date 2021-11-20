import sys
import config.config as cf
import time
from alg2 import VerMove

sys.path.append("./")


def get_time_in_second():
    t = time.time()
    return int(t * 1000000)


# Confirm the Closest
def broadcast_cc():
    raise Exception("method not implement")


# CC - ack
def receive_CCack_mess():
    raise Exception("method not implement")


def parallel_move(sensor):
    t_start = get_time_in_second()
    broadcast_cc()
    while get_time_in_second() - t_start < cf.T_CC:
        if receive_CCack_mess():
            VerMove(sensor)
            return
        time.sleep(cf.T_SLEEP)

    vp = None  # vp = VP(si)[0]
    sensor.move_to()

    VerMove(sensor)
    return
