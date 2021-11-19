import sys
from utils.gendata import getGenRandListSensor
from utils.visuallize import Visualize3DWithSensor
from alg.alg1 import initMove

sys.path.append("./")

if __name__ == "__main__":

    listSensor_GLOBAL = getGenRandListSensor()

    Visualize3DWithSensor(listSensor_GLOBAL)

    for sensor in listSensor_GLOBAL:
        sensor = initMove(sensor)

    Visualize3DWithSensor(listSensor_GLOBAL)
