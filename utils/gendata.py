import sys
sys.path.append("./")

import config.config as cf
import numpy as np
from entity.corr import Corr3D
from entity.sensor import Sensor

def getGenRandData():
    x = np.random.uniform(1,cf.WIDTH,size=cf.NUM_OF_SENSOR)
    y = np.random.uniform(1,cf.HEIGHT,size=cf.NUM_OF_SENSOR)
    z = np.random.uniform(1,cf.LENGTH,size=cf.NUM_OF_SENSOR)
    return x,y,z

def getGenRandListSensor():
    listSensor =[]
    x,y,z = getGenRandData()  # init 3 array ?-corr
    for index in range(len(x)):
        corr3D = Corr3D(x[index],y[index],z[index])
        sensor = Sensor(corr3D)
        listSensor.append(sensor)
    return listSensor