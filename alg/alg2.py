import sys
sys.path.append("./")

import config.config as cf


# thực tế thì nó sẽ quảng bá để biết 
def getC(sensor):
    
    listSensor = []
    # for all sensor 

    x_sensor = sensor.corr3D.x
    y_sensor = sensor.corr3D.y
    z_sensor = sensor.corr3D.z

    for sensor_iter in listSensor_GLOBAL : 

        x_sensor_tmp = sensor_iter.corr3D.x
        y_sensor_tmp = sensor_iter.corr3D.y
        z_sensor_tmp = sensor_iter.corr3D.z

        if y_sensor == y_sensor_tmp and z_sensor == z_sensor_tmp:
            if sensor_iter.corr3D.x < sensor.corr3D.x :
                listSensor.append(sensor_iter)

    return listSensor

def containFixSensor(listSensor):
    for sensor in listSensor:
        if sensor.isFixed == True:
            return True
    
    return False

def getFixSensor(listSensor):

    listFixedSensor = []
    for sensor in listSensor:
        if sensor.isFixed == True:
            listFixedSensor.append(sensor)
    
    return listFixedSensor

def VerMove(sensor):
    listSensor = getC(sensor)

    x_sensor = sensor.corr3D.x
    y_sensor = sensor.corr3D.y
    z_sensor = sensor.corr3D.z

    while len(listSensor) == 0 and sensor.corr3D.x !=0:
        # move theo x voi van toc 
        sensor.MoveTo(Corr3D(x_sensor - cf.VELOCITY* cf.MINIMUM_TIME , y_sensor,z_sensor))
        listSensor = getC(sensor)

    if len(listSensor) >0 : 
        if containFixSensor(listSensor):
            for fixSensor in getFixSensor(listSensor):
                # while ... move out side
                # end while   
                pass 

        else: 
            # keep 
            pass
    # if VP(sensor)

    # end if 

    # call alg3 








