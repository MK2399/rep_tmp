from hw_07_01_base import shape
from hw_07_03_txt import cirle
from hw_07_02_txt import rectangle


class box:
    def __init__(self):
        self.collection = []
        self.acc = 0
    def add_shape(self, inst):
        if isinstance(inst, shape):
            self.collection.append(inst)
        pass

    def remove_shape(self):
        self.collection.pop(-1)
        pass

    def _clear_acc(self):
        if self.acc != 0:
            self.acc = 0

    def get_common_area(self):
        self._clear_acc()
        for i in self.collection:
            self.acc += i.get_area()
        return self.acc


new_box = box()
first_circle = cirle(3,6,5)
second_circle = cirle(1,1,4)
first_rectangle = rectangle(1.5, 2)
second_rectangle = rectangle(2, 4)
new_box.add_shape(first_circle)
new_box.add_shape(second_circle)
new_box.add_shape(first_rectangle)
print(new_box.get_common_area())

def test_box():
    assert len(new_box.collection) == 3
    new_box.remove_shape()
    assert len(new_box.collection) == 2
    assert first_circle.get_area() + second_circle.get_area() == new_box.get_common_area()
    new_box.add_shape(second_rectangle)
    assert first_circle.get_area() + second_circle.get_area() + second_rectangle.get_area() == new_box.get_common_area()

