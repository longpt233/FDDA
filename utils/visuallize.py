import sys
from entity.coordinate import Point3D
import numpy as np
import matplotlib.pyplot as plt

sys.path.append("./")


# x,y,z í numpy array 
def Visualize3D(x, y, z):
    fig = plt.figure()

    # syntax for 3-D projection
    ax = plt.axes(projection='3d')

    # plotting
    ax.scatter(x, y, z, 'green')
    ax.set_title('3D visualize')
    plt.show()


def Visualize2D(x, y):
    plt.scatter(x, y)
    plt.show()


def Visualize3DWithSensor(listSensor):
    x = []
    y = []
    z = []
    for sensor in listSensor:
        point_3d = sensor.point_3d
        x_coor = point_3d.x
        y_coor = point_3d.y
        z_coor = point_3d.z

        x.append(x_coor)
        y.append(y_coor)
        z.append(z_coor)

    Visualize3D(x, y, z)
