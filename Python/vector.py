class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector(self.x * other, self.y * other)
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
