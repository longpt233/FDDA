class Layer:
    '''
        params:
            flag: state of layer
                flag = 0            default layer
                flag = 1            constructing layer
                flag = 2            constructed layer
            list_VP: list vacant position
                list_VP[i] = True   position is vacant
                list_VP[i] = False  position is occupied
    '''
    def __init__(self, flag, id):
        self.flag = flag    # cờ để nhận diện layer là loại layer gì
        self.list_VP = []   # list chứa những vị trí trống trên mỗi layer
        self.layer_id = id  # định danh của layer, bắt đầu từ 1 -> maximum layelayer

    def __repr__(self) -> str:
        return f'Layer(flag={self.flag}, layer={self.layer_id}, list_VP={self.list_VP})'

    # thực hiện đổi cờ cho layer dựa vào số lượng ví trí trống còn lại trên layer
    def set_flag(self, flag):
        self.flag = flag
        