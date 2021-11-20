class Coordinate3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Coordinate3D(x={self.x}, y={self.y}, z={self.z})'

    def to_list(self):
        return [self.x, self.y, self.z]

class Coordinate2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Coordinate2D(x={self.x}, y={self.y})'

    def to_list(self):
        return [self.x, self.y]