import math


class Vector:
    def __init__(self, **kwargs):
        if 'x' in kwargs:
            self.x = kwargs['x']
            self.y = kwargs['y']
        else:  # from polar
            self.x = math.sin(math.radians(kwargs['d'])) * kwargs['m']
            self.y = math.cos(math.radians(kwargs['d'])) * kwargs['m']

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector(x=self.x * other, y=self.y * other)
        elif other is Vector:
            return self.x * other.x + self.y + other.y
        else:
            raise TypeError

    def __truediv__(self, other):
        return self * (1 / other)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'
