import sys
sys.path.append("./")

from entity.corr import Corr3D


class Sensor:
    
    def __init__(self, corr3D):
        self.corr3D = corr3D

    def MoveTo(self, corr3D_new):
        self.corr3D = corr3D_new

    pass