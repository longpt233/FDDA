from alg.cal_funcs import distance3D
import configs.config as cfg


def vacant_position_processing(sensor_si, curr_layer, layers):
    '''
    Alg3: Phần này đã được sửa lại khá nhiều. 
    Không theo thuật toán chi tiết của họ nữa.
    Mục tiêu của phần này là cập nhật lại toàn bộ listVP của từng thằng sensor. 
    (Ở đây là xét riêng cho sensor si)  
    Cần phải lưu lại biến curr_layer để biết tầng nào đang thực hiện.
    '''
    # t_start = time.time()
    if sensor_si.is_fixed:
        return sensor_si
    else:
        sensor_si_coor3D_list = [sensor_si.coor3D.x, sensor_si.coor3D.y, sensor_si.coor3D.z]
        # while(time.time() - t_start < cfg['T_RCV']:
        # phần này sẽ cố gắng lấy ra những vị trí trống trong cfg['LAYERS'] để gán lại cho từng thằng sensor. 
        temp_VP = layers[curr_layer - 1].list_VP  
        temp_dict_VP = {}
        for i in range(len(temp_VP)):
            temp_dict_VP[i] = temp_VP[i]
        # chú ý là phải sort lại dict để vị trí trống đầu tiên của các sensor là vị trí gần với nó nhất 
        temp_dict_VP = {k: v for k, v in sorted(temp_dict_VP.items(), key=lambda item: distance3D(sensor_si_coor3D_list, item[1]))}
        sensor_si.set_vp(list(temp_dict_VP.values()))

        return sensor_si





    


        





        