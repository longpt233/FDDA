import sys
sys.path.append(".")

import json
import math
import os
import matplotlib.pyplot as plt

from alg.cal_funcs import f_s
from alg.alg1 import init_move
from alg.alg2 import vertical_move
from alg.alg3 import vacant_position_processing
from alg.alg4 import parallel_move
from entity.coordinate import Coordinate3D
from entity.layer import Layer
from entity.sensor import Sensor
from utils.gen_data import gen_data_and_write
from utils.visuallize import visualize3D_with_sensor
from utils.file_util import create_if_not_exist
from configs.config import cfg


if __name__ == "__main__":
    # Gen data and write to files
    dir_name = gen_data_and_write()

    # Read data
    list_data = {}
    for file_name in os.listdir(f'data/{dir_name}'):
        if file_name == 'config.yml':
            continue

        with open(f'data/{dir_name}/{file_name}') as f:
            data = f.readlines()
            file_name_without_ext = file_name.split('.')[0]

            list_data[file_name_without_ext] = data

    for item in list_data.items():
        num_sensor = int(item[0])
        data = item[1]

        # Calculate constants
        MIN_SENSOR_PER_LAYER = f_s(cfg['WIDTH'], cfg['HEIGHT'], cfg['RADIUS'])
        MAX_LAYERS_BY_SENSOR = math.floor(num_sensor / MIN_SENSOR_PER_LAYER)
        MAX_LAYERS_BY_LENGTH = math.floor(cfg['LENGTH'] / cfg['GAMMA']) + 1
        MAX_LAYERS = min(MAX_LAYERS_BY_LENGTH, MAX_LAYERS_BY_SENSOR)

        layers = [Layer(0, i + 1) for i in range(MAX_LAYERS + 1)]

        for i in range(MAX_LAYERS + 1):
            for j in range(MIN_SENSOR_PER_LAYER):
                layers[i].list_VP.append(
                    [i * cfg['GAMMA'], cfg['LIST_HCP'][j].x, cfg['LIST_HCP'][j].y])

        count = MAX_LAYERS * MIN_SENSOR_PER_LAYER
        path = 0
        list_sensor_global = []

        for row in data:
            id, pos = tuple(row.split('-'))
            id = int(id)
            pos = json.loads(pos)
            list_sensor_global.append(Sensor(Coordinate3D(*pos), id, False, 0))

        visualize3D_with_sensor(list_sensor_global, 'Init')

        list_coor_sensor = []
        new_list_coor_sensor = []
        for sensor in list_sensor_global:
            path = init_move(sensor, list_coor_sensor, path)

        for sensor in list_sensor_global:
            new_list_coor_sensor.append(tuple(sensor.coor3D.to_list()))

        for i in list(set(new_list_coor_sensor)):
            new_list_coor_sensor.remove(i)

        # now all sensor are on centerlize

        # visualize3D_with_sensor(list_sensor_global, 'Algorithm 1: Initial Movement')

        curr_layer = 1
        a = 1
        while (count > 0):
            for sensor_si in list_sensor_global:
                if sensor_si.is_fixed:
                    continue
                list_sensor_global_without_sensor_si = list_sensor_global.copy()
                list_sensor_global_without_sensor_si.remove(sensor_si)
                sensor_si, curr_layer, count, path = vertical_move(
                    sensor_si, list_sensor_global_without_sensor_si, count, curr_layer, path, layers)
            # visualize3D_with_sensor(list_sensor_global, 'Algorithm 2: Vertical Movement')
            for sensor_si in list_sensor_global:
                if sensor_si.is_fixed:
                    continue
                # print("Start vacant processing no ...")
                list_sensor_global_without_sensor_si = list_sensor_global.copy()
                list_sensor_global_without_sensor_si.remove(sensor_si)
                sensor_si = vacant_position_processing(
                    sensor_si, curr_layer, layers)

            for sensor_si in list_sensor_global:
                if sensor_si.is_fixed:
                    continue
                list_sensor_global_without_sensor_si = list_sensor_global.copy()
                list_sensor_global_without_sensor_si.remove(sensor_si)
                sensor_si, list_sensor_global_without_sensor_si, path = parallel_move(
                    sensor_si, list_sensor_global_without_sensor_si, list_coor_sensor, path)

            print("\nVacant position left: ", count)
            print("Current layer: ", curr_layer)
            count_fixed_sensor = 0
            list_coor_not_fixed_sensor = []
            for sensor in list_sensor_global:
                if sensor.is_fixed:
                    count_fixed_sensor += 1
                else:
                    list_coor_not_fixed_sensor.append(
                        tuple(sensor.coor3D.to_list()))
            print("Fixed sensor: ", count_fixed_sensor)
            # visualize3D_with_sensor(list_sensor_global, 'Algorithm 4: Parallel Movement')
            a += 1
            print("Generation: ", a)
        # plt.show()

        list_coor_not_fixed_sensor = []
        for sensor in list_sensor_global:
            if not sensor.is_fixed:
                list_coor_not_fixed_sensor.append(
                    tuple(sensor.coor3D.to_list()))
        # print("List coor: ", list_coor_not_fixed_sensor)
        visualize3D_with_sensor(list_sensor_global, 'Result')

        all_sensors_path = []
        max_path = 0
        average_path = 0
        for sensor in list_sensor_global:
            max_path = max(max_path, sensor.path)
            average_path += sensor.path
            all_sensors_path.append(sensor.path)

        print("=========================EVALUATION==============================")
        print("Num of sensors: ", num_sensor)
        print("Maximum movement distance versus number of sensors: ", max_path)
        print("Average movement distance versus each sensor: ",
                average_path / num_sensor)
        print("Total movement distance versus number of sensors: ", path)
        print("=================================================================")

        create_if_not_exist(f'out/{dir_name}')

        with open(f'out/{dir_name}/{num_sensor}.out', 'w') as f:
            f.write('1. Final evaluation:\n')
            f.write(f'Num of sensors: {num_sensor}\n')
            f.write(
                f'Maximum movement distance versus number of sensors: {max_path}\n')
            f.write(
                f'Average movement distance versus each sensor: {average_path / num_sensor}\n')
            f.write(
                f'Total movement distance versus number of sensors: {path}\n')
            f.write("2. Final position for all sensors:\n")
            for sensor in list_sensor_global:
                f.write(f'{sensor.id}-{sensor.coor3D.to_list()}\n')
