import matplotlib.pyplot as plt


def visualize2D(list_coor, title=''):
    list_coor = list(map(lambda coor: coor.to_list(), list_coor))
    list_x, list_y = tuple(zip(*list_coor))
    plt.scatter(list_x, list_y)
    plt.show()


def visualize3D_with_sensor(list_sensor, title=''):
    list_coor = list(map(lambda sensor: sensor.coor3D.to_list(), list_sensor))
    list_x, list_y, list_z = tuple(zip(*list_coor))
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    
    ax.scatter(list_x, list_y, list_z,color = 'b',  marker='o', s=20*20)    # s for square
    # ax.scatter(list_x, list_y, list_z,color = 'blue',  marker='o', s=40*40)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(title) 
    # plt.show()