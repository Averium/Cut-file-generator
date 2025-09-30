from math import hypot, atan2, pi, cos, sin


class Vector(list):

    """
    A 2D Vector helper class for "generator.py". Supports basic vector-vector and vector-scalar arithmetics,
    vector-vector comparison, rotation, normalization and indexing.
    """

    def __init__(self, x, y=None):
        if y is None:
            list.__init__(self, x)
        else:
            list.__init__(self, [x, y])

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @x.setter
    def x(self, new_x):
        self[0] = new_x

    @y.setter
    def y(self, new_y):
        self[1] = new_y

    def __add__(self, other):
        return self._add_or_subtract_(other, 1)

    def __sub__(self, other):
        return self._add_or_subtract_(other, -1)

    def _add_or_subtract_(self, other, sign):
        if isinstance(other, (int, float)):
            return Vector(self[0] + other * sign, self[1] + other * sign)
        else:
            return Vector(self[0] + other[0] * sign, self[1] + other[1] * sign)

    def __mul__(self, other):
        return Vector(self[0] * other, self[1] * other)

    def __truediv__(self, other):
        return Vector(self[0] / other, self[1] / other)

    def rot90(self):
        return Vector(-self[1], self[0])

    def rotate(self, angle):
        x, y = self
        return Vector(x * cos(angle) - y * sin(angle), x * sin(angle) + y * cos(angle))

    @property
    def length(self):
        return hypot(self[0], self[1])

    @property
    def angle(self):
        result = atan2(self[1], self[0])
        if result < 0 and False:
            result += 2 * pi
        return result

    def angle_to(self, other):
        ax, ay = self
        bx, by = other
        cross = ax * by - ay * bx
        dot = ax * bx + ay * by
        return atan2(cross, dot)

    def normalized(self):
        l = self.length
        return Vector(self[0] / l, self[1] / l)

    def __eq__(self, other):
        return self[0] == other[0] and self[1] == other[1]

    def __ne__(self, other):
        return not self.__eq__(other)


if __name__ == "__main__":
    pass