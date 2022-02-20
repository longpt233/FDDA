import math
import sys
sys.path.append(".")
from alg.cal_funcs import get_hexagon_center_points
from entity.coordinate import Coordinate3D
from entity.layer import Layer

lines = []
config = []
with open("data/config.txt", "r") as f:
    lines = f.readlines()
    for line in lines: 
        config.append(int(line.strip().replace(" ", "").split("=")[1]))

WIDTH = config[0]
HEIGHT = config[1]
LENGTH = config[2]
RADIUS = config[3]
NUM_OF_SENSOR = config[4]
VELOCITY = config[5]
GAMMA = config[6]

# Time constraints
MINIMUM_TIME = config[7]   # seconds
T_CC = config[8]         # time out of CC messages
T_SLEEP = config[9]      # in algorithm 3,4
T_MD = config[10]             # in algorithm 3 when s_i is fixed sensor
T_RCV = config[11]          # mess receiving time in alg3

LIST_HCP = get_hexagon_center_points(WIDTH, HEIGHT, RADIUS)

