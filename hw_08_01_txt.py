from datetime import datetime
class Emplooyee:
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self._onboarding = datetime.now()

    @property
    def onboarding_time(self):
        return self._onboarding

    @property
    def info(self):
        return {'fullname': f'{self.first_name} {self.last_name}',
                'age': f'{self.age}',
                'working_time': f'{datetime.now() - self.onboarding_time}'
                }

Emplooyee.department = None
