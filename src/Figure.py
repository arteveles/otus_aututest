from src import Triangle, Rectangle, Square, Circle
from Triangle import triangle
from Square import square

class Figure:
    def __init__(self, side):
        self.side = side
    def plis(self):
        return 10

    def add_area(self, other_figure):
        return self.area + other_figure.area

fig = Figure(10)

print(fig.side)