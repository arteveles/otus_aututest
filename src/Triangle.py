import math
from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, attr_1, attr_2, attr_3):
        self.attr_1 = attr_1
        self.attr_2 = attr_2
        self.attr_3 = attr_3
        if attr_1 + attr_2 <= attr_3 or attr_1 + attr_2 <= attr_3 or attr_3 + attr_2 <= attr_1:
            raise ValueError("Треугольник не построился, проверьте корректность заданных сторон!")

    def name(self):
        name = "Треугольник"
        return name

    @property
    def perimeter(self):
        perimeter = (self.attr_1 + self.attr_2 + self.attr_3) / 2
        return perimeter

    @property
    def area(self):
        area = math.sqrt(
            self.perimeter * (self.perimeter - self.attr_1) * (self.perimeter - self.attr_2) * (
                    self.perimeter - self.attr_3))
        return area
