from visuallize import Visualze3D
import sys
sys.path.append("./")

import config.config as cf
import numpy as np

def getGenRandData():
    x = np.random.uniform(1,cf.WIDTH,size=cf.NUM_OF_SENSOR)
    y = np.random.uniform(1,cf.HEIGHT,size=cf.NUM_OF_SENSOR)
    z = np.random.uniform(1,cf.LENGTH,size=cf.NUM_OF_SENSOR)
    return x,y,z

x,y,z = getGenRandData()
Visualze3D(x, y, z)