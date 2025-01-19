import vector


class Circle:
    def __init__(self):
        self.start_coordinates = vector.Vector(0, 0)
        self.coordinates = vector.Vector(0, 0)
        self.radius = 0
        self.items = {}

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items[item.id] = item

    def remove_item(self, ID):
        del self.items[ID]

    def move(self, coordinates):
        self.coordinates = coordinates

    def change_size(self, radius):
        self.radius = radius

    def __contains__(self, coordinates):
        return (
            (coordinates.x - self.x) ** 2 + (coordinates.y - self.y) ** 2
        ) < self.radius**2
