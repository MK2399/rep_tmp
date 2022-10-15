from datetime import datetime
class Emplooyee:
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    @property
    def onboarding_time(self):
        return datetime.now()

    @property
    def info(self):
        return {'fullname': f'{self.first_name} {self.last_name}',
                'age': self.age,
                'working_time': f'{self.onboarding_time - datetime.now()}'
                }

setattr(Emplooyee, 'department', None)
#new_person = Emplooyee('Jhon', 'Smith', 25, 'Enginer')
#print(new_person.info)
#print(new_person.department)