import sys
import config.config as cf
from entity.coordinate import Point3D
import utils.gendata as gd

sys.path.append("./")

# all sensor in one center line or all sensor in space
globalListSensor = gd.getGenRandListSensor()


# thực tế thì nó sẽ quảng bá để biết
def getC(sensor):
    listSensor = []
    # for all sensor 

    x_sensor = sensor.corr3D.x
    y_sensor = sensor.corr3D.y
    z_sensor = sensor.corr3D.z

    for sensor_iter in globalListSensor:
        x_sensor_tmp = sensor_iter.corr3D.x
        y_sensor_tmp = sensor_iter.corr3D.y
        z_sensor_tmp = sensor_iter.corr3D.z

        if y_sensor == y_sensor_tmp and z_sensor == z_sensor_tmp:
            if sensor_iter.corr3D.x < sensor.corr3D.x:
                listSensor.append(sensor_iter)

    return listSensor


def containFixSensor(listSensor):
    for sensor in listSensor:
        if sensor.isFixed:
            return True

    return False


def VerticalMove(sensor):
    listSensor = getC(sensor)

    x_sensor = sensor.corr3D.x
    y_sensor = sensor.corr3D.y
    z_sensor = sensor.corr3D.z

    while len(listSensor) == 0 and sensor.corr3D.x != 0:
        # move theo x voi van toc 
        sensor.MoveTo(Point3D(x_sensor - cf.VELOCITY * cf.MINIMUM_TIME, y_sensor, z_sensor))
        listSensor = getC(sensor)

    if len(listSensor) > 0:
        if containFixSensor(listSensor):
            pass

        else:
            # keep 
            pass
    # if VP(sensor)

    # end if 

    # call alg3
