class Sensor:
    def __init__(self, coor3D):
        self.coor3D = coor3D
        self.is_fixed = False
        self.closer_sensors = []

    def __repr__(self):
        return f'Sensor({self.coor3D}, is_fixed={self.is_fixed}, closer_sensors={self.closer_sensors})'

    def move_to(self, new_pos):
        self.coor3D = new_pos