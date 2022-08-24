class Figure:
    def __init__(self, side):
        self.side = side

    @property
    def perimeter(self):
        return sum(self.side)

    @property
    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Make sure you pass a figure to add area')
        return self.area + figure.area

