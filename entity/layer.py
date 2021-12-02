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
    def __init__(self, flag):
        self.flag = flag    
        self.list_VP = []

    def __repr__(self) -> str:
        return f'Layer(flag={self.flag}, list_VP={self.list_VP})'