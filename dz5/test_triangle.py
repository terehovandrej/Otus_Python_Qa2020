import pytest

from geometria import Triangle


class TestSquare:
    def test_triangle_perimeter(self):
        triangle = Triangle(a = 2, b = 3, c = 4)
        assert triangle.perimeter() == 9

    def test_triangle_area(self):
        triangle = Triangle(a = 2, b = 3, c = 4)
        assert triangle.area() == 2.905

    def test_triangle_angels(self):
        triangle = Triangle(a = 2, b = 3, c = 4)
        assert triangle.angels() == 3

    def test_add_square_not_figure(self):
        triangle = Triangle(a = 2, b = 3, c = 4)
        with pytest.raises(AttributeError):
            assert triangle.add_square('not figure object')

    def test_add_square_figure(self):
        triangle_one = Triangle(a = 3, b = 4, c = 6)
        triangle_two = Triangle(a = 4, b = 5, c = 6)
        assert triangle_one.add_square(triangle_two) == 15.255

    def test_triangle_name(self):
        triangle = Triangle(a = 2, b = 3, c = 4)
        assert triangle.name == 'triangle'
