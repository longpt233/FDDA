from entity.sensor import Sensor
from entity.coordinate import Coordinate3D
import config.config as cf
from numpy.random import uniform


def gen_list_sensor():
    list_x, list_y, list_z = tuple(map(lambda dimension: uniform(1, dimension, size=cf.NUM_OF_SENSOR),
                                       [cf.LENGTH, cf.WIDTH, cf.HEIGHT]))

    list_sensor = [Sensor(Coordinate3D(*coor3D)) for coor3D in zip(list_x, list_y, list_z)]
    
    return list_sensor