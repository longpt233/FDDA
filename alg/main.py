import sys
from alg.alg4 import parallel_move
from alg.alg3 import vacant_position_processing
from entity.layer import Layer
sys.path.append(".")
from alg.alg1 import init_move
from alg.alg2 import vertical_move
from utils.gen_data import gen_list_sensor
from utils.visuallize import visualize3D_with_sensor
import config.config as cf
import matplotlib.pyplot as plt



if __name__ == "__main__":
    # cf.NUM_OF_SENSOR = 400
    path = 0
    list_sensor_global = gen_list_sensor()
    # visualize3D_with_sensor(list_sensor_global, 'Init Sensor')
    list_coor_sensor = []
    new_list_coor_sensor = []
    for sensor in list_sensor_global:
        path = init_move(sensor, list_coor_sensor, path)
    
    for sensor in list_sensor_global:
        new_list_coor_sensor.append(tuple(sensor.coor3D.to_list()))
 
    for i in list(set(new_list_coor_sensor)):
        new_list_coor_sensor.remove(i)
    # # now all sensor are on centerlize 
    visualize3D_with_sensor(list_sensor_global, 'Algorithm 1: Initial Movement')
    curr_layer = 1
    count = cf.MAX_LAYERS*cf.MIN_SENSOR_PER_LAYER
    a = 1
    while (count > 0):
        for sensor_si in list_sensor_global:
            if sensor_si.is_fixed:
                continue
            list_sensor_global_without_sensor_si = list_sensor_global.copy()
            list_sensor_global_without_sensor_si.remove(sensor_si)
            sensor_si, curr_layer, count, path = vertical_move(sensor_si, list_sensor_global_without_sensor_si, count, curr_layer, path)
        visualize3D_with_sensor(list_sensor_global, 'Algorithm 2: Vertical Movement')
        for sensor_si in list_sensor_global:
            if sensor_si.is_fixed:
                continue
            # print("Start vacant processing no ...")
            list_sensor_global_without_sensor_si = list_sensor_global.copy()
            list_sensor_global_without_sensor_si.remove(sensor_si)
            sensor_si = vacant_position_processing(sensor_si, curr_layer)

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
        visualize3D_with_sensor(list_sensor_global, 'Algorithm 4: Parallel Movement')
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