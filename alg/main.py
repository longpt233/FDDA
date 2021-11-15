import sys
sys.path.append("./")


from utils.gendata import getGenRandListSensor 
from utils.visuallize import Visualze3DWithSensor
from alg.alg1 import initMove



if __name__ == "__main__": 

    listSensor = getGenRandListSensor()

    Visualze3DWithSensor(listSensor)

    for sensor in listSensor:
        sensor = initMove(sensor)

    Visualze3DWithSensor(listSensor)
    
