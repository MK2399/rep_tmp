class Auto:
    def __init__(self, brand, age : int, mark, weight = 0, color ='Default'):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.weight = weight
        self.color = color
    def move(self):
        return 'move'
    def stop(self):
        return 'Stop'

    def birthday(self):
        return self.age + 1

