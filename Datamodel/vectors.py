from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __str__ is for the programmer, __repr__ for displaying
    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    # absolute value
    def __abs__(self):
        return hypot(self.x, self.y)

    # boolean value,
    # also works with 'and' and 'or'
    def __bool__(self):
        return bool(abs(self))

    # allows usage of the '+' operator
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # allows usage of the '*' operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)