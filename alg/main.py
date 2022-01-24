import sys
from alg.alg4 import parallel_move
from alg.alg3 import vacant_position_processing
from entity.layer import Layer
sys.path.append(".")
# from alg.update import update_closer_sensors
from alg.alg1 import init_move
from alg.alg2 import vertical_move
from utils.gen_data import gen_list_sensor
from utils.visuallize import visualize3D_with_sensor
import config.config as cf
import matplotlib.pyplot as plt


if __name__ == "__main__":
    list_sensor_global = gen_list_sensor()
    # print("List global sensor: ", list_sensor_global)
    visualize3D_with_sensor(list_sensor_global, 'Init Sensor')
    list_coor_sensor = []
    new_list_coor_sensor = []
    for sensor in list_sensor_global:
        init_move(sensor, list_coor_sensor)
    for sensor in list_sensor_global:
        new_list_coor_sensor.append(tuple(sensor.coor3D.to_list()))
    print("New list len: ", len(new_list_coor_sensor))
    print("Set len: ", len(set(new_list_coor_sensor)))
    # print("List coor: ", new_list_coor_sensor)  
    for i in list(set(new_list_coor_sensor)):
        new_list_coor_sensor.remove(i)
    print(new_list_coor_sensor)
    # print("Solve oh no: ", list_coor_sensor)
    # print("Len oh no: ", len(list_coor_sensor))
    # print("List global sensor: ", list_sensor_global)
    # # now all sensor are on centerlize 
    # visualize3D_with_sensor(list_sensor_global, 'Algorithm 1: Initial Movement')
    curr_layer = 1
    count = cf.MAX_LAYERS*cf.MIN_SENSOR_PER_LAYER
    a = 1
    # count = 1
    while (count > 0):
    # while(a < 7):
        for sensor_si in list_sensor_global:
            if sensor_si.is_fixed:
                # print("Sensor is fixed\n")
                continue
            list_sensor_global_without_sensor_si = list_sensor_global.copy()
            # print("Sensor si main: ", sensor_si)
            list_sensor_global_without_sensor_si.remove(sensor_si)
            # print("\nList sensor without si:", list_sensor_global_without_sensor_si)
            # print("List VP of sensor_si - before vertical_move", sensor_si.VP)
            sensor_si, curr_layer, count = vertical_move(sensor_si, list_sensor_global_without_sensor_si, count, curr_layer)
            # print("List VP of sensor_si - after vertical_move", sensor_si.VP)
            # print("Len of VP", len(sensor_si.VP))
        # visualize3D_with_sensor(list_sensor_global, 'Algorithm 2: Vertical Movement')
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
            sensor_si, list_sensor_global_without_sensor_si = parallel_move(sensor_si, list_sensor_global_without_sensor_si, list_coor_sensor)

        print("\nVacant position left: ", count)
        print("Current layer: ", curr_layer)
        count_fixed_sensor = 0
        list_coor_not_fixed_sensor = []
        for sensor in list_sensor_global:
            if sensor.is_fixed:
                count_fixed_sensor += 1
            else: 
                list_coor_not_fixed_sensor.append(tuple(sensor.coor3D.to_list()))
        print("List coor not fixed: ", list_coor_not_fixed_sensor)  
        print("Fixed sensor: ", count_fixed_sensor)
        # if curr_layer > 1: 
        #     print("kdfkdjf: ", cf.LAYERS[curr_layer - 2].list_VP)
        # print("List VP per layers: ", cf.LAYERS[curr_layer -1 ].list_VP) 
        visualize3D_with_sensor(list_sensor_global, 'Algorithm 4: Parallel Movement')
        a +=1
        print("Generation: ", a)
    # plt.show()
        print("List sensor: ", list_sensor_global)


    list_coor_not_fixed_sensor = []
    for sensor in list_sensor_global:
        if not sensor.is_fixed:
            list_coor_not_fixed_sensor.append(tuple(sensor.coor3D.to_list()))
    print("List coor: ", list_coor_not_fixed_sensor)            
    visualize3D_with_sensor(list_sensor_global, 'Algorithm 4: Parallel Movement')