from hw_07_01_base import shape

class rectangle(shape):
    def __init__(self, a : float, b : float):
        self.a = a
        self.b = b
        super().__init__('rectangle')

    def get_area(self):
        super().get_area()
        return self.a * self.b

    def __add__(self, other):
        flag = isinstance(other, rectangle)
        if flag == True:
            return self.get_area() + other.get_area()
        else:
            return 'Второй элемент сложения не относится к классу rectangle.'

    def __sub__(self, other):
        flag = isinstance(other, rectangle)
        if flag == True:
            return self.get_area() - other.get_area()
        else:
            return 'Второй элемент сложения не относится к классу rectangle.'


first_rectangle = rectangle(1.5, 2)
second_rectangle = rectangle(2, 4)

def test_rectangle():
    assert type(first_rectangle + second_rectangle) == float
    assert type(first_rectangle - second_rectangle) == float
    assert isinstance(first_rectangle, shape)
    assert isinstance(second_rectangle, shape)
    assert first_rectangle.get_area() == 3