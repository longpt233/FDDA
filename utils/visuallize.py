import matplotlib.pyplot as plt


def visualize2D(list_coor):
    list_x, list_y = tuple(zip(*list_coor))
    plt.scatter(list_x, list_y)
    plt.show()


def visualize3D_with_sensor(list_sensor):
    list_coor = list(map(lambda sensor: sensor.coor3D.to_list(), list_sensor))
    list_x, list_y, list_z = tuple(zip(*list_coor))
    ax = plt.axes(projection='3d')
    ax.scatter(list_x, list_y, list_z, 'green')
    ax.set_title('3D visualize')
    plt.show()