import random
from typing import Protocol
from dataclasses import dataclass

def get_2_ints(_from: int = 1, _to: int = 10) -> list[int]:
    if _from > _to: _from, _to = _to, _from
    return [random.randint(_from, _to), random.randint(_from, _to)]

class Aufgabe(Protocol):
    symbol: str

    def make_Aufgabe(self) -> list:
        ...
    def get_result(self) -> int:
        ...

class Multiplizieren(Aufgabe):
    def __init__(self):
        self.symbol = "x"

    def make_Aufgabe(self, _from: int = 0, _to: int = 9):
        self.a, self.b = get_2_ints(_from, _to)
        return [self.a, self.symbol, self.b]
    
    def get_result(self):
        return self.a*self.b

def main():
    Mio = Multiplizieren()
    Mio.make_Aufgabe()
    print(Mio.get_result())

if __name__ == "__main__":
    main()