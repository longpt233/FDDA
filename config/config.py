import math
from typing import List 
from alg.cal_funcs import f_s, get_hexagon_center_points
from entity.coordinate import Coordinate3D
from entity.layer import Layer


WIDTH = 50
HEIGHT = 50
LENGTH = 50
# WIDTH = 4000
# HEIGHT = 3800
# LENGTH = 4200
# RADIUS = 200
# NUM_OF_SENSOR = 500
# VELOCITY = 2
# GAMMA = 380
# For sensors
RADIUS = 10         # the distance between the centers of the 2 sensors so that it creates a barrier
NUM_OF_SENSOR = 50
VELOCITY = 1
GAMMA = 20          # the distance between the centers of the 2 sensors so that it can sense each other

# Time constraints
MINIMUM_TIME = 1    # seconds
T_CC = None         # time out of CC messages
T_SLEEP = None      # in algorithm 3,4
T_MD = None             # in algorithm 3 when s_i is fixed sensor
T_RCV = 10          # mess receiving time in alg3
MIN_SENSOR_PER_LAYER = f_s(WIDTH, HEIGHT, RADIUS)
MAX_LAYERS = math.floor(NUM_OF_SENSOR / MIN_SENSOR_PER_LAYER)

LIST_HCP = get_hexagon_center_points(WIDTH, HEIGHT, RADIUS)
LAYERS = [Layer(0, i+1) for i in range(MAX_LAYERS)]

for i in range(MAX_LAYERS):
    for j in range(MIN_SENSOR_PER_LAYER):
        LAYERS[i].list_VP.append(Coordinate3D(i*GAMMA, LIST_HCP[j].x, LIST_HCP[j].y))

