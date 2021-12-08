import sys
sys.path.append(".")

from alg.update import update_closer_sensors
from alg.alg1 import init_move
from alg.alg2 import vertical_move
from utils.gen_data import gen_list_sensor
from utils.visuallize import visualize3D_with_sensor
import matplotlib.pyplot as plt


if __name__ == "__main__":
    list_sensor_global = gen_list_sensor()

    visualize3D_with_sensor(list_sensor_global)
 
    for sensor in list_sensor_global:
        init_move(sensor)
    
    # now all sensor are on centerlize 
    visualize3D_with_sensor(list_sensor_global, 'Algorithm 1: Initial Movement')

    # i =0 
    # while i < 2:
    #     i = i+1 
    list_ini_sensors  = list_sensor_global.copy()

    for sensor in list_sensor_global:
        sensor = vertical_move(sensor,list_ini_sensors)

    # visualize3D_with_sensor(list_sensor_global, 'Algorithm 2: Initial Movement')

