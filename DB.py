from dataclasses import dataclass
from datetime import datetime


USERS = dict()


class User:
    def __init__(self, id: int, time: datetime):
        self.id: int = id
        self.time: datetime = time
        self.location: tuple = None
        self.FIO: str = 'unkown'
        self.phone: str = 'unkowm'
        self.gender: str = 'unkowm'
        self.age: int = None
        self.info: str = 'unkowm'
        self.priority: int = 0
        self.step: int = 0
        self.last_msg: str = None
