import pytest

from geometria import Square


class TestSquare:
    def test_square_perimeter(self):
        square = Square(a = 2)
        assert square.perimeter() == 8

    def test_square_area(self):
        square = Square(a = 3)
        assert square.area() == 9

    def test_square_angels(self):
        square = Square(a = 5)
        assert square.angels() == 4

    def test_add_square_not_figure(self):
        square = Square(a = 5)
        with pytest.raises(AttributeError):
            assert square.add_square('not figure object')

    def test_add_square_figure(self):
        square_one = Square(a = 5)
        square_two = Square(a = 7)
        assert square_one.add_square(square_two) == 74

    def test_square_name(self):
        square = Square(a = 5)
        assert square.name == 'square'
