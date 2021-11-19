import sys
sys.path.append("./")


class Sensor:

    isFixed = False
    
    def __init__(self, point_3d):
        self.point_3d = point_3d

    def MoveTo(self, point_3d_new):
        self.point_3d = point_3d_new
