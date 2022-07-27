import pytest
from src.Triangle import Triangle
from src.Square import Square



@pytest.fixture
def standart_triangle():
    standart_triangle = Triangle(13,14,15)
    return standart_triangle

@pytest.fixture
def standart_square():
    standart_square = Square(2)
    return standart_square

