import matplotlib.pyplot as plt
import config.config as cf 

def visualize2D(list_coor, title=''):
    list_coor = list(map(lambda coor: coor.to_list(), list_coor))
    list_x, list_y = tuple(zip(*list_coor))
    plt.scatter(list_x, list_y)
    plt.show()


def visualize3D_with_sensor(list_sensor, title=''):
    list_coor_not_fixed = []
    list_coor_fixed = [] 
    list_fixed_sensor = [] 
    for sensor in list_sensor:
        if (sensor.is_fixed):
            list_fixed_sensor.append(sensor)
            list_coor_fixed.append(sensor.coor3D.to_list())
        else:
            list_coor_not_fixed.append(sensor.coor3D.to_list())

    # print("List fixed sensor: ", list_fixed_sensor)
    if len(list_coor_not_fixed):
        list_x, list_y, list_z = tuple(zip(*list_coor_not_fixed))
    if len(list_coor_fixed):
        list_x_fixed, list_y_fixed, list_z_fixed = tuple(zip(*list_coor_fixed))
    px = 1/plt.rcParams['figure.dpi']
    # fig = plt.figure(figsize=(cf.WIDTH*px, cf.HEIGHT*px))
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    if len(list_coor_not_fixed):
        ax.scatter(list_x, list_y, list_z,color = 'b',  marker='o', s=5*5)
    if len(list_coor_fixed):
        ax.scatter(list_x_fixed, list_y_fixed, list_z_fixed, color = 'r',  marker='o', s=3*3)    # s for square
    # ax.scatter(list_x, list_y, list_z,color = 'blue',  marker='o', s=40*40)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(title) 
    plt.show()

def show_hcp(list_hcp):
    visualize2D(list_hcp)