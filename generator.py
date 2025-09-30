from math import pi
from os.path import join

from matplotlib import pyplot as plt

from vector import Vector
from functools import wraps


class Generator:
    """
    Singleton class that supports cut file generation for Prohászka Zoli's foam cutter, making it usable for normal
    human beings.
    """

    EXPORT_FOLDER = "generated"

    position = Vector(0, 0)

    _filename: str = ""
    _header: str = ""
    _memory: list = []

    # ===[ HELPER FUNCTIONS ]========================================================================================= #

    @staticmethod
    def deg_to_rad(deg: float) -> float:
        """ Changes an angle from degrees to radians """
        return deg * pi / 180.0

    @classmethod
    def _mark_(cls):
        """ Registers a point the current position in memory """
        x, y = cls.position
        cls._memory.append((x, y))

    @classmethod
    def _goto_(cls, x, y):
        """ Moves the current position to [x, y] and registers the movement direction vector """
        new_position = Vector(x, y)
        if new_position != cls.position:
            cls.direction = (new_position - cls.position).normalized()
            cls.position = new_position

    @classmethod
    def _arc_(cls, center, radius, start_direction, end_direction, n_points, direction):
        """
        Draws an arc with <n_points> number of points around <center> position with a given <radius>.
        The start position is given by a normalized <start_direction> and the end position is given
        by a normalized <end_direction>. The direction vectors are measured compared to <center> position.
        <direction> specifies CCW (1) or CW (-1) arc.
        """

        max_angle = start_direction.angle_to(end_direction)
        if max_angle * direction < 0:
            max_angle += pi * 2 * direction

        for index in range(1, n_points):
            rot = max_angle * index / (n_points - 1)
            radius_vector = start_direction.rotate(rot) * radius
            position = center + radius_vector

            cls._goto_(*position)
            cls._mark_()

        cls.direction = end_direction.rot90() * direction

    @classmethod
    def _save_data_to_file_(cls):
        """ Saves all registered positions into a cut file with a <_header> """

        with open(join(cls.EXPORT_FOLDER, cls._filename), "w") as file:
            file.write(cls._header + "\n")

            for x, y in cls._memory[1:]:
                file.write(f"{x:.5f} {y:.5f}\n")

    # ===[ USER FUNCTIONS ]=========================================================================================== #

    @classmethod
    def begin(cls, filename: str, header: str):
        """ Begins a new cut file from [0, 0]. Discards the last cut data. """
        cls._filename = filename
        cls._header = header
        cls._memory = []
        cls._mark_()

    @classmethod
    def end(cls):
        """ Ends a cut file and saves it's data to a file """
        cls._save_data_to_file_()
        cls._goto_(0, 0)
        cls.direction = Vector(1, 0)

    @classmethod
    def move_to(cls, x, y):
        """ Draws a line from current position to [x, y]. Moves the effector to [x, y]. """
        cls._goto_(x, y)
        cls._mark_()

    @classmethod
    def move(cls, dx, dy):
        """ Moves the effector by [dx, dy] vector and draws a line along the path """
        position = cls.position + (dx, dy)
        cls._goto_(*position)
        cls._mark_()

    @classmethod
    def move_home(cls):
        """ Moves the effector to [0, 0] and draws a line along the path """
        cls.move_to(0, 0)

    @classmethod
    def turn(cls, angle):
        """ Turns the direction vector by <angle> counter-clockwise """
        cls.direction = cls.direction.rotate(cls.deg_to_rad(angle))

    @classmethod
    def orient(cls, dx, dy):
        """ Turns the direction vector to a new direction [dx, dy]. The direction is normalized. """
        cls.direction = Vector(dx, dy).normalized()

    @classmethod
    def circle_to(cls, x, y, radius, n_points, direction=1):
        """
        Draws a circle between current position and a given [x, y] position with a given <radius> by
        generating lines between <n_points> number of points. <direction> specifies CCW (1) or CW (-1) arc.
        The circle will be tangent with the last direction at the starting point and the new direction will
        be tangent with the circle at the end point.
        """

        start = cls.position
        end = Vector(x, y)
        center = start + (cls.direction.rot90() * radius * direction)

        center_to_end = (end - center).normalized()
        center_to_start = (start - center).normalized()

        cls._arc_(center, radius, center_to_start, center_to_end, n_points, direction)

    @classmethod
    def circle(cls, dx, dy, radius, n_points, direction=1):
        """
        Moves the effector to [x, y] position along a circle with a given <radius> and generates <n_points>
        number of points in-between. <direction> specifies CCW (1) or CW (-1) arc.
        The circle will be tangent with the last direction at the starting point and the new direction will
        be tangent with the circle at the end point.
        """

        position = cls.position + Vector(dx, dy)
        cls.circle_to(*position, radius, n_points, direction)

    @classmethod
    def circle_around(cls, x, y, angle, n_points):
        """
        Moves the effector around a center point [x, y] by a given <angle> and generates <n_points>
        number of points in-between. The sign of the angle defines the direction ([+] = CCW and [-] = CW).
        The new direction will be tangent with the circle at the end point.
        """

        center = Vector(x, y)
        center_to_start = cls.position - center

        radius = center_to_start.length
        start_direction = center_to_start.normalized()
        end_direction = start_direction.rotate(cls.deg_to_rad(angle))

        cls._arc_(center, radius, start_direction, end_direction, n_points, 1 if angle > 0 else -1)

    @classmethod
    def plot(cls):
        """ Plots the registered path to the screen for debugging """

        x_vals, y_vals = zip(*cls._memory)

        plt.figure(figsize=(5, 5))
        plt.plot(x_vals, y_vals, 'o-', label="Arc path")
        plt.axis("equal")
        plt.legend()
        plt.title(cls._header)
        plt.show()


def movement(name, header):

    def outer_wrapper(original_function):

        def inner_wrapper(*args, **kwargs):
            Generator.begin(name, header)
            original_function(*args, **kwargs)
            Generator.end()
            Generator.plot()

        return inner_wrapper
    return outer_wrapper