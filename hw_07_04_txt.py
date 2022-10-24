from hw_07_01_base import shape
from hw_07_03_txt import cirle
from hw_07_02_txt import rectangle
from matf import


class box:
    def __init__(self):
        self.collection = []
        self._acc = 0

    def add_shape(self, inst):
        if isinstance(inst, shape):
            self.collection.append(inst)
            self._acc += inst.get_area()

    def remove_shape(self):
        self._acc -= self.collection[-1].get_area()
        self.collection.pop(-1)

    @property
    def acc(self):
        if self._acc:
            return self._acc
        else:
            self._acc = sum(x.get_area() for x in self.collection)
        return self._acc
    def get_common_area(self):
        return self.acc

def test_box():
     new_box = box()
     first_circle = cirle(3, 6, 5)
     second_circle = cirle(1, 1, 4)
     second_rectangle = rectangle(2, 4)
     new_box.add_shape(first_circle)
     assert len(new_box.collection) == 1
     assert first_circle.get_area() == new_box.get_common_area()
     new_box.add_shape(second_circle)
     assert len(new_box.collection) == 2
     assert first_circle.get_area() + second_circle.get_area() == new_box.get_common_area()
     new_box.remove_shape()
     assert first_circle.get_area() == new_box.get_common_area()
     new_box.add_shape(second_rectangle)
     assert first_circle.get_area() + second_circle.get_area() + second_rectangle.get_area() == new_box.get_common_area()

