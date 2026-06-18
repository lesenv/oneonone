from typing import Protocol
from abc import abstractmethod
import random

def get_2_ints(_from: int = 1, _to: int = 10) -> list[int]:
    if _from > _to: _from, _to = _to, _from
    return [random.randint(_from, _to), random.randint(_from, _to)]


class Task(Protocol):
    symbol: str

    def make_task(self, _from: int = 1, _to: int = 10):
        self.a, self.b = get_2_ints(_from, _to)
        return [self.a, self.symbol, self.b]
    
    @abstractmethod
    def get_result(self) -> int:
        ...

class Multiplizieren(Task):
    def __init__(self):
        self.symbol = "x"
    
    def get_result(self):
        return self.a*self.b