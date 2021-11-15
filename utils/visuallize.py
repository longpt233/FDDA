import sys
sys.path.append("./")

from entity.corr import Corr3D


import numpy as np
import matplotlib.pyplot as plt 

# x,y,z í numpy array 
def Visualze3D(x,y,z):

    fig = plt.figure()
    
    # syntax for 3-D projection
    ax = plt.axes(projection ='3d')
    
    # plotting
    ax.scatter(x, y, z, 'green')
    ax.set_title('3D visualize')
    plt.show()

def Visualze2D(x,y):

    plt.scatter(x, y)
    plt.show()


def Visualze3DWithSensor(listSensor):
    x= []
    y=[]
    z=[]
    for sensor in listSensor:

        corr3d = sensor.corr3D
        x_coor = corr3d.x
        y_coor = corr3d.y
        z_coor = corr3d.z

        x.append(x_coor)
        y.append(y_coor)
        z.append(z_coor)
    
    Visualze3D(x, y, z)