from src import Triangle, Rectangle, Square, Circle
from Triangle import triangle
from Square import square


class Figure:
    def __init__(self, side):
        self.side = side

    @property
    def other_figure(self):
        pass

    @property
    def add_area(self, other_figure):
        return self.area + other_figure.area
