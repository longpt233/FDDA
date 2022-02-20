import sys
sys.path.append('.')
import config.config as cf
from entity.coordinate import  Coordinate3D
from alg.broadcast_n_rcv import broadcast_po_mess


def contain_fix_sensor(list_sensor):
    '''
    Check xem trong list sensor (ngoại trừ sensor si đang xét có thằng nào là sensor tĩnh hay không.
    Nếu nó là sensor tĩnh (True) thì có nhiều thứ cần phải xử lí hơn  
    '''
    for sensor in list_sensor:
        if sensor.is_fixed:
            return True
    return False


def get_same_centerline_sensors(list_sensor, sensor_si):
    '''
    Lấy ra tất cả những sensor nằm cùng trên centerline với sensor si (không chứa si). 
    Một số dòng bị commented là do khi lấy theo các tạo ra một Sensor() mới sẽ có vấn đề khi set up lại hàm set_fixed 
    '''
    # list_x_centerlined_sensors = []
    # list_x_centerlined_sensors_is_fixed = []
    # print("Ok list sensor: ", list_sensor)
    same_centerlined_sensors = []
    x = sensor_si.coor3D.x
    y = sensor_si.coor3D.y
    z = sensor_si.coor3D.z 
    for sensor in list_sensor:
        x_i, y_i, z_i = sensor.coor3D.x, sensor.coor3D.y, sensor.coor3D.z
        if y_i == y and z_i == z:
            if x_i == x:
                pass
                # print("Oh my god!")
                # print("Before: ", sensor)
                # sensor.move_to(Coordinate3D(x_i+1, y_i, z_i))
                # print("After: ", sensor)
            same_centerlined_sensors.append(sensor)
            # list_x_centerlined_sensors.append((x_i, id_i))
            # list_x_centerlined_sensors_is_fixed.append(sensor_si.is_fixed)
    # list_x_centerlined_sensors = sorted(list_x_centerlined_sensors)
    # print("\nIs fixed: ", list_x_centerlined_sensors_is_fixed)
    # for i in range(len(list_x_centerlined_sensors)):
    #     same_centerlined_sensors.append(Sensor(Coordinate3D(list_x_centerlined_sensors[i][0], y, z), list_x_centerlined_sensors[i][1], list_x_centerlined_sensors_is_fixed[i]))
    return same_centerlined_sensors
        

def update_closer_sensors(same_centerline_sensors, sensor_si):
    '''
        update list sensors closer to base layer than sensor s_i 
    '''
    C_si = []
    for sensor in same_centerline_sensors:
        if (abs(sensor_si.coor3D.x - sensor.coor3D.x) < cf.GAMMA and sensor_si.coor3D.x >= sensor.coor3D.x):
            C_si.append(sensor)
    return C_si


def vertical_move(sensor_si, list_sensor, count, curr_layer, path, layers):

    x_sensor = sensor_si.coor3D.x
    y_sensor = sensor_si.coor3D.y
    z_sensor = sensor_si.coor3D.z

    # lấy tất cả các sensor cùng senterlize 
    list_same_centerline_sensors = get_same_centerline_sensors(list_sensor, sensor_si)
    # print("\nSensor si:", sensor_si)
    # print("\nList same centerline:", list_same_centerline_sensors)
    # lọc ra những sensor gàn base hơn so với nó, tính theo GAMMA 
    list_closer_sensors = update_closer_sensors(list_same_centerline_sensors, sensor_si)
    # print("List closer sensors: ", list_closer_sensors)
    # sensor đó sẽ chuyển động đến khi gặp sensor khác hoặc base layer thì thôi
    while len(list_closer_sensors) == 0 and sensor_si.coor3D.x > 0:
        path += sensor_si.count_path([sensor_si.coor3D.x - cf.VELOCITY, y_sensor, z_sensor])
        sensor_si.set_path([sensor_si.coor3D.x - cf.VELOCITY, y_sensor, z_sensor])
        sensor_si.move_to(Coordinate3D(sensor_si.coor3D.x - cf.VELOCITY, y_sensor, z_sensor))      # chuyển động với một khoảng bằng vận tốc (lấy là 1 - đơn vị )
        list_closer_sensors = update_closer_sensors(list_same_centerline_sensors, sensor_si) # lúc nào cũng phải update lại mỗi khi di chuyển được V m. 
        # có thể đặt biến tính time chuyển động ở đây 
    # print("After moving to base layer: ", sensor_si.coor3D)
    # print("List closer sensor before: ", list_closer_sensors)
    # Phần này có tinh chỉnh lại: sau khi 1 số sensor đã tới được base layer, để xét các tầng tiếp theo thì phải là (curr_layer - 1) * Gamma
    # Đồng thời cũng cần phải để cho len nó bằng 0 vì khác không đã có đoạn bên dưới xử lí => nếu không thì toàn bug, fix rất mệt. 
    if (sensor_si.coor3D.x == (curr_layer - 1)*cf.GAMMA and len(list_closer_sensors) == 0):
        # print("Sensor should be fixed")
        sensor_si.set_fixed(True) # ban đầu chỉ đặt là sensor_si.fixed = True. Như này thì sẽ không thay đổi được giá trị bên trong sensor
        # Bắt buộc phải đổi lại trong lớp sensor (mất cả buổi đề fixed mỗi cái lỗi này thôi ấy. Khó đcđ) 
        # sensor_si.move_to(Coordinate3D(0, y_sensor, z_sensor))
        sensor_si_coor3D_list = [sensor_si.coor3D.x, sensor_si.coor3D.y, sensor_si.coor3D.z] # đổi tọa độ sensor về dạng list để tương thích với layers 
        if (len(layers[curr_layer-1].list_VP) > 1):
            if  sensor_si_coor3D_list in layers[curr_layer - 1].list_VP:
                layers[curr_layer - 1].list_VP.remove(sensor_si_coor3D_list)
                count -= 1 # count phải bỏ vào bên trong này. Ban đầu để ngoài thì bị lỗi (do nó ko cover được hết case) 
            # else: 
                # sensor_si.move_to(Coordinate3D(sensor_si.coor3D.x + cf.VELOCITY, y_sensor, z_sensor))
                
        elif (len(layers[curr_layer-1].list_VP) == 1): #còn mỗi 1 vị trí trống thì set nó rỗng thôi cho dễ 
            layers[curr_layer-1].list_VP = []
            layers[curr_layer-1].set_flag(2) 
            curr_layer += 1
            count -= 1 # phải đặt count và curr_layer ở trong if thì mới ổn. 
        return sensor_si, curr_layer, count, path
        # time = sensor_si_x / velocity 

    # nếu nó gặp một sensor trước nó 
    # vì mình chỉ nhảy một lần 1 đơn vị, VÀ init theo trục x là số nguyên (bội của 1 )
    # hàm closer tính biên, tức là cách nhau đúng GAMMA là được, không cần <= GAMMA -1 
    if len(list_closer_sensors) > 0:

        # check fix sensor , lần đầu chạy thì chắc là không có rồi 
        # nếu có thì lùi ra xa một đoạn cho bằng GAMMA 
        # print("List closer sensors: ", list_closer_sensors)
        closer_sensor_list_coor = [sensor.coor3D.to_list() for sensor in list_closer_sensors]
        if sensor_si.coor3D.to_list() in closer_sensor_list_coor:
            # print("God damn it!")
            path += sensor_si.count_path([x_sensor + 1, y_sensor, z_sensor])
            sensor_si.set_path([x_sensor + 1, y_sensor, z_sensor])
            sensor_si.move_to(Coordinate3D(x_sensor + 1, y_sensor, z_sensor))
        if contain_fix_sensor(list_closer_sensors):
            # print("Have fixed sensor!")
            closest_to_si_sensor = list_closer_sensors[-1]   # cần check xem cái nào gần nhất ? 
            # print("Closest to sensor si : ", closest_to_si_sensor.coor3D)
            if (sensor_si.coor3D.x - closest_to_si_sensor.coor3D.x < cf.GAMMA):
                path += sensor_si.count_path([closest_to_si_sensor.coor3D.x + cf.GAMMA, y_sensor, z_sensor])
                sensor_si.set_path([closest_to_si_sensor.coor3D.x + cf.GAMMA, y_sensor, z_sensor])
                sensor_si.move_to(Coordinate3D(closest_to_si_sensor.coor3D.x + cf.GAMMA, y_sensor, z_sensor))
                # time = cf.Gamma / velocity
        # print("Sensor move backward base layer: ", sensor_si.coor3D)
        # else thi đứng while
    
    
    if len(sensor_si.VP) > 0:  # nếu mà hàng đợi vị trí trống của nó khogn rỗng 
        p0 = sensor_si.VP[0]
        # print("List VP of sensor si after all: ", sensor_si.VP)
        if sensor_si.coor3D.x == p0[0]:    # t đang ở cùng layer với môt vị trí trống 
            broadcast_po_mess(sensor_si)        # quảng bá cho bon khác biết là nó đang nằm cùng layer với VP của nó ( nó có xu hướng dich chuyển tới base tới khi cùng layer tới vị trí trống sẽ quảng bá cái po)
            # print("List VP layers after all: ", layers[curr_layer - 1].list_VP)
            sensor_si_coor3D_list = [sensor_si.coor3D.x, sensor_si.coor3D.y, sensor_si.coor3D.z]
            if (len(layers[curr_layer-1].list_VP) > 1):
                if  sensor_si_coor3D_list in layers[curr_layer - 1].list_VP:
                    layers[curr_layer - 1].list_VP.remove(sensor_si_coor3D_list)
                    count -= 1
                    sensor_si.set_fixed(True)
                # else: 
                #     sensor_si.move_to(Coordinate3D(sensor_si.coor3D.x + cf.VELOCITY, y_sensor, z_sensor))
            elif (len(layers[curr_layer-1].list_VP) == 1):
                layers[curr_layer-1].list_VP = []
                layers[curr_layer-1].set_flag(2)
                curr_layer += 1
                count -= 1
                sensor_si.set_fixed(True)

    # is_done = True # điều kiện dừng cho toàn bộ chương trình
    # nếu tất cả các layer đều ở trạng thái 2 => kết thúc toàn bộ các thuật toán. 
    # for i in range(cf.MAX_LAYERS):
    #     if (layers[i].flag != 2):
    #         is_done = False
    #         break
    # if (is_done):
    #     print("Hoan thanh chuowng trinh!")
    #     visualize3D_with_sensor(list_sensors_after_init_move)
    return sensor_si, curr_layer, count, path



