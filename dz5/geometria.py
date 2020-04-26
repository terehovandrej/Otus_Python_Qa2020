import math
from abc import ABC, abstractmethod


class Fig(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def angels(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def add_square(self, figure):
        if isinstance(figure, Fig):
            figures_area = (self.area() + figure.area())
            return figures_area
        else:
            raise AttributeError('object of wrong class')


class Square(Fig):
    def __init__(self, a):
        super().__init__(name = 'square')
        if a <= 0:
            raise Exception('Wrong length of side')
        self.a = a

    def area(self):
        return self.a ** 2

    def angels(self):
        return 4

    def perimeter(self):
        return self.a * 4


class Rectangle(Fig):
    def __init__(self, a, b):
        super().__init__(name = 'rectangle')
        if a <= 0 or b <= 0:
            raise Exception('Wrong length of sides')
        else:
            self.a = a
            self.b = b

    def area(self):
        return self.a * self.b

    def angels(self):
        return 4

    def perimeter(self):
        return 2 * (self.a + self.b)


class Triangle(Fig):
    def __init__(self, a, b, c):
        super().__init__(name = 'triangle')
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise Exception('Wrong length of sides')
        else:
            self.a = a
            self.b = b
            self.c = c

    def area(self):
        semi_p = (self.a + self.b + self.c) / 2
        s = round((semi_p * (semi_p - self.a) * (semi_p - self.b) * (semi_p - self.c)) ** 0.5, 3)
        return s

    def angels(self):
        return 3

    def perimeter(self):
        p = self.a + self.b + self.c
        return p


class Circle(Fig):
    def __init__(self, a):
        super().__init__(name = 'circle')
        if a <= 0:
            raise Exception('Wrong length of sides')
        else:
            self.a = a

    def area(self):
        return round(math.pi * self.a ** 2, 3)

    def angels(self):
        return 0

    def perimeter(self):
        return round(2 * self.a * math.pi, 3)