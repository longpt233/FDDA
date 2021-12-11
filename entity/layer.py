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
        self.flag = flag    
        self.list_VP = []
        self.layer_id = id

    def __repr__(self) -> str:
        return f'Layer(flag={self.flag}, layer={self.layer_id}, list_VP={self.list_VP})'

    def change_flag(self, min_sensor_per_layer):
        if (len(self.list_VP) == 0):
            self.flag = 2
        elif (len(self.list_VP != min_sensor_per_layer)):
            self.flag = 1
        