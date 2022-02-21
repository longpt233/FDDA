import matplotlib.pyplot as plt
import os


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
    px = 1 / plt.rcParams['figure.dpi']
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    if len(list_coor_not_fixed):
        ax.scatter(list_x, list_y, list_z, color='b', marker='o', s=5 * 5)
    if len(list_coor_fixed):
        ax.scatter(list_x_fixed, list_y_fixed, list_z_fixed,
                   color='r', marker='o', s=3 * 3)    # s for square
    # ax.scatter(list_x, list_y, list_z,color = 'blue',  marker='o', s=40*40)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(title)
    plt.show()


def show_hcp(list_hcp):
    visualize2D(list_hcp)


def show_evaluation():
    max_list_paper = {}
    avg_list_paper = {}
    total_list_paper = {}

    max_list = {}
    avg_list = {}
    total_list = {}

    count_folder = 0

    for dir_name in os.listdir('out'):
        count_folder += 1
        for file_name in os.listdir(f'out/{dir_name}'):
            with open(f'out/{dir_name}/{file_name}') as f:
                data = f.readlines()

            num_sensor = int(data[1].split(':')[-1])

            if num_sensor <= 100:
                continue

            max, avg, total = tuple(
                [int(float(row.split(':')[-1])) for row in data[2:5]])

            key = str(num_sensor)

            if dir_name == 'paper':
                max_list_paper[key] = max
                avg_list_paper[key] = avg
                total_list_paper[key] = total

            if key not in max_list.keys():
                max_list[key] = max
                avg_list[key] = avg
                total_list[key] = total
            else:
                max_list[key] += max
                avg_list[key] += avg
                total_list[key] += total

    key_list = max_list.keys()

    for key in key_list:
        max_list[key] /= count_folder
        avg_list[key] /= count_folder
        total_list[key] /= count_folder
    


    plt.plot(key_list, max_list.values(), color='blue', marker='o', label='My Alg')
    plt.plot(key_list, max_list_paper.values(), color='red', marker='*', label='Paper')
    plt.xlabel('Number of sensors')
    plt.ylabel('Maximum movement distance versus number of sensors')
    plt.ylim(bottom=4500, top=6500)
    plt.legend()
    plt.show()

    plt.plot(key_list, avg_list.values(), color='blue', marker='o', label='My Alg')
    plt.plot(key_list, avg_list_paper.values(), color='red', marker='*', label='Paper')
    plt.xlabel('Number of sensors')
    plt.ylabel('Average movement distance versus number of sensors')
    plt.ylim(bottom=1000, top=3000)
    plt.legend()
    plt.show()

    plt.plot(key_list, total_list.values(), color='blue', marker='o', label='My Alg')
    plt.plot(key_list, total_list_paper.values(), color='red', marker='*', label='Paper')
    plt.xlabel('Number of sensors')
    plt.ylabel('Total movement distance versus number of sensors')
    plt.ylim(bottom=0, top=1500000)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    show_evaluation()
