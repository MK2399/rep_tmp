from hw_07_01_preza import auto
from time import sleep



class truck(auto):
    def __init__(self,
                 brand : str,
                 age : int,
                 mark : str,
                 max_load : int,
                 ):
        super().__init__(brand=brand,
                         age=age,
                         mark=mark,
                         weight=None,
                         color='Default'
                         )
        self.max_load = max_load

    def move(self):
        print('attention')
        return super().move()

    def load(self):
        sleep(1)
        print('load')
        sleep(1)



class car(auto):
    def __init__(self,
                 brand : str,
                 age : int,
                 mark : str,
                 max_speed : int,
                 ):
        super().__init__(brand=brand,
                         age=age,
                         mark=mark,
                         weight=None,
                         color='Default'
                         )
        self.max_speed = f'Max speed is {max_speed}'

    def move(self):
        super().move()
        return self.max_speed


pickup = car("Ram", 5, 's300', 160)
pickup.color = 'Green'
pickup.weight = 3500
pickup.max_load = 10
wagon = truck('Iveco', 7, 'Stralis', 7)
wagon.color = 'Black'
wagon.weight = 12000
def test_wagon():
    assert wagon.birthday() == 8
    assert wagon.max_load == 7
    assert wagon.load() != 7
    assert wagon.color == 'Black'
    assert wagon.weight == 12000
    assert wagon.brand == 'Iveco'
    assert wagon.mark == 'Stralis'
    #assert pickup.move()
def test_pickup():
    assert pickup.birthday() == 6
    #assert wagon.move()
    assert pickup.max_speed == 'Max speed is 160'
    assert pickup.color == 'Green'
    assert pickup.weight == 3500
    assert pickup.brand == 'Ram'
    assert pickup.mark == 's300'


