from queue import PriorityQueue


class Sensor:
    def __init__(self, coor3D, id):
        self.coor3D = coor3D
        self.is_fixed = False
        self.id = id
        self.VP = PriorityQueue()   # hàng đợi vị trí trống type :  Coordinate3D

    def __repr__(self):
        return f'Id={self.id}, Sensor({self.coor3D}, is_fixed={self.is_fixed}, VP={[i for i in self.VP]})'

    def move_to(self, new_pos):
        self.coor3D = new_pos