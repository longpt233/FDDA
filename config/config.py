import math
import sys
sys.path.append(".")
from alg.cal_funcs import f_s, get_hexagon_center_points
from entity.coordinate import Coordinate3D
from entity.layer import Layer

WIDTH = 100
HEIGHT = 100
LENGTH = 100
RADIUS = 10
NUM_OF_SENSOR = 100
VELOCITY = 1
GAMMA = 20


# WIDTH = 4000
# HEIGHT = 3800
# LENGTH = 4200
# RADIUS = 200
# NUM_OF_SENSOR = 300
# VELOCITY = 1
# GAMMA = 380
# Time constraints
MINIMUM_TIME = 1    # seconds
T_CC = None         # time out of CC messages
T_SLEEP = None      # in algorithm 3,4
T_MD = None             # in algorithm 3 when s_i is fixed sensor
T_RCV = 10          # mess receiving time in alg3
MIN_SENSOR_PER_LAYER = f_s(WIDTH, HEIGHT, RADIUS)
MAX_LAYERS_BY_SENSOR = math.floor(NUM_OF_SENSOR / MIN_SENSOR_PER_LAYER)
MAX_LAYERS_BY_LENGTH = math.floor(LENGTH / GAMMA) + 1
MAX_LAYERS = min(MAX_LAYERS_BY_LENGTH, MAX_LAYERS_BY_SENSOR)
LIST_HCP = get_hexagon_center_points(WIDTH, HEIGHT, RADIUS)
LAYERS = [Layer(0, i+1) for i in range(MAX_LAYERS + 1)]
for i in range(MAX_LAYERS + 1):
    for j in range(MIN_SENSOR_PER_LAYER):
        LAYERS[i].list_VP.append([i*GAMMA, LIST_HCP[j].x, LIST_HCP[j].y])
