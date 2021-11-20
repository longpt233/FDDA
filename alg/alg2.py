import config.config as cf
from entity.coordinate import Coordinate3D
from utils.gen_data import gen_list_sensor


# all sensor in one center line or all sensor in space
list_sensor = gen_list_sensor()


def contain_fix_sensor(list_sensor):
    for sensor in list_sensor:
        if sensor.is_fixed:
            return True
    return False


def vertical_move(sensor):
    list_sensor = sensor.closer_sensors

    x_sensor = sensor.coor3D.x
    y_sensor = sensor.coor3D.y
    z_sensor = sensor.coor3D.z

    while len(list_sensor) == 0 and sensor.coor3D.x != 0:
        sensor.move_to(Coordinate3D(x_sensor - cf.VELOCITY * cf.MINIMUM_TIME, y_sensor, z_sensor))
        list_sensor = sensor.c

    if len(list_sensor) > 0:
        if contain_fix_sensor(list_sensor):
            pass

        else:
            # keep 
            pass
    # if VP(sensor)

    # end if 

    # call alg3
