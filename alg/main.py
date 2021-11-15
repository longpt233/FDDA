import sys
sys.path.append("./")


from utils.gendata import getGenRandListSensor 
from utils.visuallize import Visualze3DWithSensor
from alg.alg1 import initMove



if __name__ == "__main__": 

    listSensor_GLOBAL = getGenRandListSensor()

    Visualze3DWithSensor(listSensor_GLOBAL)

    for sensor in listSensor_GLOBAL:
        sensor = initMove(sensor)

    Visualze3DWithSensor(listSensor_GLOBAL)
    
