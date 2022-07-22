import math


class Circle:

    def __init__(self, attr_1):
        self.attr_1 = attr_1

    def name(self):
        name = "Круг"
        return name

    def perimeter(self):
        perimeter = 2 * math.pi * self.attr_1
        return perimeter

    def area(self):
        area = 2 * math.pi * math.pow(self.attr_1, 2)
        return area


circle = Circle(10)
