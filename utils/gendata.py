import sys
import config.config as cf
import numpy as np
from entity.coordinate import Point3D
from entity.sensor import Sensor

sys.path.append("./")


def getGenRandData():
    x = np.random.uniform(1, cf.WIDTH, size=cf.NUM_OF_SENSOR)
    y = np.random.uniform(1, cf.HEIGHT, size=cf.NUM_OF_SENSOR)
    z = np.random.uniform(1, cf.LENGTH, size=cf.NUM_OF_SENSOR)
    return x, y, z


def getGenRandListSensor():
    listSensor = []
    x, y, z = getGenRandData()  # init 3 array ?-corr
    for index in range(len(x)):
        point_3d = Point3D(x[index], y[index], z[index])
        sensor = Sensor(point_3d)
        listSensor.append(sensor)
    return listSensor
