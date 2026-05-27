import random
from typing import Protocol
from dataclasses import dataclass
from abc import abstractmethod

def get_2_ints(_from: int = 1, _to: int = 10) -> list[int]:
    if _from > _to: _from, _to = _to, _from
    return [random.randint(_from, _to), random.randint(_from, _to)]

class Viewer(Protocol):
    @abstractmethod
    def write_on(self) -> None: ...
    @abstractmethod
    def get_input(self) -> int:...

class Terminal(Viewer):
    def write_on(self, txt_list: list[str]) -> None:
        print(f"{txt}\n" for txt in txt_list)
    
    def header(self) -> str:
        # subprocess.call('cls' if os.name == 'nt' else 'clear')
        txt = ["1x1-Übungen    -  Schluss mit 'zzz', 'ppp' ist neuer Spieler"]
        txt.append(self.seperate_line())
        return txt
    
    def seperate_line(self) -> None:
        return "================"

    def get_input(self, txt: str) -> int:
        return int(input(txt))
    
    def start(self) -> None:
        self.write_on(self.header())
        self.write_on()

class Aufgabe(Protocol):
    symbol: str

    @abstractmethod
    def make_Aufgabe(self) -> list:
        ...
    @abstractmethod
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
    MioApril2024 = Multiplizieren()
    MioApril2024.make_Aufgabe()
    print(MioApril2024.get_result())

if __name__ == "__main__":
    main()