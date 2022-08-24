from Figure import Figure


class Rectangle(Figure):

    def __init__(self, attr_1, attr_2):
        self.attr_1 = attr_1
        self.attr_2 = attr_2

    def name(self):
        name = "Прямоугольник"
        return name

    @property
    def perimeter(self):
        perimeter = 2 * (self.attr_1 + self.attr_2)
        return perimeter

    @property
    def area(self):
        area = self.attr_1 * self.attr_2
        return area
