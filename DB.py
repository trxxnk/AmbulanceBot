from dataclasses import dataclass
from datetime import datetime

# библиотека для логгирования

from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext


USERS = dict()


class User:
    def __init__(self, id: int, time: datetime):
        self.id: int = id
        self.time: datetime = time
        self.location: tuple = None
        self.FIO: str = 'unkown'
        self.phone: str = 'unkowm'
        self.gender: str = 'unkowm'
        self.name: str = 'unkowm'
        self.surname: str = 'unkowm'
        self.lastname: str = 'unkowm'
        self.age: int = None
        self.info: str = 'unkowm'
        self.priority: int = 0
        self.step: dict[str:FSMContext, str:'func'] = {
            'state': None, 'func': None}
        self.last_msg: str = None


if __name__ == '__main__':

    def g():
        return 10
    x = User(id=100, time=0)
    print(x.step)
    x.step['func'] = g
    print(x.step)
