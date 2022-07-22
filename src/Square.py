import math


class Square:

    def __init__(self, attr_1):
        self.attr_1 = attr_1

    def name(self):
        name = "Квадрат"
        return name

    def perimeter(self):
        perimeter = 4 * self.attr_1
        return perimeter

    def area(self):
        area = math.pow(self.attr_1, 2)
        return area


square = Square(10)
