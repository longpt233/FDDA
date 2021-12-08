# cube 
WIDTH = 50
HEIGHT = 50
LENGTH = 50

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