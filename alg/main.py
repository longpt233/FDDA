import json
import math
import sys
from alg.alg4 import parallel_move
from alg.alg3 import vacant_position_processing
from alg.cal_funcs import f_s
from entity.coordinate import Coordinate3D
from entity.layer import Layer
from entity.sensor import Sensor
sys.path.append(".")
from alg.alg1 import init_move
from alg.alg2 import vertical_move
from utils.gen_data import gen_list_sensor
from utils.visuallize import visualize3D_with_sensor
import config.config as cf
import matplotlib.pyplot as plt



if __name__ == "__main__":
    # list_sensor_global = gen_list_sensor()
    print("Welcome to our FDDA demo!")
    num_of_sensor = 0 
    while True: 
        num_of_sensor += 100
        if (num_of_sensor > 800):
            break
        print("Sample number of sensors: ", num_of_sensor)
        cf.NUM_OF_SENSOR = num_of_sensor
        MIN_SENSOR_PER_LAYER = f_s(cf.WIDTH, cf.HEIGHT, cf.RADIUS)
        MAX_LAYERS_BY_SENSOR = math.floor(cf.NUM_OF_SENSOR / MIN_SENSOR_PER_LAYER)
        MAX_LAYERS_BY_LENGTH = math.floor(cf.LENGTH / cf.GAMMA) + 1
        MAX_LAYERS = min(MAX_LAYERS_BY_LENGTH, MAX_LAYERS_BY_SENSOR)

        LAYERS = [Layer(0, i+1) for i in range(MAX_LAYERS + 1)]
        for i in range(MAX_LAYERS + 1):
            for j in range(MIN_SENSOR_PER_LAYER):
                LAYERS[i].list_VP.append([i*cf.GAMMA, cf.LIST_HCP[j].x, cf.LIST_HCP[j].y])
        count = MAX_LAYERS*MIN_SENSOR_PER_LAYER
        path = 0
        list_sensor_global = []
        config = []
        sample_file = open("data/sample/sample" + str(cf.NUM_OF_SENSOR)+ ".txt")
        config_file = open("data/config.txt")
        config_lines = config_file.readlines()
        positions = sample_file.readlines()
        for line in config_lines:
            config.append(line.strip())

        for line in positions:
            # print(line.strip())
            id = line.strip().split('-')[0]
            pos = line.strip().split('-')[1]
            id = int(id)
            pos = json.loads(pos)
            list_sensor_global.append(Sensor(Coordinate3D(*pos), id, False, 0))
        visualize3D_with_sensor(list_sensor_global, 'Init Sensor')
        list_coor_sensor = []
        new_list_coor_sensor = []
        for sensor in list_sensor_global:
            # print(sensor)
            path = init_move(sensor, list_coor_sensor, path)
        
        for sensor in list_sensor_global:
            new_list_coor_sensor.append(tuple(sensor.coor3D.to_list()))
    
        for i in list(set(new_list_coor_sensor)):
            new_list_coor_sensor.remove(i)
        # # now all sensor are on centerlize 
        # visualize3D_with_sensor(list_sensor_global, 'Algorithm 1: Initial Movement')
        curr_layer = 1
        a = 1
        while (count > 0):
            for sensor_si in list_sensor_global:
                if sensor_si.is_fixed:
                    continue
                list_sensor_global_without_sensor_si = list_sensor_global.copy()
                list_sensor_global_without_sensor_si.remove(sensor_si)
                sensor_si, curr_layer, count, path = vertical_move(sensor_si, list_sensor_global_without_sensor_si, count, curr_layer, path, LAYERS)
            # visualize3D_with_sensor(list_sensor_global, 'Algorithm 2: Vertical Movement')
            for sensor_si in list_sensor_global:
                if sensor_si.is_fixed:
                    continue
                # print("Start vacant processing no ...")
                list_sensor_global_without_sensor_si = list_sensor_global.copy()
                list_sensor_global_without_sensor_si.remove(sensor_si)
                sensor_si = vacant_position_processing(sensor_si, curr_layer, LAYERS)

            for sensor_si in list_sensor_global:
                if sensor_si.is_fixed: 
                    continue
                list_sensor_global_without_sensor_si = list_sensor_global.copy()
                list_sensor_global_without_sensor_si.remove(sensor_si)
                sensor_si, list_sensor_global_without_sensor_si, path = parallel_move(sensor_si, list_sensor_global_without_sensor_si, list_coor_sensor, path)

            print("\nVacant position left: ", count)
            print("Current layer: ", curr_layer)
            count_fixed_sensor = 0
            list_coor_not_fixed_sensor = []
            for sensor in list_sensor_global:
                if sensor.is_fixed:
                    count_fixed_sensor += 1
                else: 
                    list_coor_not_fixed_sensor.append(tuple(sensor.coor3D.to_list())) 
            print("Fixed sensor: ", count_fixed_sensor)
            # visualize3D_with_sensor(list_sensor_global, 'Algorithm 4: Parallel Movement')
            a +=1
            print("Generation: ", a)
        # plt.show()


        list_coor_not_fixed_sensor = []
        for sensor in list_sensor_global:
            if not sensor.is_fixed:
                list_coor_not_fixed_sensor.append(tuple(sensor.coor3D.to_list()))
        # print("List coor: ", list_coor_not_fixed_sensor)            
        visualize3D_with_sensor(list_sensor_global, 'Algorithm 4: Parallel Movement')
        all_sensors_path = []
        max_path = 0
        average_path = 0
        for sensor in list_sensor_global:
            max_path = max(max_path, sensor.path)
            average_path += sensor.path 
            all_sensors_path.append(sensor.path)

        print("=========================EVALUATION==============================")
        print("Num of sensors: ", cf.NUM_OF_SENSOR)
        print("Maximum movement distance versus number of sensors: ", max_path)
        print("Average movement distance versus each sensor: ", average_path/cf.NUM_OF_SENSOR)
        print("Total movement distance versus number of sensors: ", path)
        print("=================================================================")

        with open("data/result/result" + str(cf.NUM_OF_SENSOR) + ".txt", "w") as f: 
            f.write("1. Final evaluation: \n")
            f.write("Num of sensors: " + str(cf.NUM_OF_SENSOR) + "\n")
            f.write("Maximum movement distance versus number of sensors: " + str(max_path) + "\n")
            f.write("Average movement distance versus each sensor: " + str(average_path/cf.NUM_OF_SENSOR) + "\n")
            f.write("Total movement distance versus number of sensors: " + str(path) + "\n")
            f.write("2. Final position for all sensors \n")
            for sensor in list_sensor_global:
                f.write(str(sensor.id) + "-" + str(sensor.coor3D.to_list()) + "\n")