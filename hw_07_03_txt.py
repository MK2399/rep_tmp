from hw_07_01_base import shape
from math import pi

class cirle(shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        super().__init__('Circle')

    def get_area(self):
        s = pi * self.r **2
        super().get_area()
        return s

    def __add__(self, other):
        flag = isinstance(other, cirle)
        if flag == True:
            return self.get_area() + other.get_area()
        else:
            return 'Второй элемент сложения не относится к классу circle.'

    def __sub__(self, other):
        flag = isinstance(other, cirle)
        if flag == True:
            return self.get_area() - other.get_area()
        else:
            return 'Второй элемент сложения не относится к классу circle.'

first_circle = cirle(0,0,5)
second_circle = cirle(1,1,4)

def test_circle():
    assert type(first_circle + second_circle) == float
    assert type(first_circle + second_circle) == float
    assert isinstance(first_circle, shape)
    assert isinstance(second_circle, shape)