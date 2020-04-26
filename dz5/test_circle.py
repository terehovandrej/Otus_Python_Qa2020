import pytest
from geometria import Circle


class TestSquare:
    def test_circle_perimeter(self):
        circle = Circle(a = 2)
        assert circle.perimeter() == 12.566

    def test_circle_area(self):
        circle = Circle(a = 3)
        assert circle.area() == 28.274

    def test_square_angels(self):
        circle = Circle(a = 5)
        assert circle.angels() == 0

    def test_add_square_not_figure(self):
        circle = Circle(a = 5)
        with pytest.raises(AttributeError):
            assert circle.add_square('not figure object')

    def test_add_square_figure(self):
        circle_one = Circle(a = 5)
        circle_two = Circle(a = 7)
        assert circle_one.add_square(circle_two) == 232.478

    def test_triangle_name(self):
        circle = Circle(a = 2)
        assert circle.name == 'circle'
