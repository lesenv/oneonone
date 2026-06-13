import random
from typing import Protocol
#from dataclasses import dataclass
from abc import abstractmethod

def get_2_ints(_from: int = 1, _to: int = 10) -> list[int]:
    if _from > _to: _from, _to = _to, _from
    return [random.randint(_from, _to), random.randint(_from, _to)]

class Viewer(Protocol):
    @abstractmethod
    def output(self) -> None: ...
    @abstractmethod
    def get_input(self, str) -> int:...
    @abstractmethod
    def get_name(self, str) -> str:...

class Terminal(Viewer):
    def output(self, txt_list: list[str]) -> None:
        # only method to print
        # all the others are returning the strings
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
    
    def get_name(self, txt: str) -> str:
        return input(txt)
    
    def start(self) -> None:
        self.output(self.header())
        self.output()

    def get_task(self, task: list = []) -> str:
        return("{} {} {} = ".format(*task))

class Person():
    def __init__(self, name):
        self.points = 5
        self.name = name

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
    
def get_answer_3_times(viewer, tasker):
    new_mult_task = tasker.make_task()
    for _ in range(3):
        ans = viewer.get_input(viewer.get_task(new_mult_task))
        if ans == tasker.get_result():
            return True
    return False

class Game():
    def __init__(self, tasker, viewer):
        pass

def main():
    tasker = Multiplizieren()
    viewer = Terminal()
    people = []
    people.append(Person(viewer))
    anotherone = True
    while anotherone:
        get_answer_3_times(viewer, tasker)
        anotherone = False

if __name__ == "__main__":
    main()