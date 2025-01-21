import circle
import vector


class CircleManager:
    def __init__(
        self,
        center=vector.Vector(x=0, y=0),
        num_circles=10,
        num_items_per_circle=13,
        base_size=10,
        large_size=50,
        distance_to_center=100,
        NUM_ROTATION_TICKS=50,
    ):
        self.center = center
        self.distance_to_center = distance_to_center
        self.num_circles = num_circles
        self.degrees_per_circle = 360 / self.num_circles
        self.circles = []
        for _ in range(num_circles):
            self.circles.append(circle.Circle())
        self.is_rotating = False
        self.rotation_phase = 0
        self.rotation_end_circle = None
        self.rotation_speed = 0
        self.bottom_circle = 0
        self.circles[self.bottom_circle].change_size(large_size)

        self.NUM_ROTATION_TICKS = NUM_ROTATION_TICKS
        self.TOTAL_ROTATION_PIECES = int(
            (
                0.125 * NUM_ROTATION_TICKS**3
                - 0.375 * NUM_ROTATION_TICKS**2
                + 0.25 * NUM_ROTATION_TICKS
            )
            / 3
        )

    def get_clicked_circle(self, coordinates):
        for i in range(len(self.circles)):
            if coordinates in self.circles[i]:
                return i
        return None

    def set_all_circle_coordinates(self, rotation_degrees):
        starting_circle = self.bottom_circle
        for i in range(self.num_circles):
            segments_off = (starting_circle - i) % self.num_circles
            base_angle = segments_off * self.degrees_per_circle + 90
            angle = (base_angle - rotation_degrees) % 360
            self.circles[i].coordinates = self.center + vector.Vector(
                d=angle, m=self.distance_to_center
            )

    def start_rotation(self, target_circle_index):
        self.rotation_phase = 0
        self.rotation_end_circle = target_circle_index
        self.rotation_speed = 0
        self.is_rotating = True

        self.total_movement = 0

    def has_exceeded_half_rotation(self):
        return self.rotation_phase >= self.NUM_ROTATION_TICKS // 2

    def has_completed_rotation(self):
        return self.rotation_phase == self.NUM_ROTATION_TICKS

    def continue_rotation(self):
        self.total_movement += self.rotation_speed
        if self.has_completed_rotation():
            self.finish_rotation()
            return
        if self.has_exceeded_half_rotation():
            modifier = 1 - self.NUM_ROTATION_TICKS
        else:
            modifier = 0
        self.rotation_speed += self.rotation_phase + modifier
        self.rotation_phase += 1
        rotation_percent = self.total_movement / self.TOTAL_ROTATION_PIECES

        segments_off = self.bottom_circle - self.rotation_end_circle
        total_rotation_amount = (
            segments_off * self.degrees_per_circle + 180
        ) % 360 - 180
        rotation_degrees = rotation_percent * total_rotation_amount
        self.set_all_circle_coordinates(rotation_degrees)
        return None

    def finish_rotation(self):
        self.is_rotating = False
        self.bottom_circle = self.rotation_end_circle

        self.set_all_circle_coordinates(0)

    def add_item_to_circle(self, item):
        self.circles[self.bottom_circle].add_item(item)

    def remove_item_from_circle(self, itemID):
        self.circles[self.bottom_circle].remove_item(itemID)
