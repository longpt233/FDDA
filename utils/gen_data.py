import sys
sys.path.append('.')

import time
import shutil
from numpy.random import randint

from entity.sensor import Sensor
from entity.coordinate import Coordinate3D
from utils.file_util import create_if_not_exist
from configs.config import cfg


def gen_list_sensor(num_sensor):
    list_x = randint(1, cfg['LENGTH'], size=num_sensor)
    list_y = randint(1, cfg['WIDTH'], size=num_sensor)
    list_z = randint(1, cfg['HEIGHT'], size=num_sensor)

    list_sensor = []

    for coor3D, id in zip(zip(list_x, list_y, list_z), range(1, len(list_x) + 1)):
        list_sensor.append(Sensor(Coordinate3D(*coor3D), id, False, 0))

    return list_sensor


def gen_data_and_write():
    dir_name = time.strftime(r'%Y%m%d-%H%M%S')

    for num_sensor in range(100, cfg['NUM_SENSOR'] + 1, 100):
        list_sensor_gen = gen_list_sensor(num_sensor)

        create_if_not_exist(f'data/{dir_name}')

        with open(f'data/{dir_name}/{num_sensor}.inp', 'w') as f:
            for sensor in list_sensor_gen:
                f.write(f'{sensor.id}-{sensor.coor3D.to_list()}\n')
    
    # Copy config file
    shutil.copy('configs/config.yml', f'data/{dir_name}')

    return dir_name