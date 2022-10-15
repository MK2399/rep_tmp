from hw_08_01_txt import Emplooyee
from datetime import datetime


class TechnicalStaff(Emplooyee):
    def __init__(self, first_name, last_name, age, profession):
        super().__init__(first_name = first_name,
                         last_name = last_name,
                         age = age,
                         profession = profession,
                         )

    def change_department(self):
        self.department = input('Enter department ')

    @property
    def info(self):
        return {'fullname': f'{self.first_name} {self.last_name}',
                'age': self.age,
                'working_time': f'{self.onboarding_time - datetime.now()}'
                ,'Department' : self.department
                }
    @staticmethod
    def get_info():
        if Emplooyee.department == TechnicalStaff.department:
            return 'Welcome'


t = TechnicalStaff('Jhon', 'Smith', 25, 'Enginer')
Emplooyee.department = 'si'
t.change_department()
print(t.get_info())