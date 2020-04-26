import pytest

from geometria import Rectangle


class TestSquare:
    def test_rectangle_perimeter(self):
        rectangle = Rectangle(a = 2, b = 4)
        assert rectangle.perimeter() == 12

    def test_rectangle_area(self):
        rectangle = Rectangle(a = 3, b = 5)
        assert rectangle.area() == 15

    def test_rectangle_angels(self):
        rectangle = Rectangle(a = 5, b = 3)
        assert rectangle.angels() == 4

    def test_add_square_not_figure(self):
        rectangle = Rectangle(a = 5, b = 3)
        with pytest.raises(AttributeError):
            assert rectangle.add_square('not figure object')

    def test_add_square_figure(self):
        rectangle_one = Rectangle(a = 1, b = 2)
        rectangle_two = Rectangle(a = 2, b = 3)
        assert rectangle_one.add_square(rectangle_two) == 8

    def test_rectangle_name(self):
        rectangle = Rectangle(a = 2, b = 3)
        assert rectangle.name == 'rectangle'
