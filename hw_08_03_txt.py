from uuid import uuid4
from enum import Enum
import pytest

class Currency(Enum):
    usd = 'USD'
    eur = 'EUR'
    byn = 'BYN'

class Account:
    def __init__(self, currency : Currency, amount = 0):
        self.person_id = uuid4()
        self.currency = currency
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        if new_amount <= 0:
            raise ValueError(f'Must be value positive, amount = {new_amount}')
        self._amount = new_amount
    def __repr__(self):
        return f"perrson_id = {self.person_id};currency = {self.currency};amount = {self.amount}"
Citizen = Account(currency = Currency.eur)
with pytest.raises(ValueError):
    Citizen.amount = -1
print(Citizen)