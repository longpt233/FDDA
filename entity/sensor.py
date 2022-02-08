from queue import PriorityQueue
import math 

class Sensor:
    def __init__(self, coor3D, id, is_fixed, sensor_path):
        self.coor3D = coor3D
        self.is_fixed = is_fixed
        self.id = id
        self.VP = []   # hàng đợi vị trí trống type :  Coordinate3D
        self.path = sensor_path

    def __repr__(self):
        # return f'Id={self.id}, Sensor({self.coor3D}, is_fixed={self.is_fixed}, VP={[i for i in self.VP]})'
        return f'(Id={self.id}, {self.coor3D.to_list()}, is_fixed={self.is_fixed})'

    def set_fixed(self, is_fixed):
        self.is_fixed = is_fixed

    def set_vp(self, list_VP):
        self.VP = list_VP
     
    def move_to(self, new_pos):
        self.coor3D = new_pos

    def set_path(self, new_pos):
        x, y, z = new_pos
        self.path += math.sqrt((self.coor3D.x - x)**2 + (self.coor3D.y - y)**2 + (self.coor3D.z - z)**2)
    def count_path(self, new_pos):
        x, y, z = new_pos
        return math.sqrt((self.coor3D.x - x)**2 + (self.coor3D.y - y)**2 + (self.coor3D.z - z)**2)