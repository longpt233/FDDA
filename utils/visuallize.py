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