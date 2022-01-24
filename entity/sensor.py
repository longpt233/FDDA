from queue import PriorityQueue


class Sensor:
    def __init__(self, coor3D, id, is_fixed):
        self.coor3D = coor3D
        self.is_fixed = is_fixed
        self.id = id
        self.VP = []   # hàng đợi vị trí trống type :  Coordinate3D

    def __repr__(self):
        # return f'Id={self.id}, Sensor({self.coor3D}, is_fixed={self.is_fixed}, VP={[i for i in self.VP]})'
        return f'(Id={self.id}, {self.coor3D.to_list()}, is_fixed={self.is_fixed})'

    def move_to(self, new_pos):
        self.coor3D = new_pos

    def set_fixed(self, is_fixed):
        self.is_fixed = is_fixed

    def set_vp(self, list_VP):
        self.VP = list_VP