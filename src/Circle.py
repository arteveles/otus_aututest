import math
from src.Figure import Figure


class Circle(Figure):

    def __init__(self, attr_1):
        self.attr_1 = attr_1

    def name(self):
        name = "Круг"
        return name

    @property
    def perimeter(self):
        perimeter = 2 * math.pi * self.attr_1
        return perimeter

    @property
    def area(self):
        area = 2 * math.pi * math.pow(self.attr_1, 2)
        return area
