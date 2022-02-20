from entity.sensor import Sensor
from entity.coordinate import Coordinate3D
import config.config as cf
from numpy.random import randint



def gen_list_sensor():
    list_x, list_y, list_z = tuple(
        map(
            lambda dimension: randint(1, dimension, size=cf.NUM_OF_SENSOR),
            [cf.LENGTH, cf.WIDTH, cf.HEIGHT],
        )
    )
    sensors_len = len(list_x)
    list_sensor = [
        Sensor(Coordinate3D(*coor3D), id, False, 0)
        for coor3D, id in zip(
            zip(list_x, list_y, list_z), range(1, sensors_len + 1)
        )
    ]

    return list_sensor

list_sensor_sample = gen_list_sensor()
num_of_sensor = cf.NUM_OF_SENSOR
while True: 
    if num_of_sensor < 100: 
        break
    with open("data/sample/sample" + str(num_of_sensor) + ".txt", "w") as f: 
        for index in range(0, num_of_sensor):
            sensor = list_sensor_sample[index]
            line = str(sensor.id )+ "-" + str(sensor.coor3D.to_list()) + '\n'
            f.write(line)
    num_of_sensor -= 100