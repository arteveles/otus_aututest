from src import Triangle, Rectangle, Square, Circle
from Triangle import triangle
from Square import square

class Figure:

    def other_figure(self, area):
        return area

    def add_area(self, other_figure):
        return self.area + other_figure.area


figure = Figure()
print(triangle(square))