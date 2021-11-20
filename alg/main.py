import sys
sys.path.append(".")

from alg.update import update_closer_sensors
from alg.alg1 import init_move
from utils.gen_data import gen_list_sensor
from utils.visuallize import visualize3D_with_sensor


if __name__ == "__main__":
    list_sensor_global = gen_list_sensor()

    visualize3D_with_sensor(list_sensor_global)

    for sensor in list_sensor_global:
        sensor = init_move(sensor)
    
    update_closer_sensors(list_sensor_global)
    
    visualize3D_with_sensor(list_sensor_global, 'Algorithm 1: Initial Movement')