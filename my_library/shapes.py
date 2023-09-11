import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2
