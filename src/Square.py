import math
from src.Figure import Figure


class Square(Figure):

    def __init__(self, attr_1):
        self.attr_1 = attr_1

    def name(self):
        name = "Квадрат"
        return name

    @property
    def perimeter(self):
        perimeter = 4 * self.attr_1
        return perimeter

    @property
    def area(self):
        area = math.pow(self.attr_1, 2)
        return area
